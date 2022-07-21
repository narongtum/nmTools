#     __________________
# - -/__ Description __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# spine ik Rig by Dode
# need cog_ctrl and hip_bJnt first//



from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

def spineRig(spineNum = '' , hipJnt = 'hip_bJnt', cog_ctrl = 'cog_gmbCtrl'):
	
	# ---------- SPINE RIG ---------- #
	mainCtrl = 'spineRig_grp'
	mc.group( n = mainCtrl, em = True)
	giveLock = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']

	
	for i in range(len(giveLock)):
	    attr = mainCtrl + '.' + giveLock[i]
	    mc.setAttr( attr, lock = True, keyable = False)

	for i in range(spineNum): # create & parent [ bJnt ]
		name = 'spine%02d'%(i+1)
		tmpJnt = core.Dag( name + '_tmpJnt')
		bJnt = core.Dag( name + '_bJnt')
		jnt = rigTools.jointAt( tmpJnt )#Create bJnt at tmpJnt
		jnt.rename( bJnt)
		if i > 0:
			upName = 'spine%02d'%(i)
			upJnt = core.Dag(upName + '_bJnt')
			bJnt.parent( upJnt )
		elif i == 0:
			bJnt.parent( hipJnt )
	
	# ---------- FK SPINE ---------- #
	for i in range(spineNum): # Control spine FK
		
		name = 'spine%02d'%(i+1)
		tmpJnt = core.Dag( name + '_tmpJnt')
		fkJnt = core.Dag( name + '_fkJnt')
		jnt = rigTools.jointAt( tmpJnt )#Create fkJ at tJ
		jnt.rename( fkJnt) #Rename Joint
		ctrl = core.Dag( name + '_ctrl' )#Create Ctrl
		ctrl.nmCreateController('neck_ctrlShape')
		ctrl.editCtrlShape( axis = 1.5 )#Edit Shape
		Zro_grp = rigTools.zeroGroup( ctrl )
		Zro_grp.name = name + 'Zro_grp' # Create Zro_Grp
		Gmbl_ctrl = core.createGimbal( ctrl )
		# shape adjustment
		ctrl.color = 'yellow'
		# Parenting and positioning
		Zro_grp.matchAll( tmpJnt )
		if i > 0:
			upName = 'spine%02d'%(i)
			upGmbl = core.Dag(upName + '_gmbCtrl')
			upJnt = core.Dag(upName + '_fkJnt')
			fkJnt.parent( upJnt )
			Zro_grp.parent( upGmbl )
			
		core.parentConstraint(ctrl,fkJnt)
		if i == 0:
			Zro_grp.parent( mainCtrl )
			
			fkHeadGrp = 'spineFK_grp'
			fkJntHeadGrp = 'spineFKJnt_Grp'
			
			mc.group( n = fkHeadGrp, em = 1)
			mc.group( n = fkJntHeadGrp, em = 1)
			
			mc.parent( fkJntHeadGrp, fkHeadGrp)
			mc.parentConstraint( hipJnt, fkHeadGrp, mo = 0, w = 1 )
			mc.parentConstraint( cog_ctrl, Zro_grp, mo = 1, w = 1 ) 
			mc.parent( fkJnt, fkJntHeadGrp)
			mc.parent( Zro_grp, fkHeadGrp)
			mc.parent( fkHeadGrp, mainCtrl)

	# ---------- IK SPINE ----------- #
	# Create Living Group
	ikHeadGrp = 'spineIK_grp'
	ikJntHeadGrp = 'spineIKJnt_Grp'
	ikHeadCtrlGrp = 'spineIKCtrl_Grp'
	
	mc.group( n = ikHeadGrp, em = 1)
	mc.group( n = ikJntHeadGrp, em = 1)
	mc.group( n = ikHeadCtrlGrp, em = 1)
	mc.parent( ikJntHeadGrp, ikHeadCtrlGrp, ikHeadGrp)
	mc.parentConstraint( hipJnt, ikHeadGrp, mo = 0, w = 1 )

	for i in range(spineNum): # create & parent [ ikJnt ]
		name = 'spine%02d'%(i+1)
		tmpJnt = core.Dag( name + '_tmpJnt')
		ikJnt = core.Dag( name + '_ikJnt')
		jnt = rigTools.jointAt( tmpJnt )#Create ikJnt at tmpJnt
		jnt.rename( ikJnt)
		if i > 0:
			upName = 'spine%02d'%(i)
			upJnt = core.Dag(upName + '_ikJnt')
			ikJnt.parent( upJnt )
		elif i == 0:
			ikJnt.parent( ikJntHeadGrp)
			
	# Naming    
	upJnt = 'spine%02d_ikJnt' % (spineNum)
	midJnt = 'spine%02d_ikJnt' % (spineNum/2)
	lowJnt = 'spine01_ikJnt'
	
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
		ctrl.nmCreateController('spine_ctrlShape')#Create Ctrl
		ctrl.editCtrlShape( axis =  1.5 )#Edit Shape
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
	rev = 'spineBlend_rev'
	
	mc.addAttr( 'cog_ctrl' , longName = 'FK_IK', attributeType = 'float', k = True, min = 0, max = 1 )

	
	revOutFK = rev + '.outputX'
	revOutIK = rev + '.inputX'
	mc.createNode( 'reverse', n = rev)
	mc.connectAttr( cogAttr, rev + '.inputX')
	# Blend loop
	for i in range(spineNum): # create & parent [ bJnt ]
		name = 'spine%02d'%(i+1)
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

	mc.connectAttr( revOutIK, 'spineIKCtrl_Grp.v' )
	mc.connectAttr( revOutFK, 'spine01Zro_grp.v' )
	# Goodbye vis
	# DONE IK_FK SPINE RIG ----------<>
	
	return mainCtrl # spineRig_grp

spineRig(spineNum = 4 , hipJnt = 'hip_bJnt', cog_ctrl = 'cog_gmbCtrl') #
#mc.delete('*_tmpJnt')

