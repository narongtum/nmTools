#... forgetten function not sure should delete it.


'''
from function.rigging.autoRig.bodyRig.spineRigExt import spineFkRigExt
reload(spineFkRigExt)
'''


'''
 Collection of spine rig 
'''


from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc
reload( misc )

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)






#... copy from addRig.createFkRig
#... using with tempjoint 
#... priorJnt can be None

def newSpineFkRig(	nameSpace = '' , name = 'spine' , parentTo = 'ctrl_grp' ,
					tmpJnt = 	('spine01_tmpJnt','spine02_tmpJnt'  ,'spine03_tmpJnt')	,
					charScale = 1, priorJnt = 'hip_bJnt' 			,
					side = '', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'red', curlCtrl = False, suffix = '_bJnt', useHierarchy = True, cogCtrl = 'cog_gmbCtrl'	):

	
	''' priorJnt can be False then it will be parent to world instead '''
	part = name + side
	# Create main group
	rigGrp = core.Null()
	rigGrp.name = '%sRig%s_grp' % ( name , side )

	# Creatre empyt for append name
	ctrls = []
	jnts = []
	gmbls = []
	zGrps = []
	bJnts = []
	ofGrps = []


	# For loop in tmpJnt 
	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		# print  num 
		ctrl = core.Dag(     '%s%s%02d%s_ctrl'  %(nameSpace , name,( num +1),side)     )
		ctrl.nmCreateController( ctrlShape )
		ctrl.editCtrlShape( axis = charScale * 6.4 )

		if not color:
			if side:
				if side == 'LFT':
					ctrl.color = 'red'
				elif side == 'RGT':
					ctrl.color = 'blue'


			ctrl.color = 'red'
		else:
			ctrl.color = color


		gimbal = core.createGimbal( ctrl )
		tmp = core.Dag( tmpJnt[  num  ] )
		bJnt = rigTools.jointAt( tmp )


		bJnt.name =  '%s%s%02d%s%s'  %(nameSpace,	name,( num +1),side,suffix	)
		zroGrp,offsetGrp = rigTools.zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%s%02d%sZro_grp'  %(nameSpace,	name,( num +1),side	)
		offsetGrp.name = '%s%s%02d%sOffset_grp'  %(nameSpace,	name,( num +1),side	)

		
		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		bJnts.append( bJnt )
		ofGrps.append( offsetGrp )


		if useHierarchy == True:
			if not num == 0:
				print('\nERROR\n')
				zroGrp.parent( gmbls[ num -1] )
				bJnt.parent( bJnts[ num -1] )
			else:
				print('\nERROR\n')
				rigGrp.maSnap(bJnts[0])
				zroGrp.parent( rigGrp )

		elif useHierarchy == False:
			bJnt.parent( priorJnt )
			zroGrp.parent( rigGrp )

	if mc.objExists(parentTo):
		if useHierarchy == True:	
			if priorJnt :
				rigGrp.parent( parentTo )
				bJnts[0].parent( priorJnt )
			else:
				print ('There are no joint arg return blind joint name: %s' %rigGrp.name)
				print ('There are no joint arg return blind joint name: %s' %bJnts[0])

		elif useHierarchy == False:
			rigGrp.parent( parentTo )
	else:
		if priorJnt == '':
			pass
		else:
			print('\nERROR\n')
			bJnts[0].parent( priorJnt )


	# create local / world follwer arg #
	if localWorld:
		Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( ctrls[0] , rigGrp.name , parentTo , zGrps[0] )
		Loc_grp.name = part + 'Local_grp'
		World_grp.name = part + 'World_grp'
		WorldGrp_orientCons.name = part + 'WorldGrp_orientCons'
		ZroGrp_orientCons.name = part + 'ZroGrp_orientCons'
		reverseNode_rev.name = part + 'ZroGrpOrientCons_rev'

	# Make curl controller 
	if curlCtrl:
		curl_ctrl = core.Dag('%s%s%s%s_ctrl'  %(nameSpace, name,'Curl',side))
		curl_ctrl.nmCreateController( ctrlShape )
		curl_ctrl.editCtrlShape( axis = charScale * 7.4 )
		curl_ctrl.color = 'white'
		zroGrpCurl = rigTools.zeroGroupNam(curl_ctrl)
		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )
		curl_parCons = core.parentConstraint( bJnts[0],zroGrpCurl , mo = False )
		# zroGrpCurl.maSnap(bJnts[0])
		curl_parCons.name = '%s%s%s%s_psCons'  %(nameSpace,	name , 'Curl',side	)

		for eachObj in ofGrps:
			print (type( eachObj ))
			curl_ctrl.attr('rotate') >> eachObj.attr( 'rotate' )

		zroGrpCurl.parent( rigGrp )
		if priorJnt :
			mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side ) ,mo = True)


	# If having priorJnt but disable curl then just pa
	if priorJnt :
		if curlCtrl == False:
			mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )   ,mo = True)
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side )   ,mo = True)

	# create another loop here because of bJnt will wrong orient when constraint and then parent
	# parent joint to controller
	# quarantine zone			
	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		parCons = core.parentConstraint( gmbls[num] , bJnts[num]  )
		parCons.name = '%s%s%02d%s_psCons'  %(nameSpace, name, ( num +1), side	)
		print ('\nPARENT IT ...')

	#... make hip shakable
	if cogCtrl:
		print(cogCtrl)
		print(zGrps[0])
		mc.parentConstraint( cogCtrl , zGrps[0] , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )


	#... Add meta node
	metaNode = core.MetaGeneric(name+'_meta')



	if curlCtrl:
		# Add return all ctrl name at index 4
		return gmbls[0] ,rigGrp.name , bJnts , zroGrpCurl.name , ctrls
	else:
		return gmbls[0] ,rigGrp.name , bJnts  , ctrls
	# End