import maya.cmds as mc

def setup_locator_follow_curve(locator_name, curve_shape_name, parameter=0.0):
	# Create pointOnCurveInfo node
	poc = mc.createNode('pointOnCurveInfo', name=f'{locator_name}_poc')
	mc.connectAttr(f'{curve_shape_name}.worldSpace[0]', f'{poc}.inputCurve')

	# Set parameter position on curve
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

	# Connect matrix network
	mc.connectAttr(f'{fbfm}.output', f'{mm}.matrixIn[0]')
	mc.connectAttr(f'{locator_name}.parentInverseMatrix[0]', f'{mm}.matrixIn[1]')
	mc.connectAttr(f'{mm}.matrixSum', f'{dcm}.inputMatrix')

	# Connect output to locator
	mc.connectAttr(f'{dcm}.outputTranslate', f'{locator_name}.translate')
	mc.connectAttr(f'{dcm}.outputRotate', f'{locator_name}.rotate')

	print(f'Locator {locator_name} is now following {curve_shape_name} with rotation at parameter {parameter}!')

# Example usage
#setup_locator_follow_curve('locator1', 'curveShape1', parameter=0.5)
