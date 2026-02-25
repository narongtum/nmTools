
# # # # # # # # # # # #  # # # # # # # # # # # #  # # # # # # # # # # # #   Make share position

'''
#... This code is help create wtAddMatrix for weight space between 2 point

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)



selected = mc.ls(sl=True)[0]
base_name = core.findBaseName(selected)
share_wtAddMatrix = core.WtAddMatrixWithChannal('{0}_share'.format(base_name),2)

share_multAddMatrix = core.MultMatrixWithValue('{0}_share'.format(base_name))



'''
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)


side = 'C'
# # # # # # # # # # # #  # # # # # # # # # # # #  # # # # # # # # # # # #   snap slave ctrl to locator
pattern = f'{side}_mainCV##_ctrl'
main_ctrl_list = core.generate_named_pattern(pattern, 4)


for each in main_ctrl_list:
	for attr in ["rx","ry","rz"]:
	    mc.setAttr(f"{each}.{attr}", 0)
	for attrScal in ["sx","sy","sz"]:
		mc.setAttr(f"{each}.{attrScal}", 1)







base_name = 'childCV'
# # # # # # # # # # # #  # # # # # # # # # # # #  # # # # # # # # # # # #   snap slave ctrl to locator

pattern = f'{side}_{base_name}##_ctrl'
slave_ctrl_list = core.generate_named_pattern(pattern, pCount)

pattern = f'{side}_{base_name}##'
loc_ctrl_list = core.generate_named_pattern(pattern, pCount)


for index, slave in enumerate(slave_ctrl_list):
	slave_obj = core.Dag(slave)
	loc_obj = core.Dag(loc_ctrl_list[index])
	slave_obj.maSnap(loc_obj)







# # # # # # # # # # # #  # # # # # # # # # # # #  # # # # # # # # # # # #   zero out slave ctrl

number = pCount + 1






#... manual
'''
num = '02'
'''

for numRound in range(1,number):
	num = "{:02d}".format(numRound)
	print(num)


	# num = '08'
	
	source = "{1}_{2}{0}_ctrl".format(num, side, base_name)
	source_obj = core.Dag(source)
	rot_num = source_obj.rotateOrder

	destination_loc = mc.spaceLocator( name = '{1}_buffer{0}_loc'.format(num,side))[0]
	destination_loc_obj = core.Dag(destination_loc)
	destination_loc_obj.rotateOrder  = rot_num


	tx = mc.getAttr("{0}.translateX".format(source))
	ty = mc.getAttr("{0}.translateY".format(source))
	tz = mc.getAttr("{0}.translateZ".format(source))
	rx = mc.getAttr("{0}.rotateX".format(source))
	ry = mc.getAttr("{0}.rotateY".format(source))
	rz = mc.getAttr("{0}.rotateZ".format(source))


	mc.setAttr("{0}.translateX".format(destination_loc), tx)
	mc.setAttr("{0}.translateY".format(destination_loc), ty)
	mc.setAttr("{0}.translateZ".format(destination_loc), tz)

	mc.setAttr("{0}.rotateX".format(destination_loc), rx)
	mc.setAttr("{0}.rotateY".format(destination_loc), ry)
	mc.setAttr("{0}.rotateZ".format(destination_loc), rz)


	offset_node = '{1}_offSetMatrix{0}_multMat'.format(num,side)
	mc.createNode('multMatrix', name = offset_node)
	mc.addAttr( offset_node, ln='offsetMatrixVal', at = 'matrix')

	# connectAttr -f buffer05.worldMatrix[0] offSetMatrix05_multMat.offsetMatrixVal;
	# connectAttr -f offSetMatrix05_multMat.offsetMatrixVal offSetMatrix05_multMat.matrixIn[0];


	mc.connectAttr('{0}.worldMatrix[0]'.format(destination_loc), '{0}.offsetMatrixVal'.format(offset_node))
	mc.connectAttr('{0}.offsetMatrixVal'.format(offset_node), '{0}.matrixIn[0]'.format(offset_node))


	noScale_node = '{1}_noScale{0}_pickMat'.format(num, side)


	# connectAttr -f noScale05.outputMatrix offSetMatrix05_multMat.matrixIn[1];
	# connectAttr -f offSetMatrix05_multMat.matrixSum L_ChildCv05_ctrl.offsetParentMatrix;


	mc.connectAttr('{0}.outputMatrix'.format(noScale_node), '{0}.matrixIn[1]'.format(offset_node))


	#... Disconnect attributes first
	mc.disconnectAttr('{0}.outputMatrix'.format(noScale_node), '{0}.offsetParentMatrix'.format(source))

	mc.connectAttr('{0}.matrixSum'.format(offset_node), '{0}.offsetParentMatrix'.format(source))
	
	
	
	
	
	
	
	
	
	
#... applied zero TRS at child CV by manual