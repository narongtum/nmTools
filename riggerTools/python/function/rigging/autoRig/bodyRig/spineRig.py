#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# spine ik Rig by Dode
# need cog_ctrl and hip_bJnt first//

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

import maya.cmds as mc

#cog_gmbCtrl
#hip_bJnt


'''# = = = = = 03 Create spine IK Rig ( Optional rig you must select one ) = = = = = #
topSpine_bJnt = spineRig.spineIK(nameSpace = ''                  ,
						spineNum = 4                  	 ,
						hipJnt = 'hip_bJnt'           	,
					   cog_ctrl = 'cog_gmbCtrl'			,
					   ctrl_grp = 'ctrl_grp'      		,
					   isIK = True                      ,
					   charScale = charScale                  )'''




def spineIK(nameSpace = '' 			,
			spineNum = '' 			,
			hipJnt = 'hip_bJnt'		, 
			cog_ctrl = 'cog_gmbCtrl', 
			ctrl_grp = 'ctrl_grp' 	,
			isIK = False			,
			charScale = ''			):
	
	# ---------- SPINE RIG ---------- #
	spName = nameSpace + 'spine'
	mainCtrl = spName + 'Rig_grp'
	mc.group( n = mainCtrl, em = True)
	giveLock = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	mc.parent (mainCtrl , ctrl_grp)


	for i in range(len(giveLock)):
		attr = mainCtrl + '.' + giveLock[i]
		mc.setAttr( attr, lock = True, keyable = False)

	for i in range(spineNum): # create & parent [ bJnt ]
		name = spName + '%02d'%(i+1)
		tmpJnt = core.Dag( name + '_tmpJnt')
		bJnt = core.Dag( name + '_bJnt')
		jnt = rigTools.jointAt( tmpJnt )#Create bJnt at tmpJnt
		jnt.rename( bJnt)
		if i > 0:
			upName = spName + '%02d'%(i)
			upJnt = core.Dag(upName + '_bJnt')
			bJnt.parent( upJnt )
		elif i == 0:
			bJnt.parent( hipJnt )
	
	# ---------- FK SPINE ---------- #
	for i in range(spineNum): # Control spine FK
		
		name = spName + '%02d'%(i+1)
		tmpJnt = core.Dag( name + '_tmpJnt')
		fkJnt = core.Dag( name + '_fkJnt')
		jnt = rigTools.jointAt( tmpJnt )#Create fkJ at tJ
		jnt.rename( fkJnt) #Rename Joint
		ctrl = core.Dag( name + '_ctrl' )#Create Ctrl
		ctrl.nmCreateController('neck_ctrlShape')
		ctrl.editCtrlShape( axis = 0.5*charScale )#Edit Shape
		Zro_grp = rigTools.zeroGroup( ctrl )
		Zro_grp.name = name + 'Zro_grp' # Create Zro_Grp
		Gmbl_ctrl = core.createGimbal( ctrl )
		# shape adjustment
		ctrl.color = 'yellow'
		# Parenting and positioning
		Zro_grp.matchAll( tmpJnt )
		if i > 0:
			upName = spName + '%02d'%(i)
			upGmbl = core.Dag(upName + '_gmbCtrl')
			upJnt = core.Dag(upName + '_fkJnt')
			fkJnt.parent( upJnt )
			Zro_grp.parent( upGmbl )
			
		core.parentConstraint(ctrl,fkJnt)
		if i == 0:
			Zro_grp.parent( mainCtrl )
			
			fkHeadGrp = spName + 'FK_grp'
			fkJntHeadGrp = 'spineFKJnt_Grp'
			
			mc.group( n = fkHeadGrp, em = 1)
			mc.group( n = fkJntHeadGrp, em = 1)
			
			mc.parent( fkJntHeadGrp, fkHeadGrp)
			mc.parentConstraint( cog_ctrl, fkHeadGrp, mo = 0, w = 1 )
			mc.parentConstraint( cog_ctrl, Zro_grp, mo = 1, w = 1 ) 
			mc.parent( fkJnt, fkJntHeadGrp)
			mc.parent( Zro_grp, fkHeadGrp)
			mc.parent( fkHeadGrp, mainCtrl)


	if isIK == True:
		# ---------- IK SPINE ----------- #
		# Create Living Group
		ikHeadGrp = spName + 'IK_grp'
		ikJntHeadGrp = spName + 'IKJnt_Grp'
		ikHeadCtrlGrp = spName + 'IKCtrl_Grp'
		
		mc.group( n = ikHeadGrp, em = 1)
		mc.group( n = ikJntHeadGrp, em = 1)
		mc.group( n = ikHeadCtrlGrp, em = 1)
		mc.parent( ikJntHeadGrp, ikHeadCtrlGrp, ikHeadGrp)
		mc.parentConstraint( cog_ctrl, ikHeadGrp, mo = 0, w = 1 )

		for i in range(spineNum): # create & parent [ ikJnt ]
			name = spName + '%02d'%(i+1)
			tmpJnt = core.Dag( name + '_tmpJnt')
			ikJnt = core.Dag( name + '_ikJnt')
			jnt = rigTools.jointAt( tmpJnt )#Create ikJnt at tmpJnt
			jnt.rename( ikJnt)
			if i > 0:
				upName = spName + '%02d'%(i)
				upJnt = core.Dag(upName + '_ikJnt')
				ikJnt.parent( upJnt )
			elif i == 0:
				ikJnt.parent( ikJntHeadGrp)
				
		# Naming    
		upJnt = spName + '%02d_ikJnt' % (spineNum)
		midJnt = spName + '%02d_ikJnt' % (spineNum/2)
		lowJnt = spName + '01_ikJnt'
		
		upClu = 'upperBack_clu'
		lowClu = 'lowerBack_clu'
		
		ikHand = 'backIK_handle'
		ikCrv = 'backIK_crv'

		# Function 
		# IK CTRL
		giveCtrl = ['upper','mid','lower']
		for c in range(len(giveCtrl)):
			aka = giveCtrl[c]
			if aka == 'upper':
				name = aka + 'Back'
				tmpPos = upJnt
			elif aka == 'mid':
				name = 'backBend'
				tmpPos = midJnt
			elif aka == 'lower':
				name = aka + 'Back'
				tmpPos = lowJnt
				
			ctrl = core.Dag( name + '_ctrl' )
			ctrl.nmCreateController( 'spine_ctrlShape')#Create Ctrl
			ctrl.editCtrlShape( axis =  0.5*charScale )#Edit Shape
			ctrl.color = 'red'
			
			zGrp = rigTools.zeroGroup( ctrl )
			zGrp.name = name + '_zGrp' # Create zGrp
			Gmbl_ctrl = core.createGimbal( ctrl )
			zGrp.matchAll( tmpPos )
		
		mc.parent('upperBack_zGrp', 'backBend_gmbCtrl')
		mc.parent( 'lowerBack_zGrp' ,'backBend_zGrp', ikHeadCtrlGrp)
		
		# IK handle
		mc.ikHandle( n = ikHand, sj = lowJnt, ee = upJnt, sol = 'ikSplineSolver', pcv = False)
		mc.rename('curve1', ikCrv)
		mc.connectAttr( 'backBend_gmbCtrl.ry', ikHand + '.twist' )
		mc.setAttr( ikCrv + '.inheritsTransform', 0)
		mc.cluster( ikCrv + '.cv[0:1]',n = lowClu)
		mc.cluster( ikCrv + '.cv[2:3]',n = upClu)
		mc.rename( lowClu + 'Handle', lowClu)
		mc.rename( upClu + 'Handle', upClu)
		mc.parent( lowClu + '1','lowerBack_gmbCtrl')
		mc.parent( upClu + '1','upperBack_gmbCtrl')
		
		mc.parent( ikHand, ikCrv, mainCtrl)
		mc.parent( ikHeadGrp, mainCtrl)

		# BORN FOR BLEND
		
		# created Ctrl Name
		cogAttr =  'cog_ctrl.FK_IK'
		rev = spName + 'Blend_rev'
		
		mc.addAttr( 'cog_ctrl' , longName = 'FK_IK', attributeType = 'float', k = True, min = 0, max = 1 )

		
		revOutFK = rev + '.outputX'
		revOutIK = rev + '.inputX'
		mc.createNode( 'reverse', n = rev)
		mc.connectAttr( cogAttr, rev + '.inputX')
		# Blend loop
		for i in range(spineNum): # create & parent [ bJnt ]
			name = spName + '%02d'%(i+1)
			bJnt = name + '_bJnt'
			ikJnt = name + '_ikJnt'
			fkJnt = name + '_fkJnt'
			con = bJnt + '_parentConstraint1'
			conFK = con + '.' + fkJnt + 'W0'
			conIK = con + '.' + ikJnt + 'W1'
			# FUNC
			mc.parentConstraint( fkJnt, ikJnt, bJnt, mo = True, w = 0)
			mc.connectAttr( revOutIK, conIK )
			mc.connectAttr( revOutFK, conFK )


		# TURN OFF VIS
		mc.setAttr( ikHand + '.v',0 )
		mc.setAttr( ikCrv + '.v',0 )
		
		mc.setAttr( lowClu + '1' + '.v',0 )
		mc.setAttr( upClu + '1' + '.v',0 )
		mc.setAttr( fkJntHeadGrp + '.v',0 )
		mc.setAttr( ikJntHeadGrp + '.v',0 )

		mc.connectAttr( revOutIK, spName + 'IKCtrl_Grp.v' )
		mc.connectAttr( revOutFK, spName + '01Zro_grp.v' )


	elif isIK == False:

		for i in range(spineNum): # create & parent [ bJnt ]
			name = spName + '%02d'%(i+1)
			bJnt = name + '_bJnt'
			fkJnt = name + '_fkJnt'
			# FUNC
			mc.parentConstraint( fkJnt, bJnt, mo = True, w = 1)


		mc.setAttr( fkJntHeadGrp + '.v',0 )

	# Goodbye vis
	print  ('DONE IK_FK SPINE RIG ----------<>')
	
	return bJnt # spineRig_grp

#spineRig(spineNum = 4 , hipJnt = 'hip_bJnt', cog_ctrl = 'cog_gmbCtrl') #
