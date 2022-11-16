# export model/skin to path
from function.rigging.skin import skinUtil as skinUtil
reload(skinUtil)
from function.pipeline import fileTools as fileTools 
reload(fileTools)
import maya.cmds as mc
import os


class Function:
# HOPE automate export FBX 
# select geo and run


	def export( self, *args):

		ExportItem = mc.ls(sl=True)


		# set key frame
		mc.currentTime(0)
		skinUtil.selectBindJnt()
		mc.setKeyframe()

		# Select and delete
		#mc.select(  , r = True )
		
		if mc.objExists('rig_grp'):
			print 'Deleting rig_grp...'
			mc.delete( 'rig_grp' )
		else:
			print 'rig_grp has been already deleted'


		if mc.objExists('*Root'):
			root = '*Root'
		else:
			root = '*root'


		for model in ExportItem:

			#if mc.parent( model, w = True, q = True):
			mc.parent ( model, w = True )

			mc.select( cl=True )

			pathString = mc.textField('pathField', tx = True, q = True )

			filePath = pathString # To Path

			fileTools.checkExistFolder( filename = filePath )
			
			mc.select( root , model)

			fileName = model
			mc.file(filePath + '/' + fileName + '.fbx', f=True, op=('v=0'), typ='FBX export', pr=True, es = True)
			print 'File has been export at: %s' %filePath

		# Open in Explore
		#if len( ExportItem ) > 0:
		#	fileTools.openContainerFile( path = filePath )


class Ui:
	def __init__(self):
		self.Function = Function()

	def createGUI(self, *args):
		# Make a new window
		if mc.window('shdWin', exists = True):
			mc.deleteUI('shdWin')

		dWin = mc.window('shdWin', title="Export Model From Select", iconName='css', widthHeight=(300, 100), s = True, mm = False, mxb = False, mw = False )
		
		mc.frameLayout( label='select model',collapsable=False, mw=5, mh=5 )
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 50), (2, 230)] )
		mc.text( label='Path :' )
		mc.textField('pathField', tx = '', h = 25 )

		mc.setParent("..")
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 300)])

		mc.text( label='  >>  paste path here  <<   ', h = 15)
		mc.text( label='' )
		mc.button( label='Export fbx' ,w=100, h=30, c = self.Function.export )
		mc.showWindow( dWin )
	