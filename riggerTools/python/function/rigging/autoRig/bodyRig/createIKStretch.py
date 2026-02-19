# Dode Create IK strerchy 
import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.tools import dTool as dc 
reload(dc)

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

	if alongAxis == 'y':
		strJntPosi = mc.getAttr( midJnt+'.ty')  
		endJntPosi = mc.getAttr( endJnt+'.ty')
	elif alongAxis == 'x':
		strJntPosi = mc.getAttr( midJnt+'.tx')  
		endJntPosi = mc.getAttr( endJnt+'.tx')
	elif alongAxis == 'z':
		strJntPosi = mc.getAttr( midJnt+'.tz')  
		endJntPosi = mc.getAttr( endJnt+'.tz')

	if side == 'LFT':
		disJnt = strJntPosi + endJntPosi
		ampVal = 0.1

	elif side == 'RGT':
		disJnt = (strJntPosi + endJntPosi)*(-1)
		ampVal = (-0.1)

	else:
		disJnt = strJntPosi + endJntPosi
		ampVal = 0.1

	print(f'plus method: {disJnt}')
	print(f'vecter method: {vec_ABC}')


	# Ctrl Name
	strCtrl = ikCtrl[0]
	endCtrl = ikCtrl[1]


	# Start End Loc Name
	strLoc = part + 'StartDist' + side + '_loc'
	endLoc = part + 'EndDist' + side + '_loc'

	# Speicify Node Name System
	disNode 		= part + 'AutoStretch' + side + '_dtw'
	mdvAutoNode 	= part + 'AutoStretch' + side + '_mdv'
	mdvNode 		= part + 'Stretch' + side + '_mdv'
	mdvAmpNode 		= part + 'StretchAmp' + side + '_mdv'
	cndNode 		= part + 'AutoStretch' + side +  '_cnd'
	bcNode 			= part + 'AutoStretch' + side + '_bc'
	pmaNode 		= part + 'Stretch' + side + '_pma'
	minusNode 		= part + 'MinuseStretch' + side + '_mdv'

	# add mdvNode for scale compansate
	scaleNode = part + 'Compensate' + 'Stretch' + side + '_mdv' 


	# Create Locator
	# mc.spaceLocator( n = strLoc )
	# mc.spaceLocator( n = endLoc )


	loc1 = core.Locator( strLoc )
	loc2 = core.Locator( endLoc )


	locator_grp = core.Null(part + 'Loc'+ side + '_grp')
	mc.parent( loc1.name, loc2.name, locator_grp.name)

	# Set the distance
	mc.parent( locator_grp.name ,  noTouchGrp )

	# SnapLocator to start and end point

	mc.parentConstraint( strCtrl, loc1.name, mo = 0, w = 1 , name = part + 'StartDist' + side + '_parCons')
	mc.matchTransform( loc2.name, endJnt , pos = 1 )
	psConEndNam = part + 'EndDist' + side + '_parCons'
	mc.parentConstraint( endCtrl, loc2.name, mo = 1, w = 1 , name = psConEndNam)



	# Measurement distance
	mc.createNode('distanceBetween', n = disNode)
	mc.connectAttr( loc1.name + 'Shape.worldPosition', disNode + '.point1')
	mc.connectAttr( loc2.name + 'Shape.worldPosition', disNode + '.point2')
	mc.setAttr( loc1.name + '.v', 0)
	mc.setAttr( loc2.name + '.v', 0)


	# Create AutoStretch_mdv and Set
	mc.createNode('multiplyDivide', n = mdvAutoNode)
	mc.setAttr( mdvAutoNode + '.operation', 2)
	mc.setAttr( mdvAutoNode + '.input2.input2X', disJnt)
	# Connect
	mc.connectAttr( disNode + '.distance', mdvAutoNode + '.input1.input1X ')


	# Create legAutoStretch_cnd
	mc.createNode('condition', n = cndNode)
	mc.setAttr( cndNode + '.operation', 3)
	mc.setAttr( cndNode + '.secondTerm', disJnt)

	# Connect
	mc.connectAttr( mdvAutoNode + '.output.outputX', cndNode + '.colorIfTrue.colorIfTrueR')
	mc.connectAttr( disNode + '.distance', cndNode + '.firstTerm')

	# Create legStretchLFT_mdv and Set
	mc.createNode('multiplyDivide', n = mdvNode)
	mc.setAttr ( mdvNode + '.operation', 1)
	mc.setAttr( mdvNode + '.input2.input2X', strJntPosi)
	mc.setAttr( mdvNode + '.input2.input2Y', endJntPosi)
	# Connect
	mc.connectAttr( cndNode + '.outColor.outColorR', mdvNode + '.input1.input1X')
	mc.connectAttr( cndNode + '.outColor.outColorR', mdvNode + '.input1.input1Y')

	# Create legStretchLFT_mdv and Set
	mc.createNode('multiplyDivide', n = mdvAmpNode)
	mc.setAttr( mdvAmpNode + '.input2X', ampVal)
	mc.setAttr( mdvAmpNode + '.input2Y', ampVal)

	# Connect
	mc.connectAttr( endCtrl + '.lowStretch', mdvAmpNode + '.input1.input1Y') # NEED TO BE FIX "lowLegStretch"
	mc.connectAttr( endCtrl + '.upStretch', mdvAmpNode + '.input1.input1X') # NEED TO BE FIX "upLegStretch"

	# Create blendColors
	mc.createNode('blendColors', n = bcNode)
	mc.setAttr( bcNode + '.color2R', strJntPosi)
	mc.setAttr( bcNode + '.color2G', endJntPosi)
	# connect
	mc.connectAttr( mdvNode + '.output', bcNode + '.color1')
	mc.connectAttr( endCtrl + '.autoStretch', bcNode + '.blender')

	# Create legStretchLFT_pma
	mc.createNode('plusMinusAverage', n = pmaNode)
	# connect KEY bc
	mc.connectAttr( bcNode + '.outputR', pmaNode + '.input2D[1].input2Dx')
	mc.connectAttr( bcNode + '.outputG', pmaNode + '.input2D[1].input2Dy')
	# connect KEY amp
	mc.connectAttr( mdvAmpNode + '.outputX', pmaNode + '.input2D[2].input2Dx')
	mc.connectAttr( mdvAmpNode + '.outputY', pmaNode + '.input2D[2].input2Dy')

	#... Check condition for Export translante to Joint
	#... find arg to accept axis

	if alongAxis == 'y':
		mc.connectAttr ( pmaNode + '.output2D.output2Dx', midJnt + '.ty')
		mc.connectAttr ( pmaNode + '.output2D.output2Dy', endJnt + '.ty')
	elif alongAxis == 'x':
		mc.connectAttr ( pmaNode + '.output2D.output2Dx', midJnt + '.tx')
		mc.connectAttr ( pmaNode + '.output2D.output2Dy', endJnt + '.tx')
	elif alongAxis == 'z':
		mc.connectAttr ( pmaNode + '.output2D.output2Dx', midJnt + '.tz')
		mc.connectAttr ( pmaNode + '.output2D.output2Dy', endJnt + '.tz')
	# ==================== # End of Dode Create IK strerchy 



	# ==================== # Create AutoStretch_mdv for scale compensete
	# sum a -> b length
	# abLength = strJnt + endJnt
	# change this value to abs for fix the RGT side not stretch properly
	abLength = abs(strJntPosi + endJntPosi)

	if abLength == 0:
		mc.error('Length is zero something wrong please check')

	# get the c lenge
	cLength = mc.getAttr( disNode + '.distance')
	mc.createNode('multiplyDivide', name = scaleNode)
	# set value to 1 prevent to unexpect error
	mc.setAttr( scaleNode + '.input1X', 1)



	# set lengte of c edge
	print(f'abLength is: {abLength}')
	print(f'vec_ABC is: {vec_ABC}')
	
	if povPosi == 'front':
		mc.setAttr( scaleNode + '.input2.input2X', abLength)
	elif povPosi == 'back':
		mc.setAttr( scaleNode + '.input2.input2X', vec_ABC)
	else:
		mc.error('There must be front or back position.')


	# Connect
	mc.connectAttr( scaleNode + '.output.outputX', mdvAutoNode + '.input2.input2X')
	# Connect value to condition
	mc.connectAttr( scaleNode + '.output.outputX' , cndNode + '.secondTerm' )

	scaleCtrlNam = scaleCtrl
	if mc.objExists( scaleCtrlNam ):
		mc.connectAttr( '%s.scale.scaleX' %scaleCtrlNam , '%s.input1.input1X' %scaleNode  )

	# return psConEndNam(parent constraint end name) for fix an ik stretchy
	return pmaNode,psConEndNam
