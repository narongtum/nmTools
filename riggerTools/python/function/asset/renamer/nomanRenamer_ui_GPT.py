# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nomanRenamer_v012.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

'''
from function.framework.Qtpy.Qt import QtCore, QtGui, QtWidgets
from function.asset.renamer import nomanRenamer_ui_GPT
reload(nomanRenamer_ui_GPT)
Form = QtWidgets.QWidget()
ui = nomanRenamer_ui_GPT.Ui_ReNameUi()
ui.setupUi(Form)
Form.show()
'''






from function.framework.reloadWrapper import reloadWrapper as reload

import logging
logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)
logger.info('Start of %s module' %__name__)


import maya.cmds as mc

MAYA_VERSION = int(mc.about(v=True))

print(MAYA_VERSION)
type(MAYA_VERSION)

from function.framework.Qtpy.Qt import QtCore, QtGui, QtWidgets
from function.rigging.util import misc as misc

if MAYA_VERSION >= 2022:
	import importlib
	importlib.reload( misc )
else:
	reload( misc )








# from Qt import QtCore, QtGui, QtWidgets

naming_txtField = 'object@##'

alphabet = (	'A','B','C','D','E','F','G','H','L','J','K','M','N',
				'O','P','Q','R','S','T','U','V','W','X','Y','Z'			)



try:
	from shiboken2 import wrapInstance
except:
	from sid import wrapInstance as wrapInstance




# get this window on top
# chad vernon said about parent window on top at 1:16 (crateing the remapping dialog)


import maya.OpenMayaUI as OpenMayaUI

def getMayaMainWindow():# still fail why ?
	main_window_ptr = OpenMayaUI.MQtUtil.mainWindow() # find maya pointer
	if MAYA_VERSION >= 2022:
		pointer = wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
	else:
		pointer = wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
	return pointer



def replace_sharp_pattern(name_pattern, index):
	import re
	pattern = re.compile(r"(#+)")
	match = pattern.search(name_pattern)
	if match:
		num_digits = len(match.group(1))
		return pattern.sub(str(index).zfill(num_digits), name_pattern, count=1)
	return name_pattern


class Ui_ReNameUi(QtWidgets.QWidget):
	def __init__(self):
		parent = getMayaMainWindow()
		super(Ui_ReNameUi, self).__init__(parent=parent)
		
		
	def setupUi(self, ReNameUi):
		
		self.setObjectName('ReNameUi')
		self.resize(476, 389)
		self.setMinimumSize(QtCore.QSize(476, 355))
		self.setMaximumSize(QtCore.QSize(476, 389))
		self.layoutWidget = QtWidgets.QWidget(ReNameUi)
		self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 430, 81))
		self.layoutWidget.setObjectName("layoutWidget")
		self.editName_layout = QtWidgets.QGridLayout(self.layoutWidget)
		self.editName_layout.setContentsMargins(2, 0, 0, 0)
		self.editName_layout.setObjectName("editName_layout")
		self.prefix_txtField = QtWidgets.QLineEdit(self.layoutWidget)
		self.prefix_txtField.setMaximumSize(QtCore.QSize(100, 16777215))
		self.prefix_txtField.setObjectName("prefix_txtField")
		self.editName_layout.addWidget(self.prefix_txtField, 0, 0, 1, 1)
		self.suffix_txtField = QtWidgets.QLineEdit(self.layoutWidget)
		self.suffix_txtField.setMaximumSize(QtCore.QSize(100, 16777215))
		self.suffix_txtField.setObjectName("suffix_txtField")
		self.editName_layout.addWidget(self.suffix_txtField, 0, 4, 1, 1)
		self.prefix_btn = QtWidgets.QPushButton(self.layoutWidget)
		self.prefix_btn.setMaximumSize(QtCore.QSize(100, 16777215))
		self.prefix_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.prefix_btn.setObjectName("prefix_btn")
		self.editName_layout.addWidget(self.prefix_btn, 1, 0, 1, 1)
		spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.editName_layout.addItem(spacerItem, 1, 3, 1, 1)
		self.base_btn = QtWidgets.QPushButton(self.layoutWidget)
		self.base_btn.setMaximumSize(QtCore.QSize(122, 16777215))
		self.base_btn.setObjectName("base_btn")
		self.editName_layout.addWidget(self.base_btn, 1, 2, 1, 1)
		self.suffix_btn = QtWidgets.QPushButton(self.layoutWidget)
		self.suffix_btn.setMaximumSize(QtCore.QSize(100, 16777215))
		self.suffix_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.suffix_btn.setObjectName("suffix_btn")
		self.editName_layout.addWidget(self.suffix_btn, 1, 4, 1, 1)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.editName_layout.addItem(spacerItem1, 1, 1, 1, 1)
		self.base_txtField = QtWidgets.QLineEdit(self.layoutWidget)
		self.base_txtField.setObjectName("base_txtField")
		self.editName_layout.addWidget(self.base_txtField, 0, 1, 1, 3)
		self.effect_check = QtWidgets.QCheckBox(self.layoutWidget)
		self.effect_check.setObjectName("effect_check")

		# make alway check
		self.effect_check.setChecked(True)

		self.editName_layout.addWidget(self.effect_check, 2, 0, 1, 1)
		self.autoSuffix_check = QtWidgets.QCheckBox(self.layoutWidget)
		self.autoSuffix_check.setObjectName("autoSuffix_check")
		self.editName_layout.addWidget(self.autoSuffix_check, 2, 4, 1, 1)
		self.insert_txext = QtWidgets.QLabel(self.layoutWidget)
		self.insert_txext.setObjectName("insert_txext")
		self.editName_layout.addWidget(self.insert_txext, 2, 2, 1, 1)
		self.layoutWidget1 = QtWidgets.QWidget(ReNameUi)
		self.layoutWidget1.setGeometry(QtCore.QRect(20, 260, 431, 87))
		self.layoutWidget1.setObjectName("layoutWidget1")
		self.replace_layout = QtWidgets.QGridLayout(self.layoutWidget1)
		self.replace_layout.setContentsMargins(2, 4, 2, 6)
		self.replace_layout.setVerticalSpacing(7)
		self.replace_layout.setObjectName("replace_layout")
		self.search_txtField = QtWidgets.QLineEdit(self.layoutWidget1)
		self.search_txtField.setObjectName("search_txtField")
		self.replace_layout.addWidget(self.search_txtField, 0, 1, 1, 1)
		self.replace_text = QtWidgets.QLabel(self.layoutWidget1)
		self.replace_text.setObjectName("replace_text")
		self.replace_layout.addWidget(self.replace_text, 1, 0, 1, 1)
		self.replace_txtField = QtWidgets.QLineEdit(self.layoutWidget1)
		self.replace_txtField.setObjectName("replace_txtField")
		self.replace_layout.addWidget(self.replace_txtField, 1, 1, 1, 1)
		self.searchNReplace_btn = QtWidgets.QPushButton(self.layoutWidget1)
		self.searchNReplace_btn.setMaximumSize(QtCore.QSize(16777215, 35))
		self.searchNReplace_btn.setObjectName("searchNReplace_btn")
		self.replace_layout.addWidget(self.searchNReplace_btn, 2, 0, 1, 2)
		self.search_text = QtWidgets.QLabel(self.layoutWidget1)
		self.search_text.setObjectName("search_text")
		self.replace_layout.addWidget(self.search_text, 0, 0, 1, 1)
		self.layoutWidget2 = QtWidgets.QWidget(ReNameUi)
		self.layoutWidget2.setGeometry(QtCore.QRect(20, 150, 431, 44))
		self.layoutWidget2.setObjectName("layoutWidget2")
		self.addPosition_layout = QtWidgets.QGridLayout(self.layoutWidget2)
		self.addPosition_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
		self.addPosition_layout.setContentsMargins(0, 0, 0, 0)
		self.addPosition_layout.setObjectName("addPosition_layout")
		self.LWR_btn = QtWidgets.QPushButton(self.layoutWidget2)
		self.LWR_btn.setMaximumSize(QtCore.QSize(60, 30))
		self.LWR_btn.setObjectName("LWR_btn")
		self.addPosition_layout.addWidget(self.LWR_btn, 1, 5, 1, 1)
		self.LFT_btn = QtWidgets.QPushButton(self.layoutWidget2)
		self.LFT_btn.setMaximumSize(QtCore.QSize(60, 30))
		self.LFT_btn.setObjectName("LFT_btn")
		self.addPosition_layout.addWidget(self.LFT_btn, 1, 0, 1, 1)
		self.BAK_btn = QtWidgets.QPushButton(self.layoutWidget2)
		self.BAK_btn.setMaximumSize(QtCore.QSize(60, 30))
		self.BAK_btn.setObjectName("BAK_btn")
		self.addPosition_layout.addWidget(self.BAK_btn, 1, 3, 1, 1)
		self.RGT_btn = QtWidgets.QPushButton(self.layoutWidget2)
		self.RGT_btn.setMaximumSize(QtCore.QSize(60, 30))
		self.RGT_btn.setObjectName("RGT_btn")
		self.addPosition_layout.addWidget(self.RGT_btn, 1, 1, 1, 1)
		self.FRT_btn = QtWidgets.QPushButton(self.layoutWidget2)
		self.FRT_btn.setMaximumSize(QtCore.QSize(60, 30))
		self.FRT_btn.setObjectName("FRT_btn")
		self.addPosition_layout.addWidget(self.FRT_btn, 1, 2, 1, 1)
		self.UPR_btn = QtWidgets.QPushButton(self.layoutWidget2)
		self.UPR_btn.setMaximumSize(QtCore.QSize(60, 30))
		self.UPR_btn.setObjectName("UPR_btn")
		self.addPosition_layout.addWidget(self.UPR_btn, 1, 4, 1, 1)
		self.addPosition_text = QtWidgets.QLabel(self.layoutWidget2)
		self.addPosition_text.setObjectName("addPosition_text")
		self.addPosition_layout.addWidget(self.addPosition_text, 0, 0, 1, 2)
		self.horizontalLayoutWidget_2 = QtWidgets.QWidget(ReNameUi)
		self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 200, 431, 31))
		self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
		self.execName_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
		self.execName_layout.setContentsMargins(4, 0, 10, 0)
		self.execName_layout.setObjectName("execName_layout")
		self.rename_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
		self.rename_btn.setMaximumSize(QtCore.QSize(16777215, 25))
		self.rename_btn.setObjectName("rename_btn")
		self.execName_layout.addWidget(self.rename_btn)

		self.retranslateUi(ReNameUi)
		QtCore.QMetaObject.connectSlotsByName(ReNameUi)



		#                       #
		# Link function here    #
		#                       #

		# Set text in the field
		self.base_txtField.setText( naming_txtField )
		# do this when click rename
		self.base_btn.clicked.connect( self.clickBase )
		self.prefix_btn.clicked.connect( self.clickPrefix )
		self.suffix_btn.clicked.connect( self.clickSuffix )
		self.rename_btn.clicked.connect( self.clickRename )
		self.LFT_btn.clicked.connect( self.clickLFT )
		self.RGT_btn.clicked.connect( self.clickRGT )
		self.UPR_btn.clicked.connect( self.clickUPR )
		self.LWR_btn.clicked.connect( self.clickLWR )
		self.FRT_btn.clicked.connect( self.clickFRT )
		self.BAK_btn.clicked.connect( self.clickBCK )

		self.searchNReplace_btn.clicked.connect( self.clickSearchNreplace)

		# self.autoSuffix_check.clicked.connect( self.autoSuffix )

		# self.app = app.reBaseName()

		
	def retranslateUi(self, ReNameUi):
		_translate = QtCore.QCoreApplication.translate
		ReNameUi.setWindowTitle(_translate("ReNameUi", "nomanRenamer v1.00"))

		# Make this widget a standalone window even though it is parented 
		ReNameUi.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) 

		self.prefix_btn.setText(_translate("ReNameUi", "Prefix"))
		self.base_btn.setText(_translate("ReNameUi", "Base"))
		self.suffix_btn.setText(_translate("ReNameUi", "Suffix"))
		self.effect_check.setText(_translate("ReNameUi", "effect child"))
		self.autoSuffix_check.setText(_translate("ReNameUi", "auto suffix"))
		self.insert_txext.setText(_translate("ReNameUi", "insert ## to add number"))
		self.replace_text.setText(_translate("ReNameUi", "Replace"))
		self.searchNReplace_btn.setText(_translate("ReNameUi", "Search and Replace"))
		self.search_text.setText(_translate("ReNameUi", "Search"))
		self.LWR_btn.setText(_translate("ReNameUi", "LWR"))
		self.LFT_btn.setText(_translate("ReNameUi", "LFT"))
		self.BAK_btn.setText(_translate("ReNameUi", "BCK"))
		self.RGT_btn.setText(_translate("ReNameUi", "RGT"))
		self.FRT_btn.setText(_translate("ReNameUi", "FRT"))
		self.UPR_btn.setText(_translate("ReNameUi", "UPR"))
		self.addPosition_text.setText(_translate("ReNameUi", "Add Position to Base name"))
		self.rename_btn.setText(_translate("ReNameUi", "Rename"))




		#                       #
		# Core function here    #
		#                       #


	def clickPrefix(self):
		pre_txt = self.prefix_txtField.text()
		misc.rePre(pre_txt)





	""" first get the string then check is autosuffix """
	def clickSuffix(self):

		# check is autoSuffix_check is check 
		selection = mc.ls(sl=True)
		if self.autoSuffix_check.isChecked() == True:
			

			if selection:
				for each in selection:
					# convert unicode to ascii
					# each = each.encode('ascii')
					each = str(each)
					# disable for now
					lastname = misc._findExtension(each)
					# lastname = '_ply'

					mc.rename(each ,each +  '_' + lastname )

				suffix_txt = self.suffix_txtField.text()	
				self.suffix_txtField.setText( '_' + lastname )
				



			else:
				mc.error('Please select something first!.')

		else:
			self.suffix_txt = self.suffix_txtField.text()
			for each in selection:
				# convert unicode to ascii
				# each = each.encode('ascii')
				each = str(each)

				mc.rename(each ,each + self.suffix_txt )

				





	def _nmRenamer(self, prefix='',newName='',suffix=''):
		sel = mc.ls(sl=True)

		if sel:
			rename_dict = {}
			addSight = []
			sharp = []

			alphabet = (	'A','B','C','D','E','F','G','H','I','J','K','M','N',
					'O','P','Q','R','S','T','U','V','W','X','Y','Z'			)

			for each in newName:
				if each == '@':
					addSight.append(each)
				elif each == '#':
					sharp.append(each)			
					digit = len(sharp)



			for each in range(len(sel)):
				
				fullDagPath = mc.listRelatives( sel[each] , allDescendents = True , type='transform' , fullPath=True )

				if not fullDagPath:
					rename_dict[alphabet[each % len(alphabet)]] = sel[each]

				else:
					# add themself
					fullDagPath.append(sel[each])
					rename_dict[ alphabet[each] ] = fullDagPath



			# for each key
			for keysDict in rename_dict.keys():
				# mc.select(clear=True)
				logger.info(keysDict)
				amount = len(rename_dict[ keysDict ])-1

				
				# loop for each child object
				logger.info(amount)
				member = rename_dict[ keysDict ]
				
				# # # # # # # # # # # # 
				# arg is a List
				# # # # # # # # # # # # 

				if type(member) == type(['l','i','s','t']):
					print ('This is list')
					
					# reverse iteration for solve can't rename with redundance name
					rev_List = member[::-1]				
					betIdx = 0
					num = 1


					for each in range(amount,-1,-1):
						numIdx = each
						if digit:
							logger.info('this is digit number: %s' %digit)
							numName = each+1
							logger.info('loop: ' + str(each))
							strNum = str(numName)
							replaceStr = strNum.zfill(digit)

							newVal = replace_sharp_pattern(newName, numName)

							
							newBet = newVal.replace('@', keysDict)


								
							logger.info('doing rename in maya')
							logger.info('rename %s ==> %s' %(rev_List[numIdx] , newBet))
							mc.rename( rev_List[numIdx] ,  prefix + newBet + suffix)
							logger.info(numIdx)

							num = num+1

						else:

							newBet = newName.replace( '@' , keysDict )
							logger.info('rename alphabet only')
							logger.info('rename %s ==> %s' %(rev_List[numIdx] , newBet))
							mc.rename( rev_List[numIdx] ,  prefix + newBet + suffix)




				# # # # # # # # # # # # 
				# arg is a String
				# # # # # # # # # # # # 


				if MAYA_VERSION >= 2022:
					if type(member) in [bytes, str]:
						logger.info('This is string of python3.')

				else:
					if type(member) in [str, unicode]:
						logger.info('This is string of of python2.')

				logger.info('this is digit number: %s' %digit)
				# noneed to reverse
				rev_List = member
				betIdx = 0
				num = 1
				logger.info('loop: ' + str(each))
				logger.info('insert the number start.')

				if digit != 0:
					numName = 1
					strNum = str(numName)
					replaceStr = strNum.zfill(digit)
					logger.info('replaceStr is: %s' %replaceStr)
					newVal = replace_sharp_pattern(newName, numName)
					logger.info(keysDict)
					newBet = newVal.replace('@', keysDict)


					logger.info('doing rename in maya')
					logger.info('rename %s ==> %s' %(rev_List , newBet))

					try:
						mc.rename( rev_List , prefix + newBet + suffix )
					except Exception as e:
						logger.warning(f"Rename failed: {rev_List} → {prefix + newBet + suffix}. Reason: {e}")

				else:
					logger.info('there is no didit.')
					newBet = newName.replace( '@' , keysDict )
					logger.info('rename %s ==> %s' %(rev_List , newBet))
					mc.rename( rev_List , prefix + newBet + suffix )

		else:
			mc.error('Select something si.')





	

	def clickBase( self ):
		# alphabet = app.alphabet
		sel = mc.ls(sl=True)

		
		self.base_txt = self.base_txtField.text()
		newName = self.base_txt
	

		if self.effect_check.isChecked() == True:
			self._nmRenamer(newName = newName)


		elif self.effect_check.isChecked() == False:

			# this redundance code with naRenamer
			addSight = []
			sharp = []
			for each in newName:
				if each == '@':
					addSight.append(each)
				elif each == '#':
					sharp.append(each)			
					digit = len(sharp)
			# this redundance code with naRenamer

			amount = len(sel)-1
			betIdx = 0
			num = 1
			for each in range(amount,-1,-1):
				numIdx = each
				numName = each+1		
				strNum = str(numName)
				replaceStr = strNum.zfill(digit)
				newVal = replace_sharp_pattern(newName, numName)
				newBet = newVal.replace( '@' , alphabet[betIdx] )
				mc.rename( sel[numIdx] , newBet )		

		mc.select(clear=True)
		

		


	def clickRename(self):
		# collect 3 texfield
		pre_txt = self.prefix_txtField.text()
		base_txt = self.base_txtField.text()
		suffix_txt = self.suffix_txtField.text()

		store = []
		rename_dict = {}
		effHirechy = True
		addSight = []
		sharp = []
		
		self.base_txt = self.base_txtField.text()
		newName = self.base_txt
		
		for each in newName:
			if each == '@':
				addSight.append(each)
			elif each == '#':
				sharp.append(each)		
				digit = len(sharp)

		# alphabet = app.alphabet
		sel = mc.ls(sl=True)

		if self.effect_check.isChecked() == True:
			self._nmRenamer(prefix = pre_txt , newName = newName , suffix = suffix_txt)


				


		elif self.effect_check.isChecked() == False:
			amount = len(sel)-1
			betIdx = 0
			num = 1
			for each in range(amount,-1,-1):
				numIdx = each
				numName = each+1		
				strNum = str(numName)
				replaceStr = strNum.zfill(digit)
				newVal = replace_sharp_pattern(newName, numName)
				newBet = newVal.replace( '@' , alphabet[betIdx] )

				# option for use underscore as separater
				# pName = '_'.join( [pre_txt , newBet , suffix_txt] )

				mc.rename( sel[numIdx] , pre_txt + newBet + suffix_txt )

		mc.select(clear=True)

		print (pre_txt + base_txt + suffix_txt)



	def clickLFT( self ):
		# check is having name in field
		if self.base_txtField.text():

			oldText = self.base_txtField.text()
			self.base_txtField.setText( oldText + 'LFT' )
	
		else:

			self.base_txtField.setText('LFT')


	def clickRGT( self ):
		# check is having name in field
		if self.base_txtField.text():

			oldText = self.base_txtField.text()
			self.base_txtField.setText( oldText + 'RGT' )
	
		else:

			self.base_txtField.setText('RGT')	



	def clickUPR( self ):
		# check is having name in field
		if self.base_txtField.text():

			oldText = self.base_txtField.text()
			self.base_txtField.setText( oldText + 'UPR' )
	
		else:

			self.base_txtField.setText('UPR')	



	def clickLWR( self ):
		# check is having name in field
		if self.base_txtField.text():

			oldText = self.base_txtField.text()
			self.base_txtField.setText( oldText + 'LWR' )
	
		else:

			self.base_txtField.setText('LWR')	



	def clickFRT( self ):
		# check is having name in field
		if self.base_txtField.text():

			oldText = self.base_txtField.text()
			self.base_txtField.setText( oldText + 'FRT' )
	
		else:

			self.base_txtField.setText('FRT')	


	def clickBCK( self ):
		# check is having name in field
		if self.base_txtField.text():

			oldText = self.base_txtField.text()
			self.base_txtField.setText( oldText + 'BCK' )
	
		else:

			self.base_txtField.setText('BAK')	

	def clickSearchNreplace( self ):
		selection = mc.ls(sl=True)
		search_txt = self.search_txtField.text()
		replace_txt = self.replace_txtField.text()
		misc.searchReplace( searchText = search_txt, replaceText = replace_txt )





def showUI():
	ui = Ui_ReNameUi()
	ui.show()


