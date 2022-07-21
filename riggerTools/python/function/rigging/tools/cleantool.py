'''
# >>>>>  Clean up Menu   <<<<<
# Parent Point Orient Scale and with option to maintain offset
# DelHistory FT RT Match-transform
# Sel_bJnt Skin[] mirror[] copy[]
# reset Lock and Hide // Reset All *_ctrl
'''
version = '0.4'

import sys
import maya.utils
import maya.cmds as mc
import maya.mel as mel
#sys.path.append(r'C:\Users\LEMEL\Dropbox\dode_script')


from function.rigging.tools import dTool as dc 
reload(dc)

from function.rigging.tools import proc as pc 
reload(pc)

from function.rigging import RESET as re
reload(re)

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
	def _renameSelShd(self,*args):
		dc.renameShd( overideName = '' )

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


	# local RIG
	def _localWorldOri( self, *args ):
		pc.localWorldSel( ori = True )

	def _localWorldPar( self, *args ):
		pc.localWorldSel( ori = False )

	# Special
	def _setupSelArmor( self, *args ):
		pc.setupSelectedArmor()

	def _exportSelArmor( self, *args ):
		pc.exportSelArmor()

	def _setupSelOutfit( self, *args ):
		pc.setupSelectedOutfit()

	def _exportSelOutfit( self, *args ):
		pc.exportSelOutfit()



	# Skin

	def _sel_bJnt(self, *args):
		if mc.checkBox("bind_jnt", value = True , q = True):
			mc.select('*_bind_jnt')
		else:
			mc.select('*_bJnt')

	def _skin(self, *args):
		#mc.skinCluster(tsb=True, dr = 5)
		mc.skinCluster(tsb=True, dr = 5, prune = True)

	def _mirror(self, *args):
		mel.eval( 'MirrorSkinWeightsOptions;' )

	def _copy(self, *args):
		mel.eval( 'CopySkinWeightsOptions;' )

	# Ctrl
	def _ctrlThis(self, *args):
		dc.quickCtrl()

	def _createChainCtrl(self, *args):
		dc.chainCtrl()

	# Reset
	def _unLockHide(self, *args):
		sel = mc.ls( sl=True )
		for each in sel:
			attrs = 'tx','ty','tz','rx','ry','rz','sx','sy','sz','v'
			for attr in attrs:
				mc.setAttr( each + '.' + attr ,lock = False, keyable = True )

	def _reset(self, *args):
		re.resetAllController(reference = False)

class Ui:
	def __init__(self):
		self.Function = Function()

	def createGUI(self,*args):
		# Make a new window
		if mc.window('cleanTool', exists = True):
			mc.deleteUI('cleanTool')
		
		ui_size = 30
			
		dWin = mc.window('cleanTool', title="CleanTool", iconName='RIGs', widthHeight=(200, 200), s = 1, mm = 1, mxb = 0, mw = 0 )
		
		mc.frameLayout( label='Clean Up  v ' + version,collapsable=False, mw=5, mh=5 )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 100), (2, 100)] )

		mc.separator( ann = 'Model', w=150, h = 20, style='in' )
		mc.text( label='                  Model' )

		mc.button( label='Unlock' , command = self.Function._parCon,h=ui_size, ann = 'select model')
		mc.button( label='SoftEdge' , command = self.Function._pointCon,h=ui_size, ann = 'select edge')
		mc.button( label='Separate', command = self.Function._oriCon ,w=50, h=ui_size, ann = 'select mother and child for orient constrain' )
		mc.button( label='Combine', command = self.Function._sclCon ,w=50, h=ui_size, ann = 'select mother and child for scale constrain' )

		#mc.checkBox("mo", l='maintainOffset', value = 0 , h = 20, ann = 'check for maintain offset')
		#mc.text( label='')

		mc.separator( ann = 'Util', w=150, h = 20, style='in' )
		mc.text( label='                  Shader' )

		#nonDef = mc.checkBox("nonDef", l='nonDeformer', value = 0 , h = 20, ann = 'check for delete history with non deformer')
		#mc.text( label='')

		mc.button( label='renameShd' , command = self.Function._renameSelShd,h=ui_size, ann = 'rename select shader of select Object() and friends')
		mc.button( label='FT' , command = self.Function._freezeSel,h=ui_size, ann = 'freeze transform select object()')
		mc.button( label='RT', command = self.Function._resetSel ,w=50, h=ui_size, ann = 'reset transform select object()')
		mc.button( label='MAT', command = self.Function._matSel ,w=50, h=ui_size,  ann = 'select object A to match transformation with oject B')

		mc.separator( ann = 'Util', w=150, h = 20, style='in' )
		mc.text( label='                  Local Rig' )

		mc.button( label=' LocalOrient ' , command = self.Function._localWorldOri,h=ui_size, ann = 'select armor and connect them to Armor swap group' )
		mc.button( label=' LocalParent ' , command = self.Function._localWorldPar,h=ui_size, ann = 'bake root animation and delete rig group , then select armor' )


		mc.text( label='', h = 10 )
		mc.text( label='' )

		mc.separator( w=150, h = 20, style='in' )
		mc.text( label='                    Special' )

		#mc.checkBox("bind_jnt", l='_bind_jnt', value = 0 , h = 20, ann = 'check for bind_jnt*' )
		mc.separator( w=170, h = 20, style='in' )
		mc.text( label='                        [ PH ]' , h = 20)
		
		mc.button( label=' ConnectArmor ' , command = self.Function._setupSelArmor,h=ui_size, ann = 'select armor and connect them to Armor swap group' )
		mc.button( label=' ExportArmor ' , command = self.Function._exportSelArmor,h=ui_size, ann = 'bake root animation and delete rig group , then select armor' )
		
		mc.separator( w=170, h = 20, style='in' )
		mc.text( label='                        [ EH ]' , h = 20)

		mc.button( label=' ConnectOutfit ' , command = self.Function._setupSelOutfit,h=ui_size, ann = 'select armor and connect them to Outfit swap group' )
		mc.button( label=' ExportOutfit ' , command = self.Function._exportSelOutfit,h=ui_size, ann = 'bake root animation and delete rig group , then select Outfit' )
		
		#mc.button( label='copy', command = self.Function._copy ,w=50, h=ui_size, ann = 'open copy option' )

		#mc.text( label='', h = 10 )
		#mc.text( label='' )

		#mc.separator( w=170, h = 30, style='in' )
		#mc.text( label='                      Ctrl' )
		#mc.button( label='ctrl' , command = self.Function._ctrlThis,h=ui_size, ann = 'create Ctrl to selected')
		#mc.button( label='chain' , command = self.Function._createChainCtrl,h=ui_size, ann = 'pls select _bJnt with "ctrl" in the scene')

		#mc.text( label='', h = 1 )
		#mc.text( label='' )

		#mc.separator( w=160, h = 30, style='in' )
		#mc.text( label='                      Reset' )

		#mc.button( label='unLock/Hide', command = self.Function._unLockHide ,w=50, h=ui_size*2, ann = 'unlock and unhide selected Attributes' )
		#mc.button( label='RESET', command = self.Function._reset ,w=50, h=ui_size*2, ann = 'reset *ctrl')
		
		mc.showWindow( dWin )
		
#local run	
#call = Ui()
#call.createGUI()

