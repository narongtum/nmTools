'''
from function.rigging.skin import saveLoadCurveSkinweight as slk
reload (slk)

#... select curve first
slk.run_save_curve_skinweights()
slk.run_load_curve_skinweights()

'''
import os
import json
import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline import fileTools as fileTools 
reload(fileTools)

def save_curve_skinweights(curve_name, json_path):
	#... find name shape and skinCluster
	shape = mc.listRelatives(curve_name, shapes=True, fullPath=True)[0]
	history = mc.listHistory(shape)
	skin_clusters = [node for node in history if mc.nodeType(node) == "skinCluster"]
	if not skin_clusters:
		mc.warning(f"No skinCluster found on {curve_name}")
		return
	skin_cluster = skin_clusters[0]

	#... get joint that use as influence
	joints = mc.skinCluster(skin_cluster, query=True, influence=True)

	#... prepare data
	weight_data = {}
	cv_count = mc.getAttr(f"{shape}.spans") + mc.getAttr(f"{shape}.degree")

	for i in range(cv_count):
		cv_name = f"{shape}.cv[{i}]"
		values = mc.skinPercent(skin_cluster, cv_name, query=True, value=True)
		#... keep only joint more than 0
		joint_weights = {joints[j]: values[j] for j in range(len(joints)) if values[j] > 0.0}
		weight_data[f"cv[{i}]"] = joint_weights

	#... write as JSON
	with open(json_path, 'w') as f:
		json.dump(weight_data, f, indent=4)

	print(f"Skin weights saved to {json_path}")


def run_save_curve_skinweights():
	#... file state print
	fileTools.fileState()

	#... check selection
	sel = mc.ls(sl=True)
	if not sel:
		mc.warning("Please select a NURBS curve first.")
		return

	curve_name = sel[0]

	#... get data path and build sub-folder
	data_path = fileTools.returnDataFolderPath()
	skin_folder = os.path.join(data_path, 'skinData')

	#... create folder if not exist
	if not os.path.exists(skin_folder):
		os.makedirs(skin_folder)
		print(f"Created folder: {skin_folder}")

	#... full file path
	json_path = os.path.join(skin_folder, f"{curve_name}.json")

	#... save skin weight
	save_curve_skinweights(curve_name, json_path)


def load_curve_skinweights(curve_name, json_path):
	#... check exists JSON 
	if not os.path.exists(json_path):
		mc.warning(f"File not found: {json_path}")
		return

	#... find shape and skinCluster
	shape = mc.listRelatives(curve_name, shapes=True, fullPath=True)[0]
	history = mc.listHistory(shape)
	skin_clusters = [node for node in history if mc.nodeType(node) == "skinCluster"]
	if not skin_clusters:
		mc.warning(f"No skinCluster found on {curve_name}")
		return
	skin_cluster = skin_clusters[0]

	#... pull list name of joint influence
	joints = mc.skinCluster(skin_cluster, query=True, influence=True)

	#... load data from JSON
	with open(json_path, 'r') as f:
		weight_data = json.load(f)

	#... write skinweight back to CV
	for cv_label, joint_weights in weight_data.items():
		#... reconstruct ordinary name
		full_cv = f"{shape}.{cv_label}"
		#... prepair value and joint list in order
		value_list = []
		for joint in joints:
			value = joint_weights.get(joint, 0.0)
			value_list.append(value)
		#... apply skinweight
		mc.skinPercent(skin_cluster, full_cv, transformValue=list(zip(joints, value_list)))

	print(f"✅ Loaded skin weights to {curve_name} from {json_path}")




def run_load_curve_skinweights():
	#... file state print
	fileTools.fileState()

	#... check selection
	sel = mc.ls(sl=True)
	if not sel:
		mc.warning("Please select a NURBS curve first.")
		return False

	curve_name = sel[0]

	#... get data path and build sub-folder
	data_path = fileTools.returnDataFolderPath()
	skin_folder = os.path.join(data_path, 'skinData')

	#... create folder if not exist
	if not os.path.exists(skin_folder):
		print('Folder in Exists.')
		return False

	#... full file path
	json_path = os.path.join(skin_folder, f"{curve_name}.json")

	#... save skin weight
	load_curve_skinweights(curve_name, json_path)