from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import os

FFMPEG = r'D:\\sysTools\\nmTools\\riggerTools\\python\\function\\pipeline\\playBlast\\framework\\ffmpeg-20181016-b2adc31-win64-static\\bin\\ffmpeg.exe'



"""
 modify from  Raures
 https://python-forum.io/Thread-PyQt-Drag-and-drop-converter
"""

"""
read the txt file for the path (ignore it)
"""


"""
savePath = ""
settingsFilePath = Path("settings.txt")
 
if not settingsFilePath.is_file():
	f = open("settings.txt", "w")
	savePath = os.environ["HOMEPATH"] + "\\Desktop\\"
	f.write(savePath)
	f.close()
else:
	f = open("settings.txt", "r")
	savePath = f.readline()
	f.close()
"""




# when drop what will happen
def convertMedia(INPUT_PATH):

	print (INPUT_PATH)
	indexIn = INPUT_PATH.index('.')
	cleanIn = (INPUT_PATH[:indexIn])
	print (cleanIn)
	OUTPUT_PATH = cleanIn + '_lite.mp4'
	ffFormat = '-acodec aac' , '-pix_fmt yuv420p'
	print ('\nUsing {} format.'.format(ffFormat[1])) 
	cmd ='%s -i %s -f mp4 -vcodec libx264 -preset fast -profile:v main %s %s ' %( FFMPEG , INPUT_PATH, ffFormat[1] , OUTPUT_PATH)
	print (cmd)
	# subprocess.call(cmd)
	os.system(cmd)
	print ( "# # # # # Convert Complete # # # # # ")
	# print( '\nconverted path file is ' +str(OUTPUT_PATH) )
	# os.system('pyuic5 -o "' + savePath + '/convertedfile.py" "' + target + '"')




class Label(QtWidgets.QLabel):
	def __init__(self):
		super(Label, self).__init__()
 
		self.setAcceptDrops(True)
 
	def dragEnterEvent(self, e): # guess check the text file when drag the data to the area
		if e.mimeData().hasFormat("text/uri-list"):
			print ('this is correct format')
			e.accept()
		else:
			e.ignore()
 
	def dropEvent(self, e):
		print (e.mimeData().text()[8:])
		print ('Sending file path ...')
		convertMedia(e.mimeData().text()[8:])
 
class MainWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
 
		self.windowTitle = "FFmgeg Converter: "
		self.windowSize = (438, 348)
 
		self.setupUi(self)
 
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setWindowTitle(self.windowTitle)
		Form.resize(self.windowSize[0], self.windowSize[1])
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.frame = QtWidgets.QFrame(Form)
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.labelIcon = QtWidgets.QLabel(self.frame)
		self.labelIcon.setMaximumSize(QtCore.QSize(50, 50))
		self.labelIcon.setText("")
		self.labelIcon.setPixmap(QtGui.QPixmap("info.png"))
		self.labelIcon.setScaledContents(True)
		self.labelIcon.setObjectName("labelIcon")
		self.horizontalLayout.addWidget(self.labelIcon)
		self.labelInfo = QtWidgets.QLabel(self.frame)
		self.labelInfo.setWordWrap(True)
		self.labelInfo.setObjectName("labelInfo")
		# self.labelInfo.setText("Before converting, please make sure that you have PyQt5 installed. To install PyQt5, you can visit <a href='https://sourceforge.net/projects/pyqt/'>this link</a> to download it, or run the following command in <b>cmd</b>: <font face='Consolas'>pip3 install PyQt5</font>")
		self.labelInfo.setText("Convert file will be on the same directory of source file.")
		self.labelInfo.setOpenExternalLinks(True)
		self.horizontalLayout.addWidget(self.labelInfo)
		self.horizontalLayout_2.addLayout(self.horizontalLayout)
		self.verticalLayout.addWidget(self.frame)
		self.frame_2 = QtWidgets.QFrame(Form)
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout()
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.labelTarget = Label()
		# what is it?
		font = QtGui.QFont()
		font.setFamily("Myanmar Text")
		self.labelTarget.setFont(font)
		self.labelTarget.setAlignment(QtCore.Qt.AlignCenter)
		self.labelTarget.setObjectName("labelTarget")
		self.labelTarget.setText("Drag and drop the <b>Media file</b> (<b>*.mov</b>) here")
		self.labelTarget.setStyleSheet("QLabel { border: 1px dotted black; }")
		self.labelTarget.setMinimumHeight(150)
		self.labelTarget.setAcceptDrops(True)
		self.verticalLayout_5.addWidget(self.labelTarget)
		self.horizontalLayout_3.addLayout(self.verticalLayout_5)
		self.verticalLayout.addWidget(self.frame_2)
		self.frame_3 = QtWidgets.QFrame(Form)
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.labelQuestion = QtWidgets.QLabel(self.frame_3)
		self.labelQuestion.setObjectName("labelQuestion")
		# self.labelQuestion.setText("Where should the <b>python</b> file be saved at?")
		self.verticalLayout_3.addWidget(self.labelQuestion)
		self.frame_4 = QtWidgets.QFrame(self.frame_3)
		self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setObjectName("frame_4")
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		# self.inputDirectory = QtWidgets.QLineEdit(self.frame_4)
		# self.inputDirectory.setObjectName("inputDirectory")
		# self.inputDirectory.setText(savePath)
		# self.inputDirectory.setStyleSheet("QLineEdit { padding-bottom: 2px; padding-left: 2px; }")
		# self.horizontalLayout_5.addWidget(self.inputDirectory)
		# self.buttonBrowse = QtWidgets.QPushButton(self.frame_4)
		# self.buttonBrowse.setObjectName("buttonBrowse")
		# self.buttonBrowse.setText("Browse")
		# self.horizontalLayout_5.addWidget(self.buttonBrowse)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
		self.verticalLayout_3.addWidget(self.frame_4)
		self.verticalLayout_4.addLayout(self.verticalLayout_3)
		self.verticalLayout.addWidget(self.frame_3)
		self.verticalLayout_2.addLayout(self.verticalLayout)
 
		QtCore.QMetaObject.connectSlotsByName(Form)
 
		# self.buttonBrowse.clicked.connect(self.browsePath)
	"""
	def browsePath(self):
		savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory"))
		self.inputDirectory.setText(savePath)
		with open(settingsFilePath, "w") as f:
			f.write(savePath)
	"""
 
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	hGUI = QtWidgets.QWidget()
	ui = MainWindow()
	ui.setupUi(hGUI)
	hGUI.show()
	sys.exit(app.exec_())