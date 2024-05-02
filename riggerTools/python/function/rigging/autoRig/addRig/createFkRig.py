'''
from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
'''


'''
#... detail import
import sys
import maya.utils
import importlib
import maya.cmds as mc
sys.path.append('D:/sysTools/nmTools_github/riggerTools/python')
from nmMenu import nmMenu2023
importlib.reload(nmMenu2023)
maya.utils.executeDeferred('nmMenu2023.runMenu()')
from function.framework.reloadWrapper import reloadWrapper as reload
'''





'''
[Latast] Collection of FK additional controller
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






#.... Make [broad joint] >>> control >>> nurb >>> [locator] >>> constraint >>> [controller] >>> [bind joint]
def smoothFk(	broad_jnt = ['frontSkirtBroad01_jnt','frontSkirtBroad02_jnt','frontSkirtBroad03_jnt','frontSkirtBroad04_jnt'],
				nurbs = 'frontSkirt_nrb',region = 'front',side = '',scale = 1, ctrlShape='circle_ctrlShape'):

	broad_jnt_skc = core.SkinCluster( broad_jnt, nurbs, dropoffRate = 7, maximumInfluences = 2 )
	broad_jnt_skc.name = region + side + '_skc'

	createFkRig_direct(	nameSpace = ''  ,  name = region , parentTo = ''  ,
					tmpJnt = 	broad_jnt	,
					charScale = scale	, priorJnt = '' 			,
					side = side ,ctrlShape = ctrlShape  , localWorld = False , 
					color = 'red' , curlCtrl = True ,suffix = '_jnt',parentToPriorJnt = False,
					parentMatrix = False, rotateOrder = 'xzy')
	#... is not finish yet
	#... next make the slave bind joint and the locator




#... FK the attatch with joint in Arg directly
#... connect direct with joint arg





#... everything same but edit curl condition
#... [useHierarchy] is mean joint that create will moved to under priorJnt by not parent old useHierarchy
#... [isTmpJnt] is ask the arg is temp joint or not

def fkRig_newCurl(	nameSpace = '' , name = 'ear' , parentTo = 'ctrl_grp' ,
					tmpJnt = 	( 	'ear01LFT_tmpJnt','ear02LFT_tmpJnt', 'ear03LFT_tmpJnt')	,
					charScale = 1, priorJnt = 'head01_bJnt' , priorCtrl = '' ,
					side = 'LFT', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'red', curlCtrl = False, suffix = '_bJnt', useHierarchy = True, rotateOrder = 'zxy'	,isTmpJnt = True, useParentInstead = False,
					curlCtrlShape = 'stick_ctrlShape'):

	
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
		elif color:
			ctrl.color = color
		else:
			ctrl.color = 'white'


		
		gimbal = core.createGimbal( ctrl )
		tmp = core.Dag( tmpJnt[  num  ] )

		if isTmpJnt:
			bJnt = rigTools.jointAt( tmp )
			bJnt.name =  '%s%s%02d%s%s'  %(nameSpace,	name,( num +1),side,suffix	)
		else:
			bJnt = core.Dag( tmpJnt[  num  ] )





		
		
		
		zroGrp,offsetGrp = rigTools.zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%s%02d%sZro_grp'  %(nameSpace,	name,( num +1),side	)
		offsetGrp.name = '%s%s%02d%sOffset_grp'  %(nameSpace,	name,( num +1),side	)


		#... set Rotation Order
		ctrl.rotateOrder = rotateOrder 
		gimbal.rotateOrder = rotateOrder

		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		bJnts.append( bJnt )
		ofGrps.append( offsetGrp )


		#...  useHierarchy is mean not parent same Hierarchy to it.
		if useHierarchy == True:
			if not num == 0:
				print('\nNo need to useHierarchy.\n')
				zroGrp.parent( gmbls[ num -1] )

				if isTmpJnt == True:
					bJnt.parent( bJnts[num -1] )
					# mc.error('WHAT165')
				else:
					pass
			else:
				print('\nUse Hierarchy.\n')
				rigGrp.maSnap(bJnts[0])
				zroGrp.parent( rigGrp )

		elif useHierarchy == False: #... if not mean not parent same Hierarchy to it.
			if isTmpJnt == True:
				print('This is useHierarchy == False')
				bJnt.parent( priorJnt )
			else:
				pass
			zroGrp.parent( rigGrp )
			



	if mc.objExists(parentTo):

		if useHierarchy == True:
			
			if priorJnt :
				rigGrp.parent( parentTo )
				
				bJnts[0].parent( priorJnt )


			elif isTmpJnt == False:
				#... parent control grp under
				rigGrp.parent( parentTo )



			else:
				print ('There are no joint arg return blind joint name: %s' %rigGrp.name)
				print ('There are no joint arg return blind joint name: %s' %bJnts[0])



		elif useHierarchy == False:
			rigGrp.parent( parentTo )
			print(rigGrp.name)
			




	else:
		if priorJnt == '':
			pass
		else:
			print('\nERROROO_214\n')
			bJnts[0].parent( priorJnt )




	# Make curl controller 
	if curlCtrl:
		curl_ctrl = core.Dag('%s%s%s%s_ctrl'  %(nameSpace, name,'Curl',side))
		curl_ctrl.nmCreateController( curlCtrlShape )
		curl_ctrl.editCtrlShape( axis = charScale * 7.4 )
		curl_ctrl.color = color
		zroGrpCurl = rigTools.zeroGroupNam(curl_ctrl)
		curl_ctrl.rotateOrder = rotateOrder 

		#... Do it later
		# curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )

		#... Not use anymore
		# curl_parCons = core.parentConstraint( bJnts[0],zroGrpCurl , mo = False )
		# curl_parCons.name = '%s%s%s%s_psCons'  %(nameSpace,	name , 'Curl',side	)

		#... snap position to root 
		zroGrpCurl.maSnap(bJnts[0])
		
		first_offset_grp = core.Dag(ofGrps[0])

		#... connect attr
		curl_ctrl.attr('tx') >> first_offset_grp.attr('tx')
		curl_ctrl.attr('ty') >> first_offset_grp.attr('ty')
		curl_ctrl.attr('tz') >> first_offset_grp.attr('tz')

		curl_ctrl.attr('sx') >> first_offset_grp.attr('sx')
		curl_ctrl.attr('sy') >> first_offset_grp.attr('sy')
		curl_ctrl.attr('sz') >> first_offset_grp.attr('sz')

		
		#... Make attr at curl ctrl
		curlShape_ctrl = core.Dag(curl_ctrl.shape)
		curlShape_ctrl.addAttribute(at = 'long', min = 0, max = 1, longName = 'Detail', keyable = True, defaultValue = 0)
		mc.connectAttr('{0}.Detail'.format(curlShape_ctrl.name), '{0}.visibility'.format(zGrps[0]), f=True )

		#... Next try to use MDV for make multiplier [Do it now]

		#... Create PMA
		passValue_pma = core.PlusMinusAverage( nameSpace+name+'Curl'+side+'_pma' )

		#... Create MDV
		multiplyValue_mdv = core.MultiplyDivine( nameSpace+name+'_storeCurl'+side+'_mdv' )


		curl_ctrl.attr('rotate') >> passValue_pma.attr('input3D[0]')
		passValue_pma.attr('output3D') >> multiplyValue_mdv.attr('input1')

		#... Create meta node

		# metaNode = core.MetaRoot('fkRig_newCurl_meta')
		fkRig_newCurl_meta = core.MetaGeneric( name + side + '_meta')
		fkRig_newCurl_meta.addAttribute( attributeType = 'message' , longName =  name+side)

		passValue_pma.attr('message') >> fkRig_newCurl_meta.attr(name+side)
		curl_ctrl.attr('message') >> fkRig_newCurl_meta.attr('Rig_Prior')

		fkRig_newCurl_meta.setAttribute('Color', color, type = 'string')
		fkRig_newCurl_meta.setAttribute('Side', side, type = 'string')
		fkRig_newCurl_meta.setAttribute('Base_Name', rigGrp.name, type = 'string')
		
		for eachObj in ofGrps:
			# curl_ctrl.attr('rotate') >> eachObj.attr( 'rotate' )
			multiplyValue_mdv.attr('output') >> eachObj.attr( 'rotate' ) #... change line to use multiplt divide instead

		zroGrpCurl.parent( rigGrp )

		if useParentInstead == False:

			if priorCtrl :
				mc.parentConstraint( priorCtrl , rigGrp , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )
				mc.scaleConstraint( priorCtrl , rigGrp , name = '%sRig%s_scaleCons' % ( name,side ) ,mo = True)
			elif priorJnt: #... this case if for spineFK rig make hip shake
				mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )
				mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side ) ,mo = True)

		elif useParentInstead == True:
			#... just parent under to it
			if mc.objExists(priorCtrl):
				print('#... just parent under to it')
				print(rigGrp.name)
				print(priorCtrl)

				mc.parent(rigGrp.name, priorCtrl)
			else:
				print('#... do noting pass it.')


	if curlCtrl:
		localWorld_attr = curlShape_ctrl.name
	else:
		#... find shape name
		

		ctrl_shape = misc.shapeName(ctrls[0])

		localWorld_attr = ctrl_shape


	# create local / world follwer arg #
	if localWorld:



																										# where attr occur	[rig_grp_name]	[]
		Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( localWorld_attr , rigGrp.name , parentTo , zGrps[0] )
		Loc_grp.name = part + 'Local_grp'
		World_grp.name = part + 'World_grp'
		WorldGrp_orientCons.name = part + 'WorldGrp_orientCons'
		ZroGrp_orientCons.name = part + 'ZroGrp_orientCons'
		reverseNode_rev.name = part + 'ZroGrpOrientCons_rev'

			




	# If having priorJnt but disable curl then just paCon
	if priorJnt :
		if curlCtrl == False:
			mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )   ,mo = True)
			mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side )   ,mo = True)

	# create another loop here because of bJnt will wrong orient when constraint and then parent
	# parent joint to controller
		
	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		parCons = core.parentConstraint( gmbls[num] , bJnts[num]  )
		parCons.name = '%s%s%02d%s_psCons'  %(nameSpace, name, ( num +1), side	)
		print ('\nPARENT IT DONE...')

	misc.makeHeader('End of {0}'.format(__name__))


	if curlCtrl:
		# Add return all ctrl name at index 4
		return gmbls[0] ,rigGrp.name , bJnts , zroGrpCurl.name , ctrls
	else:
		return gmbls[0] ,rigGrp.name , bJnts  , ctrls

	
	





def createFkRig_direct(	nameSpace = ''  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'ear01LFT_bJnt','ear02LFT_bJnt'  ,'ear03LFT_bJnt')	,
					charScale = 1	, priorJnt = 'head01_bJnt' 			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = False ,suffix = '_bJnt',parentToPriorJnt = False,
					parentMatrix = False, rotateOrder = 'zxy'):

	
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
		# print  (num) 
		ctrl = core.Dag(     '%s%s%02d%s_ctrl'  %(nameSpace , name,( num +1),side)     )
		ctrl.nmCreateController( ctrlShape )
		ctrl.editCtrlShape( axis = charScale * 6.4 )


		if side:
			myColor = mnd.askColor(side)
			ctrl.color = myColor
		else:
			ctrl.color = color




		
		gimbal = core.createGimbal( ctrl )
		bJnt = core.Dag( tmpJnt[  num  ] )
		# bJnt = rigTools.jointAt( tmp )



		zroGrp,offsetGrp = rigTools.zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%s%02d%sZro_grp'  %(nameSpace,	name,( num +1),side	)
		offsetGrp.name = '%s%s%02d%sOffset_grp'  %(nameSpace,	name,( num +1),side	)


		#... set RotationOrder
		ctrl.rotateOrder = rotateOrder 
		gimbal.rotateOrder = rotateOrder
			
		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		# bJnts.append( bJnt )
		ofGrps.append( offsetGrp )
		
		if not  num  == 0:
			zroGrp.parent( gmbls[ num -1] )
			# bJnt.parent( bJnts[ num -1] )
		else:
			# rigGrp.maSnap(bJnts[0])
			zroGrp.parent( rigGrp )



		
	if priorJnt :
		rigGrp.parent( parentTo )
		print('There are having prior joint')
		# bJnts[0].parent( priorJnt )
	else:
		print ('There are no joint arg return blind joint name: %s' %rigGrp.name)
		# print 'There are no joint arg return blind joint name: %s' %bJnts[0]
		

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

		if parentMatrix:
			# create offset for parent matrix choice 
			offsetCurl = core.Null('%s%s%sOffset%s_grp'  %(nameSpace, name,'Curl',side))
			offsetCurl.maSnap(zroGrpCurl)
			offsetCurl.parent(zroGrpCurl)
			curl_ctrl.parent(offsetCurl)

		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )


		
		if parentMatrix:
			
			# curl_parCons = core.parentConstraint( tmpJnt[0], zroGrpCurl , mo = False )
			zroGrpCurl.snap(tmpJnt[0])
			#mc.error('Wrong here...')
			# misc.parentMatrix( tmpJnt[0], zroGrpCurl.name, mo = True, translate = True, rotate = True, scale = True)
			misc.parentMatrix( tmpJnt[0], offsetCurl.name, mo = True, translate = True, rotate = True, scale = True)
			

		else:
			curl_parCons = core.parentConstraint( tmpJnt[0], zroGrpCurl , mo = False )
			# zroGrpCurl.maSnap(tmpJnt[0])
			curl_parCons.name = '%s%s%s%s_psCons'  %(nameSpace,	name , 'Curl',side	)
		

		'''
		curl_parCons = core.parentConstraint( tmpJnt[0], zroGrpCurl , mo = False )
		curl_parCons.name = '%s%s%s%s_psCons'  %(nameSpace,	name , 'Curl',side	)
		'''

		for eachObj in ofGrps:
			print (type( eachObj ))
			curl_ctrl.attr('rotate') >> eachObj.attr( 'rotate' )

		zroGrpCurl.parent( rigGrp )

		# cause proble ignore for now

		
		if priorJnt:
				mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )
				mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side ) ,mo = True)
				
				'''
				# cause proble ignore for now
				if parentMatrix:
					misc.parentMatrix( priorJnt, rigGrp.name, mo = True, translate = True, rotate = True, scale = True) # problem here if joint orient is zero the grp will be zero no matter is correct axis or not
				else:
					mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )
					mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side ) ,mo = True)
				'''
				


	# If having priorJnt but disable curl then just parentCon

	if priorJnt:
		if curlCtrl == False:
			if parentMatrix:

				misc.parentMatrix( priorJnt, rigGrp.name, mo = True, translate = True, rotate = True, scale = True)
			else:
				mc.parentConstraint( priorJnt , rigGrp , name = '%sRig%s_psCons' % ( name,side )   ,mo = True)
				mc.scaleConstraint( priorJnt , rigGrp , name = '%sRig%s_scaleCons' % ( name,side )   ,mo = True)
			

	# create another loop here because of bJnt will wrong orient when constraint and then parent
	# parent joint to controller
	# quarantine zone			
	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		if parentMatrix:
			misc.parentMatrix( gmbls[num], tmpJnt[num], mo = True, translate = True, rotate = True, scale = True)
		else:
			parCons = core.parentConstraint( gmbls[num] , tmpJnt[num]  )
			parCons.name = '%s%s%02d%s_psCons'  %(nameSpace, name, ( num+1), side	)
		
			scaleCons = core.scaleConstraint( gmbls[num] , tmpJnt[num]  )
			scaleCons.name = '%s%s%02d%s_scaleCons'  %(nameSpace, name, ( num+1), side	)

		print ('\nPARENT IT ...')



	#... End
	if parentToPriorJnt:
		print('mc.parent(jnts[0], priorJnt)')
		mc.parent(jnts[0], priorJnt)

	print ('\nPARENT IT Complete' )
	if curlCtrl:
		# Add return all ctrl name at index 4
		return gmbls[0] ,rigGrp.name , tmpJnt , zroGrpCurl.name , ctrls
	else:
		return gmbls[0] ,rigGrp.name , tmpJnt  , ctrls
		









#... using with tempjoint 
#... priorJnt can be None
def newCreateFkRig(	nameSpace = '' , name = 'ear' , parentTo = 'ctrl_grp' ,
					tmpJnt = 	( 	'ear01LFT_tmpJnt','ear02LFT_tmpJnt', 'ear03LFT_tmpJnt')	,
					charScale = 1, priorJnt = 'head01_bJnt' , priorCtrl = '' ,
					side = 'LFT', ctrlShape = 'circle_ctrlShape', localWorld = False , 
					color = 'red', curlCtrl = False, suffix = '_bJnt', useHierarchy = True, rotateOrder = 'zxy'	):

	
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


		#... set Rotation Order
		ctrl.rotateOrder = rotateOrder 
		gimbal.rotateOrder = rotateOrder

		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		bJnts.append( bJnt )
		ofGrps.append( offsetGrp )


		'''
		
		if not num == 0:
			if useHierarchy == True:
				zroGrp.parent( gmbls[ num -1] )
				bJnt.parent( bJnts[ num -1] )
			else:
				zroGrp.parent( rigGrp )
		else:
			rigGrp.maSnap(bJnts[0])
			zroGrp.parent( rigGrp )
		'''

		if useHierarchy == True:
			if not num == 0:
				print('\nNo need to useHierarchy.\n')
				zroGrp.parent( gmbls[ num -1] )
				bJnt.parent( bJnts[ num -1] )
			else:
				print('\nUse Hierarchy.\n')
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
			print('\nERROROO_348\n')
			bJnts[0].parent( priorJnt )


		

	# create local / world follwer arg #
	if localWorld:
		first_ctrl = core.Dag(ctrls[0])
		Loc_grp , World_grp , WorldGrp_orientCons , ZroGrp_orientCons , reverseNode_rev = rigTools.orientLocalWorldCtrl( first_ctrl.shape , rigGrp.name , parentTo , zGrps[0] )
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
		if priorCtrl :
			mc.parentConstraint( priorCtrl , rigGrp , name = '%sRig%s_psCons' % ( name,side )  ,mo = True )
			mc.scaleConstraint( priorCtrl , rigGrp , name = '%sRig%s_scaleCons' % ( name,side ) ,mo = True)
		elif priorJnt: #... this case if for spineFK rig make hip shake
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


	if curlCtrl:
		# Add return all ctrl name at index 4
		return gmbls[0] ,rigGrp.name , bJnts , zroGrpCurl.name , ctrls
	else:
		return gmbls[0] ,rigGrp.name , bJnts  , ctrls
	# End









# old version
def createFkRig(	nameSpace = ''  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'ear01LFT_tmpJnt','ear02LFT_tmpJnt'  ,'ear03LFT_tmpJnt')	,
					charScale = ''	, priorJnt = 'head01_bJnt' 			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = False	):

	
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
		# print  (num) 
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




		
		
		bJnt.name =  '%s%s%02d%s_bJnt'  %(nameSpace,	name,( num +1),side	)
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
		
		if not  num  == 0:
			zroGrp.parent( gmbls[ num -1] )
			bJnt.parent( bJnts[ num -1] )
		else:
			rigGrp.maSnap(bJnts[0])
			zroGrp.parent( rigGrp )



		
	if priorJnt :
		rigGrp.parent( parentTo )
		bJnts[0].parent( priorJnt )
	else:
		mc.error('There are no joint arg.')
		return False

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

	return bJnt.name , gmbls[0]
	# end
	





# new function for create fk chaing rig with multiple child 
# sample command
'''
fkMulChild(		nameSpace = ''  ,  name = 'hair' , parentTo = 'ctrl_grp'  ,
						tmpJnt = ( 		 'hairRoot_tmpJnt' , ['hairA1_tmpJnt','hairA2_tmpJnt','hairA3_tmpJnt'] , 
										['hairB1_tmpJnt','hairB2_tmpJnt','hairB3_tmpJnt'] 	, 
										['hairC1_tmpJnt','hairC2_tmpJnt','hairC3_tmpJnt']	)		,
										charScale = charScale	, 
										priorJnt = 'head_bJnt' 							,
										side = '' ,ctrlShape = 'circle_ctrlShape' 	 	, 
										color = 'red' , 
										curlCtrl = True	)

_fkMulSubChild( tmpJnt = (['hairD1_tmpJnt','hairD2_tmpJnt','hairD3_tmpJnt'] ) , nameSpace= '' , parentTo = 'hairC2_gmbCtrl' , priorJnt = 'hairC2_bJnt'  ,charScale=charScale ,curlCtrl=True)
'''





def checkUnerScore(name):
	if name.count('_') == 1:
		rawName = name.split('_')[0]

	elif name.count('_') == 0:
		rawName = each

	elif name.count('_') == 2: # for naming that use underscore more than one
		each_split = name.split('_')
		rawName = each_split[0] +'_'+ each_split[1]
	print('this is rawname: '+rawName)
	return rawName







#... new function for create fk chain rig with multiple child 
#... use with temp joint
def fkMulChild(	nameSpace = ''  ,  name = 'hair' , parentTo = 'ctrl_grp'  ,
						tmpJnt = (  'hairRoot_tmpJnt' , ['hairA1_tmpJnt','hairA2_tmpJnt','hairA3_tmpJnt'] , ['hairB1_tmpJnt','hairB2_tmpJnt','hairB3_tmpJnt'] 	)		,
						charScale = 1	, 
						priorJnt = '' 							,
						side = '' ,ctrlShape = 'circle_ctrlShape' 	 	, 
						color = 'red' , 
						curlCtrl = False,
						scaleCons = False,
						#... if useParentInstead priorJnt will be ignore
						useParentInstead = False,
						priorCtrl = ''	):

	#... priorCtrl will active if 'priorJnt' is None
	# rigGrp = core.Null()
	# rigGrp.name = '%sRig%s_grp' % ( name , side )

	for num in range( 0 , len(tmpJnt)):
		if num == 0 :
			# Loop of root controller
			print ('---------------------------')
			print ('%s is root for sure' %tmpJnt[num])
			print ('---------------------------')
			# tmpName  = tmpJnt[num].split('_')[0]
			tmpName = checkUnerScore(tmpJnt[num])
			ctrl = core.Dag(  '%s%s_ctrl'%(nameSpace,tmpName )    )
			ctrl.nmCreateController( ctrlShape )
			ctrl.editCtrlShape( axis = charScale * 6.5 )
			
			gimbal = core.createGimbal( ctrl )
			tmp = core.Dag( tmpJnt[  num  ] )
			bJnt = rigTools.jointAt( tmp )

			bJnt.name =  '%s%s_bJnt'  %(nameSpace,tmpName )
			zroGrp,offsetGrp = rigTools.zroNewGrpWithOffset( ctrl )
			zroGrp.snap( bJnt )
			zroGrp.name = '%s%sZro_grp'  %(nameSpace,tmpName )
			offsetGrp.name = '%s%sOffset_grp'  %(nameSpace,tmpName )



			if not color:
				if side:
					if side == 'LFT':
						ctrl.color = 'red'
					elif side == 'RGT':
						ctrl.color = 'blue'

			else:
				ctrl.color = color


			# Parent to joint
			parCons = core.parentConstraint( gimbal , bJnt  )
			parCons.name = '%s%s_psCons'  %(nameSpace, tmpName	)
			print ('\nParentConstraint ...'			)



		else:
			print ('---------------------------')
			print ('%s is child for sure' %tmpJnt[num])
			print ('---------------------------')
			jnts , zros , gmbls =  _createFkChild( tmpJnt=tmpJnt[num] , nameSpace=nameSpace, ctrlShape=ctrlShape, charScale=charScale, color=color, curlCtrl=curlCtrl, parentTo = parentTo, scaleCons = True)
			child_bJnt = jnts[0]
			zro_grp = zros[0]


			mc.parent( child_bJnt , bJnt.name )
			mc.parent( zro_grp , gimbal.name )



	if useParentInstead == False:
		if priorJnt :
			# Parent root grp of this child
			print ('---------------------------')
			print (zroGrp.name)
			print ('---------------------------')

			
			zroGrp.parent( parentTo )
			bJnt.parent( priorJnt )
			mc.parentConstraint( priorJnt , zroGrp , name = '%sRig%s_psCons' % ( tmpName,side )  ,mo = True )
			mc.scaleConstraint( priorJnt , zroGrp , name = '%sRig%s_scaleCons' % ( tmpName,side ) ,mo = True)

	else:
		print ('There are no prior joint using useParentInstead')
		bJnt.parent( priorJnt )
		zroGrp.parent( priorCtrl )


		


		



#... subfunction for fkMulChild
def _createFkChild( tmpJnt, nameSpace, ctrlShape, charScale, color, curlCtrl, parentTo, scaleCons ):
	# 7 arg
	# store var 
	tmpGrps =[]
	ctrls = []
	jnts = []
	gmbls = []
	zGrps = []
	bJnts = []
	ofGrps = []



	for num in range( 0 , ( len( tmpJnt )  ) ):
		
		# tmpName  = tmpJnt[num].split('_')[0]
		tmpName = checkUnerScore(tmpJnt[num])
		ctrl = core.Dag(  '%s%s_ctrl'%(nameSpace,tmpName )    )
		print ('****')
		print ('%s%s_ctrl'%(nameSpace,tmpName ))
		print ('****')
		
		ctrl.nmCreateController( ctrlShape )
		ctrl.editCtrlShape( axis = charScale * 6.4 )
		
		gimbal = core.createGimbal( ctrl )
		tmp = core.Dag( tmpJnt[  num  ] )
		bJnt = rigTools.jointAt( tmp )

		bJnt.name =  '%s%s_bJnt'  %(nameSpace,tmpName )
		zroGrp,offsetGrp = rigTools.zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%sZro_grp'  %(nameSpace,tmpName )
		offsetGrp.name = '%s%sOffset_grp'  %(nameSpace,tmpName )

		if not color:
			if side:
				if side == 'LFT':
					ctrl.color = 'red'
				elif side == 'RGT':
					ctrl.color = 'blue'

		else:
			ctrl.color = color



				

		tmpGrps.append( tmpName )
		ctrls.append( ctrl )
		jnts.append( tmpJnt[ num ] )
		gmbls.append( gimbal )
		zGrps.append( zroGrp )
		bJnts.append( bJnt )
		ofGrps.append( offsetGrp )
		
		if not  num  == 0:
			zroGrp.parent( gmbls[ num -1] )
			bJnt.parent( bJnts[ num -1] )
		'''	
		else:
			rigGrp.maSnap(bJnts[0])
			zroGrp.parent( rigGrp )
		'''



	#... Make curl controller 
	if curlCtrl:
		curl_ctrl = core.Dag('%s%s_ctrl'  %( tmpGrps[0] , 'Curl')	)
		#... change style
		curl_ctrl.nmCreateController( 'circle_ctrlShape' )
		curl_ctrl.editCtrlShape( axis = charScale * 3.3 )
		# curl_ctrl.rotateShape( rotate = ( 90 , 0 , 0) )
		curl_ctrl.color = 'white'
		zroGrpCurl = rigTools.zeroGroupNam(curl_ctrl)
		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )
		curl_parCons = core.parentConstraint( bJnts[0],zroGrpCurl , mo = False )
		curl_parCons.name = '%s%s_psCons'  %(tmpGrps[0],'Curl')

		for eachObj in ofGrps:
			print (type( eachObj ))
			curl_ctrl.attr('rotate') >> eachObj.attr( 'rotate' )

		# Parent curl to ctrlGrp for good alinement
		if parentTo:
			zroGrpCurl.parent( parentTo )


	# quarantine zone	
	# create another loop here because of bJnt will wrong orient when constraint and then parent
	# parent joint to controller

	for  num  in range( 0 , ( len( tmpJnt )  ) ):
		parCons = core.parentConstraint( gmbls[num] , bJnts[num]  )
		parCons.name = '%s%s_psCons'  %(nameSpace, tmpName	)
		print ('\nParentConstraint ...')

		if scaleCons:
			scaleCons = core.scaleConstraint( gmbls[num] , bJnts[num]  )
			scaleCons.name = '%s%s_scaleCons'  %(nameSpace, tmpName	)

	return bJnts , zGrps ,gmbls





def _fkMulSubChild(parentTo, priorJnt ,tmpJnt, nameSpace,ctrlShape='circle_ctrlShape' , charScale=1 , color='red' ,curlCtrl=False  ):
	''' just small function that create fk and parent it to prior '''
	childJnt_grp , childZro_grp, gmbl = _createFkChild( tmpJnt , nameSpace , ctrlShape , charScale , color ,curlCtrl ,parentTo )
														
	mc.parent( childJnt_grp[0] ,  priorJnt )
	mc.parent( childZro_grp[0] ,  parentTo )
	mc.select( deselect = True )


	