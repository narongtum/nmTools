#.... select and export for regulus pipeline


import maya.cmds as mc

from function.asset import exportFBX
reload(exportFBX)

def _unparent(export_grp):
	#... Check if the object has a parent
	parent = mc.listRelatives(export_grp, parent=True)

	if parent is None:
		print(f"{export_grp} is already parented to the world.")
	else:
		print(f"{export_grp} is parented to {parent[0]}.")
		mc.parent(export_grp, w=True)

#... export Gameplay_Model
selection = ('model_grp', 'Export_grp')

mc.select(selection)




if mc.objExists('rig_grp.asset_name'):
	print('Having name.')
	asset_name = mc.getAttr('rig_grp.asset_name')
	weapon_name = mc.getAttr('rig_grp.weapon_name')
else:
	asset_name = mc.ls(sl=True)[0]

#... export for char + weapon
export_asset_name = f"{asset_name}_Gameplay_Model"

exportFBX.exportFBXnoConnection(selection, fileName = asset_name)



#... export for char only
mc.delete(weapon_name)
mc.delete('root_weapon')

#... export for char + weapon
export_asset_name = f"{asset_name}_Character_Model"

exportFBX.exportFBXnoConnection(selection, fileName = export_asset_name)