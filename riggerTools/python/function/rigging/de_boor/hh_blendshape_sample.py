from maya.cmds as mc

from function.rigging.de_boor import hh_blendshape as blendshape
reload(blendshape)




# ----- example 3, from hh_blendshape_sample.ma

base_msh = 'base'
msh = 'lipDN'
crv = 'curve1'


sample_crv = mc.curve(p=((-0.5, 0, 0), (0.5, 0, 0)), k=(0, 1), d=1) 


blendshape.split_with_curve(msh, base_msh, crv, ['left_blendShape', 'centre_blendShape', 'right_blendShape'])






# ----- example 1, curve form = open
mc.file(new=True, f=True)

base_msh, base_msh_con = mc.polyCube()
mc.setAttr(f'{base_msh_con}.subdivisionsWidth', 50)

msh = mc.duplicate(base_msh)[0]
mc.setAttr(f'{msh}.sy', 2)
mc.makeIdentity(msh, a=True)

crv = mc.curve(p=((-0.5, 0, 0), (0.5, 0, 0)), k=(0, 1), d=1)

blendshape.split_with_curve(
	msh, base_msh, crv, ['left_blendShape', 'centre_blendShape', 'right_blendShape'])

# ----- example 2, closed curve with linear degree
mc.file(new=True, f=True)

base_msh, base_msh_con = mc.polyTorus()

msh = mc.duplicate(base_msh)[0]
mc.setAttr(f'{msh}.sy', 2)
mc.makeIdentity(msh, a=True)

crv = mc.circle(normal=(0, 1, 0))[0]

blendshape.split_with_curve(
	msh, base_msh, crv, [f'blendShape_{i}' for i in range(4)])