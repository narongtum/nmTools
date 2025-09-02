from function.framework.reloadWrapper import reloadWrapper as reload


from function.rigging.tools import dTool as dc 
reload(dc)

import maya.cmds as mc

def baseFingerSpread( nameSpace = '',  tmpJnt = 'baseSpreadLFT_tmpJnt' , stick = 'LWRstickNamLFT' , fingerGrpNam = 'LWRfingerLFT', jointNum = 3, fingerGrp = ['index', 'middle', 'ring', 'pinky']): # only for 5 finger spread
	
	realTempJnt = nameSpace + tmpJnt
	bsName = realTempJnt.split('_')[0]
	#nameSpace = bsName.split('baseSpread')[0] find in namo
	side = bsName[-3:]


	#... edit incase finger joint number is 4
	# if jointNum == 3:
	# 	fingers = ['index01', 'middle01', 'ring01', 'pinky01']
	# elif jointNum == 4:
	# 	fingers = ('indexBase', 'middleBase', 'ringBase', 'pinkyBase')



	if jointNum == 3:
	    suffix = '01'
	    fingers = [f + suffix for f in fingerGrp]

	elif jointNum == 4:
	    suffix = 'Base'
	    fingers = [f + suffix for f in fingerGrp]


	# Setup
	bsZroGrp = mc.group( n = bsName + 'Zro_grp', em = True )
	dc.allMat( bsZroGrp , realTempJnt )
	mc.parent( bsZroGrp, fingerGrpNam )
	mc.addAttr( stick, ln = 'baseSpread', sn = 'bs', at = 'float', k = True )
	mdv = mc.createNode( 'multiplyDivide', n = bsName + '_mdv' )
	rev = mc.createNode( 'reverse', n =bsName + '_rev' )

	# Connect
	mc.connectAttr( stick + '.baseSpread', rev + '.ix' )
	mc.connectAttr( rev + '.ox', mdv + '.i1x' )
	mc.connectAttr( rev + '.ox', mdv + '.i1y' )
	mc.connectAttr( rev + '.ox', mdv + '.i1z' )
	
	mc.setAttr( mdv + '.i2x', 0.5 )
	mc.setAttr( mdv + '.i2y', -0.5 )
	mc.setAttr( mdv + '.i2z', -2 )
	

	for finger in fingers:
		conGrp = mc.group( name = nameSpace + finger + side + 'Con_grp', em = True )

		dc.allMat( conGrp, bsZroGrp )
		mc.parent( conGrp, bsZroGrp )
		mc.parent( nameSpace + finger + side + 'Zro_grp' )

		if finger == 'index':
			mc.connectAttr( mdv + '.ox' , conGrp + '.rz' )
		elif finger == 'ring':
			mc.connectAttr( mdv + '.oy' , conGrp + '.rz' )
		elif finger == 'pinky':
			mc.connectAttr( mdv + '.oz' , conGrp + '.rz' )

	mc.delete( realTempJnt )
	mc.select( cl=True )
	
	
#baseFingerSpread( nameSpace = '',  tmpJnt = 'baseSpreadLFT_tmpJnt' , stick = 'armStickLFT_ctrl' )
#baseFingerSpread( nameSpace = '', tmpJnt = 'baseSpreadRGT_tmpJnt' , stick = 'armStickRGT_ctrl' )
	
	