from function.rigging.de_boor import hh_skincluster_curve as hhskcc
reload(hhskcc)


cmds.file(new=True, f=True)

msh, msh_con = cmds.polyCube()
for attr, val in zip(('hbl', 'h', 'sh'), (-1, 3, 30)):
	cmds.setAttr(f'{msh_con}.{attr}', val)
crv = cmds.curve(p=[(0, 0, 0), (0, 3, 0)], d=1, k=(0, 1))
jnts = []
for p in (0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 3, 0):
	cmds.select(cl=True)
	jnt = cmds.joint(p=p)
	jnts.append(jnt)

cmds.skinCluster(jnts, msh)

hhskcc.split_with_curve(msh, jnts, crv)