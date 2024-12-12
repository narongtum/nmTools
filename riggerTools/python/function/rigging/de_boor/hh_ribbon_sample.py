from function.rigging.de_boor import hh_ribbon as ribbon 




cvs = []
for i in range(3):
	loc = cmds.spaceLocator()[0]
	cvs.append(loc)
	cmds.setAttr(f'{loc}.t', i, 0, 0)

	
jnts = ribbon.de_boor_ribbon(cvs)
	
jnts = ribbon.de_boor_ribbon(cvs, name='use_scale_true', use_scale=True)

jnts = ribbon.de_boor_ribbon(cvs, name='aim_y_up_z', aim_axis='y', up_axis='z', use_scale=True)

jnts = ribbon.de_boor_ribbon(cvs, name='aim_y_up_z', aim_axis='y', up_axis='z')

for jnt in jnts:
	cmds.setAttr(f'{jnt}.displayLocalAxis', True)