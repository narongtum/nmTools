# new world local 2020
# by TDX

#from function.rigging.autoRig.object import createLocalWorldAtSelected as lcwAt
#reload (lcwAt)
#createLocalWorldAtSelected( ctrl_grp = 'ctrl_grp' )
import maya.cmds as mc
from function.rigging.tools import dTool as dc
reload (dc)

def createLocalWorldAtSelected( ctrl_grp = 'ctrl_grp', style = 'orient' ):
	sel = mc.ls(sl=1)
	for each in sel:
		ctrl = each

		# create Name
		name = each.split('_')[0]
		print name
		print ctrl
		print 'add Attr at  ' + ctrl


		# find parent name Zro_grp
		mc.select(cl=1)
		mc.select( each )
		upGrp = mc.pickWalk( d = 'up' )
		if 'Offset' in upGrp:
			parent = mc.pickWalk( d = 'up' )
		else:
			parent = upGrp
		print parent
		mc.select(cl=1)

		
		#find master name like master_grp
		mc.select( parent )
		masterGrp = mc.pickWalk( d = 'up' )
		mc.select(cl=1)
		print masterGrp



		# grp
		localGrp = mc.group( em=1, n = name + 'Loc_grp')
		worldGrp = mc.group( em=1, n = name + 'Wor_grp')
		# snap
		dc.allMat( localGrp ,parent )
		dc.allMat( worldGrp ,parent )
		# parent
		mc.parent( localGrp, masterGrp )
		mc.parent( worldGrp, masterGrp )
		
		con = name + 'LocalWorld_oriCons'

		if style == 'orient':
			# ori Cons
			dc.oriCon( ctrl_grp, worldGrp )
			mc.orientConstraint( localGrp,worldGrp, parent, mo=1, w=0, name = con )
		elif style == 'parent':
			# par Cons
			dc.parCon( ctrl_grp, worldGrp )
			mc.parentConstraint( localGrp,worldGrp, parent, mo=1, w=0, name = con )


		# rev
		rev = name + '_rev'
		mc.createNode('reverse', name = name + '_rev')
		print rev
		print ctrl
		# rev and conect

		# add Attr to ctrl and connect Attr to constraint
		if mc.objExists (ctrl+'.localWorld'):
			print 'localWorld is Exists'
		else:
			mc.addAttr ( ctrl, sn = 'lcw' ,ln = 'localWorld', min = 0, max = 1, dv = 0, k = True)
			print 'add localWorld'

		print 'addAttr At  ' + ctrl
		mc.connectAttr ( ctrl + '.localWorld', rev + '.input.inputX' )
		print 'connectAttr ctrl ->rev iX'
		mc.connectAttr ( rev + '.output.outputX', con + '.w0' )
		print 'connectAttr rev ->con W0'
		mc.connectAttr ( rev + '.input.inputX', con + '.w1' )
		print 'connectAttr rev ->con W1'
		
