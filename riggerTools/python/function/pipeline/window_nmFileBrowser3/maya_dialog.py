"""
Maya Command Sender Dialog
UI for sending code/commands to Autodesk Maya
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTextEdit, 
							   QPushButton, QLabel, QComboBox, QMessageBox)
from PySide6.QtCore import Qt
from maya_sender import get_maya_sender, send_to_maya


class MayaCommandDialog(QDialog):
	"""Dialog for sending commands to Maya"""
	
	def __init__(self, parent=None, file_path=None):
		super().__init__(parent)
		self.file_path = file_path
		self.maya_sender = get_maya_sender()
		self.setup_ui()
		
	def setup_ui(self):
		"""Setup the dialog UI"""
		self.setWindowTitle("Send to Maya")
		self.setGeometry(100, 100, 600, 400)
		
		layout = QVBoxLayout()
		
		# Language selector
		lang_layout = QHBoxLayout()
		lang_layout.addWidget(QLabel("Command Type:"))
		self.lang_combo = QComboBox()
		self.lang_combo.addItems(["MEL", "Python"])
		lang_layout.addWidget(self.lang_combo)
		lang_layout.addStretch()
		layout.addLayout(lang_layout)
		
		# Command/Code editor
		layout.addWidget(QLabel("Command/Code:"))
		self.code_edit = QTextEdit()
		self.code_edit.setPlaceholderText("Enter MEL or Python code here...\n\nExample:\n  sphere;\n\nOr Python:\n  import maya.cmds as cmds\n  cmds.sphere()")
		layout.addWidget(self.code_edit)
		
		# Buttons
		button_layout = QHBoxLayout()
		
		send_btn = QPushButton("Send to Maya")
		send_btn.clicked.connect(self.send_command)
		button_layout.addWidget(send_btn)
		
		if self.file_path:
			load_btn = QPushButton("Load File in Maya")
			load_btn.clicked.connect(self.load_file_in_maya)
			button_layout.addWidget(load_btn)
		
		close_btn = QPushButton("Close")
		close_btn.clicked.connect(self.close)
		button_layout.addWidget(close_btn)
		
		layout.addLayout(button_layout)
		self.setLayout(layout)
	
	def send_command(self):
		"""Send the command to Maya"""
		command = self.code_edit.toPlainText().strip()
		if not command:
			QMessageBox.warning(self, "Error", "Please enter a command or code snippet.")
			return
		
		is_python = self.lang_combo.currentText() == "Python"
		success, response = send_to_maya(command, is_python=is_python)
		
		if success:
			QMessageBox.information(self, "Success", f"Command sent to Maya.\n\nResponse:\n{response}")
		else:
			QMessageBox.critical(self, "Error", f"Failed to send command:\n\n{response}")
	
	def load_file_in_maya(self):
		"""Load the current file in Maya"""
		if not self.file_path:
			QMessageBox.warning(self, "Error", "No file path available.")
			return
		
		sender = get_maya_sender()
		success, msg = sender.send_file_to_maya(self.file_path)
		
		if success:
			QMessageBox.information(self, "Success", f"File loaded in Maya:\n{self.file_path}")
		else:
			QMessageBox.critical(self, "Error", f"Failed to load file:\n\n{msg}")
