'''
from function.rigging import templateUi 
reload(templateUi)
'''

import maya.cmds as mc
from functools import partial
import maya.mel as mm




class templateUi(object):
	"""docstring for templateUi"""
	def __init__(self, name, title, width=400, height=200 ,info='', menu=True):

		self.name = name
		self.title = title
		self.width = width
		self.height = height
		self.info = info
		self.menu = menu


	def __enter__(self):
		self.buildWindow()
		return self


	def __exit__(self, *args):
		self.finish()


	def buildWindow(self):
		'''
		Initialize Ui
		'''

		if mc.window(self.name, exists = True):
			mc.deleteUI(self.name)

		mc.window(self.name, title='TrueAxion:: ' + self.title, iconName = self.title, width=self.width, height=self.height )

		self.form = mc.formLayout()
		self.column = mc.columnLayout(adj=True)

		mc.rowLayout( numberOfColumns=2, columnWidth2=(34, self.width-34), adjustableColumn=2,
					  columnAlign2=('right','left'),
					  columnAttach=[(1,'both',0),(2,'both',8)]		)

		'''
		if not self.menu:
			mc.popupMenu(button=1)
			mc.menuItem(label = 'Help', command = (_showHelpCommand(TOOL_URL+self.name+'/')))'''
			
		mc.text(label=self.info)
		mc.setParent('..')
		mc.separator(height=8, style='single', horizontal=True)


	def selectionField(self, label='', annotation='', buttonLabel ='Set Selected', text=''):
		'''
		Create a field with a button that adds the selection to the field.
		'''
		field = mc.textFieldButtonGrp(	label = label, 
										text = text,
									 	buttonLabel = buttonLabel
									 	)
		mc.textFieldButtonGrp(field, edit=True, annotation = annotation, buttonCommand=partial(self._populateSelectionField, field))
		return field	



	def _populateSelectionField(self, field, *args):
		""" return object that be selected """
				
		sel = mc.ls(sl=True)
		if not sel:
			raise RuntimeError('Please select a node.')
		if len(sel) > 1:
			selection = sel
		elif len(sel) == 1:
			selection = sel[0]


		# This will be show the somethin you selected
		mc.textFieldButtonGrp(field, edit=True, text=str(selection))


	def finish(self):
		'''
		Finalize Ui
		'''

		mc.setParent(self.form)

		frame = mc.frameLayout(labelVisible = False)
		mc.helpLine()

		mc.formLayout( self.form, edit=True,
				   attachForm=((self.column, 'top', 0), (self.column, 'left', 0),
							   (self.column, 'right', 0), (frame, 'left', 0),
							   (frame, 'bottom', 0), (frame, 'right', 0)),
				   attachNone=((self.column, 'bottom'), (frame, 'top')) )

		mc.showWindow(self.name)
		mc.window(self.name, edit=True, width=self.width, height=self.height)		