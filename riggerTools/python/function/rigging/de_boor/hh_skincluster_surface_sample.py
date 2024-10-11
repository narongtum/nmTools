#... using nrb as a proxy to skin mesh with joint

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.de_boor import hh_de_boor_core as core
reload(core)

from function.rigging.de_boor import hh_skincluster_surface as sff
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

cmds.skinCluster(flat_jnts, msh)

sff.split_with_surface(msh, jnts, nrb)




#... manual use
msh = 'R_brow'
jnts = [['eyebrow01RGT_bJnt','eyebrow02RGT_bJnt','eyebrow03RGT_bJnt']]
nrb = 'eyebrowRGT_nrb'






mc.skinCluster('joint1', 'joint3', 'pPlane1',tsb=True)


sff.split_with_surface(msh, jnts, nrb)













# ----- example 2, UV form = periodic, periodic
#... use this for skirt
cmds.file(new=True, f=True)

JNT_POS_LISTS = [[[1.0, -0.5, 0.0], [0.0, -0.5, 1.0], [-1.0, -0.5, 0.0], [0.0, -0.5, -1.0]],
                 [[1.5, 0.0, 0.0], [0.0, 0.0, 1.5], [-1.5, 0.0, 0.0], [0.0, 0.0, -1.5]],
                 [[1.0, 0.5, 0.0], [0.0, 0.5, 1.0], [-1.0, 0.5, 0.0], [0.0, 0.5, -1.0]],
                 [[0.5, 0.0, 0.0], [0.0, 0.0, 0.5], [-0.5, 0.0, 0.0], [0.0, 0.0, -0.5]]]

jnts = []
flat_jnts = []
for i, jnt_pos_list in enumerate(JNT_POS_LISTS):
    v_jnts = []
    for jnt_pos in jnt_pos_list:
        cmds.select(cl=True)
        jnt = cmds.joint(p=jnt_pos)
        v_jnts.append(jnt)
        flat_jnts.append(jnt)
    jnts.append(v_jnts)

msh, msh_con = cmds.polyTorus()

nrb, nrb_con = cmds.torus(ax=(0, 1, 0))
cmds.setAttr(f'{nrb_con}.heightRatio', 0.5)

cmds.skinCluster(flat_jnts, msh)

sff.split_with_surface(msh, jnts, nrb)



msh = 'Skirt02'
aac = mc.ls(sl=True)
nrb = 'loftedSurface1'

  
  
  
jnts_1 = ['objectA01','objectA02','objectA03','objectA04']
jnts_2 = ['objectB01','objectB02','objectB03','objectB04'] 
jnts_3 = ['objectC01','objectC02','objectC03','objectC04'] 
jnts_4 = ['objectD01','objectD02','objectD03','objectD04']  
jnts_5 = ['objectE01','objectE02','objectE03','objectE04'] 
jnts_6 = ['objectF01','objectF02','objectF03','objectF04']   


jnts_1 = ['objectAA01','objectAA02','objectAA03','objectAA04']
jnts_2 = ['objectBB01','objectBB02','objectBB03','objectBB04']
jnts_3 = ['objectCC01','objectCC02','objectCC03','objectCC04']
jnt_grp = [jnts_1, jnts_2,jnts_3 ]  
# jnt_grp = [jnts_1, jnts_2,jnts_3, jnts_4,jnts_5, jnts_6]  
  
  

msh  = 'Skirt02'
nrb =   'loft03'
sff.split_with_surface(msh, jnt_grp, nrb)






















# ----- example 2
flat_jnts = ['joint1','joint2','joint3']
msh = 'polySurface67'
nrb = 'loftedSurface2'
nrb_con = 'loft1'
jnts = [['joint1','joint2','joint3']]



# cmds.skinCluster(flat_jnts, msh)

sff.split_with_surface(msh, jnts, nrb)

