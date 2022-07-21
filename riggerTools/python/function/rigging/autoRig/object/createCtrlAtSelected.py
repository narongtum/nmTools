# create controller from selected
# can select multiple geo

'''
# local run
from function.rigging.autoRig.object import  createCtrlAtSelected
reload( createCtrlAtSelected )


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
								scale = 1							,
								ctrlShape = 'circle_ctrlShape'		,
								color = 'yellow'						,
				):

		rawName = ''
		rawNamLst = []
		storeNamLst = []
		selected = mc.ls(sl = True)
		for each in selected:
			rawName = each.split('_')[0]
			# name with first index
			storeNamLst.append( rawName )
			# full name
			rawNamLst.append( each )


		'''rawName=[]
								selected = mc.ls(sl = True)
								for each in selected:
									rawName.split(each)'''

		for i in range(len(storeNamLst)):

			
			self.__name = str( storeNamLst[i] )

			# Create  controller
			self.child_ctrl = core.Dag( storeNamLst[i] + '_ctrl' )
			self.child_ctrl.nmCreateController(ctrlShape)
			self.child_ctrl.editCtrlShape( axis = scale * 1.2 )
			self.child_ctrl.color = color
			self.child_ctrl.rotateOrder = 'xzy'
			self.child_ctrl.hideArnoldNode()

			print 'create gimbal controller'
			self.gimbal_ctrl = core.createGimbal( self.child_ctrl )
			self.gimbal_ctrl.hideArnoldNode()

			# Create zero group
			self.childZro_grp = rigTools.zroGrpWithOffset( self.child_ctrl )


			self.childZro_grp.matchPosition( rawNamLst[i] )
			self.childZro_grp.matchRotation( rawNamLst[i] )
			

			# Making joint parent of controller
			self.joint_parCons = core.parentConstraint( self.gimbal_ctrl , rawNamLst[i] )
			self.joint_parCons.name = storeNamLst[i] + 'Jnt_parCons'

			self.joint_ScalCons = core.scaleConstraint( self.gimbal_ctrl , rawNamLst[i] )
			self.joint_ScalCons.name = storeNamLst[i] + 'Jnt_scalCons'


	def __str__(self):
		return str(self.name)

	def getName(self):
		return self.__name

	name = property( getName , None , None , None )







def creControllerFunc(	scale = 1,ctrlShape = 'circle_ctrlShape',color = 'yellow'	):
	rawName = ''
	rawNamLst = []
	storeNamLst = []
	selected = mc.ls(sl = True)
	for each in selected:
		rawName = each.split('_')[0]
		# name with first index
		storeNamLst.append( rawName )
		# full name
		rawNamLst.append( each )



	for i in range(len(storeNamLst)):

			
			#name = str( storeNamLst[i] )

			# Create  controller
			child_ctrl = core.Dag( storeNamLst[i] + '_ctrl' )
			child_ctrl.nmCreateController(ctrlShape)
			child_ctrl.editCtrlShape( axis = scale * 1.2 )
			child_ctrl.color = color
			child_ctrl.rotateOrder = 'xzy'
			child_ctrl.hideArnoldNode()

			print 'create gimbal controller'
			gimbal_ctrl = core.createGimbal( child_ctrl )
			gimbal_ctrl.hideArnoldNode()

			# Create zero group
			childZro_grp = rigTools.zroGrpWithOffset( child_ctrl )


			childZro_grp.matchPosition( rawNamLst[i] )
			childZro_grp.matchRotation( rawNamLst[i] )
			

			# Making joint parent of controller
			joint_parCons = core.parentConstraint( gimbal_ctrl , rawNamLst[i] )
			joint_parCons.name = storeNamLst[i] + '_parCons'

			joint_ScalCons = core.scaleConstraint( gimbal_ctrl , rawNamLst[i] )
			joint_ScalCons.name = storeNamLst[i] + '_scalCons'





		
		
