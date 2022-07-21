'''
# >>>>>  Rigger Quick Menu   <<<<<
# Parent Point Orient Scale and with option to maintain offset
# DelHistory FT RT Match-transform
# Sel_bJnt Skin[] mirror[] copy[]
# reset Lock and Hide // Reset All *_ctrl
'''
version = '1.6'

import sys
import maya.utils
import maya.cmds as mc
import maya.mel as mel
#sys.path.append(r'C:\Users\LEMEL\Dropbox\dode_script')


from function.rigging.tools import dTool as dc 
reload(dc)

from function.rigging import RESET as re
reload(re)

from function.rigging.autoRig.object import createLocalWorldAtSelected as lcwAt
reload (lcwAt)

from function.asset import selBakeExport as sbe
reload(sbe)

class Function:

	# Constrain
	
	def _parCon(self, *args):
		if mc.checkBox("mo", value = True , q = True):
			dc.cons( mo = 1, type = 'parent')
		else:	
			dc.cons( mo = 0, type = 'parent')
	
	def _pointCon(self,*args):
		if mc.checkBox("mo", value = True , q = True):
			dc.cons( mo = 1, type = 'point')
		else:
			dc.cons( mo = 0, type = 'point')

	def _oriCon(self,*args):
		if mc.checkBox("mo", value = True , q = True):
			dc.cons( mo = 1, type = 'orient')
		else:
			dc.cons( mo = 0, type = 'orient')

	def _sclCon(self,*args):
		if mc.checkBox("mo", value = True , q = True):
			dc.cons( mo = 1, type = 'scale')
		else:
			dc.cons( mo = 0, type = 'scale')
	# Util

	def _delHistory(self, *args):
		sel = mc.ls( sl=True )
		if len(sel) > 0:
			if mc.checkBox("nonDef", value = True , q = True):
				mc.bakePartialHistory( sel )
			else:
				sel = mc.ls( sl=True )
				mc.delete( sel, constructionHistory = True )
		else:
			print "."
			print "select something"
			print "."

	def _freezeSel(self, *args):
		sel = mc.ls( sl=True )
		if len(sel) > 0:
			mc.select( sel )
			mc.makeIdentity( apply = True, t=1, r=1, s=1 )
		else:
			print "."
			print "select something"
			print "."

	def _resetSel(self, *args):
		sel = mc.ls( sl=True )
		if len(sel) > 0:
			mc.select( sel )
			mc.makeIdentity( apply = False, t=1, r=1, s=1 )
		else:
			print "."
			print "select something"
			print "."

	def _matSel(self, *args):
		sel = mc.ls( sl=True )
		if len(sel) > 0:
			for i in range(len(sel)-1):
				tgt = sel[i]
				src = sel[-1]
				print tgt + '____' + src
				dc.allMat( tgt, src )
		else:
			print "."
			print "select something"
			print "."

	# Skin

	def _sel_bJnt(self, *args):
		if mc.checkBox("bind_jnt", value = True , q = True):
			mc.select('*_bind_jnt')
		else:
			mc.select('*_bJnt')

	def _skin(self, *args):
		#mc.skinCluster(tsb=True, dr = 5)
		#mc.skinCluster(tsb=True, dr = 5, prune = True)
		mel.eval( 'SmoothBindSkinOptions;' )

	def _unbine(self, *args):
		mel.eval( 'doDetachSkin "2" { "1","1" };' )

	def _prune(self, *args):
		mel.eval( 'PruneSmallWeightsOptions;' )

	def _mirror(self, *args):
		mel.eval( 'MirrorSkinWeightsOptions;' )

	def _copy(self, *args):
		mel.eval( 'CopySkinWeightsOptions;' )

	# Ctrl
	def _ctrlThis(self, *args):
		dc.quickCtrl()

	def _createChainCtrl(self, *args):
		dc.chainCtrl()

	# Spacial Tool
	def _localWorldRotThis(self, *args):
		lcwAt.createLocalWorldAtSelected( ctrl_grp = 'ctrl_grp', style = 'orient' )

	def _localWorldParThis(self, *args):
		lcwAt.createLocalWorldAtSelected( ctrl_grp = 'ctrl_grp', style = 'parent' )

	# Reset
	def _unLockHide(self, *args):
		sel = mc.ls( sl=True )
		for each in sel:
			attrs = 'tx','ty','tz','rx','ry','rz','sx','sy','sz','v'
			for attr in attrs:
				mc.setAttr( each + '.' + attr ,lock = False, keyable = True )

	def _reset(self, *args):
		re.resetAllController(reference = False)


	def _toFBXFolder(self, *args):
		sbe.toFBXFolder()

	def _toHereFolder(self, *args):
		sbe.toHereFolder()

class Ui:
	def __init__(self):
		self.Function = Function()

	def createGUI(self,*args):
		# Make a new window
		if mc.window('rigTool', exists = True):
			mc.deleteUI('rigTool')
		
		ui_size = 30
			
		dWin = mc.window('rigTool', title="Rig Tool", iconName='RIGs', widthHeight=(200, 200), s = 1, mm = 1, mxb = 0, mw = 0 )
		
		mc.frameLayout( label='Quick Shelf  v ' + version,collapsable=False, mw=5, mh=5 )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 100), (2, 100)] )

		mc.separator( ann = 'Constraint', w=140, h = 20, style='in' )
		mc.text( label='               Constraint' )

		mc.button( label='Parent' , command = self.Function._parCon,h=ui_size*2, ann = 'select mother and child for parent constrain')
		mc.button( label='Scale', command = self.Function._sclCon ,w=50, h=ui_size*2, ann = 'select mother and child for scale constrain' )
		mc.button( label='Point' , command = self.Function._pointCon,h=ui_size, ann = 'select mother and child for point constrain')
		mc.button( label='Orient', command = self.Function._oriCon ,w=50, h=ui_size, ann = 'select mother and child for orient constrain' )
		

		mc.checkBox("mo", l='maintainOffset', value = 0 , h = 20, ann = 'check for maintain offset')
		mc.text( label='')

		mc.separator( ann = 'Util', w=170, h = 20, style='in' )
		mc.text( label='                        Util' )

		nonDef = mc.checkBox("nonDef", l='nonDeformer', value = 0 , h = 20, ann = 'check for delete history with non deformer')
		mc.text( label='')

		mc.button( label='DelHistory' , command = self.Function._delHistory,h=ui_size, ann = 'delete constructionHistory of select Object()')
		mc.button( label='FT' , command = self.Function._freezeSel,h=ui_size, ann = 'freeze transform select object()')
		mc.button( label='RT', command = self.Function._resetSel ,w=50, h=ui_size, ann = 'reset transform select object()')
		mc.button( label='MAT', command = self.Function._matSel ,w=50, h=ui_size,  ann = 'select object A to match transformation with oject B')


		mc.text( label='', h = 10 )
		mc.text( label='' )

		
		mc.separator( w=160, h = 20, style='in' )
		mc.text( label='                       Skin' )


		mc.checkBox("bind_jnt", l='_bind_jnt', value = 0 , h = 20, ann = 'check for bind_jnt*' )
		mc.text( label='' )
		

		mc.button( label='*_bJnt' , command = self.Function._sel_bJnt,h=ui_size, ann = 'select *bJnt')
		mc.button( label='bind' , command = self.Function._skin,h=ui_size, ann = 'open skin option')

		mc.button( label='unbine' , command = self.Function._unbine,h=ui_size, ann = 'unbine option')
		mc.button( label='prune' , command = self.Function._prune,h=ui_size, ann = 'open prune option')
		
		mc.button( label='mirror', command = self.Function._mirror ,w=50, h=ui_size, ann = 'open mirror skin option' )
		mc.button( label='copy', command = self.Function._copy ,w=50, h=ui_size, ann = 'open copy option' )

		#mc.text( label='', h = 10 )
		#mc.text( label='' )

		mc.separator( w=170, h = 30, style='in' )
		mc.text( label='                      Ctrl' )
		mc.button( label='ctrl' , command = self.Function._ctrlThis,h=ui_size, ann = 'create Ctrl to selected')
		mc.button( label='chain' , command = self.Function._createChainCtrl,h=ui_size, ann = 'pls select _bJnt with "ctrl" in the scene')
		#mc.button( label='prop' , command = self.Function._createChainCtrl,h=ui_size, ann = 'pls select _bJnt with "ctrl" in the scene')
		#mc.button( label='tail' , command = self.Function._createChainCtrl,h=ui_size, ann = 'pls select _bJnt with "ctrl" in the scene')

		mc.separator( w=130, h = 30, style='in' )
		mc.text( label='            LocalWorld' )
		mc.button( label='orient' , command = self.Function._localWorldRotThis,h=ui_size, ann = 'pls select _ctrl you want')
		mc.button( label='parent' , command = self.Function._localWorldParThis,h=ui_size, ann = 'pls select _ctrl you want')
		#mc.text( label='', h = 1 )
		#mc.text( label='' )

		mc.separator( w=130, h = 30, style='in' )
		mc.text( label='           Export' )
		mc.button( label='to fbx', command = self.Function._toFBXFolder ,w=100, h=ui_size*1, ann = 'pls select all model you want to export as FBX to fbx folder' )
		mc.button( label='to here', command = self.Function._toHereFolder ,w=100, h=ui_size*1, ann = 'pls select all model you want to export as FBX to project save folder' )


		mc.separator( w=160, h = 30, style='in' )
		mc.text( label='                      Reset' )

		mc.button( label='unLock/Hide', command = self.Function._unLockHide ,w=50, h=ui_size*2, ann = 'unlock and unhide selected Attributes' )
		mc.button( label='RESET', command = self.Function._reset ,w=50, h=ui_size*2, ann = 'reset *ctrl')


		mc.showWindow( dWin )
		
#local run	
#call = Ui()
#call.createGUI()

