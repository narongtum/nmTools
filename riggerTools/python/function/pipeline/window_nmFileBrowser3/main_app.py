import sys
import os
import shutil
import re
import subprocess
import string
from functools import partial
from PySide6.QtGui import QAction, QCursor, QGuiApplication
import datetime as dt
from PySide6.QtWidgets import QLineEdit, QInputDialog, QFileDialog
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QListWidgetItem, 
							   QMessageBox, QMenu, QTextEdit, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, QSize

# --- Import UI Modules ---
# These must match the filenames you generated using pyside6-uic
try:
	from sceneBrowser_ui import Ui_mainWindow
	from passFile_ui import Ui_passFileDialog
except ImportError as e:
	print("Error: Could not import UI files. Please ensure 'sceneBrowser_ui.py' and 'passFile_ui.py' are in the same directory.")
	print(f"Details: {e}")
	sys.exit(1)

# --- Import Maya Sender ---
try:
	from maya_sender import get_maya_sender, send_to_maya
	MAYA_AVAILABLE = True
except ImportError:
	MAYA_AVAILABLE = False
	print("Warning: maya_sender module not found. Maya integration disabled.")

# --- Configuration ---
# You can customize your drive and project lists here
CONFIG = {
	"drives": ["D:\\"], # Add your working drives
	"projects": ["myJob", "NFT"],
	"entity_types": ["asset", "template"],
	"version_padding": 3,
	"folder_structure_depth": {
		# This helps logic understand where it is relative to the root
		# Based on: Drive/Project/Type/Chapter/Sequence/Shot/Job
		"chapter": 0, 
		"sequence": 1,
		"shot": 2,
		"job": 3
	}
}

class PassFileDialog(QDialog, Ui_passFileDialog):
	"""
	Dialog for selecting the destination Job and Element name when passing files.
	"""
	def __init__(self, parent=None, job_list=None):
		super().__init__(parent)
		self.setupUi(self)
		
		if job_list:
			self.jobComboBox.addItems(sorted(job_list))
		
		# Connect Buttons
		self.okPushButton.clicked.connect(self.accept)
		self.canclePushButton.clicked.connect(self.reject)

	def get_data(self):
		"""Returns the user input from the dialog."""
		return {
			'job': self.jobComboBox.currentText(),
			'element': self.elementLineEdit.text().strip()
		}

class NomanFileBrowser(QMainWindow, Ui_mainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Noman Asset Browser (Standalone)")

		# Remove unused top-level menus from the menubar
		try:
			mb = self.menuBar() if hasattr(self, 'menuBar') else None
			if mb is not None:
				if hasattr(self, 'menuAsset') and self.menuAsset is not None:
					mb.removeAction(self.menuAsset.menuAction())
				if hasattr(self, 'menuTools') and self.menuTools is not None:
					mb.removeAction(self.menuTools.menuAction())
		except Exception:
			pass

		# Hide Open/Save/Publish buttons we don't use
		for btn_name in ('openPushButton', 'savePushButton', 'pubPushButton', 'libraryPublishPushButton'):
			try:
				btn = getattr(self, btn_name, None)
				if btn is not None:
					btn.hide()
			except Exception:
				pass

		# Backward-compatible UI aliases (old UI names -> new variable names)
		if not hasattr(self, 'yearListWidget') and hasattr(self, 'chListWidget'):
			self.yearListWidget = self.chListWidget
		if not hasattr(self, 'quoterListWidget') and hasattr(self, 'sqListWidget'):
			self.quoterListWidget = self.sqListWidget
		if not hasattr(self, 'nameListWidget') and hasattr(self, 'shListWidget'):
			self.nameListWidget = self.shListWidget

		# Initialize Data
		self.current_path = None
		self._ctx_busy = False
		
		# Setup UI
		self.populate_defaults()
		self.create_connections()
		
		# Initial refresh
		self.refresh_chapters()

	def populate_defaults(self):
		"""Populate the top-level ComboBoxes from CONFIG."""
		self.driveComboBox.clear()
		self.driveComboBox.addItems(CONFIG["drives"])
		self.projComboBox.clear()
		self.projComboBox.addItems(CONFIG["projects"])
		self.entityTypeComboBox.clear()
		self.entityTypeComboBox.addItems(CONFIG["entity_types"])

	def create_connections(self):
		# Setup context menus for folder creation
		self.chapterMenu = QMenu(self)
		self.chapterMenu.addAction(QAction('Create...', self))
		self.sqMenu = QMenu(self)
		self.sqMenu.addAction(QAction('Create...', self))
		self.shMenu = QMenu(self)
		self.shMenu.addAction(QAction('Create...', self))
		# Process (Job) context menu
		self.procMenu = QMenu(self)
		self.procMenu.addAction(QAction('Create...', self))

		# Top Level Navigation (use lambdas to defer attribute lookup)
		self.driveComboBox.currentIndexChanged.connect(lambda *_: self.refresh_chapters())
		self.projComboBox.currentIndexChanged.connect(lambda *_: self.refresh_chapters())
		self.entityTypeComboBox.currentIndexChanged.connect(lambda *_: self.refresh_chapters())

		# List Widget Navigation (defer lookup)
		self.yearListWidget.itemSelectionChanged.connect(lambda *_: self.refresh_quoters())
		self.quoterListWidget.itemSelectionChanged.connect(lambda *_: self.refresh_names())
		self.nameListWidget.itemSelectionChanged.connect(lambda *_: self.refresh_jobs())
		self.jobListWidget.itemSelectionChanged.connect(lambda *_: self.refresh_files())

		# Right-click context menus for folder creation (defer lookup)
		self.yearListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.yearListWidget.customContextMenuRequested.connect(lambda pos: self.chapterPopupMenu(pos))
		self.quoterListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.quoterListWidget.customContextMenuRequested.connect(lambda pos: self.sequencePopupMenu(pos))
		self.nameListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.nameListWidget.customContextMenuRequested.connect(lambda pos: self.shotPopupMenu(pos))
		self.jobListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.jobListWidget.customContextMenuRequested.connect(lambda pos: self.processPopupMenu(pos))

		# Filters
		self.chapterFilterLineEdit.textChanged.connect(self.filter_list_widget(self.yearListWidget))
		self.sqFilterLineEdit.textChanged.connect(self.filter_list_widget(self.quoterListWidget))
		self.shFilterLineEdit.textChanged.connect(self.filter_list_widget(self.nameListWidget))

		# Actions (Buttons/Menus)
		# Assuming actionPass_File exists in your UI menu or you want to hook it to a button
		if hasattr(self, 'actionPass_File'):
			self.actionPass_File.triggered.connect(lambda checked=False: self.pass_file_operation())

		# File menu actions: Copy Path and Create Date/Time to clipboard
		menu_file = getattr(self, 'menuFile', None)
		if menu_file is None and hasattr(self, 'menuBar'):
			try:
				menu_file = self.menuBar().addMenu('File')
				self.menuFile = menu_file
			except Exception:
				menu_file = None

		if menu_file is not None:
			copyAct = QAction('Copy selected to clipboard', self)
			copyAct.setShortcut('Ctrl+Shift+C')
			copyAct.triggered.connect(lambda checked=False: self.copyFilePathToClipBoard())
			menu_file.addAction(copyAct)

			datetimeAct = QAction('Create date time to clipboard', self)
			datetimeAct.setShortcut('Ctrl+D')
			datetimeAct.triggered.connect(lambda checked=False: self.dateTimeFormat())
			menu_file.addAction(datetimeAct)

			# Import external file into selected process with new naming
			importAct = QAction('Import file to process...', self)
			importAct.setShortcut('Ctrl+I')
			importAct.triggered.connect(lambda checked=False: self.import_file_to_process())
			menu_file.addAction(importAct)
			
			# Maya integration menu
			if MAYA_AVAILABLE:
				menu_file.addSeparator()
				mayaAct = QAction('Send Command to Maya...', self)
				mayaAct.setShortcut('Ctrl+M')
				mayaAct.triggered.connect(lambda checked=False: self.open_maya_sender())
				menu_file.addAction(mayaAct)
		
		# Double click to open folder/file
		self.verListWidget.itemDoubleClicked.connect(lambda *_: self.open_selected_file())
		self.heroListWidget.itemDoubleClicked.connect(lambda *_: self.open_selected_file())
		self.jobListWidget.itemDoubleClicked.connect(lambda *_: self.open_current_folder())
		if hasattr(self, 'libHeroListWidget'):
			self.libHeroListWidget.itemDoubleClicked.connect(lambda item: self.open_lib_hero_file(item))

		# Remove old widget hookups if present (now using year/quoter/name widgets above)
		# Double click on folder lists to open folder in Explorer
		self.yearListWidget.itemDoubleClicked.connect(self.open_folder)
		self.quoterListWidget.itemDoubleClicked.connect(self.open_folder)
		self.nameListWidget.itemDoubleClicked.connect(self.open_folder)



	def get_root_path(self):
		"""Construct the base path Drive/Project/Type, auto-detecting 'all'."""
		drive = self.driveComboBox.currentText()
		proj = self.projComboBox.currentText()
		etype = self.entityTypeComboBox.currentText()
		p_with_all = Path(drive) / proj / 'all' / etype
		p_plain = Path(drive) / proj / etype
		if p_with_all.exists():
			return p_with_all
		if p_plain.exists():
			return p_plain
		# Fallback to 'with_all' to keep structure consistent for creation
		return p_with_all

	# --- Dynamic Project & Entity Type Refresh Methods ---

	def refresh_projects(self):
		"""Lists folders in the Project ComboBox based on selected drive."""
		self.projComboBox.clear()
		drive = self.driveComboBox.currentText()
		if not drive: return
		path = Path(drive)
		if path.exists():
			# Safely iterate directories, skip inaccessible folders
			try:
				iter_entries = path.iterdir()
			except PermissionError:
				iter_entries = []
			items = [d.name for d in iter_entries if d.is_dir()]
			self.projComboBox.addItems(sorted(items))
		# After updating projects, refresh chapters
		self.refresh_chapters()

	def refresh_entity_types(self):
		"""Lists folders in the Entity Type ComboBox based on selected drive and project."""
		self.entityTypeComboBox.clear()
		drive = self.driveComboBox.currentText()
		proj = self.projComboBox.currentText()
		if not drive or not proj:
			return

		path = Path(drive) / proj
		if path.exists():
			# Safely iterate directories, skip inaccessible folders
			try:
				entries = path.iterdir()
			except PermissionError:
				entries = []
			items = [d.name for d in entries if d.is_dir()]
			self.entityTypeComboBox.addItems(sorted(items))

		# Once entities are loaded, refresh chapters
		self.refresh_chapters()

	def refresh_chapters(self):
		"""Lists folders in the Chapter column."""
		self.yearListWidget.clear()
		self.quoterListWidget.clear()
		self.nameListWidget.clear()
		self.jobListWidget.clear()
		self.verListWidget.clear()
		self.heroListWidget.clear()
		if hasattr(self, 'libHeroListWidget'):
			self.libHeroListWidget.clear()

		path = self.get_root_path()
		if path.exists():
			try:
				iter_entries = path.iterdir()
			except PermissionError:
				iter_entries = []
			dirs = [d.name for d in iter_entries if d.is_dir()]
			self.yearListWidget.addItems(sorted(dirs))

	def refresh_quoters(self):
		"""Lists folders in the Sequence column."""
		self.quoterListWidget.clear()
		self.nameListWidget.clear()
		self.jobListWidget.clear()
		if hasattr(self, 'libHeroListWidget'):
			self.libHeroListWidget.clear()
		
		if not self.yearListWidget.currentItem(): return

		path = self.get_root_path() / self.yearListWidget.currentItem().text()
		if path.exists():
			try:
				dirs = [d.name for d in path.iterdir() if d.is_dir()]
				self.quoterListWidget.addItems(sorted(dirs))
			except PermissionError:
				pass

	def refresh_names(self):
		"""Lists folders in the Shot column."""
		self.nameListWidget.clear()
		self.jobListWidget.clear()
		if hasattr(self, 'libHeroListWidget'):
			self.libHeroListWidget.clear()
		
		if not self.quoterListWidget.currentItem(): return

		path = self.get_root_path() / \
		   self.yearListWidget.currentItem().text() / \
		   self.quoterListWidget.currentItem().text()
			   
		if path.exists():
			try:
				dirs = [d.name for d in path.iterdir() if d.is_dir()]
				self.nameListWidget.addItems(sorted(dirs))
			except PermissionError:
				pass

	def refresh_jobs(self):
		"""Lists folders in the Job column."""
		self.jobListWidget.clear()
		# Also refresh Name-level hero files into libHeroListWidget
		if hasattr(self, 'libHeroListWidget'):
			self.libHeroListWidget.clear()
		
		if not self.nameListWidget.currentItem(): return

		path = self.get_root_path() / \
		   self.yearListWidget.currentItem().text() / \
		   self.quoterListWidget.currentItem().text() / \
		   self.nameListWidget.currentItem().text()
			   
		if path.exists():
			try:
				# Exclude 'final' or 'version' if they exist at this level by mistake
				dirs = [d.name for d in path.iterdir() if d.is_dir() and d.name not in ['final', 'version']]
				self.jobListWidget.addItems(sorted(dirs))

				# Populate Name-level hero files into libHeroListWidget
				name_final = path / 'final'
				if hasattr(self, 'libHeroListWidget') and name_final.exists():
					files = [f.name for f in name_final.iterdir() if f.is_file()]
					self.libHeroListWidget.addItems(sorted(files, reverse=True))
			except PermissionError:
				pass

	def refresh_files(self):
		"""Lists files in 'version' and 'final' subfolders."""
		self.verListWidget.clear()
		self.heroListWidget.clear()
		
		if not self.jobListWidget.currentItem(): return
		
		base_path = self.get_root_path() / \
					self.yearListWidget.currentItem().text() / \
					self.quoterListWidget.currentItem().text() / \
					self.nameListWidget.currentItem().text() / \
					self.jobListWidget.currentItem().text()

		# Populate Version List
		ver_path = base_path / 'version'
		if ver_path.exists():
			try:
				files = [f.name for f in ver_path.iterdir() if f.is_file()]
				self.verListWidget.addItems(sorted(files, reverse=True))
			except PermissionError:
				pass


		# Populate Hero (Final) List from both base_path/final and base_path/version/final
		collected = set()
		hero_path = base_path / 'final'
		if hero_path.exists():
			try:
				for f in hero_path.iterdir():
					if f.is_file():
						collected.add(f.name)
			except PermissionError:
				pass
		ver_final_path = ver_path / 'final'
		if ver_final_path.exists():
			try:
				for f in ver_final_path.iterdir():
					if f.is_file():
						collected.add(f.name)
			except PermissionError:
				pass
		if collected:
			self.heroListWidget.addItems(sorted(collected, reverse=True))

	# --- Core Logic: Naming & Versioning ---

	def get_latest_version_number(self, folder_path, element_name):
		"""
		Scans folder for files matching the pattern and returns the next version integer.
		Pattern: *{element_name}*v{number}*
		"""
		path = Path(folder_path)
		if not path.exists():
			return 1 # Start at v001

		max_ver = 0
		# Regex to find 'v' followed by 3 digits
		regex = re.compile(r'v(\d+)')
		
		# Scan all files
		for file in path.iterdir():
			if file.is_file() and element_name.lower() in file.name.lower():
				match = regex.search(file.name)
				if match:
					try:
						ver_num = int(match.group(1))
						if ver_num > max_ver:
							max_ver = ver_num
					except ValueError:
						continue
		
		return max_ver + 1

	# --- Feature: Pass File (Copy & Rename) ---

	def pass_file_operation(self):
		"""
		The main logic to copy a selected file to a new job/element with auto-versioning.
		"""
		# 1. Validate Selection
		selected_item = self.verListWidget.currentItem() or self.heroListWidget.currentItem()
		if not selected_item:
			QMessageBox.warning(self, "Selection Error", "Please select a file to pass.")
			return

		# 2. Identify Source File
		is_hero_list = (self.heroListWidget.currentItem() is not None)
		sub_folder = 'final' if is_hero_list else 'version'
		
		# Reconstruct path variables (use get_root_path() for consistency)
		base_root = self.get_root_path()
		ch = self.yearListWidget.currentItem().text()
		sq = self.quoterListWidget.currentItem().text()
		sh = self.nameListWidget.currentItem().text()
		current_job = self.jobListWidget.currentItem().text()
		filename = selected_item.text()

		source_path = base_root / ch / sq / sh / current_job / sub_folder / filename
		
		# 3. Get Destination Info (Dialog)
		shot_level_path = base_root / ch / sq / sh
		
		# Get list of sibling jobs to show in dialog
		sibling_jobs = []
		if shot_level_path.exists():
			sibling_jobs = [d.name for d in shot_level_path.iterdir() if d.is_dir()]

		dialog = PassFileDialog(self, job_list=sibling_jobs)
		if dialog.exec():
			data = dialog.get_data()
			target_job = data['job']
			target_element = data['element']

			if not target_job:
				QMessageBox.warning(self, "Error", "Target Job cannot be empty.")
				return
			
			# Default element name if empty
			if not target_element:
				target_element = "main"

			# 4. Construct Destination Path
			target_folder = shot_level_path / target_job / 'version'
			
			# Create directories if they don't exist
			target_folder.mkdir(parents=True, exist_ok=True)
			(shot_level_path / target_job / 'final').mkdir(parents=True, exist_ok=True)

			# 5. Determine New Filename
			next_ver = self.get_latest_version_number(target_folder, target_element)
			extension = source_path.suffix
			pad = CONFIG.get('version_padding', 3)
			# Naming Convention: {Shot}_{Job}_{Element}_v{Version}.{ext}
			# Adjust this pattern to match your studio's requirement
			new_filename = f"{sh}_{target_job}_{target_element}_v{next_ver:0{pad}d}{extension}"
			
			destination_path = target_folder / new_filename

			# 6. Perform Copy
			try:
				shutil.copy2(source_path, destination_path)
				print(f"# Copied: {source_path} -> {destination_path}")
				
				# If we passed to the current job, refresh the list
				if target_job == current_job:
					self.refresh_files()
				else:
					QMessageBox.information(self, "Success", f"File Passed to: {target_job}\n{new_filename}")
					
			except Exception as e:
				QMessageBox.critical(self, "Copy Error", f"Failed to copy file:\n{e}")

	# --- Utils ---

	def filter_list_widget(self, list_widget):
		"""Returns a function to filter items in a specific ListWidget."""
		def filter_func(text):
			for i in range(list_widget.count()):
				item = list_widget.item(i)
				item.setHidden(text.lower() not in item.text().lower())
		return filter_func

	def open_selected_file(self):
		"""Opens the selected file with the OS default application."""
		item = self.verListWidget.currentItem() or self.heroListWidget.currentItem()
		if not item: return
		
		is_hero = (self.heroListWidget.currentItem() is not None)
		base = self.get_root_path() / \
		   self.yearListWidget.currentItem().text() / \
		   self.quoterListWidget.currentItem().text() / \
		   self.nameListWidget.currentItem().text() / \
		   self.jobListWidget.currentItem().text()
		if is_hero:
			# Try job/final then version/final
			try_paths = [base / 'final' / item.text(), base / 'version' / 'final' / item.text()]
			for p in try_paths:
				if p.exists():
					os.startfile(p)
					return
		else:
			p = base / 'version' / item.text()
			if p.exists():
				os.startfile(p)

	def open_current_folder(self):
		"""Opens the current Job folder in Explorer."""
		if not self.jobListWidget.currentItem(): return
		
		path = self.get_root_path() / \
		   self.yearListWidget.currentItem().text() / \
		   self.quoterListWidget.currentItem().text() / \
		   self.nameListWidget.currentItem().text() / \
		   self.jobListWidget.currentItem().text()
			   
		if path.exists():
			os.startfile(path)

	def open_lib_hero_file(self, item):
		"""Opens file from Name-level 'final' shown in libHeroListWidget."""
		if not item:
			return
		path = self.get_root_path() / \
		   self.yearListWidget.currentItem().text() / \
		   self.quoterListWidget.currentItem().text() / \
		   self.nameListWidget.currentItem().text() / 'final' / item.text()
		if path.exists():
			os.startfile(path)

	# --- Clipboard Utilities & File menu actions ---
	def dateTimeFormat(self):
		"""Copy a formatted date-time stamp to the system clipboard."""
		current = dt.datetime.now().strftime('%y-%m-%b-%d-%a_')
		QGuiApplication.clipboard().setText(current)
		# Optional: give quick feedback
		try:
			self.statusbar.showMessage(f'Copied: {current}', 2000)
		except Exception:
			pass

	def copyFilePathToClipBoard(self):
		"""Copy the currently selected folder/file path to clipboard based on UI selections."""
		path = self.get_root_path()
		# Drill down based on selections
		if self.yearListWidget.currentItem():
			path = path / self.yearListWidget.currentItem().text()
		if self.quoterListWidget.currentItem():
			path = path / self.quoterListWidget.currentItem().text()
		if self.nameListWidget.currentItem():
			path = path / self.nameListWidget.currentItem().text()
		if self.jobListWidget.currentItem():
			path = path / self.jobListWidget.currentItem().text()
			# If a file is selected in version/final, include it
			if self.verListWidget.currentItem():
				path = path / 'version' / self.verListWidget.currentItem().text()
			elif self.heroListWidget.currentItem():
				path = path / 'final' / self.heroListWidget.currentItem().text()
		else:
			# Optional: library hero list if exists
			if hasattr(self, 'libHeroListWidget') and self.libHeroListWidget.currentItem():
				path = path / 'final' / self.libHeroListWidget.currentItem().text()

		QGuiApplication.clipboard().setText(str(path))
		try:
			self.statusbar.showMessage(f'Copied path: {path}', 2000)
		except Exception:
			pass

	def import_file_to_process(self):
		"""Prompt for a source file and a step name, then copy into the selected process with new naming.

		Naming: Name_Process_Step_v###.ext (### padded to 3). Uses 'version' subfolder.
		"""
		# 1) Select file
		src_path_str, _ = QFileDialog.getOpenFileName(self, 'Select file to import')
		if not src_path_str:
			return
		src_path = Path(src_path_str)

		# 2) Step name
		step, ok = QInputDialog.getText(self, 'Step name', 'Enter step:')
		if not ok:
			return
		step = step.strip()
		if not step:
			QMessageBox.warning(self, 'Input required', 'Please enter a step name.')
			return
		# sanitize step to filename-friendly
		step = re.sub(r'\s+', '_', step)

		# 3) Validate selections (year, month, name, process)
		missing = []
		if not self.yearListWidget.currentItem():
			missing.append('Year')
		if not self.quoterListWidget.currentItem():
			missing.append('Month')
		if not self.nameListWidget.currentItem():
			missing.append('Name')
		if not self.jobListWidget.currentItem():
			missing.append('Process')
		if missing:
			QMessageBox.warning(self, 'Selection required', 'Please select: ' + ', '.join(missing))
			return

		# 4) Build destination folder (version under current process)
		dest_base = self.get_root_path() / \
			self.yearListWidget.currentItem().text() / \
			self.quoterListWidget.currentItem().text() / \
			self.nameListWidget.currentItem().text() / \
			self.jobListWidget.currentItem().text()
		version_folder = dest_base / 'version'
		version_folder.mkdir(parents=True, exist_ok=True)

		# 5) Compose filename and determine next version
		name_part = self.nameListWidget.currentItem().text()
		proc_part = self.jobListWidget.currentItem().text()
		stem = f"{name_part}_{proc_part}_{step}"
		next_ver = self.get_latest_version_number(version_folder, stem)
		ext = src_path.suffix
		pad = CONFIG.get('version_padding', 3)
		dest_name = f"{stem}_v{next_ver:0{pad}d}{ext}"
		dest_path = version_folder / dest_name

		# 6) Copy
		try:
			shutil.copy2(src_path, dest_path)
			# Feedback + refresh
			try:
				self.statusbar.showMessage(f'Imported: {dest_name}', 3000)
			except Exception:
				pass
			self.refresh_files()
		except Exception as e:
			QMessageBox.critical(self, 'Import failed', f'Could not import file:\n{e}')

	def open_folder(self, item):
		"""Opens the selected folder in Explorer."""
		base = self.get_root_path()
		sender = self.sender()
		if sender == self.yearListWidget:
			path = base / item.text()
		elif sender == self.quoterListWidget:
			ch = self.yearListWidget.currentItem().text()
			path = base / ch / item.text()
		elif sender == self.nameListWidget:
			ch = self.yearListWidget.currentItem().text()
			sq = self.quoterListWidget.currentItem().text()
			path = base / ch / sq / item.text()
		elif sender == self.jobListWidget:
			ch = self.yearListWidget.currentItem().text()
			sq = self.quoterListWidget.currentItem().text()
			sh = self.nameListWidget.currentItem().text()
			path = base / ch / sq / sh / self.jobListWidget.currentItem().text()
		else:
			return
		if path.exists():
			os.startfile(path)
			
		# --- Folder Creation Context Menus ---

	# --- Folder Creation Context Menus ---

	# --- Folder Creation Context Menus (override last) ---
	def chapterPopupMenu(self, pos):
		"""Context menu for Years: on Create... open input and make folder."""
		if self._ctx_busy:
			return
		self._ctx_busy = True
		try:
			action = self.chapterMenu.exec(self.yearListWidget.mapToGlobal(pos))
			if not action or action.text() != 'Create...':
				return
			name, ok = QInputDialog.getText(self, "Create Year", "Folder name:")
			if not ok or not name.strip():
				return
			base = self.get_root_path()
			path = base / name.strip()
			os.makedirs(path, exist_ok=True)
			self.refresh_chapters()
		finally:
			self._ctx_busy = False

	def sequencePopupMenu(self, pos):
		"""Context menu for Month: on Create... open input and make folder under selected Year."""
		if self._ctx_busy:
			return
		self._ctx_busy = True
		try:
			action = self.sqMenu.exec(self.quoterListWidget.mapToGlobal(pos))
			if not action or action.text() != 'Create...':
				return
			year = self.yearListWidget.currentItem().text() if self.yearListWidget.currentItem() else ''
			if not year:
				return
			name, ok = QInputDialog.getText(self, "Create Month", "Folder name:")
			if not ok or not name.strip():
				return
			base = self.get_root_path()
			path = base / year / name.strip()
			os.makedirs(path, exist_ok=True)
			self.refresh_quoters()
		finally:
			self._ctx_busy = False

	def shotPopupMenu(self, pos):
		"""Context menu for Name: on Create... open input and make folder under selected Year/Month."""
		if self._ctx_busy:
			return
		self._ctx_busy = True
		try:
			action = self.shMenu.exec(self.nameListWidget.mapToGlobal(pos))
			if not action or action.text() != 'Create...':
				return
			year = self.yearListWidget.currentItem().text() if self.yearListWidget.currentItem() else ''
			month = self.quoterListWidget.currentItem().text() if self.quoterListWidget.currentItem() else ''
			if not year or not month:
				return
			name, ok = QInputDialog.getText(self, "Create Name", "Folder name:")
			if not ok or not name.strip():
				return
			base_root = self.get_root_path()
			new_name = name.strip()
			base = base_root / year / month / new_name
			os.makedirs(base, exist_ok=True)
			# Scaffold department folders and their subfolders
			dept_names = ['final', 'design', 'footage']
			sub_folders = ['final', 'version', 'output']
			for d in dept_names:
				dp = base / d
				os.makedirs(dp, exist_ok=True)
				for sf in sub_folders:
					os.makedirs(dp / sf, exist_ok=True)
			# Refresh Name list and select the newly created one
			self.refresh_names()
			for i in range(self.nameListWidget.count()):
				it = self.nameListWidget.item(i)
				if it and it.text() == new_name:
					self.nameListWidget.setCurrentRow(i)
					break
			# Now refresh Process list to show dept_names
			self.refresh_jobs()
		finally:
			self._ctx_busy = False

	def processPopupMenu(self, pos):
		"""Context menu for Process: create new process under selected Name with inner folders.

		Creates the folder structure: version, final, data, output
		"""
		if self._ctx_busy:
			return
		self._ctx_busy = True
		try:
			action = self.procMenu.exec(self.jobListWidget.mapToGlobal(pos))
			if not action or action.text() != 'Create...':
				return
			# Validate parent selections (Year, Month, Name)
			if not (self.yearListWidget.currentItem() and self.quoterListWidget.currentItem() and self.nameListWidget.currentItem()):
				return
			proc_name, ok = QInputDialog.getText(self, "Create Process", "Process name:")
			if not ok:
				return
			proc_name = proc_name.strip()
			if not proc_name:
				return
			# sanitize to filesystem-friendly
			proc_name = re.sub(r"\s+", "_", proc_name)

			base_root = self.get_root_path()
			year = self.yearListWidget.currentItem().text()
			month = self.quoterListWidget.currentItem().text()
			name = self.nameListWidget.currentItem().text()
			process_base = base_root / year / month / name / proc_name
			os.makedirs(process_base, exist_ok=True)

			inner_folder_list = ['version', 'final', 'data', 'output']
			for sub in inner_folder_list:
				os.makedirs(process_base / sub, exist_ok=True)

			# Refresh and select newly created process
			self.refresh_jobs()
			for i in range(self.jobListWidget.count()):
				it = self.jobListWidget.item(i)
				if it and it.text() == proc_name:
					self.jobListWidget.setCurrentRow(i)
					break
			self.refresh_files()
		finally:
			self._ctx_busy = False

	def open_maya_sender(self):
		"""Open the Maya command sender dialog"""
		if not MAYA_AVAILABLE:
			QMessageBox.warning(self, "Error", "Maya sender module not available.")
			return
		
		from maya_dialog import MayaCommandDialog
		
		# Get currently selected file if any
		current_item = None
		if hasattr(self, 'verListWidget'):
			current_item = self.verListWidget.currentItem()
		
		file_path = None
		if current_item:
			# Try to build the full path from current selection
			file_path = self.get_current_file_path()
		
		dialog = MayaCommandDialog(self, file_path)
		dialog.exec()

	def get_current_file_path(self):
		"""Get the full path of the currently selected file"""
		try:
			if hasattr(self, 'verListWidget'):
				item = self.verListWidget.currentItem()
				if item:
					file_name = item.text()
					# Build from current_path if available
					if self.current_path:
						full_path = self.current_path / file_name
						return str(full_path)
		except Exception as e:
			print(f"Error getting file path: {e}")
		
		return None

if __name__ == "__main__":
	app = QApplication(sys.argv)
	
	# Optional: Set Style to Fusion for better look on Windows
	app.setStyle("Fusion")
	
	window = NomanFileBrowser()
	window.show()
	sys.exit(app.exec())