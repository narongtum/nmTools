from maya import cmds
from function.rigging.de_boor import hh_skincluster_curve as skincluster_curve
from function.framework.reloadWrapper import reloadWrapper as reload
reload(skincluster_curve)


# ----- example 1, curve form = periodic
cmds.file(new=True, f=True)

msh = cmds.polyTorus()[0]
crv = cmds.circle(normal=(0, 1, 0))[0]
jnts = []
for p in (0, 0, -1), (-1, 0, 0), (0, 0, 1), (1, 0, 0):
	cmds.select(cl=True)
	jnt = cmds.joint(p=p)
	jnts.append(jnt)

cmds.skinCluster(jnts, msh)

skincluster_curve.split_with_curve(msh, jnts, crv)

# ----- example 2, curve form = open
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

skincluster_curve.split_with_curve(msh, jnts, crv)