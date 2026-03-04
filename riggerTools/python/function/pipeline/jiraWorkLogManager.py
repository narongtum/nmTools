import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import json
import os
import requests
import logging
from requests.auth import HTTPBasicAuth
from datetime import datetime

# --- 1. การจัดการ Path และ Folder ---
DOCS_PATH = os.path.join(os.path.expanduser("~"), "Documents")
JIRA_PATH = os.path.join(DOCS_PATH, "Jira")

if not os.path.exists(JIRA_PATH):
	os.makedirs(JIRA_PATH)

CONFIG_FILE = os.path.join(JIRA_PATH, "jira_config.json")
DB_FILE = os.path.join(JIRA_PATH, "worklog_db.json")
FAV_FILE = os.path.join(JIRA_PATH, "favorite_tickets.json")
HOLIDAY_FILE = os.path.join(JIRA_PATH, "holidays.json")
LOG_FILE = os.path.join(JIRA_PATH, "jira_app.log")


# --- 2. Setup Logging ---
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s',
	handlers=[
		logging.FileHandler(LOG_FILE, encoding='utf-8'),
		logging.StreamHandler()
	]
)

#... เปลี่ยนจาก DEBUG เป็น WARNING เพื่อลดการบันทึก


logger = logging.getLogger("JiraWorklog")

logger.debug("--- PROGAM STARTED ---")
logger.debug(f"Config: {CONFIG_FILE}")
logger.debug(f"DB: {DB_FILE}")

# --- 3. Helper Functions ---
def load_json(filepath, default):
	if not os.path.exists(filepath):
		with open(filepath, 'w', encoding='utf-8') as f:
			json.dump(default, f, indent=4)
		return default
	with open(filepath, 'r', encoding='utf-8') as f:
		return json.load(f)

def save_json(filepath, data):
	with open(filepath, 'w', encoding='utf-8') as f:
		json.dump(data, f, indent=4)

def parse_time_to_minutes(time_str):
	"""
	Safely parse time strings like '2h', '30m', '1.5h' into minutes.
	Returns 0 if parsing fails.
	"""
	if not time_str:
		return 0
	
	total_m = 0
	time_str = time_str.lower().strip()
	
	try:
		if 'h' in time_str:
			# Handles cases like '2h' or '1.5h'
			h_part = time_str.replace('h', '').strip()
			if h_part:
				total_m += float(h_part) * 60
		elif 'm' in time_str:
			# Handles cases like '30m'
			m_part = time_str.replace('m', '').strip()
			if m_part:
				total_m += float(m_part)
		else:
			# If no unit provided, assume it's just a number (could be hours or minutes, but let's assume minutes for safety or just return 0)
			# Actually, Jira usually requires the unit.
			return 0
	except ValueError:
		# If the numeric part isn't a valid float (e.g., '2r' or '2hr')
		return 0
		
	return total_m

# --- 3. Main Application Class ---
class JiraWorklogApp:
	def __init__(self, root):
		logger.debug("Initializing JiraWorklogApp...")
		self.root = root
		self.root.title("Jira Worklog Manager v1.0")
		self.root.geometry("1000x600")
		
		# Load Config & Database
		logger.debug("Loading configurations...")
		self.config = load_json(CONFIG_FILE, {"url": "https://your-domain.atlassian.net", "email": "your-email@example.com", "token": "your-api-token"})
		self.db = load_json(DB_FILE, {})
		self.favorites = load_json(FAV_FILE, [])
		self.holidays = load_json(HOLIDAY_FILE, {}) # format: {"YYYY-MM-DD": "Name"}
		
		logger.debug("Setting up UI components...")
		self.setup_ui()
		logger.debug("Refreshing highlights and initial selection...")
		self.refresh_calendar_highlights()
		self.load_favorites_to_ui()
		self.on_date_selected()  # โหลดข้อมูลวันปัจจุบันทันทีที่เปิดโปรแกรม

	def setup_ui(self):
		# Main Container
		self.main_pane = tk.PanedWindow(self.root, orient="horizontal", sashrelief="raised", sashwidth=4)
		self.main_pane.pack(fill="both", expand=True)

		# --- Left: Favorite Tickets ---
		self.fav_frame = tk.Frame(self.main_pane, padx=10, pady=10, width=250)
		self.main_pane.add(self.fav_frame)
		
		tk.Label(self.fav_frame, text="favorite ticket", font=("Arial", 12, "bold")).pack(pady=5)
		
		# Favorite Table Headers
		fav_header = tk.Frame(self.fav_frame)
		fav_header.pack(fill="x")
		tk.Label(fav_header, text="ticket", width=10).pack(side="left")
		tk.Label(fav_header, text="detail", padx=10).pack(side="left", expand=True)
		
		self.fav_rows = []
		self.fav_scroll_frame = tk.Frame(self.fav_frame)
		self.fav_scroll_frame.pack(fill="both", expand=True)
		
		for i in range(10):  # 10 rows as per mockup
			row_frame = tk.Frame(self.fav_scroll_frame, pady=2)
			row_frame.pack(fill="x")
			
			e_ticket = tk.Entry(row_frame, width=10)
			e_ticket.pack(side="left")
			
			e_detail = tk.Entry(row_frame)
			e_detail.pack(side="left", fill="x", expand=True, padx=2)
			
			btn_del = tk.Button(row_frame, text="X", width=2, command=lambda idx=i: self.clear_fav_row(idx))
			btn_del.pack(side="right")
			
			self.fav_rows.append({"ticket": e_ticket, "detail": e_detail})

		tk.Button(self.fav_frame, text="save", command=self.save_favorites, width=10).pack(pady=10, anchor="w")

		# --- Middle: Calendar ---
		self.left_frame = tk.Frame(self.main_pane, padx=15, pady=15)
		self.main_pane.add(self.left_frame)
		
		tk.Label(self.left_frame, text="Select Work Date", font=("Arial", 12, "bold")).pack(pady=5)
		now = datetime.now()
		self.cal = Calendar(self.left_frame, selectmode='day', date_pattern='y-mm-dd',
						   year=now.year, month=now.month, day=now.day,
						   showweeknumbers=False,
						   background="darkblue", foreground="white", headersbackground="gray")
		self.cal.pack(pady=10, fill="both", expand=True)
		self.cal.bind("<<CalendarSelected>>", self.on_date_selected)
		self.cal.bind("<<CalendarMonthChanged>>", lambda e: self.refresh_month_total())

		# --- Right: Daily Dashboard ---
		self.right_frame = tk.Frame(self.main_pane, padx=15, pady=15)
		self.main_pane.add(self.right_frame)
		
		self.date_header = tk.Label(self.right_frame, text="Today's Logs", font=("Arial", 14, "bold"), fg="#2c3e50")
		self.date_header.pack(anchor="w")

		# Table (Treeview)
		columns = ("Issue", "Time", "Comment", "Status")
		self.tree = ttk.Treeview(self.right_frame, columns=columns, show='headings', height=10)
		for col in columns:
			self.tree.heading(col, text=col)
			self.tree.column(col, width=120)
		
		self.tree.tag_configure('submitted', background='#d4edda', foreground='#155724') # สีเขียว
		self.tree.tag_configure('waiting', background='#fff3cd', foreground='#856404')   # สีเหลือง
		self.tree.pack(fill="both", expand=True, pady=10)

		# Progress Section
		self.progress = ttk.Progressbar(self.right_frame, orient="horizontal", mode="determinate")
		self.progress.pack(fill="x", pady=5)
		self.percent_text = tk.Label(self.right_frame, text="0% of daily target (0h / 8h)")
		self.percent_text.pack()

		# Action Buttons
		btn_box = tk.Frame(self.right_frame)
		btn_box.pack(fill="x", pady=10)
		tk.Button(btn_box, text="+ Add New Log", command=self.open_add_dialog, width=15).pack(side="left", padx=5)
		tk.Button(btn_box, text="Delete Selected", command=self.delete_log, width=15, fg="red").pack(side="left", padx=5)

		# Monthly Total Label
		self.month_total_label = tk.Label(self.root, text="Total for Month: 0h", font=("Arial", 10, "italic"), fg="#7f8c8d")
		self.month_total_label.pack(side="bottom", fill="x", padx=20)

		# Big Submit Button
		self.submit_btn = tk.Button(self.root, text="🚀 SUBMIT WAITING LOGS TO JIRA", 
								   command=self.submit_to_jira, bg="#0056b3", fg="white", 
								   font=("Arial", 12, "bold"), height=2)
		self.submit_btn.pack(side="bottom", fill="x", padx=20, pady=20)

	# --- Logic Methods ---
	def on_date_selected(self, event=None):
		date_str = self.cal.get_date()
		logger.debug(f"Date selected: {date_str}")
		self.date_header.config(text=f"Logs for: {date_str}")
		self.refresh_daily_list(date_str)

	def refresh_daily_list(self, date_str):
		logger.debug(f"Refreshing logs for: {date_str}")
		for i in self.tree.get_children(): self.tree.delete(i)
		day_data = self.db.get(date_str, {"logs": []})
		
		total_m = 0
		for log in day_data["logs"]:
			tag = log.get("status", "waiting")
			self.tree.insert("", "end", values=(log["issue"], log["time"], log["comment"], tag.upper()), tags=(tag,))
			
			total_m += parse_time_to_minutes(log["time"])
		
		# Calculate Logged time display
		log_h = int(total_m // 60)
		log_m = int(total_m % 60)
		logged_text = f"{log_h}h {log_m}m" if log_m > 0 else f"{log_h}h"
		
		percent = min((total_m / 480) * 100, 100)
		self.progress['value'] = percent
		
		# Calculate Remaining time display
		remaining_m = max(480 - total_m, 0)
		rem_h = int(remaining_m // 60)
		rem_m = int(remaining_m % 60)
		
		if remaining_m > 0:
			rem_display = f"{rem_h}h {rem_m}m" if rem_h > 0 else f"{rem_m}m"
			rem_text = f" | Remaining: {rem_display}"
		else:
			rem_text = " | Goal reached! 🎉"

		self.percent_text.config(text=f"{int(percent)}% of daily target ({logged_text} / 8h){rem_text}")
		self.refresh_month_total()

	def refresh_month_total(self):
		month_year = self.cal.get_displayed_month() # returns (month, year)
		month, year = month_year
		month_name = datetime(year, month, 1).strftime("%B")
		
		total_m = 0
		prefix = f"{year}-{month:02d}"
		
		for date_str, data in self.db.items():
			if date_str.startswith(prefix):
				for log in data.get("logs", []):
					total_m += parse_time_to_minutes(log.get("time", "0m"))
		
		total_h = total_m / 60
		logger.debug(f"Month total for {month_name} {year}: {total_h}h")
		self.month_total_label.config(text=f"Total for Month: {total_h:.1f}h")

	def open_add_dialog(self):
		logger.debug("Opening Add Entry dialog")
		win = tk.Toplevel(self.root)
		win.title("Add Worklog Entry")
		win.geometry("300x250")
		
		tk.Label(win, text="Issue Key (e.g. PROJ-123)").pack(pady=2)
		e_issue = tk.Entry(win); e_issue.pack()
		tk.Label(win, text="Time Spent (e.g. 2h, 45m)").pack(pady=2)
		e_time = tk.Entry(win); e_time.pack()
		tk.Label(win, text="Comment").pack(pady=2)
		e_comment = tk.Entry(win); e_comment.pack()

		def save():
			date_str = self.cal.get_date()
			time_val = e_time.get().strip()
			issue_key = e_issue.get().upper().strip()
			logger.debug(f"Attempting to save entry: Issue={issue_key}, Time={time_val}, Date={date_str}")
			
			# Validation
			if not time_val:
				logger.warning("Abort save: Empty time value")
				messagebox.showerror("Error", "กรุณาใส่เวลา (เช่น 2h หรือ 30m)")
				return
			
			minutes = parse_time_to_minutes(time_val)
			if minutes == 0 and time_val != "0":
				logger.warning(f"Abort save: Invalid time format '{time_val}'")
				messagebox.showerror("Error", f"รูปแบบเวลาไม่ถูกต้อง: '{time_val}'\nกรุณาใส่เวลา เช่น 2h, 1.5h, 45m")
				return

			if date_str not in self.db: self.db[date_str] = {"logs": []}
			self.db[date_str]["logs"].append({
				"issue": issue_key,
				"time": time_val,
				"comment": e_comment.get(),
				"status": "waiting"
			})
			save_json(DB_FILE, self.db)
			logger.info(f"Entry saved successfully for {date_str}")
			self.refresh_daily_list(date_str)
			self.refresh_calendar_highlights()
			win.destroy()

		tk.Button(win, text="Save Entry", command=save, bg="#28a745", fg="white").pack(pady=15)

		# Right-click context menu for favorites
		self.fav_menu = tk.Menu(win, tearoff=0)
		self.refresh_context_menu(e_issue, e_comment)
		
		e_issue.bind("<Button-3>", lambda e: self.show_context_menu(e)) # Windows Right Click
		
	def refresh_context_menu(self, entry_issue, entry_comment):
		self.fav_menu.delete(0, "end")
		has_favs = False
		for fav in self.favorites:
			if fav["ticket"].strip():
				has_favs = True
				label = f"{fav['ticket']} | {fav['detail']}"
				self.fav_menu.add_command(label=label, 
					command=lambda t=fav['ticket'], d=fav['detail']: self.fill_from_fav(entry_issue, entry_comment, t, d))
		
		if not has_favs:
			self.fav_menu.add_command(label="No favorites saved", state="disabled")

	def show_context_menu(self, event):
		self.fav_menu.post(event.x_root, event.y_root)

	def fill_from_fav(self, entry_issue, entry_comment, ticket, detail):
		entry_issue.delete(0, tk.END)
		entry_issue.insert(0, ticket)
		entry_comment.delete(0, tk.END)
		entry_comment.insert(0, detail)

	def clear_fav_row(self, idx):
		self.fav_rows[idx]["ticket"].delete(0, tk.END)
		self.fav_rows[idx]["detail"].delete(0, tk.END)

	def load_favorites_to_ui(self):
		for i, fav in enumerate(self.favorites):
			if i < len(self.fav_rows):
				self.fav_rows[i]["ticket"].insert(0, fav.get("ticket", ""))
				self.fav_rows[i]["detail"].insert(0, fav.get("detail", ""))

	def save_favorites(self):
		new_favs = []
		for row in self.fav_rows:
			ticket = row["ticket"].get().strip()
			detail = row["detail"].get().strip()
			if ticket:
				new_favs.append({"ticket": ticket, "detail": detail})
		
		self.favorites = new_favs
		save_json(FAV_FILE, self.favorites)
		logger.info("Favorite tickets saved")
		messagebox.showinfo("Success", "บันทึก Favorite Tickets เรียบร้อยแล้ว")

	def delete_log(self):
		selected = self.tree.selection()
		if not selected: return
		
		date_str = self.cal.get_date()
		item_idx = self.tree.index(selected[0])
		
		log = self.db[date_str]["logs"][item_idx]
		issue_id = log.get("issue", "Unknown")
		
		# 1. ยืนยันการลบเบื้องต้น
		if not messagebox.askyesno("Confirm", f"ต้องการลบรายการ '{issue_id}' ใช่หรือไม่?"):
			return

		# 2. ถ้าส่งไป Jira แล้ว ให้พยายามลบที่ Jira ด้วย
		if log.get("status") == "submitted":
			worklog_id = log.get("worklogId")
			if worklog_id:
				logger.debug(f"Attempting to delete worklog {worklog_id} from Jira for issue {issue_id}")
				auth = HTTPBasicAuth(self.config['email'], self.config['token'])
				headers = {"Accept": "application/json"}
				url = f"{self.config['url'].strip('/')}/rest/api/3/issue/{issue_id}/worklog/{worklog_id}"
				
				try:
					res = requests.delete(url, headers=headers, auth=auth, timeout=10)
					logger.debug(f"Jira Delete Response Code: {res.status_code}")
					if res.status_code == 204:
						logger.info(f"Successfully deleted worklog {worklog_id} from Jira")
					else:
						# ถ้าลบบน Jira ไม่สำเร็จ (เช่น ID หาย หรือติดสิทธิ์) ให้ถามว่าจะลบแค่ในเครื่องไหม
						logger.error(f"Failed to delete from Jira: {res.status_code} - {res.text}")
						if not messagebox.askyesno("Jira Error", f"ไม่สามารถลบข้อมูลจาก Jira ได้ (Status: {res.status_code})\n\nต้องการลบเฉพาะในโปรแกรมนี้หรือไม่?"):
							return
				except Exception as e:
					logger.exception("Connection error during Jira deletion")
					if not messagebox.askyesno("Connection Error", f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}\n\nต้องการลบเฉพาะในโปรแกรมนี้หรือไม่?"):
						return
			else:
				# กรณีไม่มี ID แต่สถานะเป็น submitted
				logger.warning(f"No worklogId found for submitted log {issue_id}")
				messagebox.showwarning("Warning", "ไม่พบ ID ของรายการนี้บน Jira\nข้อมูลใน Jira จะยังคงอยู่ แต่จะลบออกจากเครื่องให้ครับ")

		# 3. ลบออกจาก Local DB
		del self.db[date_str]["logs"][item_idx]
		save_json(DB_FILE, self.db)
		logger.info(f"Entry {issue_id} deleted from local DB")
		self.refresh_daily_list(date_str)
		self.refresh_calendar_highlights()

	def refresh_calendar_highlights(self):
		self.cal.calevent_remove('all')
		for d_str, data in self.db.items():
			total_m = 0
			for l in data["logs"]:
				total_m += parse_time_to_minutes(l["time"])
			
			if total_m >= 480: # 8 hours
				self.cal.calevent_create(datetime.strptime(d_str, "%Y-%m-%d"), "Full", "completed")
			elif total_m > 0: # Partial
				self.cal.calevent_create(datetime.strptime(d_str, "%Y-%m-%d"), "Partial", "partial")

		self.cal.tag_config("completed", background="lightgreen", foreground="black")
		self.cal.tag_config("partial", background="#fffce3", foreground="#856404") # แหลืองจางๆ
		
		# Highlights Holidays
		for d_str, name in self.holidays.items():
			try:
				self.cal.calevent_create(datetime.strptime(d_str, "%Y-%m-%d"), name, "holiday")
			except ValueError:
				logger.warning(f"Invalid holiday date format: {d_str}")
		
		self.cal.tag_config("holiday", background="#a4c2f4", foreground="black") # สีฟ้า



	def submit_to_jira(self):
		date_str = self.cal.get_date()
		logger.debug(f"Starting submit_to_jira for date: {date_str}")
		if date_str not in self.db: 
			logger.debug(f"No logs found in DB for date {date_str}")
			messagebox.showinfo("Info", f"ไม่มีข้อมูลสำหรับวันที่ {date_str}")
			return

		auth = HTTPBasicAuth(self.config['email'], self.config['token'])
		headers = {"Accept": "application/json", "Content-Type": "application/json"}
		logs = self.db[date_str]["logs"]
		
		success = 0
		errors = []
		waiting_count = 0

		for log in logs:
			if log.get("status", "").lower() == "waiting":
				waiting_count += 1
				issue_id = log['issue'].strip()
				url = f"{self.config['url'].strip('/')}/rest/api/3/issue/{issue_id}/worklog"
				logger.debug(f"Submitting log for {issue_id}: {log['time']} to {url}")
				
				payload = {
					"timeSpent": log['time'],
					"started": f"{date_str}T12:00:00.000+0700",
					"comment": {"type": "doc", "version": 1, "content": [{"type": "paragraph", "content": [{"text": log['comment'] or "Log via Python Tool", "type": "text"}]}]}
				}
				try:
					res = requests.post(url, json=payload, headers=headers, auth=auth, timeout=10)
					logger.debug(f"Jira Response Code: {res.status_code}")
					if res.status_code == 201:
						res_data = res.json()
						worklog_id = res_data.get("id")
						logger.info(f"Successfully submitted worklog for {issue_id} (ID: {worklog_id})")
						log["worklogId"] = worklog_id
						log["status"] = "submitted"
						success += 1
					else:
						# Log the specific error from Jira
						try:
							err_msg = res.json().get('errorMessages', [res.text])[0]
						except:
							err_msg = res.text
						logger.error(f"Failed to submit {issue_id}: {res.status_code} - {err_msg}")
						errors.append(f"Issue {log['issue']}: {res.status_code} - {err_msg}")
				except Exception as e:
					logger.exception(f"Exception during submission for {issue_id}")
					errors.append(f"Issue {log['issue']}: Connection Error - {str(e)}")

		logger.debug(f"Finished submission. Success: {success}, Total waiting: {waiting_count}")
		if success > 0:
			save_json(DB_FILE, self.db)
			self.refresh_daily_list(date_str)
			msg = f"ส่งข้อมูลสำเร็จ {success} รายการ"
			if errors:
				msg += "\n\nพบข้อผิดพลาดบางรายการ:\n" + "\n".join(errors)
			messagebox.showinfo("Result", msg)
		elif waiting_count > 0:
			# Found items to send, but all failed
			err_text = "\n".join(errors)
			messagebox.showerror("Submission Error", f"ไม่สามารถส่งข้อมูลได้ (ตรวจพบ {waiting_count} รายการแต่ล้มเหลว):\n\n{err_text}")
		else:
			messagebox.showinfo("Info", "ไม่มีรายการใหม่ที่ต้องส่ง (สถานะ 'waiting')")

if __name__ == "__main__":
	root = tk.Tk()
	app = JiraWorklogApp(root)
	root.mainloop()