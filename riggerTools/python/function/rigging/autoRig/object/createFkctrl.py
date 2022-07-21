# For study create object from wrapping class
# create controller at arg 
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

class fkRig( object ):
	def __init__(				self 									,
								charScale = 1							,
								name = 'ring03LFT'						,
								positionName = ''							,
								isConstraint = True						,
								ctrlShape = 'middle01LFT_ctrlShape'		,
								color = 'yellow'						,
								parentTo = ''
				):

		self.__name = str(name)
		parent_jnt = core.Dag( positionName )

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
		#self.childZro_grp = rigTools.zroGrpWithOffset( self.child_ctrl , name = name)
		#self.childZro_grp.name = name +'_Zro_grp'


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

		
		



# Create controller and snap to bind joint
class fkBrRig( object ):
	def __init__(				self 								,
								charScale = 1						,
								name = 'ring03'					,
								elem = ''						,
								side = 'LFT'					,
								ext = '_bind_jnt'	,
								ctrlShape = 'middle01LFT_ctrlShape'	,
								color = 'yellow'
				):





		parent = name + side + ext
		parent_jnt = core.Dag( parent )

		# Create  controller
		self.object_ctrl = core.Dag( name + elem + '_ctrl' )
		self.object_ctrl.nmCreateController(ctrlShape)
		self.object_ctrl.editCtrlShape( axis = charScale * 1.2 )
		self.object_ctrl.color = color
		self.object_ctrl.rotateOrder = 'xzy'



		print 'create gimbal controller'
		gimbal_ctrl = core.createGimbal( self.object_ctrl )

		# Create zero group
		childZro_grp = rigTools.zroGrpWithOffset( self.object_ctrl )
		#self.childZro_grp = rigTools.zroGrpWithOffset( self.child_ctrl , name = name)
		#self.childZro_grp.name = name +'_Zro_grp'


		childZro_grp.matchPosition( parent_jnt )
		childZro_grp.matchRotation( parent_jnt )
		

		# Making joint parent of controller
		self.joint_parCons = core.parentConstraint( gimbal_ctrl , parent_jnt )
		self.joint_parCons.name = name + 'Jnt_parCons'


		self.joint_ScalCons = core.scaleConstraint( gimbal_ctrl , parent_jnt )
		self.joint_ScalCons.name = name + 'Jnt_scalCons'