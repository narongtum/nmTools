'''
from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)
'''


import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc as misc
reload( misc )








from function.rigging.util import mayaNodeDict as mnd
reload(mnd)


# fk the attatch with arg directly
# Do not use with tempJnt
def createFkRig_direct(	nameSpace = ''  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'ear01LFT_bJnt','ear02LFT_bJnt'  ,'ear03LFT_bJnt')	,
					charScale = ''	, priorJnt = 'head01_bJnt' 			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = False ,suffix = '_bJnt',parentToPriorJnt = False	):

	
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



		myColor = mnd.askColor(side)

		ctrl.color = myColor


		'''
		if not color:
			if side:
				if side == 'LFT':
					ctrl.color = 'red'
				elif side == 'RGT':
					ctrl.color = 'blue'


			ctrl.color = 'red'
		else:
			ctrl.color = color
		'''


		
		gimbal = core.createGimbal( ctrl )
		bJnt = core.Dag( tmpJnt[  num  ] )
		# bJnt = rigTools.jointAt( tmp )


		# bJnt.name =  '%s%s%02d%s%s'  %(nameSpace,	name,( num +1),side,suffix)
		# bJnt.name =  '%s%s%02d%s%s'  %(nameSpace,	name,( num +1),side,'_bJnt')
		zroGrp,offsetGrp = rigTools.zroNewGrpWithOffset( ctrl )
		zroGrp.snap( bJnt )
		zroGrp.name = '%s%s%02d%sZro_grp'  %(nameSpace,	name,( num +1),side	)
		offsetGrp.name = '%s%s%02d%sOffset_grp'  %(nameSpace,	name,( num +1),side	)


		
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
		print 'There are no joint arg return blind joint name: %s' %rigGrp.name
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
		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )
		curl_parCons = core.parentConstraint( tmpJnt[0],zroGrpCurl , mo = False )
		# zroGrpCurl.maSnap(tmpJnt[0])
		curl_parCons.name = '%s%s%s%s_psCons'  %(nameSpace,	name , 'Curl',side	)

		for eachObj in ofGrps:
			print type( eachObj )
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
		parCons = core.parentConstraint( gmbls[num] , tmpJnt[num]  )
		parCons.name = '%s%s%02d%s_psCons'  %(nameSpace, name, ( num+1), side	)
		
		scaleCons = core.scaleConstraint( gmbls[num] , tmpJnt[num]  )
		scaleCons.name = '%s%s%02d%s_scaleCons'  %(nameSpace, name, ( num+1), side	)

		print '\nPARENT IT ...'

	# End
	if parentToPriorJnt:
		print('mc.parent(jnts[0], priorJnt)')
		mc.parent(jnts[0], priorJnt)

	print '\nPARENT IT Complete' 
	if curlCtrl:
		# Add return all ctrl name at index 4
		return gmbls[0] ,rigGrp.name , tmpJnt , zroGrpCurl.name , ctrls
	else:
		return gmbls[0] ,rigGrp.name , tmpJnt  , ctrls
		






# using with tempjoint 
def newCreateFkRig(	nameSpace = ''  ,  name = 'ear' , parentTo = 'ctrl_grp'  ,
					tmpJnt = 	( 	'ear01LFT_tmpJnt','ear02LFT_tmpJnt'  ,'ear03LFT_tmpJnt')	,
					charScale = ''	, priorJnt = 'head01_bJnt' 			,
					side = 'LFT' ,ctrlShape = 'circle_ctrlShape'  , localWorld = False , 
					color = 'red' , curlCtrl = False ,suffix = '_bJnt'	):

	
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
		print 'There are no joint arg return blind joint name: %s' %rigGrp.name
		print 'There are no joint arg return blind joint name: %s' %bJnts[0]
		

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
			print type( eachObj )
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
		print '\nPARENT IT ...'


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
			print type( eachObj )
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
		print '\nPARENT IT ...'

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










# new function for create fk chaing rig with multiple child 
# use with temp joint
def fkMulChild(	nameSpace = ''  ,  name = 'hair' , parentTo = 'ctrl_grp'  ,
						tmpJnt = (  'hairRoot_tmpJnt' , ['hairA1_tmpJnt','hairA2_tmpJnt','hairA3_tmpJnt'] , ['hairB1_tmpJnt','hairB2_tmpJnt','hairB3_tmpJnt'] 	)		,
						charScale = 1	, 
						priorJnt = '' 							,
						side = '' ,ctrlShape = 'circle_ctrlShape' 	 	, 
						color = 'red' , 
						curlCtrl = False	):


	# rigGrp = core.Null()
	# rigGrp.name = '%sRig%s_grp' % ( name , side )

	for num in range( 0 , len(tmpJnt)):
		if num == 0 :
			# Loop of root controller
			print '---------------------------'
			print '%s is root for sure' %tmpJnt[num]
			print '---------------------------'
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
			print '\nParentConstraint ...'			



		else:
			print '---------------------------'
			print '%s is child for sure' %tmpJnt[num]
			print '---------------------------'
			jnts , zros , gmbls =  _createFkChild( tmpJnt=tmpJnt[num] , nameSpace=nameSpace, ctrlShape=ctrlShape, charScale=charScale, color=color,curlCtrl=curlCtrl ,parentTo = parentTo)
			child_bJnt = jnts[0]
			zro_grp = zros[0]


			mc.parent( child_bJnt , bJnt.name )
			mc.parent( zro_grp , gimbal.name )




	if priorJnt :
		# Parent root grp of this child
		print '---------------------------'
		print zroGrp.name
		print '---------------------------'

		
		zroGrp.parent( parentTo )
		bJnt.parent( priorJnt )
		mc.parentConstraint( priorJnt , zroGrp , name = '%sRig%s_psCons' % ( tmpName,side )  ,mo = True )
		mc.scaleConstraint( priorJnt , zroGrp , name = '%sRig%s_scaleCons' % ( tmpName,side ) ,mo = True)
	else:
		pass
		



# subfunction fkMulChild
def _createFkChild( tmpJnt, nameSpace, ctrlShape, charScale, color, curlCtrl, parentTo ):
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
		print '****'
		print '%s%s_ctrl'%(nameSpace,tmpName )
		print '****'
		
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



	# Make curl controller 
	if curlCtrl:
		curl_ctrl = core.Dag('%s%s_ctrl'  %( tmpGrps[0] , 'Curl')	)
		curl_ctrl.nmCreateController( 'stick_ctrlShape' )
		curl_ctrl.editCtrlShape( axis = charScale * 3.3 )
		curl_ctrl.rotateShape( rotate = ( 90 , 90 , 0) )
		curl_ctrl.color = 'white'
		zroGrpCurl = rigTools.zeroGroupNam(curl_ctrl)
		curl_ctrl.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'sx', 'sy' , 'sz' , 'v' )
		curl_parCons = core.parentConstraint( bJnts[0],zroGrpCurl , mo = False )
		curl_parCons.name = '%s%s_psCons'  %(tmpGrps[0],'Curl')

		for eachObj in ofGrps:
			print type( eachObj )
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
		print '\nParentConstraint ...'

	return bJnts , zGrps ,gmbls





def _fkMulSubChild(parentTo, priorJnt ,tmpJnt, nameSpace,ctrlShape='circle_ctrlShape' , charScale=1 , color='red' ,curlCtrl=False  ):
	''' just small function that create fk and parent it to prior '''
	childJnt_grp , childZro_grp, gmbl = _createFkChild( tmpJnt , nameSpace , ctrlShape , charScale , color ,curlCtrl ,parentTo )
														
	mc.parent( childJnt_grp[0] ,  priorJnt )
	mc.parent( childZro_grp[0] ,  parentTo )
	mc.select( deselect = True )


	