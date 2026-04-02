import json
import os

# เส้นทางไฟล์ mirrortable.json ที่จะโดนแก้
json_path = r"d:\sysTools\nmTools_github\riggerTools\python\function\animation\mirrorAnimation\mirrortable.json"

# เปิดไฟล์ขึ้นมาอ่าน
with open(json_path, 'r', encoding='utf-8') as f:
	data = json.load(f)

# กำหนดแกนตามที่คุณทดสอบใน Shaman_make_mirror.py
rules = {
	'cog_ctrl': [-1, 1, 1],
	'hip_ctrl': [-1, 1, 1],
	'spine01FK_ctrl': [-1, 1, 1],
	'spine02FK_ctrl': [-1, 1, 1],
	'spine03FK_ctrl': [-1, 1, 1],
	'neck_ctrl': [-1, 1, 1],
	'head_ctrl': [-1, 1, 1],

	#... Arm
	'clvRGT_ctrl': [1, -1, 1],
	'armRGTIK_ctrl': [-1, -1, -1],
	'clvLFT_ctrl': [1, -1, 1],
	'armLFTIK_ctrl': [-1, -1, -1],

	'upperLegLFTIK_ctrl': [-1, 1, 1],
	'footLFTIK_ctrl': [-1, 1, 1],

	'upperLegRGTIK_ctrl': [-1, 1, 1],
	'footRGTIK_ctrl': [-1, 1, 1],

}

updates = 0

# วนลูปเช็ค Controller ทุกชิ้นใน JSON
for key in data.get('objects', {}):
	# ตัดเอาเฉพาะชื่อ Name ไม่รวม Namespace
	short_name = key.split(':')[-1]
	
	# ถ้าชื่อตรงกับ Dict ของเราเป๊ะๆ จะป้อนแกนตามนั้นเลย
	if short_name in rules:
		data['objects'][key]['mirrorAxis'] = rules[short_name]
		updates += 1
		print("Updated {} to {}".format(short_name, rules[short_name]))
	
	# กฎพิเศษ: ถ้าเป็นจำพวก strip ให้ตั้งเป็น YZ Plane ให้หมด
	elif 'strip' in short_name.lower():
		data['objects'][key]['mirrorAxis'] = [-1, 1, 1]
		updates += 1
		print("Updated {} to [-1, 1, 1] (strip rule)".format(short_name))
		
# นำข้อมูลที่แก้แล้ว Save ทับไฟล์เดิมกลับลงไป
with open(json_path, 'w', encoding='utf-8') as f:
	json.dump(data, f, indent=2)

print("\nTotal updates made: {}".format(updates))
