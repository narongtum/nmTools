# For study create object from wrapping class
# create controller at selected joint
# Copy from createCtrloject
# Can delete 


'''
# local run
from function.rigging.autoRig.object import  createFkctrl
reload( createFkctrl )


'''
import maya.cmds as mc

from function.rigging.autoRig.base import core
reload( core )

from function.rigging.autoRig.base import rigTools
reload( rigTools )

class createCtrlAtSelect( object ):
	'''
	@param charScale , isConstraint , ctrlShape , color
	@return: None
	'''

	def __init__(				self 									,
								charScale = 1							,
								isConstraint = True						,
								ctrlShape = 'middle01LFT_ctrlShape'		,
								color = 'yellow'						,
				):

		rawName=[]
		selected = mc.ls(sl = True)
		for each in selected:
			rawName.split(each)

			
		self.__name = str( name )

		# Create  controller
		self.child_ctrl = core.Dag( name + '_ctrl' )
		self.child_ctrl.nmCreateController(ctrlShape)
		self.child_ctrl.editCtrlShape( axis = charScale * 1.2 )
		self.child_ctrl.color = color
		self.child_ctrl.rotateOrder = 'xzy'
		self.child_ctrl.hideArnoldNode()

		print 'create gimbal controller'
		self.gimbal_ctrl = core.createGimbal( self.child_ctrl )
		self.gimbal_ctrl.hideArnoldNode()

		# Create zero group
		self.childZro_grp = rigTools.zroGrpWithOffset( self.child_ctrl )



		self.childZro_grp.matchPosition( parent_jnt )
		self.childZro_grp.matchRotation( parent_jnt )
		

		# Making joint parent of controller
		if isConstraint:
			self.joint_parCons = core.parentConstraint( self.gimbal_ctrl , parent_jnt )
			self.joint_parCons.name = name + 'Jnt_parCons'

			self.joint_ScalCons = core.scaleConstraint( self.gimbal_ctrl , parent_jnt )
			self.joint_ScalCons.name = name + 'Jnt_scalCons'

		if parentTo:
			self.childZro_grp.parent(parentTo)

	def __str__(self):
		return str(self.name)

	def getName(self):
		return self.__name

	name = property( getName , None , None , None )

		
		
