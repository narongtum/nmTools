from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc as misc
reload(misc)

import maya.cmds as mc

'''
from function.rigging.autoRig.base import createHelperJoint as helJnt
reload( helJnt )


from function.rigging.corrective import createHelperJoint as helJnt
reload(helJnt)



'''

'''

Create inbetween joint for help deformation using CMuscleSmartConstraint node
Spec parentA and parentB respectively by manual
Axis is difference depend on landmark body
'''

def createHelperJoint( parentA = 'lowerArmLFT_bJnt' , parentB = 'handLFT_bJnt' , side = 'LFT' ,axis = 'z'):
	'''
	return name of help joint
	'''

	if not mc.objExists(parentA):
		mc.error('There are no object match name.')
		return False

	# Part1 add more connection
	parentA_bJnt = core.Dag(parentA)
	parentB_bJnt = core.Dag(parentB)

	# make rawname for common use
	rawName = parentB_bJnt.makeRawName()

	help_jnt = core.Joint()
	help_jnt.name = rawName + side + '_pxyJnt'
	
	help_jnt.attr('radius').value = 1
	help_jnt.setLable( side ,'other')
	help_jnt.setAttribute('otherType','helper',type = 'string')
	help_jnt.attr('segmentScaleCompensate').value = 0





	# helper or muscle whatever
	muscle_cons = core.CMuscleSmartConstraint( name = rawName + side )

	parentA_bJnt.attr('worldMatrix[0]') >> muscle_cons.attr( 'worldMatrixA' )
	parentB_bJnt.attr('worldMatrix[0]') >> muscle_cons.attr( 'worldMatrixB' )
	muscle_cons.attr( 'outData.outTranslate' ) >> help_jnt.attr( 'translate' )
	muscle_cons.attr( 'outData.outRotate' ) >> help_jnt.attr( 'rotate' )

	# help_jnt.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz'  )



	# Create Bind joint as a slave of helper joint for make it parentable to bind joint group
	bind_jnt = core.Joint()
	bind_jnt.name = rawName + 'Helper' + side + '_bJnt'
	bind_jnt.attr('radius').value = 5
	bind_jnt.setJointColor('softBlue')
	bind_jnt.parent( parentB_bJnt )
	bind_jnt.snap( help_jnt )
	bind_jnt.attr('segmentScaleCompensate').value = 0
	bind_jnt.setLable( side ,'other')
	bind_jnt.setAttribute('otherType','helper',type = 'string')
	bind_jnt.freeze()
	bind_jnt.attr('useOutlinerColor').value = 1
	# Assign soft blue to outline color 
	bind_jnt.setAttribute('outlinerColor', float(0.143), float(0.930), float(0.930)  )
	

	# Create Attr
	bind_jnt.addAttribute( at = 'float', keyable = True , ln = 'multiply' ,dv = 0.1 )
	bind_jnt.addAttribute( at = 'float', keyable = True , ln = 'biasAdjust' ,dv = 0 )

	# Constraint joint parent to controller
	bind_parCons = core.parentConstraint( help_jnt , bind_jnt )
	bind_parCons.name = rawName + 'Helper' + side + 'Jnt_parCons'

	# Scale Constraint 
	bind_sacleCons = core.scaleConstraint( help_jnt , bind_jnt )
	bind_sacleCons.name = rawName + 'Helper' + side + 'Jnt_scaleCons'

	# bind_jnt.lockHideAttrLst_new( 'tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz' , lock = 0 , keyable = 1 )

	for attr in ('tx' , 'ty' , 'tz' , 'rx' , 'ry' , 'rz') :
		bind_jnt.attr( attr ).editAttrManual(lock = False , keyable = False ,channelBox = False)

	# Part2 add more connection


	muscle_MultiplyVal_mdl = core.MDLWithMul( name = rawName +'MultiplyVal'+ side )
	muscle_MultiplyVal_mdl.suffix

	muscle_ResisVal_mdl = core.MDLWithMul( name = rawName +'ResisVal'+ side )
	muscle_ResisVal_mdl.suffix
	muscle_ResisVal_mdl.attr('input1').value = -0.01


	muscleNonZro_adl = core.AddDoubleLinear( name = rawName +'NonZro'+ side )
	muscleNonZro_adl.suffix
	muscleNonZro_adl.attr('input2').value = 1


	# Connect value
	bind_jnt.attr('multiply') >> muscle_ResisVal_mdl.attr('multiply')
	muscle_ResisVal_mdl.attr('output') >> muscle_MultiplyVal_mdl.attr('multiply')

	parentB_bJnt.attr('r%s' %axis) >> muscle_MultiplyVal_mdl.attr('input1')
	muscle_MultiplyVal_mdl.attr('output') >> muscleNonZro_adl.attr('input1')
	muscleNonZro_adl.attr('output') >> help_jnt.attr('s%s' %axis)

	bind_jnt.attr('biasAdjust') >> muscle_cons.attr('biasAdjust')



	misc.makeHeader('Create helper joint %s complete' %help_jnt.name)

	return help_jnt.name


#createHelperJoint( parentA = 'upperArmLFT_bJnt' , parentB = 'lowerArmLFT_bJnt' , side = 'LFT' ,axis = 'z' )
#createHelperJoint( parentA = 'upperArmRGT_bJnt' , parentB = 'lowerArmRGT_bJnt' , side = 'LFT' ,axis = 'z' )

# name_help_jnt = createHelperJoint( parentA = 'lowerArmLFT_bJnt' , parentB = 'handLFT_bJnt' , side = 'LFT' ,axis = 'z' )
#createHelperJoint( parentA = 'handLFT_bJnt' , parentB = 'thumb01LFT_bJnt' , side = 'LFT' ,axis = 'x' )
#createHelperJoint( parentA = 'thumb01LFT_bJnt' , parentB = 'thumb02LFT_bJnt' , side = 'LFT' ,axis = 'x' )