from maya import cmds

from function.rigging.de_boor import hh_de_boor_core as core
reload(core)

# example 1
cmds.file(new=True, f=True)

group_0 = cmds.group(em=True, n='GRP_0')
group_1 = cmds.group(em=True, n='GRP_1')
group_2 = cmds.group(em=True, n='GRP_2')
group_3 = cmds.group(em=True, n='GRP_3')

n = 8
d = 2
kv = [-0.333, -0.167, 0.0, 0.167, 0.333, 0.5, 0.667, 0.833, 1.0, 1.167, 1.333]
parents = [group_2, group_3, group_0, group_1, group_2, group_3, group_0, group_1]
samples = 100

for sample in range(samples):
	t = float(sample) / (samples - 1)
	wts = core.de_boor(n, d, t, kv)

	grp_wts = {group_0: 0, group_1: 0, group_2: 0, group_3: 0}
	for i, wt in enumerate(wts):
		grp_wts[parents[i]] += wt

	for i, grp in enumerate([group_0, group_1, group_2, group_3]):
		loc = cmds.spaceLocator()[0]
		cmds.parent(loc, grp)

		cmds.setAttr('{}.t'.format(loc), *(t, grp_wts[grp], 0))
		loc_shp = cmds.listRelatives(loc, s=True)[0]
		cmds.setAttr('{}.localScale'.format(loc_shp), *(0.01, 0.01, 0.01))
		
		
		
		
		
		
		
		
		

# example 2
cmds.file(new=True, f=True)

group_0 = cmds.group(em=True, n='GRP_0')
group_1 = cmds.group(em=True, n='GRP_1')
group_2 = cmds.group(em=True, n='GRP_2')
group_3 = cmds.group(em=True, n='GRP_3')

n = 4
d = 3
kv = core.get_open_uniform_kv(n, d)
samples = 100

for sample in range(samples):
	t = float(sample) / (samples - 1)
	wts = core.de_boor(n, d, t, kv)
	for i, wt in enumerate(wts):
		loc = cmds.spaceLocator()[0]
		cmds.parent(loc, 'GRP_{}'.format(i % 4))
		cmds.setAttr('{}.t'.format(loc), *(t, wt, 0))
		loc_shp = cmds.listRelatives(loc, s=True)[0]
		cmds.setAttr('{}.localScale'.format(loc_shp), *(0.01, 0.01, 0.01))
