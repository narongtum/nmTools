# >>>>>   Untimate Color Menu   <<<<<
# 	Date: 27.May.2020
# 	Author: UI, main function		:	THEDODE 
version = '1.0'

import maya.cmds as mc

from function.rigging.tools import dTool as dc 
reload(dc)



class Function:

	# Color
	def _toRed(self, color = '' ):
		if len(mc.ls(sl=True)) > 0:
			sel = mc.ls(sl=True)
			dc.displayColorOverride( ctrl = sel, color = 'red' )

	def _toGreen(self, color = '' ):
		if len(mc.ls(sl=True)) > 0:
			sel = mc.ls(sl=True)
			dc.displayColorOverride( ctrl = sel, color = 'green' )

	def _toBlue(self, color = '' ):
		if len(mc.ls(sl=True)) > 0:
			sel = mc.ls(sl=True)
			dc.displayColorOverride( ctrl = sel, color = 'blue' )
	
	def _toYellow(self, color = '' ):
		if len(mc.ls(sl=True)) > 0:
			sel = mc.ls(sl=True)
			dc.displayColorOverride( ctrl = sel, color = 'yellow' )

	def _toWhite(self, color = '' ):
		if len(mc.ls(sl=True)) > 0:
			sel = mc.ls(sl=True)
			dc.displayColorOverride( ctrl = sel, color = 'white' )


class Ui:
	def __init__(self):
		self.Function = Function()

	def createGUI(self,*args):
		# Make a new window
		if mc.window('colorTool', exists = True):
			mc.deleteUI('colorTool')
		
		ui_size = 30
			
		colorWin = mc.window('colorTool', title="Color Tool", iconName='color', widthHeight=(200, 200), s = 1, mm = 1, mxb = 0, mw = 0 )
		
		mc.frameLayout( label='Quick Color  v ' + version,collapsable=False, mw=5, mh=5 )
		mc.rowColumnLayout( numberOfColumns=5, columnWidth=[(1, 50), (2, 50), (3, 50), (4, 50), (5, 50)] )

		#mc.separator( ann = 'Constraint', w=140, h = 20, style='in' )
		#mc.text( label='               Constraint' )

		mc.button( label='Red' , hlc= [1,1,1] , bgc = [1,0,0], command = self.Function._toRed , h=ui_size )
		mc.button( label='Green', hlc= [1,1,1] , bgc = [0,1,0], command = self.Function._toGreen , h=ui_size )
		mc.button( label='Blue' , hlc= [1,1,1] , bgc = [0,0,1], command = self.Function._toBlue , h=ui_size )
		mc.button( label='Yellow', hlc= [1,1,1] , bgc = [1,1,0], command = self.Function._toYellow , h=ui_size )
		mc.button( label='White', hlc= [1,1,1] , bgc = [1,1,1], command = self.Function._toWhite , h=ui_size )

		#mc.checkBox("mo", l='maintainOffset', value = 0 , h = 20, ann = 'check for maintain offset')
		#mc.text( label='')

		mc.showWindow( colorWin )
		

#call = Ui()
#call.createGUI()