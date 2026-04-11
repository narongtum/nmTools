# Dode Create IK strerchy 
import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.tools import dTool as dc 
reload(dc)

from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

import math
#... find magnitude
def mag( v ):
	return( math.sqrt( pow(v[0], 2) + pow(v[1], 2) + pow(v[2], 2) ) )



# 'front' (Front Leg / Straight Chain)
# 'back' (Back Leg / Zig-Zag Chain)


def iKStretch(		ikJnt = ('startJnt','middleJnt','endJnt' 			) , 
					ikCtrl = ('ikRoot' , 'ankleIk_ctrl') , region = ''	, 
					side = '' , scaleCtrl = 'placement_ctrl'	,
					noTouchGrp = 	'noTouchGrp'		,
					nameSpace ='',lowNam = '', alongAxis = 'y',povPosi = 'front' ):
	#... lowNam is lower name For use run both  arg older and newer 
	part = nameSpace + lowNam
	strJnt = ikJnt[0]
	midJnt = ikJnt[1]
	endJnt = ikJnt[2]

	#... try new method to find length
	vec_A = mc.xform( strJnt, q = True, piv = True, ws = True )
	vec_B = mc.xform( midJnt, q = True, piv = True, ws = True )
	x = vec_B[0] - vec_A[0]
	y = vec_B[1] - vec_A[1]
	z = vec_B[2] - vec_A[2]
	v = [x,y,z]
	vec_AB = mag(v)


	vec_C = mc.xform( endJnt, q = True, piv = True, ws = True )

	x = vec_C[0] - vec_B[0]
	y = vec_C[1] - vec_B[1]
	z = vec_C[2] - vec_B[2]
	v = [x,y,z]
	vec_BC = mag(v)


	vec_ABC = vec_AB + vec_BC

	# =======================================================
	# [FIX] Robust Vector-Based Stretch Calculation
	# =======================================================
	abLength = vec_ABC

	mid_tx = mc.getAttr( midJnt+'.tx')
	mid_ty = mc.getAttr( midJnt+'.ty')
	mid_tz = mc.getAttr( midJnt+'.tz')
	end_tx = mc.getAttr( endJnt+'.tx')
	end_ty = mc.getAttr( endJnt+'.ty')
	end_tz = mc.getAttr( endJnt+'.tz')

	# Keep original assignments for manual amp context
	if alongAxis == 'y':  
		strJntPosi = mid_ty
		endJntPosi = end_ty
	elif alongAxis == 'x':
		strJntPosi = mid_tx
		endJntPosi = end_tx
	elif alongAxis == 'z':
		strJntPosi = mid_tz
		endJntPosi = end_tz

	if side == 'LFT': ampVal = 0.1
	elif side == 'RGT': ampVal = -0.1
	else: ampVal = 0.1

	print(f'Vector method ABS Length: {abLength}')

	# Ctrl Name
	strCtrl = ikCtrl[0]
	endCtrl = ikCtrl[1]

	# Start/End Loc Name
	strLoc = part + 'StartDist' + side + '_loc'
	endLoc = part + 'EndDist' + side + '_loc'

	# Speicify Node Name System
	disNode 		= part + 'AutoStretch' + side + '_dtw'
	mdvAutoNode 	= part + 'AutoStretch' + side + '_mdv'
	cndNode 		= part + 'AutoStretch' + side +  '_cnd'
	bcNode 			= part + 'AutoStretch' + side + '_bc'
	mdvAmpNode 		= part + 'StretchAmp' + side + '_mdv'
	pmaNode 		= part + 'Stretch' + side + '_pma'
	scaleNode 		= part + 'Compensate' + 'Stretch' + side + '_mdv' 
	midStretch_mdv  = part + 'MidStretch' + side + '_mdv'
	endStretch_mdv  = part + 'EndStretch' + side + '_mdv'

	# Create Locator
	loc1 = core.Locator( strLoc )
	loc2 = core.Locator( endLoc )

	locator_grp = core.Null(part + 'Loc'+ side + '_grp')
	mc.parent( loc1.name, loc2.name, locator_grp.name)
	mc.parent( locator_grp.name ,  noTouchGrp )

	# SnapLocator to start and end point using standard parentConstraint (prevents DG evaluation bugs)
	mc.parentConstraint( strCtrl , loc1.name , mo=False, name=part + 'StartDist' + side + '_parCons' )
	mc.matchTransform( loc2.name, endJnt , pos = 1 )
	psConEndNam = part + 'EndDist' + side + '_parCons'
	mc.parentConstraint( endCtrl , loc2.name , mo=True, name=psConEndNam )

	# Measurement distance
	mc.createNode('distanceBetween', n = disNode)
	mc.connectAttr( loc1.name + 'Shape.worldPosition', disNode + '.point1')
	mc.connectAttr( loc2.name + 'Shape.worldPosition', disNode + '.point2')
	mc.setAttr( loc1.name + '.v', 0)
	mc.setAttr( loc2.name + '.v', 0)

	# Scale Compensate Node
	mc.createNode('multiplyDivide', name = scaleNode)
	mc.setAttr( scaleNode + '.input1X', 1)
	mc.setAttr( scaleNode + '.input2X', abLength)  # Base length is ALWAYS absolute vector length!
	
	scaleCtrlNam = scaleCtrl
	if mc.objExists( scaleCtrlNam ):
		mc.connectAttr( '%s.scale.scaleX' %scaleCtrlNam , '%s.input1.input1X' %scaleNode  )

	# AutoStretch Ratio Calculation
	mc.createNode('multiplyDivide', n = mdvAutoNode)
	mc.setAttr( mdvAutoNode + '.operation', 2) # Divide: distance / (abLength * targetScale)
	mc.connectAttr( disNode + '.distance', mdvAutoNode + '.input1X')
	mc.connectAttr( scaleNode + '.outputX', mdvAutoNode + '.input2X')

	# Condition Node - Activates when stretched past limit
	mc.createNode('condition', n = cndNode)
	mc.setAttr( cndNode + '.operation', 3) # Greater Than
	mc.setAttr( cndNode + '.colorIfFalseR', 1.0) # Rest state stretch multiplier is exactly 1.0
	mc.connectAttr( disNode + '.distance', cndNode + '.firstTerm')
	mc.connectAttr( scaleNode + '.outputX' , cndNode + '.secondTerm' )
	mc.connectAttr( mdvAutoNode + '.outputX', cndNode + '.colorIfTrueR') # Apply stretch multiplier if needed

	# Blend Colors for AutoStretch variable blending
	mc.createNode('blendColors', n = bcNode)
	mc.setAttr( bcNode + '.color2R', 1.0) # autoStretch=0 means multiplier is securely 1.0
	mc.connectAttr( cndNode + '.outColorR', bcNode + '.color1R')
	mc.connectAttr( endCtrl + '.autoStretch', bcNode + '.blender')

	# Safely project Multiplier ratio exactly onto un-oriented 3D XYZ values
	mc.createNode('multiplyDivide', n = midStretch_mdv)
	mc.setAttr( midStretch_mdv + '.input1X', mid_tx)
	mc.setAttr( midStretch_mdv + '.input1Y', mid_ty)
	mc.setAttr( midStretch_mdv + '.input1Z', mid_tz)
	mc.connectAttr( bcNode + '.outputR', midStretch_mdv + '.input2X')
	mc.connectAttr( bcNode + '.outputR', midStretch_mdv + '.input2Y')
	mc.connectAttr( bcNode + '.outputR', midStretch_mdv + '.input2Z')

	mc.createNode('multiplyDivide', n = endStretch_mdv)
	mc.setAttr( endStretch_mdv + '.input1X', end_tx)
	mc.setAttr( endStretch_mdv + '.input1Y', end_ty)
	mc.setAttr( endStretch_mdv + '.input1Z', end_tz)
	mc.connectAttr( bcNode + '.outputR', endStretch_mdv + '.input2X')
	mc.connectAttr( bcNode + '.outputR', endStretch_mdv + '.input2Y')
	mc.connectAttr( bcNode + '.outputR', endStretch_mdv + '.input2Z')

	# Manual Additive Amp Stretch Support
	mc.createNode('multiplyDivide', n = mdvAmpNode)
	mc.setAttr( mdvAmpNode + '.input2X', ampVal)
	mc.setAttr( mdvAmpNode + '.input2Y', ampVal)
	try: mc.connectAttr( endCtrl + '.upStretch', mdvAmpNode + '.input1X')
	except: pass
	try: mc.connectAttr( endCtrl + '.lowStretch', mdvAmpNode + '.input1Y') # Fallback
	except: pass

	# Assemble Target Outputs allowing midLockModule injection gracefully
	mc.createNode('plusMinusAverage', n = pmaNode)
	
	if alongAxis == 'x':
		mc.connectAttr( midStretch_mdv + '.outputX', pmaNode + '.input2D[1].input2Dx' )
		mc.connectAttr( endStretch_mdv + '.outputX', pmaNode + '.input2D[1].input2Dy' )
		mc.connectAttr( midStretch_mdv + '.outputY', midJnt + '.ty' )
		mc.connectAttr( midStretch_mdv + '.outputZ', midJnt + '.tz' )
		mc.connectAttr( endStretch_mdv + '.outputY', endJnt + '.ty' )
		mc.connectAttr( endStretch_mdv + '.outputZ', endJnt + '.tz' )
		mc.connectAttr( pmaNode + '.output2D.output2Dx', midJnt + '.tx')
		mc.connectAttr( pmaNode + '.output2D.output2Dy', endJnt + '.tx')
	elif alongAxis == 'y':
		mc.connectAttr( midStretch_mdv + '.outputY', pmaNode + '.input2D[1].input2Dx' )
		mc.connectAttr( endStretch_mdv + '.outputY', pmaNode + '.input2D[1].input2Dy' )
		mc.connectAttr( midStretch_mdv + '.outputX', midJnt + '.tx' )
		mc.connectAttr( midStretch_mdv + '.outputZ', midJnt + '.tz' )
		mc.connectAttr( endStretch_mdv + '.outputX', endJnt + '.tx' )
		mc.connectAttr( endStretch_mdv + '.outputZ', endJnt + '.tz' )
		mc.connectAttr( pmaNode + '.output2D.output2Dx', midJnt + '.ty')
		mc.connectAttr( pmaNode + '.output2D.output2Dy', endJnt + '.ty')
	elif alongAxis == 'z':
		mc.connectAttr( midStretch_mdv + '.outputZ', pmaNode + '.input2D[1].input2Dx' )
		mc.connectAttr( endStretch_mdv + '.outputZ', pmaNode + '.input2D[1].input2Dy' )
		mc.connectAttr( midStretch_mdv + '.outputX', midJnt + '.tx' )
		mc.connectAttr( midStretch_mdv + '.outputY', midJnt + '.ty' )
		mc.connectAttr( endStretch_mdv + '.outputX', endJnt + '.tx' )
		mc.connectAttr( endStretch_mdv + '.outputY', endJnt + '.ty' )
		mc.connectAttr( pmaNode + '.output2D.output2Dx', midJnt + '.tz')
		mc.connectAttr( pmaNode + '.output2D.output2Dy', endJnt + '.tz')
		
	# Apply final secondary AMP scale delta
	mc.connectAttr( mdvAmpNode + '.outputX', pmaNode + '.input2D[2].input2Dx')
	mc.connectAttr( mdvAmpNode + '.outputY', pmaNode + '.input2D[2].input2Dy')

	return pmaNode, psConEndNam