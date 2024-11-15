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









#.... My tutoria
# "D:\sysTools\nmTools_github\riggerTools\python\function\rigging\de_boor\hh_skincluster_surface_sample.ma"
#... don't forget to add skincluster first
jnts_1 = ['jntA01','jntA02','jntA03','jntA04']
jnts_2 = ['jntB01','jntB02','jntB03','jntB04'] 
jnts_3 = ['jntC01','jntC02','jntC03','jntC04'] 
jnts_4 = ['jntD01','jntD02','jntD03','jntD04']  

jnt_grp = [jnts_1, jnts_2, jnts_3, jnts_4 ]  
# jnt_grp = [jnts_1, jnts_2,jnts_3, jnts_4,jnts_5, jnts_6]  
  
  

mesh  = 'pCylinder1'
nurb =   'lofted01'
sff.split_with_surface(mesh, jnt_grp, nurb)






# ----- example 3 Hi Res version
#... haveing and controller for reposition nurbe

# jnts_1 = ['jntA04','jntA03','jntA02','jntA01']
# jnts_2 = ['jntB04','jntB03','jntB02','jntB01'] 
# jnts_3 = ['jntC04','jntC03','jntC02','jntC01'] 
# jnts_4 = ['jntD04','jntD03','jntD02','jntD01'] 
# jnts_5 = ['jntE04','jntE03','jntE02','jntE01'] 
# jnts_6 = ['jntF04','jntF03','jntF02','jntF01'] 
# jnts_7 = ['jntG04','jntG03','jntG02','jntG01'] 
# jnts_8 = ['jntH04','jntH03','jntH02','jntH01'] 

#... min to max this is right direction
jnts_1 = ['jntA01','jntA02','jntA03','jntA04']
jnts_2 = ['jntB01','jntB02','jntB03','jntB04'] 
jnts_3 = ['jntC01','jntC02','jntC03','jntC04'] 
jnts_4 = ['jntD01','jntD02','jntD03','jntD04'] 
jnts_5 = ['jntE01','jntE02','jntE03','jntE04'] 
jnts_6 = ['jntF01','jntF02','jntF03','jntF04'] 
jnts_7 = ['jntG01','jntG02','jntG03','jntG04'] 
jnts_8 = ['jntH01','jntH02','jntH03','jntH04'] 

# jnt_grp = [jnts_1, jnts_2, jnts_3, jnts_4 ]  
jnt_grp = [jnts_1, jnts_2,jnts_3, jnts_4, jnts_5, jnts_6, jnts_7, jnts_8]  

mesh  = 'skirt_polygon'
nurb =   'skirt_nurb'
sff.split_with_surface(mesh, jnt_grp, nurb)





