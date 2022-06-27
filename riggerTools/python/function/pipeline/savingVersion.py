# Writing in python 3 syntax
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import os
import sys
import shutil 











# when drop what will happen
def savingToVersion(INPUT_PATH):
	# script for pass file hero to version with same naming convention
	# todo
	# 1. get the file path and file name
	# 2. check the version folder if not exists just create
	# 3. if already "version" exists qury file in that folder find the maximum number if NotImplemented saving v001
	# 4. copy the file name at 1. rename with the proper version and copy to the version 



	# path file


	dirName = os.path.dirname(INPUT_PATH)
	fileName = os.path.basename(INPUT_PATH)


	extension = os.path.splitext(fileName)[1]
	extLen = len(extension)

	versionDir = dirName + '\\version'



	# if os.path.exists(versionDir):
	# 	print 'This folder has exists.'


	if not os.path.exists(versionDir):
		try:
			os.makedirs(versionDir)
			print ('folder create')
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	else:
		print ('The folder has exists.')


			

	#if fileTools.checkExistFolder( filename = versionDir ):
	#	print 'This folder has exists.'


	allFile = os.listdir(versionDir)
	# spName = fileName.split('hero'+extension)[0]
	spName = fileName.split(extension)[0]
	workLst = []
	num = 0 

	for each in allFile:
		if each[-extLen:] == extension:
			# 'there is already this extension in version folder'

			if spName in each:
				# 'there is already this job in version folder'
				# 'find latest version'
				workLst.append(each)
				num = num + 1
				print (each)

			else:
				continue


		else:
			print (each)








	 
	if workLst:
		print ('There is already this job in version folder.\n')
		# extract

		if num <= 9:
			digit = 3
		elif num > 9:
			 digit = 3

		version = num + 1
		strNum = str(version)
		replaceVer = strNum.zfill(digit)

		latestFile = spName +'_'+ 'v' + replaceVer + extension


	else:
		print ('There is no job in version folder.\n')
		latestFile = spName + '_v001' + extension
		


	shutil.copy( INPUT_PATH , versionDir + '\\' + latestFile )


	#fileTools.openContainerFile(versionDir)
	print ('Saving file version >>>>>> %s' %(latestFile))







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
		# convertMedia(e.mimeData().text()[8:])
		savingToVersion(e.mimeData().text()[8:])
 
class MainWindow(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
 
		self.windowTitle = "Saving to version: "
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
		self.labelInfo.setText("The version file will be on the version folder")
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
		self.labelTarget.setText("Drag and drop the <b>Hero file</b> here")
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
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
		self.verticalLayout_3.addWidget(self.frame_4)
		self.verticalLayout_4.addLayout(self.verticalLayout_3)
		self.verticalLayout.addWidget(self.frame_3)
		self.verticalLayout_2.addLayout(self.verticalLayout)
 
		QtCore.QMetaObject.connectSlotsByName(Form)
 

 
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	hGUI = QtWidgets.QWidget()
	ui = MainWindow()
	ui.setupUi(hGUI)
	hGUI.show()
	sys.exit(app.exec_())