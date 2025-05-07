'''
from function.rigging.constraint import locatorFollowToCurve as lfc
reload(lfc)

'''

import maya.cmds as mc

def locator_follow_curve_spec_position(locator_param_list, curve_name):
	#... [WARNING] for curve that havig length 0 - 1 only

	try:
		curve_shape_name = mc.listRelatives( curve_name , s = True )[ 0 ]
	except:
		print('There are no shape name to return.')
		return False

	for locator_name, parameter in locator_param_list:
		# Create pointOnCurveInfo node
		poc = mc.createNode('pointOnCurveInfo', name=f'{locator_name}_poc')
		mc.connectAttr(f'{curve_shape_name}.worldSpace[0]', f'{poc}.inputCurve')
		mc.setAttr(f'{poc}.parameter', parameter)

		# Create vectorProduct nodes
		vp_z = mc.createNode('vectorProduct', name=f'{locator_name}_vpZ')
		vp_y = mc.createNode('vectorProduct', name=f'{locator_name}_vpY')
		mc.setAttr(f'{vp_z}.operation', 2)  # Cross Product
		mc.setAttr(f'{vp_y}.operation', 2)  # Cross Product

		# Create fourByFourMatrix
		fbfm = mc.createNode('fourByFourMatrix', name=f'{locator_name}_fbfm')

		# Connect tangent to vectorProducts
		mc.connectAttr(f'{poc}.tangent', f'{vp_z}.input2')
		mc.connectAttr(f'{poc}.tangent', f'{vp_y}.input1')
		mc.connectAttr(f'{vp_z}.output', f'{vp_y}.input2')

		# Connect tangent to fourByFourMatrix row 0
		mc.connectAttr(f'{poc}.tangentX', f'{fbfm}.in00')
		mc.connectAttr(f'{poc}.tangentY', f'{fbfm}.in01')
		mc.connectAttr(f'{poc}.tangentZ', f'{fbfm}.in02')

		# Connect vectorProduct_Y to fourByFourMatrix row 1
		mc.connectAttr(f'{vp_y}.outputX', f'{fbfm}.in10')
		mc.connectAttr(f'{vp_y}.outputY', f'{fbfm}.in11')
		mc.connectAttr(f'{vp_y}.outputZ', f'{fbfm}.in12')

		# Connect vectorProduct_Z to fourByFourMatrix row 2
		mc.connectAttr(f'{vp_z}.outputX', f'{fbfm}.in20')
		mc.connectAttr(f'{vp_z}.outputY', f'{fbfm}.in21')
		mc.connectAttr(f'{vp_z}.outputZ', f'{fbfm}.in22')

		# Connect position to fourByFourMatrix row 3
		mc.connectAttr(f'{poc}.positionX', f'{fbfm}.in30')
		mc.connectAttr(f'{poc}.positionY', f'{fbfm}.in31')
		mc.connectAttr(f'{poc}.positionZ', f'{fbfm}.in32')

		# Create multMatrix and decomposeMatrix
		mm = mc.createNode('multMatrix', name=f'{locator_name}_mm')
		dcm = mc.createNode('decomposeMatrix', name=f'{locator_name}_dcm')

		mc.connectAttr(f'{fbfm}.output', f'{mm}.matrixIn[0]')
		mc.connectAttr(f'{locator_name}.parentInverseMatrix[0]', f'{mm}.matrixIn[1]')
		mc.connectAttr(f'{mm}.matrixSum', f'{dcm}.inputMatrix')

		mc.connectAttr(f'{dcm}.outputTranslate', f'{locator_name}.translate')
		mc.connectAttr(f'{dcm}.outputRotate', f'{locator_name}.rotate')

		print(f'Locator {locator_name} is now following {curve_shape_name} at parameter {parameter}.')

# Example usage
# lfc.locator_follow_curve( [('locator1', 0.0), ('locator2', 0.25), ('locator3', 0.5), ('locator4', 0.75), ('locator4', 1)], 'curve1')





def locator_follow_curve_list(locator_list, curve_name):
	try:
		curve_shape_name = mc.listRelatives(curve_name, shapes=True)[0]
	except:
		print('Curve has no shape node.')
		return False

	for locator_name in locator_list:
		# Get locator world position
		pos = mc.xform(locator_name, q=True, ws=True, t=True)

		# Find closest parameter on the curve
		npc = mc.createNode('nearestPointOnCurve', name=f'{locator_name}_npc')
		mc.connectAttr(f'{curve_shape_name}.worldSpace[0]', f'{npc}.inputCurve')
		mc.setAttr(f'{npc}.inPosition', pos[0], pos[1], pos[2])
		param = mc.getAttr(f'{npc}.parameter')
		mc.delete(npc)

		# Create pointOnCurveInfo node
		poc = mc.createNode('pointOnCurveInfo', name=f'{locator_name}_poc')
		mc.connectAttr(f'{curve_shape_name}.worldSpace[0]', f'{poc}.inputCurve')
		mc.setAttr(f'{poc}.parameter', param)

		# Create vectorProduct nodes
		vp_z = mc.createNode('vectorProduct', name=f'{locator_name}_vpZ')
		vp_y = mc.createNode('vectorProduct', name=f'{locator_name}_vpY')
		mc.setAttr(f'{vp_z}.operation', 2)
		mc.setAttr(f'{vp_y}.operation', 2)

		# Create fourByFourMatrix
		fbfm = mc.createNode('fourByFourMatrix', name=f'{locator_name}_fbfm')

		# Build matrix from tangent and cross products
		mc.connectAttr(f'{poc}.tangent', f'{vp_z}.input2')
		mc.connectAttr(f'{poc}.tangent', f'{vp_y}.input1')
		mc.connectAttr(f'{vp_z}.output', f'{vp_y}.input2')

		mc.connectAttr(f'{poc}.tangentX', f'{fbfm}.in00')
		mc.connectAttr(f'{poc}.tangentY', f'{fbfm}.in01')
		mc.connectAttr(f'{poc}.tangentZ', f'{fbfm}.in02')

		mc.connectAttr(f'{vp_y}.outputX', f'{fbfm}.in10')
		mc.connectAttr(f'{vp_y}.outputY', f'{fbfm}.in11')
		mc.connectAttr(f'{vp_y}.outputZ', f'{fbfm}.in12')

		mc.connectAttr(f'{vp_z}.outputX', f'{fbfm}.in20')
		mc.connectAttr(f'{vp_z}.outputY', f'{fbfm}.in21')
		mc.connectAttr(f'{vp_z}.outputZ', f'{fbfm}.in22')

		mc.connectAttr(f'{poc}.positionX', f'{fbfm}.in30')
		mc.connectAttr(f'{poc}.positionY', f'{fbfm}.in31')
		mc.connectAttr(f'{poc}.positionZ', f'{fbfm}.in32')

		# Decompose the matrix to drive the locator
		mm = mc.createNode('multMatrix', name=f'{locator_name}_mm')
		dcm = mc.createNode('decomposeMatrix', name=f'{locator_name}_dcm')

		mc.connectAttr(f'{fbfm}.output', f'{mm}.matrixIn[0]')
		mc.connectAttr(f'{locator_name}.parentInverseMatrix[0]', f'{mm}.matrixIn[1]')
		mc.connectAttr(f'{mm}.matrixSum', f'{dcm}.inputMatrix')

		mc.connectAttr(f'{dcm}.outputTranslate', f'{locator_name}.translate')
		mc.connectAttr(f'{dcm}.outputRotate', f'{locator_name}.rotate')

		print(f'{locator_name} is now following {curve_name} at parameter {param:.3f}')

# lfc.locator_follow_curve(['locator1','locator2','locator3','locator4'], 'curve1')

