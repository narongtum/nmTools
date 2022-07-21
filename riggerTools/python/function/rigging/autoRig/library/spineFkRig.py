import maya.cmds as mc

'''from function.rigging import core
reload(core)'''

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)

from function.rigging.util import misc as misc
reload(misc)

from function.rigging import core 
reload(core)

'''from function.rigging.autoRig.base import core
reload(core)'''

from function.rigging.readWriteCtrlSizeData import flipController as fip
reload(fip)



def cogRig(each = ('cog') , parentTo = 'fly_ctrl'):
	# ========== # Cog rig
	cogGrp = each + '_Zro_grp'
	bodyJnt = 'hip_bind_jnt'
	# func
	misc.snapParentConst( bodyJnt, cogGrp )
	mc.parent ( cogGrp, parentTo )
	
def hipRig(each = ('hip') , parentTo = 'cog_ctrl'):
	# ========== # Hip rig
	jntName = each + '_bind_jnt'
	zroName = each + '_Zro_grp'
	gmblName = each + '_Gimbal_ctrl'
	

	# func
	misc.snapParentConst( jntName , zroName )
	mc.parent (  zroName , parentTo )
	mc.parentConstraint ( gmblName , jntName , w = True)
	# Add scale Constraint
	mc.scaleConstraint ( gmblName , jntName , w = True)


def spineFK(spineList = ('lowerBody', 'chest', 'upperBody' ) , parentTo = 'cog_ctrl'):
	# ========== # Spine rig
	for each in spineList:
		jntName = each + '_bind_jnt'
		zroName = each + '_Zro_grp'
		gmblName = each + '_Gimbal_ctrl'
		# func
		misc.snapParentConst(jntName, zroName )
		mc.parentConstraint ( gmblName, jntName, w = True)
		# Add scale Constraint
		mc.scaleConstraint ( gmblName, jntName, w = True)

	# parenting Spine
	for i in range(len(spineList)-1,0,-1):
		mc.parent ( spineList[i] + '_Zro_grp' , spineList[i-1] + '_Gimbal_ctrl')
		
	mc.parent ( spineList[0]+'_Zro_grp' , parentTo )


def chainFK(chainList = ('tail01' , 'tail02' ,'tail03', 'tail04' ) , parentTo = 'cog_ctrl' , ctrlType = 'neck_ctrlShape' , ctrlColor = 'red' , scale = [1, 1, 1] 	):
	# ========== # Chain rig, Tail and ear
	for each in chainList:

		'''if each == chainList[-1]:
									continue'''

		jntName = each + '_bind_jnt'
		zroName = each + '_Zro_grp'
		gmblName = each + '_Gimbal_ctrl'
		# create controller
		fkChain = core.Base()
		fkChain.nmCreateController( ctrlType )
		fkChain.setName(each + '_ctrl')
		fkChain.setColor( ctrlColor )

		sel = mc.select( each + '_ctrl' )
		oldZroName = adjust.createZroGrp()
		zroName = mc.rename( oldZroName , zroName )

		sel = mc.select( each + '_ctrl' )
		gimbalOldName = adjust.createGimbal()
		mc.rename( gimbalOldName , gmblName )

		fkChain.renameShape(each + '_ctrl' + 'Shape')



		# snap position
		misc.snapParentConst(jntName, zroName )
		mc.parentConstraint ( gmblName, jntName, w = True)
		mc.scaleConstraint ( gmblName, jntName, w = True)

		sel = mc.select( each + '_ctrl' , r = True )
		print 'sel'
		upSize = fip.buildUI()
		upSize.flipCtrlShapeY( sel , axis = scale )



	# parenting chain
	for i in range(len(chainList)-1,0,-1):
		
		'''if chainList[i] == chainList[-1]:
									continue'''
		mc.parent ( chainList[i] + '_Zro_grp' , chainList[i-1] + '_Gimbal_ctrl')

	mc.parent ( chainList[0]+'_Zro_grp' , parentTo )
	mc.select(deselect = True)




# Function
'''
cogRig(each = ('cog') , parentTo = 'fly_ctrl')
hipRig(each = ('hip') , parentTo = 'cog_ctrl')
spineFK(spineList = ('body','lowerBody', 'chest', 'upperBody' ) , parentTo = 'cog_ctrl')
'''