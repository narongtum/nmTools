from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.de_boor import de_boor_core as core
reload(core)


from function.rigging.de_boor import de_boor_skincluster_surface as sff
reload(sff)

#... define
#... U == y
#... V == x


# ----- example 1, surface form = open, open
cmds.file(new=True, f=True)

jnts = []
flat_jnts = []
for i in range(3):
	v_jnts = []
	for j in range(3):
		cmds.select(cl=True)
		# we choose the x and z position values to align with the U and V directions of the nurbs plane
		jnt = cmds.joint(p=(i - 1, 0, 1 - j))
		v_jnts.append(jnt)
		flat_jnts.append(jnt)
	jnts.append(v_jnts)

msh, msh_con = cmds.polyPlane()
cmds.setAttr(f'{msh_con}.width', 2)
cmds.setAttr(f'{msh_con}.height', 2)
cmds.setAttr(f'{msh_con}.subdivisionsWidth', 30)
cmds.setAttr(f'{msh_con}.subdivisionsHeight', 40)

nrb, nrb_con = cmds.nurbsPlane(ax=(0, 1, 0))
cmds.setAttr(f'{nrb_con}.width', 2)



flat_jnts = ['joint1','joint2','joint3']
msh = 'polySurface67'
nrb = 'loftedSurface2'
nrb_con = 'loft1'
jnts = [['joint1','joint2','joint3']]



cmds.skinCluster(flat_jnts, msh)

sff.split_with_surface(msh, jnts, nrb)

