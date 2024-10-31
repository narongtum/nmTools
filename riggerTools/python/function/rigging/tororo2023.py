# LATEST


'''

				____
			  /     \
			  vvvvvvv  /|__/|
				 I   /O,O   |
				 I /_____   |      /|/|
				J|/^ ^ ^ /  |    /00  |    _//|		 _//|	
				 |^ ^ ^ ^ |W|   |/^^/ |   /oo |		/oo |
				  /m___m__|_|    /m_m_|   /mm_|		/mm_|	

										"Totoros" (from "My Neighbor Totoro")
											--- Duke Lee


'''



#.... Fastcopy exclude sample

# *.meta;*.pyc;\.svn\;*.mayaSwatches*\;SteamLibrary\
# https://groups.google.com/g/fastcopy-bb-eng/c/EFiHnr7tSWY

'''
FastCopy Filter Syntax Explained
FastCopy uses a filter syntax similar to UNIX wildcards for both include and exclude filters. Here's a breakdown of the syntax and some examples:

Characters:

* - Matches any number of characters (including zero). Useful for selecting multiple files with similar names.
? - Matches any single character. Great for selecting files with a specific character at a particular position.
[] - Character class. Allows you to specify a range of characters to match.
^ (or !) - Negation. Excludes files that match the following pattern within the brackets.
\ - Escape character. Used to include special characters like *, ?, [], and \ literally in your filter.
Directory Matching:

To exclude/include directories, add a backslash (\) at the end of the directory name.
Example: C:\Documents\*\ - This would include/exclude all files within the "Documents" folder but not subfolders.
Multiple Filters:

Separate multiple filter entries with a semicolon (;).
Example: *.txt;*.docx - This would include/exclude all .txt and .docx files.
Examples:

Exclude all .jpg files: *.jpg\
Include all files starting with "report_": report_*
Exclude files with a number in the filename (except ".txt" files): [!0-9]*\ ; !*.txt (notice the negation with ^ or !)
Include all files in subfolders named "data": *\data\*
Exclude folders named "temp" and "logs" anywhere in the source: temp\*;logs\*
Additional Notes:

Filters are case-sensitive by default.
You can use regular expressions for more complex filtering, but this requires enabling the option in FastCopy settings.
Remember, the exclude filter prevents copying of matching files/folders, it won't delete them.
For further details and reference, you can consult the official FastCopy Help documentation: https://fastcopy.jp/ (English)


'''





#... Create Controller at selected object.
from function.rigging.controllerBox import adjustController as adjust
reload(adjust)
selected = mc.ls(sl = True)

adjust.creControllerFunc( 		selected = selected, scale = 1, ctrlShape = 'circle_ctrlShape', color = 'yellow', 
							constraint = True, matrixConst = True, mo = False, translate=True, 
							rotate = True, scaleConstraint = True, rotateOrder = 'xzy', parentUnder = False)


from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

selected = mc.ls(sl=True)
mtc.del_selected_matrix(selected = selected)






from function.rigging.autoRig.addRig import createFkRig
reload(createFkRig)


createFkRig.fkRig_new_curl_ext(	nameSpace = '', name = 'beard', parentCtrlTo = 'head_ctrl',
					jntLst = ('beard01LFT_bJnt','beard02LFT_bJnt', 'beard03LFT_bJnt','beard04LFT_bJnt'),
					charScale = 1, priorJnt = 'head01_bJnt',side = 'LFT',
					ctrlShape = 'circle_ctrlShape', localWorld = False ,
					color = 'red', curlCtrl = True,rotateOrder = 'zxy',
					curlCtrlShape = 'stick_ctrlShape')



#... create  controller
from function.rigging.autoRig.base import core
reload(core)


cog_ctrl = core.Dag('skirt01BCK_ctrl')
cog_ctrl.nmCreateController('boomerang_ctrlShape')



#... pin to locator
from function.rigging.constraint import pinLocatorToSurface as pls
reload(pls)

pls.pin_locator_surface(	# need pxy nrb to drive locator
						nurbs = 'eyebrowLFT_nrb',
						region = 'eyebrowLFT',
						side = '',
						source_loc = ('eyebrow01LFT_loc','eyebrow02LFT_loc','eyebrow03LFT_loc'),
						locator_scale = 1,
						creJnt = False , suffixJnt = 'bJnt',
						creCtrl = False , ctrlShape = 'circle_ctrlShape',
						snapAtEnd = False,
						priorJnt = '',
						scale = 2
						)



pls.pin_locator_surface(	# need pxy nrb to drive locator
						nurbs = 'eyebrowRGT_nrb',
						region = 'eyebrowRGT',
						side = '',
						source_loc = ('eyebrow01RGT_loc','eyebrow02RGT_loc','eyebrow03RGT_loc'),
						locator_scale = 1,
						creJnt = False , suffixJnt = 'bJnt',
						creCtrl = False , ctrlShape = 'circle_ctrlShape',
						snapAtEnd = False,
						priorJnt = '',
						scale = 2
						)



#... using de boor 
from function.rigging.de_boor import hh_skincluster_surface as sff
reload(sff)
#... manual use
msh = 'extract_brow'
jnts = [['eyebrow01LFT_bJnt','eyebrow02LFT_bJnt','eyebrow03LFT_bJnt']]
nrb = 'eyebrowLFT_nrb'
sff.split_with_surface(msh, jnts, nrb)










from function.rigging.skeleton import jointTools as jtt
reload(jtt)

jtt.rename_tip_jnt(root_joint = 'joint3', search = '_bJnt', replace = '_endJnt')
jtt.change_endJnt_gray()











# cmds.skinPercent(skin_cluster, pruneWeights=tol)




# # # # # # # # # # # # # # # # # # # # 
#... reconnect to blend matrix
# # # # # # # # # # # # # # # # # # # # 
side = 'LFT'
template_ctrl = f'handProp{side}_gmbCtrl_tmp'
new_ctrl = f'handProp{side}_gmbCtrl'


mc.connectAttr(f'{new_ctrl}.worldMatrix[0]', f'R_weapon_blendMatrix.target[1].targetMatrix',f=True)
mc.connectAttr(f'{new_ctrl}.worldMatrix[0]', f'L_weapon_space_blendMatrix.target[0].targetMatrix', f=True)


# # # # # # # # # # # # # # # # # # # # 
#... export both char and char with weapon
# # # # # # # # # # # # # # # # # # # # 

from function.asset import exportFBX
reload(exportFBX)

#... unparent 'Export' and 'model_grp' to world




if mc.objExists('rig_grp.asset_name'):
	print('yeah')
	asset_name = mc.getAttr('rig_grp.asset_name')
else:
	asset_name = mc.ls(sl=True)[0]

exportFBX.exportFBXnoConnection(selection, fileName = asset_name)












# # # # # # # # # # # # # # # # # # # # 
#... close all flothing windows
# # # # # # # # # # # # # # # # # # # # 
import maya.cmds as cmds

# List all top-level UI elements
windows = cmds.lsUI(windows=True)
print(windows)


import maya.cmds as cmds

def close_floating_panel(panel_name):
	# Check if the panel exists
	if cmds.window(panel_name, exists=True):
		# Delete the UI element
		cmds.deleteUI(panel_name)

# Usage
close_floating_panel('myFloatingPanel')



# # # # # # # # # # # # # # # # # # # # 
#... ask what is state of this file 
# # # # # # # # # # # # # # # # # # # # 

from function.pipeline import fileTools as fileTools 
reload(fileTools)
from pathlib import Path
import os


if fileTools.fileState() == 'version' or fileTools.fileState() == 'local_hero':
	print('This is Version Naja.')

	pathFile = mc.file(q=True, sn=True)
	path_lib = Path(pathFile)
	wanted = path_lib.parent.parent  # Go up two levels to get the desired directory
	final_wanted_path = wanted / 'Data'

	if final_wanted_path.exists() and final_wanted_path.is_dir():
		os.startfile(final_wanted_path)

elif fileTools.fileState() == 'global_hero':
	print('This is Global hero.')
	pathFile = mc.file(q=True, sn=True)
	path_lib = Path(pathFile)
	wanted = path_lib.parent.parent  # Go up two levels to get the desired directory
	final_wanted_path = wanted / 'Rig' / 'Data'
	if final_wanted_path.exists() and final_wanted_path.is_dir():
		os.startfile(final_wanted_path)
else:
	print('There are no correct file to open.')











# # # # # # # # # # # # # # # # # # # # 
#... add snap controller 
# # # # # # # # # # # # # # # # # # # # 

#... check f'ballRolllegIk{side}Zro_grp'

side = 'LFT'
ankleIk_ctrl = core.Dag(f'foot{side}IK_ctrl')
ankleIk_ctrl.addAttribute( longName = 'pivotBar', niceName = '_' , at ='enum' , en = 'Pivot'  , keyable = True)
ankleIk_ctrl.setLocked('pivotBar')
ankleIk_ctrl.addAttribute( longName = 'pivotChoice', niceName = 'Pivot At' , at ='enum' , en = 'foot:ankle'  , keyable = True)

ankleIk_loc = core.Locator(f'ankle{side}_loc')
ankleIk_loc.maSnap(ankle_ikJnt,pos = True,rot = False,scl = False)
ankleIk_loc.parent(ankleIk_ctrl)

ankleIk_loc.attr('v').value = 0
ankleIk_loc.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz')



pivot_cnd = core.Condition(f'footIKPivot{side}_cnd')




ankleIk_loc.attr('translate') >> pivot_cnd.attr('colorIfFalse')
ankleIk_ctrl.attr('pivotChoice') >> pivot_cnd.attr('secondTerm')
pivot_cnd.attr('outColor') >> ankleIk_ctrl.attr('rotatePivot')
















# # # # # # # # # # # # # # # # # # # # 
#... relocate foot pivot 
# # # # # # # # # # # # # # # # # # # # 

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import misc
reload(misc)

#side = 'LFT'
side = 'RGT'

toeBall_loc = core.Dag('toeBall_loc')
toeTip_loc = core.Dag('toeTip_loc')

mc.delete(f'toeRollleg{side}_ikh')
mc.delete(f'ballRollleg{side}_ikh')
mc.delete(f'ballLegFk{side}_parCons')


ball_ikJnt = core.Dag(f'ball{side}_ikJnt')
new_ball_ikJnt = core.Dag(f'ball{side}_jnt')


misc.snapPointCon(toeBall_loc.name ,ball_ikJnt.name)
misc.snapPointCon(toeTip_loc.name ,f'toesTip{side}_fkJnt')


misc.snapPointCon(ball_ikJnt.name ,f'ball{side}_fkJnt')
misc.snapPointCon(toeTip_loc.name ,f'toesTip{side}_fkJnt')

misc.snapPointCon(toeTip_loc.name ,f'toesTip{side}_ikJnt')


# ball_ikJnt.snapPoint(toeBall_loc)

ankle_ikJnt = f'ankle{side}_ikJnt'
toesTip_ikJnt = f'toesTip{side}_ikJnt'

ballIk_ikh = core.IkRp( startJoint = ankle_ikJnt, endEffector = ball_ikJnt )
ballIk_ikh.name = f'ballRollleg{side}_ikh'

toesTip_ikh = core.IkRp( startJoint = ball_ikJnt, endEffector = toesTip_ikJnt )
toesTip_ikh.name = f'toeRollleg{side}_ikh'


ToeRiselegIk_zro = core.Dag(f'ToeRiselegIk{side}Zro_grp')
ToeRiselegIk_zro.snapPoint(toeBall_loc)

ankleIkhZro_grp = core.Dag(f'ankleIkh{side}Zro_grp')
mc.parent(ankleIkhZro_grp.name, world = True)

ballRolllegIkZro_grp = core.Dag(f'ballRolllegIk{side}Zro_grp')
ballRolllegIkZro_grp.snapPoint(toeBall_loc)


toeRolllegIKZro_grp = core.Dag(f'toeRolllegIK{side}Zro_grp')
toeRolllegIKZro_grp.snapPoint(toeTip_loc) #... must tip joint


ballLegFk_gmbCtrl = core.Dag(f'ballLegFk{side}_gmbCtrl')
ball_fkJnt = core.Dag(f'ball{side}_fkJnt')

misc.snapPointCon(toeBall_loc.name ,f'ballLegFk{side}Zro_grp')
core.parentConstraint( ballLegFk_gmbCtrl , ball_fkJnt, mo=True )


misc.snapPointCon(toeBall_loc.name ,f'ballRolllegIk{side}Zro_grp')

#... parent back
mc.parent(f'ballRollleg{side}_ikh', f'ballRolllegIk{side}_buffCtrl')
mc.parent(f'toeRollleg{side}_ikh', f'ToeRiselegIk{side}Offset_grp')
mc.parent(f'ankleIkh{side}Zro_grp', f'ballRolllegIk{side}_buffCtrl')










































# # # # # # # # # # # # # # # # # # # # 
#... how to remove foot joint
# # # # # # # # # # # # # # # # # # # # 

[] delete 'toeRolllegLFT_ikh'
[] delete 'ballRolllegLFT_ikh'
[] delete 'constraint of fkJnt'
[] move ikJnt to new endPosition
[] select 'ankleLFT_ikJnt' and 'ballLFT_ikJnt' create ikHandle

[] select 'ballLFT_ikJnt' and 'toesTipLFT_ikJnt' create ikHandle

[] look at node 'legballRollLFT_mdl'
[] move pivot of 'ToeRiselegIkLFTZro_grp' to new position
[] unparent 'ankleIkhLFTZro_grp' to the world
[] snap 'ballRolllegIkLFTZro_grp' to new position
[] snap 'toeRolllegIKLFTZro_grp' to new position

[] drag 'ball_ikh' to under 'ballRolllegIkLFT_buffCtrl'
[] drag 'tollRoll_ikh' to under 'ToeRiselegIkLFTOffset_grp'

[] snap 'ballLegFkLFTZro_grp', 'ballLFT_fkJnt' to new position
[] re parentConstraint 'ballLegFkLFT_gmbCtrl' to 'ballLFT_fkJnt'








'''
for key in match_naming_ctrl["noman"]:
	#print(f"Noman: {key}")
	#print(f'{match_naming_ctrl["noman"][key]}')
	for idx,value in enumerate(match_naming_ctrl["noman"][key]):
		
		dode_name = match_naming_ctrl["dode"][key][idx]
		noman_name = match_naming_ctrl["noman"][key][idx]
		
		
		if mc.objExists(noman_name):
			mc.rename(noman_name, dode_name)
			print(f'compare name {dode_name} <<>>> {noman_name}')
		else:
			print('Not found pass na ja')
		

'''



# # # # # # # # # # # # # # # # # # # # 
#... Select only body joint
# # # # # # # # # # # # # # # # # # # # 
from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

standardJnt = mnd.standardJnt_list
mc.select(deselect=True)
for each in standardJnt:
	if mc.objExists(each):
		mc.select(each, add=True)


# # # # # # # # # # # # # # # # # # # # 
#.... reconnect handle weapon joint
# # # # # # # # # # # # # # # # # # # # 


handle = 'handPropRGT_gmbCtrl'


mc.connectAttr(f"{handle}.worldMatrix[0]", 'R_weapon_space_blendMatrix.target[0].targetMatrix', f=True)
mc.connectAttr(f"{handle}.worldMatrix[0]", 'L_weapon_space_blendMatrix.target[1].targetMatrix', f=True)



handle = 'handPropLFT_gmbCtrl'
mc.connectAttr(f"{handle}.worldMatrix[0]", 'L_weapon_space_blendMatrix.target[0].targetMatrix', f=True)
mc.connectAttr(f"{handle}.worldMatrix[0]", 'R_weapon_space_blendMatrix.target[1].targetMatrix', f=True)










# # # # # # # # # # # # # # # # # # # # # # # # 
#... rename file and p2texture node
# # # # # # # # # # # # # # # # # # # # # # # # 



from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

NODE_dict = mnd.NODE_dict

file_type = 'file'

file_type_short_name = [node['shortName'] for node in NODE_dict if node['longName'] == file_type ][0]



import re

my_list = mc.ls(type = file_type)
filter_file = []
for item in my_list:
	if re.match(fr'^file[0-9]{{2}}$', item):
		print(item)
		filter_file.append(item)
		mat_name = mc.listConnections(item, source=False)[-1] 
		new_name = f"{mat_name}_{file_type_short_name}"
		print(f"Rename from {item} to {new_name}")
		mc.rename(item, new_name)
		
		
		
file_type = 'place2dTexture'
file_type_short_name = [node['shortName'] for node in NODE_dict if node['longName'] == file_type ][0]

place_list = mc.ls(type = file_type) 
for item in place_list:
	
	if item.endswith('_PT'):
		print(item)
		continue
	elif re.match(fr'^{file_type}[0-9]{{2}}$', item):
		print(f'match item: {item}')
		mat_name = mc.listConnections(item)[0]
		new_name = mat_name + '_PT'       
		mc.rename(item, new_name) 




#... export
from function.asset import exportFBX
reload(exportFBX)

if mc.objExists('rig_grp.asset_name'):
	print('yeah')
	asset_name = mc.getAttr('rig_grp.asset_name')

selection = mc.ls(sl=True)

exportFBX.exportFBXnoConnection(selection, fileName = asset_name)




#... select bJnt
from function.rigging.util import generic_maya_dict as mnd
reload(mnd)
standard_list = mnd.standardJnt_list



ribbon_joint_dict = mnd.ribbon_joint




import maya.cmds as cmds

def connectTrans():
	selObjs = cmds.ls(sl=True)
	cmds.connectAttr(selObjs[0] + ".translateX", selObjs[1] + ".translateX")
	cmds.connectAttr(selObjs[0] + ".translateY", selObjs[1] + ".translateY")
	cmds.connectAttr(selObjs[0] + ".translateZ", selObjs[1] + ".translateZ")

	cmds.connectAttr(selObjs[0] + ".rotateX", selObjs[1] + ".rotateX")
	cmds.connectAttr(selObjs[0] + ".rotateY", selObjs[1] + ".rotateY")
	cmds.connectAttr(selObjs[0] + ".rotateZ", selObjs[1] + ".rotateZ")

	cmds.connectAttr(selObjs[0] + ".scaleX", selObjs[1] + ".scaleX")
	cmds.connectAttr(selObjs[0] + ".scaleY", selObjs[1] + ".scaleY")
	cmds.connectAttr(selObjs[0] + ".scaleZ", selObjs[1] + ".scaleZ")

connectTrans()




# # # # # # # # # # # # # # # # # # # # # # # # 
# # # CHECK NAME STYLE
# # # # # # # # # # # # # # # # # # # # # # # # 


from function.rigging.util import misc
reload(misc)

got_naming = misc.check_name_style(name = 'L_brow_inn_loc')



# # # # # # # # # # # # # # # # # # # # # # # # 
#... manual publish
# # # # # # # # # # # # # # # # # # # # # # # # 



from function.pipeline import fileTools as fileTools 
reload(fileTools)
fileTools.localPublish(mayafileType = 'mb')






#... replace from my repo to office repo

#... replace from
from function.
#... replace to
from axionTools.








from function.rigging.util import misc
reload(misc)

misc.replace_name()





# # # # # # # # # # # # # # # # # # # # 
# local world
# # # # # # # # # # # # # # # # # # # # 


from function.rigging.constraint import normalConstraint as nmCon
reload(nmCon)

nmCon.parent_localWorld(	zro_grp = 'L_pinStrap02Zro_grp',  # Zero out group
						ctrl = 'L_pinStrap02_ctrl',
						local_obj = 'L_pinStrap02_gmblCtrl',  # Parent object to assign in local space):
						world_obj = 'ctrl_grp',  # Parent object to assign in world space
						base_grp = 'L_pinStrap02Offset_grp',  # Offset group
						body_part = 'L_pinStrap02',
						attr_occur = 'L_pinStrap02_ctrlShape')













# uncheck segmentScaleCompensate
selected = mc.ls(sl=True)


for each in selected:
	mc.setAttr(f"{each}.segmentScaleCompensate", 0)















# # # # # # # # # # # # # # # # # # # # 
# Select standard joint
# # # # # # # # # # # # # # # # # # # # 

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

standardJnt_list = mnd.standardJnt_list

print (standardJnt_list)

for each in standardJnt_list:
	if mc.objExists(each):
		mc.select(each, add=True)




from function.rigging.constraint import normalConstraint as nmCon
reload(nmCon)
nmCon.constraintProxyJnt( child = 'bJnt', parent = 'pxyJnt' )




































from function.rigging.constraint import pinLocatorToSurface as pls
reload(pls)

pls.pin_locator_surface(	# need pxy nrb to drive locator
						nurbs = 'L_brow_nrb',
						region = 'brow',
						side = '',
						source_loc = ('L_brow01_loc','L_brow02_loc','L_brow03_loc'),
						locator_scale = 1,
						creJnt = True , suffixJnt = 'bJnt',
						creCtrl = True , ctrlShape = 'circle_ctrlShape',
						snapAtEnd = False,
						priorJnt = 'head_bJnt',
						scale = 2
						)




#... mirror joint and rename tip joint

from function.rigging.skeleton import jointTools as jtt
reload(jtt)

selected_joints = mc.ls(sl=True)
jtt.select_tip_joint(selected_joints, '_bJnt', '_endJnt')


jtt.mirror_joint_chain(root_joint = 'R_wing01_tmpJnt', axis = 'x')













							








list_name = mc.ls('L_*')

for each in list_name:
	new_name = each.replace('L_','R_')
	print(each)
	mc.rename(each,new_name)











from function.rigging.autoRig.base import core
reload(core)

cube = core.Dag('lwrFingerMain_ctrl')
cube.addAttribute( at = 'enum', keyable = True , en = 'on:off:', longName = 'Detail'  )
#cube.addAttribute( at = 'long'  , min = 0  , max = 1, longName = 'Detail', keyable = True, defaultValue = 1   )





















from function.rigging.autoRig.base import core
reload(core)


side = ('L', 'R')
upAndDown = ('jawUpper', 'jawLower')
num = 8

for s in side:
	for ud in upAndDown:
		for n in range(1, num + 1):
			ctrl_name = f'{s}_{ud}_lip_{n:02d}_ctrl'
			loc_name = f'{s}_{ud}_lip_{n:02d}_pxyCtrl'
			mc.rename(ctrl_name, loc_name)
			

			# locator = core.Locator(loc_name,lock=True, scale = 0.25)
			# locator.snap(ctrl_name)


			# #... find folder 
			# grp_name = f'{s}_{ud}_lip_{n:02d}_GRP'

			# mc.delete(ctrl_name)
			# mc.parent(locator.name, grp_name)
			




# # # # # # # # # # # # # # # # # # # # # # # # 
# # # PIN to surfece
# # # # # # # # # # # # # # # # # # # # # # # # 




from function.rigging.autoRig.addRig import rivetWithAddMatrix as rwm

reload(rwm)

rwm.rivetMatrix( 	skinCluster = 'Marin_cloth1_skc', 
					vtx = 'Marin_cloth.vtx[1845]'	, 
					target = 'L_pinStrap01_bJnt'	, 
					thresholdValue = 0.001)
















from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)
selected = mc.ls(sl=True)
mtc.del_selected_matrix(selected = selected)



#... create controller
from function.rigging.autoRig.base import core
reload(core)


cube = core.Dag('cube')
cube.nmCreateController('cross_ctrlShape')









# verifly

rawName = misc.check_name_style(name = each)


from function.rigging.autoRig.base import core
reload(core)


multMatirix = core.MultMatrixWithValue('something')


#... call controller


node_name = 'L_pointMatrix01_wtAddMat'

mc.setAttr('{0}.wtMatrix[0].weightIn'.format(node_name), 0)
mc.setAttr('{0}.wtMatrix[1].weightIn'.format(node_name), 0)
mc.setAttr('{0}.wtMatrix[2].weightIn'.format(node_name), 1)


mc.connectAttr()
mc.addAttr(selected ,attributeType = 'float' , longName = 'local_world', minValue = 0.0, maxValue = 1.0, defaultValue = 0 , keyable = True )
mc.setAttr('wtAddMatrix1.wtMatrix[2].weightIn',0.5)


# # # # # # # # # # # # # # # #
# template the joint
# # # # # # # # # # # # # # # #

from function.rigging.util import misc
reload(misc)

selected_joints = mc.ls(sl=True)
misc.select_tip_joint(selected_joints)


for each in selected:
	mc.setAttr("{0}.overrideEnabled".format(each), 1)
	mc.setAttr("{0}.overrideDisplayType".format(each), 1)
	
	  
misc.searchReplace( searchText='_bJnt', replaceText='_endJnt' )






# # # # # # # # # # # # # # # #
# change color of tip joint
# # # # # # # # # # # # # # # #

from function.rigging.util import misc
reload(misc)
misc.select_tip_joint(selected_joints=[ 'head01_bJnt'] )
selected = mc.ls(sl=True)
misc.searchReplace( searchText='_bJnt', replaceText='_endJnt' )

for each in selected:
	mc.setAttr("{0}.overrideEnabled".format(each), 1)
	mc.setAttr("{0}.overrideDisplayType".format(each), 1)




selected = mc.ls(sl=True)
for each in selected:
	if mc.nodeType(each)== 'joint':
		if mc.getAttr('{}.segmentScaleCompensate'.format(each)) == True:
			mc.setAttr(('{}.segmentScaleCompensate'.format(each)),0)
		else:
			mc.setAttr(('{}.segmentScaleCompensate'.format(each)),1)
			
		
 





# # # # # # # # # # # # # # # #
# update function make constraint to controller
# # # # # # # # # # # # # # # #

#... 1. Parent joint to hierarchy
if snapAtEnd:	
	for num in range(len(jnt_list)):
		if num  != 0:
			mc.parent(jnt_list[num],jnt_list[num-1])
		else:
			continue



	#... 2. Parent it to prior joint that desinate
	mc.parent(jnt_list[0], priorJnt)

	#... 3. ParentConstraint from controller to joint
	print('\n')
	print(ctrl_list)
	print(jnt_list)
	print('\n')

	

	for num in range(len(jnt_list)):
		ctrl_to_jnt_parCons = core.parentConstraint( ctrl_list[num] , jnt_list[num] )
		ctrl_to_jnt_parCons.name = '{}{:02d}{}_parCons'.format(region,num+1,side)



	# mc.error('Ma tum tor tomorrow')



# # # # # # # # # # # # # # # #
#...  wire deformer in detail
# # # # # # # # # # # # # # # #

import maya.cmds as cmd

def performWireDeformer(shape, deformCurves, baseCurves):
	count = len(deformCurves)
	wireDef = cmd.wire(shape, wc= count)[0]
	for i in range(count):  
		cmd.connectAttr('%s.worldSpace[0]' % deformCurves[i], '%s.deformedWire[%s]' % (wireDef, i)) 
		cmd.connectAttr('%s.worldSpace[0]' % baseCurves[i], '%s.baseWire[%s]' % (wireDef, i)) 
	cmd.setAttr('%s.rotation' % wireDef, 0)


shape = [] #Put your mesh shape here
deformCurves=[] #Put your wire curves here
baseCurves=[] #Put your base curves here

performWireDeformer(shape, deformCurves, baseCurves)






import maya.cmds as mc

mc.mirrorJoint(mirrorYZ=True, mirrorBehavior=True, searchReplace=("LFT", "RGT"))




# # # # # # # # # # # # # # # #
#...  List hierarchy from selected in autodesk maya using python
# # # # # # # # # # # # # # # #
def listHierarchy(type = 'joint'):
	selected = mc.ls(sl=True)[0]
	list_descendent = cmds.listRelatives(selected, allDescendents=True, type=type)


# # # # # # # # # # # # # # # #
#...  list end joint
# # # # # # # # # # # # # # # #


from function.rigging.skeleton import jointTools as jtt
reload(jtt)


selected_joints = mc.ls(sl=True)
jtt.select_tip_joint(selected_joints, '_bJnt', '_endJnt')





# Get the selected joint(s)
selected_joints = mc.ls(sl=True, type='joint')

# Iterate through the selected joints
for selected_joint in selected_joints:
	 # Find the tip joint(s) in the hierarchy
	 tip_joints = mc.listRelatives(selected_joint, allDescendents=True, type='joint')
	 tip_joints = [joint for joint in tip_joints if not mc.listRelatives(joint, c=True, type='joint')]

	 # Print the tip joint(s)
	 if tip_joints:
		  print("Tip joint(s) of", selected_joint, ":", tip_joints)
		  mc.select(tip_joints, r=True )
	 else:
		  print("No tip joints found for", selected_joint)







# # # # # # # # # # # # # # # #
#...  copy pivot
# # # # # # # # # # # # # # # #

sourceObj = mc.ls(sl = True)[len(mc.ls(sl = True))-1]
targetObj = mc.ls(sl = True)[0:(len(mc.ls(sl = True))-1)]
parentList = []
for obj in targetObj:
	if mc.listRelatives( obj, parent = True):
		parentList.append(mc.listRelatives( obj, parent = True)[0])
	else:
		parentList.append('')
if len(mc.ls(sl = True))<2:
	mc.error('select 2 or more objects.')
pivotTranslate = mc.xform (sourceObj, q = True, ws = True, rotatePivot = True)
mc.parent(targetObj, sourceObj)
mc.makeIdentity(targetObj, a = True, t = True, r = True, s = True)
mc.xform (targetObj, ws = True, pivots = pivotTranslate)
for ind in range(len(targetObj)):
	if parentList[ind] != '' : 
		mc.parent(targetObj[ind], parentList[ind])
	else:
		mc.parent(targetObj[ind], world = True)






import maya.cmds as mc
import re

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

def setRotateOrder(rotateOrder = 'yzx'):

	# Get the selected objects
	selected = mc.ls(sl=True)

	# Loop through each selected object and list its children
	for obj in selected:
		 children = mc.listRelatives(obj, allDescendents=True)

	# Define the regex pattern for *_ctrl
	pattern = r'^.*_ctrl$'

	ctrl_list = []

	for each in children:
		# Basic matching
		if re.search(pattern, each):
			 print(f"String '{each}' ends with '_ctrl'")
			 ctrl_list.append(each)




	# # # # # # # # # # # # # # # #
	#... Select and set rotate order
	# # # # # # # # # # # # # # # #

	# jnt_sel = mc.ls(sl=True)

	# for each in jnt_sel:
	# 	mc.setAttr('{}.rotateX'.format(each), -180)



	rot_dict = mnd.rotOrder_dict
	index = rot_dict[order]
	

	for each in ctrl_list:
		try:
			mc.setAttr('{}.rotateOrder'.format(each), index)
			print('Change rotate order to {0} complete.'.format(order))
		except:
			print(each)
			continue








# # # # # # # # # # # # # # # #
#... change color selected joint to gray
# # # # # # # # # # # # # # # #

from function.rigging.autoRig.base import core
reload(core)


selected = mc.ls(sl=True)
for each in selected:
	joinin = core.Dag(each)
	joinin.setJointColor('gray')
	





# # # # # # # # # # # # # # # #
#... call JJmenu manual
# # # # # # # # # # # # # # # #
# Reload module


try:
	reload  # Python 2.7
	print('This might be python 2.7')
except NameError:
	try:
		from importlib import reload  # Python 3.4+
		print('Python 3.4+')
	except ImportError:
		from imp import reload  # Python 3.0 - 3.3
		print('Python 3.0 - 3.3')




# userSetup for maya2022 is not load, I donno how to fix it

# import module
import maya.cmds as mc
import sys
import maya.utils



def runThis():
	print ("TEST_maya_2022")

cmds.evalDeferred( runThis ) 


SYSTEM_PATH = r'D:\True_Axion\Tools\mayaTools\python'


import importlib

# append path
sys.path.append(SYSTEM_PATH)


from axionMenu import axionMenu2022 as axm
importlib.reload(axm)




maya.utils.executeDeferred('axm.runMenu()') 
print ('Create Axion menu...')



# Active port 7002 to recived message from Sublime to Maya
try:
	mc.commandPort(name=":7002", sourceType="python")
except :
	mc.warning('Could not active port 7002 (maybe it already opened.)')









# # # # # # # # # # # # # # # #
#... toggle scale seqmane
# # # # # # # # # # # # # # # #



selected = mc.ls(sl=True)
for each in selected:
	if mc.nodeType(each)== 'joint':
		if mc.getAttr('{}.segmentScaleCompensate'.format(each)) == True:
			mc.setAttr(('{}.segmentScaleCompensate'.format(each)),0)
		else:
			mc.setAttr(('{}.segmentScaleCompensate'.format(each)),1)







from function.rigging.util import misc as misc
from function.framework.reloadWrapper import reloadWrapper as reload
reload(misc)
sel = mc.ls(sl=True)
misc.parentMatrix( sel[0], sel[1], mo = True, t = True, r = True, s = True)





#... select delete matrix
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)
selected = mc.ls(sl=True)
mtc.del_sel_matrix(selected = selected)






from function.rigging.util import misc
reload(misc)				
selected = mc.ls(sl = True)		
misc.del_sel_matrix(selected)	



from function.rigging.util import generic_maya_dict as mnd
reload(mnd)




def setJointColor(name,color):
	COLOR_dict = mnd.COLOR_dict

	if color in COLOR_dict.keys():
		colorId = COLOR_dict[color]
		mc.setAttr( '%s.overrideEnabled'    %name , 1 )
		mc.setAttr( '%s.overrideColor'      %name, colorId )

	else:
		colorId = 0
		mc.error("Insert string keyword such as yellow")



setJointColor('skirtC02','gray')		











# # # # # # # # # # # # # # # #
#... make bigger
# # # # # # # # # # # # # # # #
make_bigger = (		'head01_ctrl','eyeCenter_ctrl','upperArmLFTFK_ctrl',
					'lowerArmLFTFK_ctrl','handLFTFK_ctrl','upperLegLFTFK_ctrl','lowerLegLFTFK_ctrl','footLFTFK_ctrl','upperArmLFTFK_ctrl','handLFTFK_ctrl'
					'lowerArmRGTFK_ctrl','handRGTFK_ctrl','upperLegRGTFK_ctrl','lowerLegRGTFK_ctrl','footRGTFK_ctrl','upperArmRGTFK_ctrl','handRGTFK_ctrl'
					'hip_ctrl','spine01FK_ctrl','spine02FK_ctrl','spine03FK_ctrl')




from function.rigging.util import misc
reload(misc)


mc.select(make_bigger, r=True)

ctrl = mc.ls(sl=True)

for each in ctrl:
	shapeCtrl = misc.shapeName(each)
	mc.setAttr('{}.lineWidth'.format(shapeCtrl), 2)






def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(5))  # Output: 120





import maya.cmds as cmds

cmds.addRecentFile("D:/projects/HomeProjects/scenes/backTest.mb", "mayaBinary")





from function.rigging.util import misc
reload(misc)
misc.del_sel_matrix()






from function.asset import exportFBX 
reload(exportFBX)

root_joint = 'root'

selected = mc.ls(sl=True)


for each in selected:
	mc.select(root_joint,r=True)
	mc.select(each,add=True)
	sel_export = mc.ls(sl=True)
	exportFBX.exportFBXnoConnection(sel_export, fileName= sel_export[-1])
	
	
	











# connectAttr -f rig_grp.asset_name root_meta.rig_grp;
'''

Sure, I can help you come up with some ideas for organizing your files and folders on your PC. Here are a few tips and suggestions:

Start with a clear naming convention: Before you start creating folders, decide on a clear and consistent naming convention for your files and folders. This will help you find what you need quickly and easily. For example, you could use dates (YYYY-MM-DD), project names, or categories like "work" and "personal".

Use subfolders: If you have a lot of files, create subfolders within your main folders to help you organize them. For example, if you have a "work" folder, you could create subfolders for each project or client.

Use descriptive names: Use descriptive names for your folders so that you can quickly identify what's inside. For example, instead of "Project 1," use "Project 1 - Marketing Campaign."

Group files by type: Create separate folders for different types of files, such as documents, images, videos, and music.

Use color-coding: If you're a visual person, consider using color-coding to help you quickly identify different folders. For example, you could use blue for work folders and green for personal folders.

Keep it simple: Don't create too many folders or subfolders, as this can make it difficult to find what you need. Stick to a few main categories and use subfolders only when necessary.

Here are some folder names you can use as a starting point:

Work
Personal
Projects
Finance
Health
Education
Photos
Videos
Music
Documents
Downloads
Important
Archived
Templates
Contacts
Travel
Social Media
Events
Receipts
Tax



Remember, the key is to find a system that works for you and stick to it consistently. Good luck organizing your files and folders!



'''


file:///D:/narongtum/research_and_developement/22.06.Jun.08.Wed_Soft%20IK/softIK%20tutorial/video/03%20softIK%20part2.mp4


file:///D:/narongtum/research_and_developement/22.06.Jun.08.Wed_Soft IK/Upgrading Rig with Soft IK (Puppeteer Lounge)-153658450.mp4











# @property sample


class MyClass:
	def __init__(self, x):
		self.x = x

	@property
	def square(self):
		return self.x ** 2



my_instance = MyClass(5)
print(my_instance.square)  # Output: 25



class MyClass:
	def __init__(self, x):
		self.x = x

	def square(self):
		return self.x ** 2


my_instance = MyClass(5)
print(my_instance.square())  # Output: 25








"""


import maya.cmds as mc

class Node:
	'''
	Template Base class for Maya nodes
	'''
	# nodeId = 0
	
	def __init__(self, name):
		# self.nodeId = Node.nodeId
		# self.nodeId += 1
		self.__name = str(name)
		print(f'Creating Object name: {self.__name}')
		
		# Clear selection
		mc.select(cl=True)
	
	# Return string name
	def __str__(self):
		return str(self.name)
	
	# Show full internal module path
	def __repr__(self):
		return str(self.name)

	'''
	def __del__(self):
		self.deleteName()
	'''
	
	def deleteName(self, **kwargs):
		'''Delete the node and construction history in Maya'''
		print(f'Deleting object {self.name} ...')
		mc.delete(self.name, **kwargs)

	# Property to get the name of the object
	@property
	def name(self):
		return self.__name
	
	# Property to rename the object
	@name.setter
	def name(self, new_name):
		print(f'Resetting name to {new_name}')
		self.__name = str(mc.rename(self.__name, new_name))
		
	# Property to get the type of the object
	@property
	def type(self):
		return mc.nodeType(self.name)

	# Property to check if the object exists
	@property
	def exists(self):
		return mc.objExists(self)






"""


'''
@echo off

set PYTHON="C:\Users\Noman\AppData\Local\Programs\Python\Python310\python.exe"
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=
git pull
call webui.bat


'''
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.skin import roundSkinWeight as rsw
reload(rsw)
selected = mc.ls(sl=True)[0]
rsw.roundSkinWeight(digit=3, selection=selected)


from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.skin.nsSkinClusterIO import nsSkinClusterIO_reFunc as skinIO
reload(skinIO)
skinIO.saveSkin()
mc.select(deselect = True)

skinIO.loadSkin()



import re

# Create a list of strings to search for prefixes
strings = ["BAK_123.txt", "bak_456.txt", "abc.txt", "BAK_789.txt"]

# Use regular expression to find strings with prefix "BAK_" and "bak_"
pattern = re.compile(r'^(BAK_|bak_).*')
prefixes = [s for s in strings if pattern.match(s)]

# Print the list of prefixes
print("List of prefixes BAK_ or bak_:")
print(prefixes)


import maya.cmds as mc
from function.enviroment import enviromentPath as env
reload(env)
REF_PATH = env.REFERENCE_PATH + '/templateJoint_biped.ma'

namespace = "_temp_ref"

mc.file(REF_PATH, 
		  r=True, 
		  type="mayaAscii", 
		  ignoreVersion=True, 
		  gl=True, 
		  mergeNamespacesOnClash=False, 
		  namespace=namespace, 
		  options="v=0;")

mc.duplicate('_temp_ref:template_ctrl')


#mc.file(PATH, r = True, type = 'mayaAscii', ignoreVersion = True, mergeNamespacesOnClash = False, renamingPrefix = '' , options = 'v=0', preserveReferences = True, importFrameRate = True,importTimeRange = "override" )











# new matrix constraint
from function.rigging.constraint import matrixConstraint as mtc
from function.framework.reloadWrapper import reloadWrapper as reload
reload(mtc)
sel = mc.ls(sl=True)
mtc.parentConMatrix( sel[0], sel[1], mo = True, translate = True, rotate = True, scale = True)






# old matrix constraint
from function.rigging.util import misc as misc
from function.framework.reloadWrapper import reloadWrapper as reload
reload(misc)
sel = mc.ls(sl=True)
misc.parentMatrix( sel[0], sel[1], mo = True, translate = True, rotate = True, scale = True)






from pymel.core import *

def connectTrans():
	selObjs = ls(sl=True)
	connectAttr(selObjs[0] + ".translateX", selObjs[1] + ".translateX")
	connectAttr(selObjs[0] + ".translateY", selObjs[1] + ".translateY")
	connectAttr(selObjs[0] + ".translateZ", selObjs[1] + ".translateZ")

	connectAttr(selObjs[0] + ".rotateX", selObjs[1] + ".rotateX")
	connectAttr(selObjs[0] + ".rotateY", selObjs[1] + ".rotateY")
	connectAttr(selObjs[0] + ".rotateZ", selObjs[1] + ".rotateZ")

	connectAttr(selObjs[0] + ".scaleX", selObjs[1] + ".scaleX")
	connectAttr(selObjs[0] + ".scaleY", selObjs[1] + ".scaleY")
	connectAttr(selObjs[0] + ".scaleZ", selObjs[1] + ".scaleZ")

connectTrans()










#... reset windows panel

for each in mc.lsUI( controls = True, windows = True):
	try:mc.window(each, edit = True, topLeftCorner = (0,0))
	except:pass




#... reset Take001 to file name
mel.eval('FBXExportSplitAnimationIntoTakes -c')
mel.eval('FBXExportUseSceneName -v true')





#... find length 
import maya.cmds as cmds
import maya.api.OpenMaya as om
cube1, cube2 = cmds.polyCube()[0], cmds.polyCube()[0]
cmds.xform(cube2, t=(1,2,3))
cmds.xform(cube1, t=(3,5,2))



t1, t2 = cmds.xform(cube1, t=1, q=1), cmds.xform(cube2, t=1, q=1)
print t1,t2
v1, v2 = om.MVector(t1), om.MVector(t2)
print v1, v2



import maya.api.OpenMaya as om
import math

# create MVector
vector = om.MVector([0,1,0])

# get component
x = vector.x
y = vector.y
z = vector.z

# now with benefit of object we can operate vector easy

# multiplt vector
multiplied_vector = vector * 2
print multiplied_vector

# get vector lenght
lenght = vector.lenght()
print lenght



import maya.api.OpenMaya as om
cube1, cube2 = cmds.polyCube()[0], cmds.polyCube()[0]
t1, t2 = cmds.xform(cube1, t=1, q=1), cmds.xform(cube2, t=1, q=1)
v1, v2 = om.MVector(t1), om.MVector(t2)
print v1, v2
v = v2-v1
print v







#... parentMatrixCon backup
from function.rigging.util import misc as misc
from function.framework.reloadWrapper import reloadWrapper as reload
reload(misc)
sel = mc.ls(sl=True)
misc.parentMatrix( sel[0], sel[1], mo = True, translate = True, rotate = True, scale = True)


#... find vector length
import pymel.core as pymel

start_loc = 'upperLegLFT_bJnt'
end_loc = 'lowerLegLFT_bJnt'
destination = 'pCone1'

startPosition = pymel.xform(start_loc,q=True,ws=True,t=True)
startPosition = pymel.datatypes.Point(startPosition)

endPosition = pymel.xform(end_loc,q=True,ws=True,t=True)
endPosition = pymel.datatypes.Point(endPosition)

startEndVector = pymel.datatypes.Vector(endPosition-startPosition)

mc.setAttr("{0}.translateX".format(destination), startEndVector.x)
mc.setAttr("{0}.translateY".format(destination), startEndVector.y)
mc.setAttr("{0}.translateZ".format(destination), startEndVector.z)






# add data for zbing asset

from function.rigging.autoRig.base import core
reload(core)

rig_grp = core.Dag('rig_grp')

rig_grp.addAttribute( attributeType = 'enum', en = 'Player:Weapon', longName = 'asset_type', keyable = False   )
rig_grp.addAttribute( dataType = 'string' , longName = 'asset_name', keyable = False )
rig_grp.addAttribute( attributeType = 'bool' , longName = 'delete_unused_skin', minValue = 0, maxValue = 1, defaultValue = 0 , keyable = False )
rig_grp.addAttribute( attributeType = 'bool' , longName = 'delete_unused_material', minValue = 0, maxValue = 1, defaultValue = 0 , keyable = False )
rig_grp.addAttribute( attributeType = 'enum', en = 'Unity:Unreal', longName = 'Engine', keyable = False   )









from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)

selected = mc.ls(sl=True)[0]
mtc.createMatrixAttr(selected, attrNam = 'destination'):




from function.asset import exportFBX 
reload(exportFBX)

selected = mc.ls(sl=True)
mc.select('root', add=True)

exportFBX.exportFBXnoConnection(selected, fileName= selected[0])













from function.rigging.autoRig.base import core
reload(core)


cube = core.Dag('handPropRGT_ctrl')
cube.addAttribute( at = 'enum', keyable = True , en = 'Hand:World', longName = 'Space'  )




meshName = mc.ls(sl=True)[0]
sel_vtx = '{0}.f[208:371]'.format(meshName)
mc.select(sel_vtx,add=True)




selected = mc.ls(sl=True)[0]
mc.addAttr(selected, ln='offsetAttr', at='matrix')

from function.rigging.util import misc
reload(misc)
misc.del_sel_matrix()


		
from function.rigging.util import misc
reload(misc)


sel = mc.ls(sl=True)
misc.parentMatrix( sel[0], sel[1], mo = False, translate = True, rotate = True, scale = True)


from function.asset import exportFBX 
reload(exportFBX)



#skinName = ['base01','male01','female01','osskin01','punk01','zombing01','reaper01']
skinName = ['base01']
skinName = ['male01','female01']
partName = ['hat','ub','lb']
for each in skinName:
	for part in partName:
		print('{0}_{1}_ply'.format(part,each) )
		
		#mc.parent('{0}_{1}_ply'.format(part, each), world=True)
		#mc.setAttr('{0}_{1}_ply.visibility'.format(part, each),1)
		mc.select('root', replace=True)
		mc.select('{0}_{1}_ply'.format(part, each), add = True)
		selected = mc.ls(sl=True)
		print(selected)
		exportFBX.exportFBXnoConnection(selected, fileName= '{0}_{1}'.format(part, each))




		
from function.asset import assetTools as ast
reload(ast)

ast.printTexturePath()

transforms = mc.ls(type='transform') #lists all the transform nodes in the scene
polyMeshes = mc.filterExpand(transforms, sm = 12 )# filters out all the non-polymesh nodes
polyMeshes = list(set(polyMeshes)) # remove duplicate name


bake_mesh = [each for each in polyMeshes if mc.objExists('{0}.bake_mesh'.format(each))]



from function.rigging.autoRig.base import core
reload(core)


selected = mc.ls(sl=True)
for each in selected:
	each_sel = core.Dag(each)
	each_sel.addAttribute( attributeType = 'bool' , longName = 'bake_mesh', minValue = 0, maxValue = 1, defaultValue = 1 )











# Nico copy skin
# in copy ski tools
def ncCopySkinWeights(source, target):
	import maya.mel as mel

	skinClusterA = mel.eval('findRelatedSkinCluster '+source)
	infList = mc.skinCluster(skinClusterA, q=True, inf = True ) 

	skinClusterB = mel.eval('findRelatedSkinCluster '+target)

	if skinClusterB != '':
		mc.setAttr(skinClusterB+'.envelope', 0)
		mc.delete(skinClusterB)
		

	# create new skinCluster on new model
	mc.skinCluster(infList,target, tsb = True)
	# copy skin weight to the new one
	mc.copySkinWeights(source, target,noMirror=True, surfaceAssociation = 'closestPoint', influenceAssociation = 'oneToOne')
	print('Copy weight from {0} to {1} was done !!!'.format(source,target))










'''
Jelley Skin rigged with Maya format has controll rigging features. FBX format has only bones and model were skinned.

'''

from function.asset import exportFBX 
reload(exportFBX)

assetName = 'CaribbeanMonkSeal'

selected = mc.ls(sl=True)
exportFBX.exportFBXnoConnection(selected, fileName= '{0}_sp1_cha.fbx'.format(assetName))


selected = mc.ls(sl=True)
exportFBX.exportFBXnoConnection(selected, fileName= '{0}_sp1_vac.fbx'.format(assetName))





# list texture path

import maya.cmds as mc

fileNodes = mc.ls(type="file")

# print texture path
for each in fileNodes:
	mc.select(each, r = True)
	fullName = mc.getAttr(".fileTextureName")
	print (fullName)
	


'''

from axionTools.framework.reloadWrapper import reloadWrapper as reload




http://www.serge-scherbakov.com/search/label/Python

Align pivots by Serge Scherbakov.
Usage:
1. Select source object(s)
2. Add to selection target object
3. Run script by 'import copyPivot\n copyPivot.copyPivot()
'''
 
import maya.cmds as cmds
import maya.mel as mel
 
def copyPivot ():
	sourceObj = cmds.ls(sl = True)[len(cmds.ls(sl = True))-1]
	targetObj = cmds.ls(sl = True)[0:(len(cmds.ls(sl = True))-1)]
	parentList = []
	for obj in targetObj:
		if cmds.listRelatives( obj, parent = True):
			parentList.append(cmds.listRelatives( obj, parent = True)[0])
		else:
			parentList.append('')
	if len(cmds.ls(sl = True))<2:
		cmds.error('select 2 or more objects.')
	pivotTranslate = cmds.xform (sourceObj, q = True, ws = True, rotatePivot = True)
	cmds.parent(targetObj, sourceObj)
	cmds.makeIdentity(targetObj, a = True, t = True, r = True, s = True)
	cmds.xform (targetObj, ws = True, pivots = pivotTranslate)
	for ind in range(len(targetObj)):
		if parentList[ind] != '' : 
			cmds.parent(targetObj[ind], parentList[ind])
		else:
			cmds.parent(targetObj[ind], world = True)
	 
 
copyPivot()





# run digital37 cleanup



# remove unused locator
# source cleanUpScene.mel first
mel.eval('source "cleanUpScene.mel"')
mel.eval( 'deleteUnusedLocators()' )

# remove unused rendering node
# mel command
mel.eval('MLdeleteUnused()')

# remove empty transform
mel.eval( 'deleteEmptyGroups()' )




from axionTools.rigging.autoRig.base import core
reload(core)




eNum = 'World:HandLFT:HandRGT'
some_ctrl = core.Dag('weapon_ctrl')
some_ctrl.addAttribute( longName = 'Snap', at = 'enum', keyable=True , en = eNum)


from axionTools.rigging.util import misc as misc
reload(misc)
misc.constraintProxyJnt( child = 'bJnt', parent = 'pxyJnt' )



# Made by Jeff Rosenthal
# JeffRosenthal.org
# 8/1/2012
################################################################################
# Creates left and ride side variations of a blendshape along the X axis
#
# Select your source face, then select the blendshape you created
# run the script!
#
# Questions? jeffrosenth at gmail dot com


#USER CAN CHANGE THIS NUMBER
###################
percentRange = .1

####  .1 = 10% falloff
####  .3 = 30% falloff
####   1 = 100% falloff (probably looks bad)
###################


import maya.cmds as cmds

def getValue(x, range, max):
		value = (1 - x / (range * max)) / 2
		return clamp(value, 0, 1)

def clamp(value, low, high):
	if value < low:
		return low
	if (value > high):
		return high
	return value
	  
def getShapeNode(transform):
	return cmds.listRelatives(transform, shapes=True)[0]

(sourceObj, targetObj) = cmds.ls(sl=1)
sourceShape = getShapeNode(sourceObj)

#look at number of verticies
cmds.select(sourceObj)
numVerts = cmds.polyEvaluate(v=1)

#figure out width of face (assume X axis)
rgtX = 0
lftX = 0
for i in range(0,numVerts):
		testX = cmds.pointPosition(targetObj + ".vtx[" + str(i) + "]", l=1)[0]
		if testX < rgtX:
				rgtX = testX
		if testX > lftX:
				lftX = testX
			  
#duplicate face twice (one left, one right)
cmds.select(targetObj)
targetObj_Lft = cmds.duplicate(n=targetObj+'_Lft')[0]
cmds.move(rgtX * -2.1, 0, 0, r=1)
cmds.select(targetObj)
targetObj_Rgt = cmds.duplicate(n=targetObj+'_Rgt')[0]
cmds.move(rgtX * 2.1, 0, 0, r=1)

side = 1
#on each object
for target in ([targetObj_Lft, targetObj_Rgt]):
	side *= -1
	#for each vert
	for i in range(0,numVerts):
		#get vert positions
		#sourcePos = cmds.getAttr(sourceShape + '.pnts[' + str(i) + ']')[0]
		#targetPos = cmds.getAttr(target + '.pnts[' + str(i) + ']')[0]
		sourcePos = cmds.pointPosition(sourceObj + ".vtx[" + str(i) + "]", l=1)
		targetPos = cmds.pointPosition(target + ".vtx[" + str(i) + "]", l=1)       
		
		#find difference
		differencePos = (sourcePos[0] - targetPos[0], sourcePos[1] - targetPos[1], sourcePos[2] - targetPos[2])
		
		#get falloff amount from side of object
		testX = cmds.pointPosition(sourceObj + ".vtx[" + str(i) + "]", l=1)[0]
		falloff = getValue(testX, percentRange, rgtX * side)
		
		#move vert difference * falloff amount
		cmds.xform(target + '.vtx[' + str(i) + ']', rt=(differencePos[0] * falloff, differencePos[1] * falloff, differencePos[2] * falloff))

cmds.select(cl=True)














#
# auto naming file name
#



#  naming file texture name
textureSelect = mc.ls(sl=True)

if textureSelect:
	for each in textureSelect:

		if mc.nodeType(each) == 'file':
			print 'This texture file'
			matNam = mc.listConnections(each)[0]
			print matNam

			#print materialName
			if matNam.endswith('_mat'):
				print 'This material is naming already'
				# convert name
				# fileMatNam = matNam.strip('_mat') + '_file'
				fileMatNam = matNam.replace('_mat','_file')
				print fileMatNam
				mc.rename( each , fileMatNam )
			else:
				print 'This is not naming'

		elif mc.nodeType(each) == 'place2dTexture':
			print 'This place2dTexture file'
			matNam = mc.listConnections(each)[0]
			print matNam

			#print materialName
			if matNam.endswith('_file'):
				print 'This material is naming already'
				# convert name
				# fileMatNam = matNam.strip('_file') + '_plce2d'
				fileMatNam = matNam.replace('_file','_plce2d')
				print fileMatNam
				mc.rename( each , fileMatNam )
			else:
				print 'This place2dTexture is not naming'

else:
	mc.warning('Please select file texture.')
	
	


listFile = mc.ls(type = 'file')


for each in listFile:
	matNam = mc.listConnections(each)[0]
	#print materialName
	if matNam.endswith('_mat'):
		print 'This is naming already'
		fileMatNam = matNam.split('_mat')[0] + '_file'
		print fileMatNam
		mc.rename( each , fileMatNam )
	else:
		print 'This is not naming'
		continue
		
		
		
listFile = mc.ls(type = 'place2dTexture')
for each in listFile:
	matNam = mc.listConnections(each)[0]
	print matNam
	#print materialName
	if matNam.endswith('_file'):
		print 'This is naming already'
		fileMatNam = matNam.split('_file')[0] + '_plce2d'
		print fileMatNam
		mc.rename( each , fileMatNam )
	else:
		print 'This is not naming'
		continue

























# nocare exporter
from axionTools.asset import exportFBX 
reload(exportFBX)
exportFBX.noCareExporter( suffix = '*_bJnt' , rootJnt = 'root')




# Find folder and important dir
partFileName = mc.file( q=1,sn=1)
splitfileName = partFileName.split('/')
preName = splitfileName[len(splitfileName)-1]

name = preName.split('.ma')[0]
# PART FINDER
path = partFileName.split('/'+name)[0]
# add preview folder
path += r'\\preview\\'
# normalize path
path = os.path.normpath( path )



# get region
region = mc.getAttr('%s.region' %stickNam )

# capital
str.capitalize()

# open recent list
list = cmds.optionVar(query='RecentFilesList')[-1]
mc.file(	list, force = True , ignoreVersion = True, type =  "mayaAscii" , open = True     )



# open recent list
import maya.cmds as cmds
list = cmds.optionVar(query='RecentFilesList')




mc.connectAttr(item + '.message', ctrl + '.' + attr)

a+b = 99.241


legType.capitalize() 




def distanceNode(	nameLoc1 = 'something' ,
					startPoint = ''		,
					endPoint = ''			):
	# return name of distance node
	if startPoint:
		dis = core.DistanceBetween(name = name )
		disObj = core.Dag(dis)
		disObj.suffix

		loc1 = core.Locator(name + '1_loc')
		loc2 = core.Locator(name + '2_loc')

		loc1.maSnap(startPoint)
		loc2.maSnap(endPoint)

		loc1shape = core.Dag(loc1.shape)
		loc2shape = core.Dag(loc2.shape)
		

		loc1shape.attr('worldPosition[0]') >> disObj.attr( 'point1' )
		loc2shape.attr('worldPosition[0]') >> disObj.attr( 'point2' )

		return disObj.name

	else:
		mc.warning("Please specify startPoint and endPoint first.")


# Create Controller at selected object.
from axionTools.rigging.controllerBox import adjustController as adjust
reload(adjust)

adjust.creControllerFunc(	scale = 0.5, ctrlShape = 'circleCurlUp_ctrlShape',color = 'yellow'	)








# message attribute
from axionTools.rigging.autoRig.base import core
reload(core)


master_ctrl = core.Dag( 'master_ctrl' )
# create message attr
master_ctrl.addAttribute(at='message', ln = 'someMessage')

# no need to create message of source u can connect '.message' to destination 
mc.connectAttr('head01_ctrl' + '.message' , 'master_ctrl.someMessage' )

# query message attr name
mc.listConnections('master_ctrl.someMessage')[0]




#  naming file texture name
textureSelect = mc.ls(sl=True)

if textureSelect:
	for each in textureSelect:

		if mc.nodeType(each) == 'file':
			print 'This texture file'
			matNam = mc.listConnections(each)[0]
			print matNam

			#print materialName
			if matNam.endswith('_mat'):
				print 'This material is naming already'
				# convert name
				# fileMatNam = matNam.strip('_mat') + '_file'
				fileMatNam = matNam.replace('_mat','_file')
				print fileMatNam
				mc.rename( each , fileMatNam )
			else:
				print 'This is not naming'

		elif mc.nodeType(each) == 'place2dTexture':
			print 'This place2dTexture file'
			matNam = mc.listConnections(each)[0]
			print matNam

			#print materialName
			if matNam.endswith('_file'):
				print 'This material is naming already'
				# convert name
				# fileMatNam = matNam.strip('_file') + '_plce2d'
				fileMatNam = matNam.replace('_file','_plce2d')
				print fileMatNam
				mc.rename( each , fileMatNam )
			else:
				print 'This place2dTexture is not naming'

else:
	mc.warning('Please select file texture.')














sel = mc.ls(sl=True)
for each in sel:
	# set sRGB
	mc.setAttr('%s.colorSpace' %each,'sRGB' , type="string" )




from axionTools.rigging.util import boundingBox as bBox
reload(bBox)

sel = mc.ls(sl=True)[0]
bb = bBox.geoBoundingBox(sel)




from axionTools.rigging.util import misc as misc
reload(misc)
misc.parentSufficMatrix( child = 'bJnt' , parent = 'pxyJnt' , mo = True, w = 1, t = True, r = True, s = True)

from axionTools.rigging.util import misc as misc
reload(misc)
sel = mc.ls(sl=True)
misc.parentMatrix( sel[0], sel[1], mo = True, t = True, r = True, s = True)


from axionTools.rigging.util import misc as misc
reload(misc)

misc.parentSufficMatrix( child = 'bJnt' , parent = 'pxyJnt' , mo = True, w = 1, t = True, r = True, s = True)


mc.select('*_bJnt')





# Python code maya screen capture
import maya.OpenMaya as om
import maya.OpenMayaUI as omui

fileType = 'jpg'
imageFile = 'd:/temp/mayaScreen.%s'%fileType
mimage = om.MImage()
view = omui.M3dView.active3dView()
view.readColorBuffer(mimage, True)
mimage.writeToFile(imageFile, fileType)








# list comphrehension
h_letters = []

for letter in 'human':
	h_letters.append(letter)

print(h_letters)



# is equal

h_letters = [ letter for letter in 'human' ]
print( h_letters)









# find shapeName
geoShape = mc.listRelatives(selGEO, shapes = True)[0]





# Create Controller at selected object.
from axionTools.rigging.controllerBox import adjustController as adjust
reload(adjust)

adjust.creControllerFunc(	scale = 1, ctrlShape = 'circle_ctrlShape',color = 'yellow'	)






# read curve file and multiply -1
from axionTools.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)
sel = mc.ls(sl=True)
shapes = wcd.getShape(sel[0])
newShapes = []


for i, each in enumerate(shapes["points"]):
	shapes["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
newShapes.append(shapes)












from axionTools.rigging.autoRig.base import rigTools
reload( rigTools )


rigTools.zroNewGrpWithOffset( obj )





# 2 decimal places
num =-1.000000
print 'hello %0.1f' %num
hello -1.0





misc.parentMulMatrix()

misc.parentSufficMatrix( child = '' , parent = '' , mo = True, w = 1, t = True, r = True, s = True)



misc.parentMatrix( src, tgt, mo = True, t = True, r = True, s = True)


from axionTools.rigging.skin import skinUtil
reload(skinUtil)

skinUtil.writeRigData()




from axionTools.rigging.util import misc as misc
reload(misc)
misc.constraintProxyJnt( child = 'bJnt', parent = 'pxyJnt' )


from axionTools.rigging.util import misc as misc
reload(misc)
misc.parentSufficMatrix( child = 'bJnt' , parent = 'pxyJnt' , mo = True, w = 1, t = True, r = True, s = True)






allJnt = mc.ls('*_proxyJnt')

for each in allJnt:
	mc.setAttr('%s.segmentScaleCompensate' %each , 0)





	


# select







# read json skinweight file
from axionTools.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload (wcd)

def skinData(filePath=''):
	vertexDict 	= 	wcd.loadData(filePath)
	skinJntLst = vertexDict['skinJnt']
	skinName = vertexDict['skinCluster']
	return skinJntLst
	return skinName
	

skinJntLst  = skinData(filePath=r"D:\True_Axion\Project_UGP\Content\3D_ART\DemonBlade\rigLowFix\data\skinData\jacket_ply_skcData.json")

filePath=r"D:\True_Axion\Project_UGP\Content\3D_ART\DemonBlade\rigLowFix\data\skinData\jacket_ply_skcData.json"
vertexDict 	= 	wcd.loadData(filePath)
skinJntLst = vertexDict['skinJnt']
skinName = vertexDict['skinCluster']

mc.select(skinJntLst , r = True)




import pymel.core as pm
print 'import pymel.core as pm'
import pymel.mayautils
import os




SYSTEM_PATH = r'D:\noman\OOP\Maya\Python'



def setup(path):
	"""
	Setup the packages that have been decoupled from the Studio Library.

	:param path: The folder location that contains all the packages.
	:type path: str

	:rtype: None
	"""
	if os.path.exists(path) and path not in sys.path:
		sys.path.append(path)
	'''
	for i in sys.path:
		print i
	'''

setup(SYSTEM_PATH)


import digital37.maya.general.menu
pymel.mayautils.executeDeferred(digital37.maya.general.menu.loadMenu)
print 'create 37digital custom menu'







# list of skincluster joint


import maya.cmds as cmds
#get the skin cluster and the joint
selection = cmds.ls(sl=True, fl=True)
jointSelection = cmds.ls(sl=True,type = "joint")
#we need the shape node to get the skincluster connection
relatives = cmds.listRelatives(selection, type = "shape")
sCluster = cmds.listConnections(relatives, type = "skinCluster")
#get the joints in the skincluster
skinInfluences = cmds.skinCluster(sCluster[0],q=True,inf=True)#get skinCluster
cmds.select(cl=True)

#loop through each influence in the cluster until it is the joint you want to query
for influence in skinInfluences:
	if jointSelection[0] == influence:
		cmds.skinCluster(sCluster[0], e=True, selectInfluenceVerts = influence)
















# open containter folder
from axionTools.pipeline import fileTools as fileTools 
reload(fileTools)

from nomanTools import aimCon as ac
reload(ac)

folder = fileTools.currentBackFolder()
ac.openContainerFile(path = folder)








# my  OOP
from axionTools.rigging import core
reload(core)


stickLFT = core.Base()
stickLFT.createController('stick_ctrlShape')
stickLFT.setColor('white')
stickLFT.setName('stickLFT_ctrl')
string = str(stickLFT.name)
stickLFT.setColor('white')
stickLFT.setOverrideColor(16)









from axionTools.rigging import core
reload(core)


stickLFTa = core.Base()

stickLFTa.createController('stick_ctrlShape')
string = str(stickLFTa.name)
stickLFTa.name
stickLFTa.setName('stickLFT_ctrl')
stickLFTa.getRotation()


from axionTools.rigging.readWriteCtrlSizeData import writeCtrlData as wcd

wcd.flipCtrlShape(axis=[2, 2, 2])














############################## LOCAL Publish
from axionTools.rigging.util import misc as misc
reload(misc)

from nomanTools import aimCon  as ac
dir(ac)

from axionTools.pipeline import fileTools as fileTools
reload (fileTools)






def runLocalPublish():

	fileTools.deleteDisplayLayer()

	ac.impRem()

	fileTools.moveToParent()

	fileTools.doDeleteGrp()

	fileTools.savingAsset(mode = 'local')




def runGlobalPublish():
	ac.impRem()

	fileTools.doHideGrp('Root',0)

	fileTools.deleteDisplayLayer()

	fileTools.moveToParent()

	fileTools.doDeleteGrp()

	fileTools.savingAsset(mode = 'global')



'''
runGlobalPublish()
runLocalPublish()
'''






















# list compherehension
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

# find upstream
source = mc.ls(sl=True)

parS = mc.listConnections( '%s_parentConstraint1.target[0].targetParentMatrix' %source[0] )



from axionTools.rigging.util import misc as misc
reload(misc)

from axionTools.pipeline import fileTools as fileTools
reload (fileTools)
fileTools.publishAsset(mode = 'local')

############################### create enum
selected = mc.ls(sl=True)
mc.addAttr( selected, longName = "localSwitch", at = 'enum', keyable=True , en = "world:neck:chest:cog")



############################### LOCAL Publish


# hero
# find asset path
from axionTools.pipeline import fileTools as fileTools
reload(fileTools)
from axionTools.rigging.util import misc as misc
reload(misc)

path = fileTools.whereAreMe()

clean_path = os.path.normpath(path)
spPath = clean_path.split("\\")
reElem = "\\"+spPath[-2]+"\\"+spPath[-1]
dataPath = 	clean_path.replace(reElem,'')
PUBLISH_LIBRARY_PATH = dataPath + "\\"


pathSplit = fileTools.splitName(path,splitwith = '/' )

fileRaw = fileTools.splitName(pathSplit[-1],splitwith = '.' )

filename = fileRaw[0] + '.' + fileRaw[1]+ '.' + fileRaw[2]
DEPARTMANE = pathSplit[-2] + '\\'
LOCAL_PATH = 'hero\\'
fullPath = PUBLISH_LIBRARY_PATH  + LOCAL_PATH + filename
print fullPath



misc.countNode('joint')

# publush
mc.file( rename = fullPath )
mc.file( save = True, type = 'mayaAscii' )






############################## GLOBAL Publish
from axionTools.rigging.util import misc as misc
reload(misc)
from nomanTools import aimCon  as ac
dir(ac)

from axionTools.pipeline import fileTools as fileTools
reload (fileTools)




fileTools.deleteDisplayLayer()
fileTools.doDeleteGrp()
fileTools.doHideGrp('Root',0)




# find asset path
path=fileTools.whereAreMe()

pathSplit = fileTools.splitName(path,splitwith = '/' )

filename = fileTools.splitName(pathSplit[-1],splitwith = '.' )


clean_path = os.path.normpath(path)
spPath = clean_path.split("\\")
reElem = "\\"+spPath[-2]+"\\"+spPath[-1]
dataPath = 	clean_path.replace(reElem,'')
PUBLISH_LIBRARY_PATH = dataPath + "\\"


# find asset name

filename = fileTools.splitName(pathSplit[-1],splitwith = '.' )
filename = filename[0] + '.' + filename[1] + '.hero'

fullPath = PUBLISH_LIBRARY_PATH + filename

misc.countNode('joint')
# publush
mc.file( rename = fullPath )
mc.file( save = True, type = 'mayaAscii' )













######################## find option for create version name

from axionTools.pipeline import fileTools as fileTools
reload(fileTools)

path = fileTools.whereAreMe()

pathSplit = fileTools.splitName(path,splitwith = '/' )

filename = fileTools.splitName(pathSplit[-1],splitwith = '.' )


assetName = []
department = []
step = []
version = []
ext = []

assetName = filename[0]
department = filename[1]
step = filename[2]
version = filename[3]
ext = filename[4]


fullPath = pathSplit[0] + '/' + pathSplit[1] + '/'+ pathSplit[2] + '/'+ pathSplit[3] + '/'+ pathSplit[4] + '/'+ pathSplit[5] + '/'+ pathSplit[6] + '/'+ pathSplit[7] + '/'+ pathSplit[8]
fileName = assetName +'.'+ department +'.'+ step +'.'+ version +'.'+ version +'.ma'

mc.file( rename='fred.ma' )
mc.file( save=True, type='mayaAscii' )


import re

match_object = re.search("(v[0-9]*)", fileName)
versionn =match_object.group(0)








######################## find option for create version name
reload(misc)
misc.parentCon()

from axionTools.pipeline import fileTools as fileTools
reload(fileTools)

path = fileTools.whereAreMe()

pathSplit = fileTools.splitName(path,splitwith = '/' )

filename = fileTools.splitName(pathSplit[-1],splitwith = '.' )

assetName = []
department = []
step = []
version = []
ext = []

assetName = filename[0]
department = filename[1]
step = filename[2]
version = filename[3]
ext = filename[4]


fullPath = pathSplit[0] + '/' + pathSplit[1] + '/'+ pathSplit[2] + '/'+ pathSplit[3] + '/'+ pathSplit[4] + '/'+ pathSplit[5] + '/'+ pathSplit[6] + '/'+ pathSplit[7] + '/'+ pathSplit[8]+'/'
version = 'v007'
fileName = assetName +'.'+ department +'.'+ step +'.'+ version +'.ma'


allPath = fullPath + fileName





mc.file( rename = allPath )
mc.file( save = True, type = 'mayaAscii' )








# add attr dropdownlist











