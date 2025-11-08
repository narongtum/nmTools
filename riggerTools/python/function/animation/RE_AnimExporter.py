#     __________________
# - -/__ Update __/- - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 
# Regulus Animation Exporter
#
#
# Add bake specific ply for switch visibility

# import sys
# sys.path.append(r'D:\True_Axion\Tools\mayaTools\python')

'''
#... Direct run
from function.animation import RegulusAnimExporter
importlib.reload(RegulusAnimExporter)
run = RegulusAnimExporter.Ui()
run.createGUI()

'''

import pymel.core as pm
import maya.mel as mel
import maya.cmds as mc
import os
import errno

from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline import fileTools as fileTools 
reload(fileTools)

from function.pipeline import data_dict as data
reload(data)

# import socket
# localMachine = socket.gethostname()

from function.pipeline import logger 
reload(logger)

from function.rigging.autoRig.base import core
reload(core)

PROJECT_NAME = 'JumboJump Animation Exporter'
version = '1.2.1'

# 1. group 'geo_grp' collect all of the skin
# 2. except than that if have '*_ply' bake the key

FACIAL_BSH = ['facial_bsh','face_bsh']
EXPORT_GRP = 'Export_grp'
MODEL_GRP = 'Model_grp'
FACIALOFFSET_JNT = 'facialOffset_jnt'
FACIALOFFSET_ATTR = 'sx'
POLY_TO_BAKE_SUFFIX = '_ply'
GRP_TO_BAKE_SUFFIX = '_grp'
RIG_GRP = 'rig_grp'
REFERENCE_FIELD_NAME = "opMenuHairSys"
ROOT_WEAPON = 'root_weapon'
ROOT = 'root'
BLENDSHAPE_PLY = 'Face'
EXPORTED_FBX = 'Export_Anim_FBX'
ROOT_CANDIDATES = ['root', 'Root', 'root_vfx', 'root_weapon', 'root_sword']
BAKE_EXT = ['*_bJnt','*_pJnt','*_rtJnt']
INCLUDE_JNT = ['skirt_jnt'] 
PREFIX = 'A_'

PREFIX_CHECK = 'prefixCheck'   # checkBox control name
PREFIX_FIELD = 'prefixField'   # textField control name
PREFIX_ROW   = 'prefixRow'     # rowLayout name

#... New constants for importing joint list from a file
IMPORT_JOINT_CHECK = 'importJointCheck'   # Checkbox control name
JOINT_FILE_FIELD   = 'jointFileField'     # TextField with button control name

class ExportLogger(logger.MayaLogger):
	LOGGER_NAME = PROJECT_NAME


def is_constrained(obj):
	constraints = mc.listConnections(obj, type='constraint', destination=True, source=False)
	return bool(constraints)


def get_joint_children_short_names(selected):

	if isinstance(selected, str):
		selected = [selected]

	all_short_names = []
	for jnt in selected:
		children = mc.listRelatives(jnt, allDescendents=True, type='joint', fullPath=False) or []
		all_short_names.extend(children)

	return all_short_names




	

def ensure_directory(filePath):
	"""
	Ensure the directory for the given file path exists. If not, create it.
	
	Args:
		filePath (str): The file path for which the directory should be ensured.
	
	Returns:
		str: The validated or created directory path.
	"""
	# Extract directory path
	directory = os.path.dirname(filePath)
	
	# Check if the directory exists
	if not os.path.exists(directory):
		try:
			os.makedirs(directory)
			ExportLogger.info('Created directory: %s' % directory)
		except OSError as exc:  # Guard against race condition
			if exc.errno != errno.EEXIST:
				ExportLogger.error('Error creating directory: %s' % exc)
				raise
	else:
		ExportLogger.info('Directory already exists: %s' % directory)

	return directory






	
def _check_case_with_namespace(namespace, name):
	"""
	Check if the given name exists in Maya, either as lowercase or capitalized,
	with or without a namespace.

	Args:
		namespace (str): The namespace of the object (if any).
		name (str): The object name to check.

	Returns:
		str or None: The existing name in the correct case, or None if not found.
	"""
	# Generate possible name variations
	name_lower = name.lower()
	name_capitalized = name.capitalize()
	
	# Check with namespace
	if namespace:
		full_lower = f"{namespace}:{name_lower}"
		full_capitalized = f"{namespace}:{name_capitalized}"

		if mc.objExists(full_lower):
			return full_lower
		elif mc.objExists(full_capitalized):
			return full_capitalized
	# Check without namespace
	else:
		if mc.objExists(name_lower):
			return name_lower
		elif mc.objExists(name_capitalized):
			return name_capitalized

	# If neither exists, return None
	return None



def unparent_group(group_name):
	#... Check if the group exists
	if not mc.objExists(group_name):
		print(f"Group '{group_name}' does not exist in the scene.")
		return

	#... Check if the group has a parent
	parent = mc.listRelatives(group_name, parent=True)
	if parent:
		#... Unparent the group to the world
		mc.parent(group_name, world=True)
		print(f"Group '{group_name}' was under '{parent[0]}'. It has been unparented to the world.")
	else:
		print(f"Group '{group_name}' is already under the world.")




class function:

	def get_scene_start_end_times(self,*args):
		"""
		Get the start and end times of the scene playback range.
		Returns:
			tuple: (start_time, end_time)
		"""
		start_time = mc.playbackOptions(query=True, minTime=True)
		end_time = mc.playbackOptions(query=True, maxTime=True)
		return start_time, end_time
	

	def setFirstJnt(self,*args):
		"""
		Bake animation for visibility, joints, and blendshapes over a specified time range.
		"""
		
		rawSelection = mc.ls(sl=True)
		if len(rawSelection) == 0:
			mc.textFieldButtonGrp("btnFirstJnt",e=True, tx="")
			mc.error("Please select the first joint of the chain.")
		else:
			firstJnt = mc.ls(sl=True, type = 'joint')
			if len(firstJnt) == 0:
				mc.error("You have to select the root joint fo the chain.")
			else:
				mc.textFieldButtonGrp("btnFirstJnt", e=True, tx=firstJnt[0])


	def getTimeLine(self,*args):
		#... TimeLine Query 
		startTime = mc.playbackOptions( min = True,q = True )
		endTime = mc.playbackOptions( max = True,q = True )

		mc.textField('startTexFld', edit = True, tx = startTime)
		mc.textField('endTexFld',edit = True, tx = endTime)
		return (startTime, endTime) 


	def setTimeLine(self,*args):
		#... Set The Query Time
		getStartTime = mc.textField('startTexFld', tx = True, q = True)
		getEndTime = mc.textField('endTexFld', tx = True, q = True)

		try:
			getStartTime = float(getStartTime)
			getEndTime = float(getEndTime)
		except:
			mc.error('Invalid literal data type for float.')
				
		# print(	"{0}{1}".format('Data type is: ',type(startTime))	)
		ExportLogger.debug("{0}{1}".format('Data type is: ',type(getStartTime)))



		mc.playbackOptions(min = getStartTime,max = getEndTime)
		

	def importRef(self,*args):

		selected_value = mc.optionMenu(REFERENCE_FIELD_NAME , query=True, value=True)
		print(f"Selected Reference: {selected_value}")
		allrefs = pm.getReferences(recursive = True )
		try:
			allrefs[selected_value].importContents( removeNamespace = True )
		except RuntimeError:
				print (f"\nCan't Import ...{selected_value}")
				pass
		print (f'\nImport and clear namespace ...{selected_value}')

		# self.update_name_field(resetName = True)


	def bakeAnim(self, *args):
		"""
		Bake animation for visibility, joints, and blendshapes over a specified time range.
		If 'Import Joint Name' is checked, it overrides the default joint finding logic.
		"""
		try:
			#... Freeze screen updates and disable undo queue
			mc.refresh(suspend=True)

			#... Get start and end time from UI
			start_time = float(mc.textField('startTexFld', q=True, tx=True))
			end_time = float(mc.textField('endTexFld', q=True, tx=True))
			bake_range = (start_time, end_time)

			#... Get state of the new joint import checkbox
			use_file_joints = mc.checkBox(IMPORT_JOINT_CHECK, q=True, v=True)
			bake_joints = []

			
			if use_file_joints:
				ExportLogger.info("Using imported joint list for baking. Bypassing default joint search.")
				joint_file_path = mc.textFieldButtonGrp(JOINT_FILE_FIELD, q=True, tx=True)
				
				if not joint_file_path:
					mc.error("Joint list file path is empty. Please browse and select the file.")
					return # Exit bake if path is missing
					
				#... Use the new helper function from core to get the joint list
				#... core.read_joint_list_from_file must be implemented in core.py
				bake_joints = core.read_joint_list_from_file(joint_file_path)
				
				if not bake_joints:
					mc.error("Joint list import failed or file is empty/invalid. Baking terminated.")
					return # Exit bake if list is empty or invalid
				
				#... Note: The tool assumes all joints in the imported list are the only ones needed.
				#... It overrides the logic below.

			else:
				ExportLogger.info("Using default joint finding mechanism for baking.")
				
				#... if root weapon in scene (Existing Logic)
				if mc.objExists(ROOT_WEAPON):
					#... list polygon from root weapon (Existing Logic)
					descendants = mc.listRelatives(ROOT_WEAPON, allDescendents=True, fullPath=False)

					if descendants is None:
						ExportLogger.debug('There are no polygon under weapon joint.')		
					else:
						for each in descendants:
							if POLY_TO_BAKE_SUFFIX in each:
								#... delete mesh under weapon joint (Existing Logic)
								if mc.nodeType(each) == 'transform':
									ExportLogger.debug(f'{each} maybe a polygon.')
									mc.delete(each)
							else:
								ExportLogger.debug(f'There are {each} mesh under weapon joint.')
				
				#... Get root joints
				root_joints=[]
				for candidate in ROOT_CANDIDATES:
					if mc.objExists(candidate):
						ExportLogger.debug(f'There are root joint: {candidate}')
						mc.setAttr(f'{candidate}.v', 1)  #... Ensure root visibility
						root_joints.append(candidate)
				
				#... Append joints found by extension (the original BAKE_EXT logic)
				for each in BAKE_EXT:
					ExportLogger.debug(f'Searching for joints with pattern: {each}')
					bake_joints.extend(mc.ls(each))

				bake_joints.extend(root_joints)

				#... include specific joint (the original INCLUDE_JNT logic)
				for each in INCLUDE_JNT:
					if mc.objExists(each):
						ExportLogger.debug(f'Include joint has been found: {each}')
						bake_joints.append(each)
					else:
						ExportLogger.debug(f'No Include joint in scene.')
			
			
			#... If an imported list or a default search resulted in no joints, raise an error
			if not bake_joints:
				 mc.error("No joints found for baking. Check scene, naming, or imported file content.")
				 return


			#... (The rest of the function continues from here, applied to the populated 'bake_joints' list)

			#... Check for group baking option
			bake_grp = 'Mask' 
			if mc.objExists(f'{bake_grp}.bake') and mc.getAttr(f'{bake_grp}.bake'):
				ExportLogger.debug(f'Group "{bake_grp}" baking option enabled.')
				bake_joints.append(bake_grp)

			#... Bake attributes for joints
			bake_attrs = ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]
			#... Use the determined bake_joints list here
			mc.bakeResults(bake_joints, preserveOutsideKeys=True, simulation=True, t=bake_range, at=bake_attrs)

			
			#... Bake face expression joint (Existing Logic)
			if mc.objExists(FACIALOFFSET_JNT):
				ExportLogger.debug(f'There are Bake face expression joint')
				bake_attrs = FACIALOFFSET_ATTR
				mc.bakeResults(FACIALOFFSET_JNT, preserveOutsideKeys=True, simulation=True, t=bake_range, at=bake_attrs)
				

			#... Bake facial blendshapes (Existing Logic)
			for each in FACIAL_BSH:
				if mc.objExists(each):
					ExportLogger.debug(f'There are Bake facial blendshapes')
					ExportLogger.info(f'Baking {each} blendshape.')
					mc.bakeResults(each, preserveOutsideKeys=True, simulation=True, t=bake_range)
					

			#... if export_grp is inside rig_grp (Existing Logic)
			if mc.objExists(EXPORT_GRP):
				unparent_group(EXPORT_GRP)


			found_model_grp = _check_case_with_namespace(None,MODEL_GRP)
			print(found_model_grp)




			#... Clean up rig group if it exists (Existing Logic)
			if mc.objExists(RIG_GRP):
				ExportLogger.debug(f'There are debug336')
				ExportLogger.info(f'Delete Rig group: {RIG_GRP}')
				mc.delete(RIG_GRP)
			if mc.objExists(found_model_grp):
				ExportLogger.debug(f'There are debug339')
				ExportLogger.info(f'Delete Model group: {found_model_grp}')
				mc.delete(found_model_grp)


		except Exception as e:
			ExportLogger.error(f"Error during export: {e}")
		finally:
			#... Re-enable UI updates and undo queue
			mc.refresh(suspend=False)
			ExportLogger.debug("Screen updates and undo queue re-enabled.")
			




		#... END ANIM BAKE ------






	def noWeapon(self,*args):

		if mc.objExists( 'root_weapon' ):
			mc.parent( 'root_weapon', w = True )
		elif mc.objExists( 'root_sword' ):
			mc.parent( 'root_sword', w = True )



	def getPath(self,*args):
		# Get path
		path = fileTools.findCurrentPath()
		path = path.replace('\\','/')
		return path


	def _list_and_select(self, export_anim):
		if mc.objExists(export_anim):
			unparent_group(export_anim)
			mc.select(export_anim, replace=True)
		elif mc.objExists('root'):
			mc.select('root', replace=True)
		else:
			mc.error("No 'Export_grp' or 'root' found in the scene. Please use Manual Option.")
			return False


	def _execute_export(self, export_path, file_name, clip_name ):

		ensure_directory(filePath = export_path)

		#...Ensure export path ends with a '/'
		export_path = export_path.rstrip('/') + '/'
		full_export_path = f'{export_path}{file_name}.fbx'


		#... Get FBX Clip Name and Export Range
		# clip_name = mc.textFieldButtonGrp('animClip', q=True, tx=True)
		# clip_name = mc.textFieldButtonGrp('nameField', q=True, tx=True)

		print(f'This is file_name: {file_name}')

		start_time = float(mc.textField('startTexFld', q=True, tx=True))
		end_time = float(mc.textField('endTexFld', q=True, tx=True))

		if not clip_name or start_time >= end_time:
			mc.error("Invalid animation clip name or time range.")
			return False

		#... MEL commands to manage FBX takes
		mel.eval('FBXExportSplitAnimationIntoTakes -c')
		mel.eval('FBXExportDeleteOriginalTakeOnSplitAnimation -v true')
		mel.eval(f'FBXExportSplitAnimationIntoTakes -v "{clip_name}" {start_time} {end_time}')

		if mc.objExists(EXPORT_GRP):
			mc.select(EXPORT_GRP, add=True)
			

		#... Export FBX Command 
		export_command = f'file -force -options "v=0;" -typ "FBX export" -pr -es "{full_export_path}"'
		ExportLogger.debug(f"Executing export command: {export_command}")
		mel.eval(export_command)

		print(f'>>> FBX successfully exported: {full_export_path}')
		ExportLogger.debug(f'FBX Export Complete: {full_export_path}')



	def exportFBX(self, *args):
		"""
		Export the FBX file based on user inputs and scene objects.
		"""
		ExportLogger.debug('Proceeding to export FBX file...')

		
		
		#...Get Path and File Name from Fields ---
		export_path = mc.textFieldButtonGrp('pathField', q=True, tx=True).replace('\\', '/')
		# export_path = mc.textField('pathField', q=True, tx=True).replace('\\', '/')

		
		#... check file path exists or not
		ensure_directory(filePath = export_path)
		# mc.error(export_path)

		file_name = mc.textField('nameField', q=True, tx=True)

		if not export_path or not file_name:
			ExportLogger.error("Export path or file name cannot be empty.")
			return False

		#...Ensure export path ends with a '/'
		export_path = export_path.rstrip('/') + '/'


		# ------------------------------------------------------------------
		# Prefix Handling
		# ------------------------------------------------------------------

		use_prefix = False
		prefix_text = ""

		if mc.checkBox(PREFIX_CHECK, exists=True):
			use_prefix = mc.checkBox(PREFIX_CHECK, q=True, v=True)

		if use_prefix and mc.textField(PREFIX_FIELD, exists=True):
			prefix_text = mc.textField(PREFIX_FIELD, q=True, tx=True).strip()

		if use_prefix and prefix_text:
			file_name = f"{prefix_text}{file_name}"
			ExportLogger.info(f"Using prefix: {prefix_text}")

		# ------------------------------------------------------------------
		# End Handling
		# ------------------------------------------------------------------



		full_export_path = f'{export_path}{file_name}.fbx'
		ExportLogger.debug(f"Export path: {full_export_path}")




		


		#... Determine Export Group or Root ---
		export_anim = _check_case_with_namespace(None, EXPORT_GRP)  #... Check for export group

		#... define clip_name here
		# clip_name = mc.textFieldButtonGrp('animClip', q=True, tx=True)

		#... Start select for export
		if mc.checkBox('bakeCutscene', query=True, value=True):
			
			if mc.objExists(ROOT_WEAPON):
				ExportLogger.debug('Having weapon: 110')
				if mc.objExists(ROOT):
					ExportLogger.debug('Having Weapon and Char root, Found Both Proceeding Cutscene Export: 210')
					#... select only 'weapon_root' and 'export_grp'

					mc.select(ROOT_WEAPON, r=True)
					#... selected export_grp
					# mc.select(export_anim, add=True)
					# name_weapon = file_name + '_Weapon'

					# # # # # # 
					#... Get weapon name
					# # # # # # 

					name_weapon = mc.textField("weaponField", q=True, tx=True)

					if name_weapon == file_name:
						mc.error('Character and Weapon could not the same file name.')
						return False
					elif name_weapon == '':
						mc.error('Weapon Field can not be empty.')
						return False


					self._execute_export(export_path, name_weapon, name_weapon)
					mc.delete(ROOT_WEAPON)

					mc.select(export_anim, r=True)


					# # # # # # 
					#... Get Character name
					# # # # # #

					self._execute_export(export_path, file_name, file_name)
					
					#... Clean up
					#... Open Export Location 
					fileTools.openContainerFile(path=export_path)

					#...Deselect 
					mc.select(deselect=True)
					if _check_case_with_namespace(None, EXPORT_GRP):
						mc.delete(EXPORT_GRP)

					#... Refresh reference after bake animation
					self.referenceInScene()
					print ('# # # %s Export Complete # # #' %PROJECT_NAME)

					return True


				else:
					ExportLogger.debug(f'Bake cutscene checked {ROOT_WEAPON} found but {ROOT} not found Proceeding Normal Export: 220')
					pass
			else:
				ExportLogger.debug(f'Bake cutscene checked but {ROOT_WEAPON} not found Proceeding Normal Export: 120')
				pass


		else:
			ExportLogger.debug("There are no bake cutscene checked.")
			# self._list_and_select(export_anim)

			#... End select for export

		#... Set Timeline 
		self.setTimeLine()


		self._list_and_select(export_anim)
		# mc.error(export_anim)

		#... Shift this to method
		self._execute_export(export_path, file_name, file_name)


		#... Clean up
		#... Open Export Location 
		fileTools.openContainerFile(path=export_path)

		#... Clean Up and Deselect 
		mc.select(deselect=True)
		if _check_case_with_namespace(None, EXPORT_GRP):
			mc.delete(EXPORT_GRP)

		#... Refresh reference after bake animation
		self.referenceInScene()
		print ('# # # %s Export Complete # # #' %PROJECT_NAME)


	def print_A(self,*args ):
		print('this is function A')

	def print_B(self,*args):
		print('this is function B')

	def exportSelectionFBX(self,*args):
		#... get path from field
		path = mc.textFieldButtonGrp('pathField', q=True, tx=True).replace('\\', '/')

		path_folder = path.rstrip('/') + '/'
		ensure_directory(filePath = path_folder)
		print(path_folder)
		# mc.error('BREAK')
		# path = mc.textField( 'pathField', tx = True, q = True)

		# get current
		# path = self.getPath()

		#... get file name from field
		fileName = mc.textField( 'nameField', tx = True, q = True)
		path = path + '\\'

		#... Set time length
		ExportLogger.debug('Set the time length: {0}'.format(path))
		setTime = function()
		setTime.setTimeLine()


		clipName = mc.textField('nameField', q=True, tx=True)
		# clipName = mc.textFieldButtonGrp('nameField', q=True, tx=True)
		#... reset Take001 to file name
		# clipName = mc.textFieldButtonGrp( 'animClip', tx = True, q = True )
		start_time = mc.textField( 'startTexFld', tx = True, q = True )
		end_time = mc.textField( 'endTexFld', tx = True, q = True )
		
		cleanUpExporterCommand = 'FBXExportSplitAnimationIntoTakes -c'
		clearExporterCommand = 'FBXExportDeleteOriginalTakeOnSplitAnimation -v true'
		createExportClipCommand = ' FBXExportSplitAnimationIntoTakes -v "{0}" {1} {2}'.format( clipName, start_time, end_time ) 
		bake_range = (start_time, end_time)

		# selected = mc.ls(sl=True, type='joint')[0] #... no need to be joint

		selected = None

		try:
			selected = mc.ls(sl=True)[0]
		except:
			mc.error('Please select root joint first.')


		# if not selected:
		# 	mc.error("Please select root joint.")
		
		if mc.checkBox(IMPORT_JOINT_CHECK, q=True, value=True):
			ExportLogger.info('Disable bake joint.')
		else:
			ExportLogger.info('Enable bake joint.')
			#... if you want to cancle bake anim again just disable these line

			#... Disable selected bake below START
			mc.setAttr(f'{selected}.visibility', 1)
			bake_joints = get_joint_children_short_names(selected)

			if is_constrained(selected):
				ExportLogger.info(f"{selected} is constrained, adding to bake list.")
				bake_joints.append(selected)

			#... Bake attributes for joints
			bake_attrs = ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]
			mc.bakeResults(bake_joints, preserveOutsideKeys=True, simulation=True, t=bake_range, at=bake_attrs)

			if mc.objExists(RIG_GRP):
				mc.delete(RIG_GRP)
			#... Disable selected bake below END


		mel.eval( cleanUpExporterCommand )
		mel.eval( clearExporterCommand )
		mel.eval( createExportClipCommand )

		#... Export obj
		exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '
		path = path.replace('\\','/')
		# ExportLogger.info('This path result%s ' %path)

		exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
		exportCommand += exportFBXPath

		ExportLogger.info('This Export result: %s' %exportCommand)
		#... Exec
		mel.eval( exportCommand )
		print ('>>> %s has been export.'%fileName)
		ExportLogger.debug('This is export command: {0}'.format(exportCommand))
		fileTools.openContainerFile( path = path )
		# Deselect
		mc.select(deselect = True)

		print ('# # # %s Selected Export Complete # # #' %PROJECT_NAME)

	def referenceInScene(self,*args):
		"""
		Query all references in the scene and populate the option menu.
		"""
		# Clear existing items in the option menu
		
		if mc.optionMenu(REFERENCE_FIELD_NAME, exists=True):
			items = mc.optionMenu(REFERENCE_FIELD_NAME, query=True, itemListLong=True)
			if items:
				for item in items:
					mc.deleteUI(item)

		#... Query all namespaces in the scene
		all_refs = pm.getReferences(recursive=True)
		
		#... Add reference namespaces or names to the dropdown
		for ref in all_refs.values():
			ref_name = ref.namespace or ref.refNode
			mc.menuItem(parent=REFERENCE_FIELD_NAME, label=ref_name)

		
		


	def refreshReferences(self, *args):
		"""
		Refresh the reference list in the option menu.
		"""
		self.referenceInScene()
		# namespace = self.update_name_field(resetName=False)
		#... get namespace
		namespace = mc.optionMenu(REFERENCE_FIELD_NAME , query=True, value=True)
		ExportLogger.info(f'Namespace is: {namespace}')
		model_grp = _check_case_with_namespace(namespace,MODEL_GRP)
		ExportLogger.info(f'Namespace is: {namespace}:{model_grp}')

		if model_grp != None:
			mc.select(model_grp, r=True)
		else:
			mc.error(f"The selected reference '{namespace}' is not valid for export. Please consult the Rigging gang for assistance.")


		# print(f"Reference name {selected_value} refresh.")

		# selected_value = mc.optionMenu("opMenuHairSys", query=True, value=True)
		# mc.textField( 'nameField', fileName = selected_value )


	def return_selected_reference(self, *args):
		selected_value = mc.optionMenu(REFERENCE_FIELD_NAME , query=True, value=True)
		print(f"Selected Reference: {selected_value}")
		return selected_value




	#... Update 'Name' in UI textfield
	#... Update 'Clip Name' in UI textfield
	def update_name_field(self, resetName = False):
		namespace = mc.optionMenu(REFERENCE_FIELD_NAME , query=True, value=True)
		ExportLogger.debug(f'This is selected reference: {namespace}')
		file_name = mc.textField('nameField', q=True, tx=True)
		clip_name = mc.textFieldButtonGrp('animClip', q=True, tx=True)

		if resetName == True:
			
			if namespace != file_name:
				ExportLogger.debug(f'This is selected reference: {namespace}')
				ExportLogger.debug(f'This is file_name: {file_name}')
				pass
			else:
				mc.textField('nameField', edit=True, text=namespace)
				mc.textFieldButtonGrp('animClip', edit=True, text=namespace)
				return namespace

		elif resetName == False:	#... if user fill name and clip name in text field then ignore
			ExportLogger.debug(f'Using custome nameField: {namespace}')
			mc.textField('nameField', edit=True, text=file_name)
			mc.textFieldButtonGrp('animClip', edit=True, text=clip_name)		
			return namespace



	#... (not use)	
	#... Update 'Name' in UI textfield
	#... Update 'Clip Name' in UI textfield
	def update_name_field_resetName_button(self, *args):
		selected_value = mc.optionMenu(REFERENCE_FIELD_NAME , query=True, value=True)
		file_name = mc.textField('nameField', q=True, tx=True)
		clip_name = mc.textFieldButtonGrp('animClip', q=True, tx=True)
		#... if user fill name and clip name in text field then ignore reset name
		if selected_value != file_name:
			ExportLogger.debug(f'This is selected reference: {selected_value}')
			ExportLogger.debug(f'This is file_name: {file_name}')
			return None
		else:
			mc.textField('nameField', edit=True, text=selected_value)
			mc.textFieldButtonGrp('animClip', edit=True, text=selected_value)
			return selected_value


	def refreshUI(self, *args):
			"""
			Query scene time and paths to refresh all primary UI fields.
			"""
			#... Get time and update fields
			self.getTimeLine()
			
			#... Get current path and update field
			path_raw = fileTools.findCurrentPath() + f'{EXPORTED_FBX}\\'
			path = os.path.normpath(path_raw).replace('\\', '/')
			mc.textFieldButtonGrp('pathField', edit=True, text=path)

			#... Get scene name and update field
			scene_anim = fileTools.Scene()
			scene_anim.get_scene_name()
			name = scene_anim.sceneNameShort_noExt
			mc.textField('nameField', edit=True, text=name)

			ExportLogger.info("UI fields have been refreshed to current scene values.")


class Ui:
	def __init__(self):
		self.function = function()
		self.winWidth = 300

		# Define constants for widget names
		self.window_name = "pbWin"
		self.path_field = "pathField"
		self.name_field = "nameField"
		self.weapon_label = "Weapon"
		self.weapon_field = "weaponField"
		self.animClip_field = "animClip"
		self.start_field = "startTexFld"
		self.end_field = "endTexFld"
		self.ref_menu = "opMenuHairSys"

		# Prefix UI names (use the module-level constants)
		self.prefix_check = PREFIX_CHECK
		self.prefix_field = PREFIX_FIELD

		#... New Joint Import UI Constants
		self.import_joint_check = IMPORT_JOINT_CHECK
		self.joint_file_field = JOINT_FILE_FIELD

	def toggle_weapon_field(self, *args):
		"""Toggle the visibility of the Weapon text field."""
		is_checked = mc.checkBox('bakeCutscene', q=True, value=True)
		mc.text(self.weapon_label, e=True, visible=is_checked)
		# mc.text(l='Weapon', e=True, visible=is_checked)
		mc.textField(self.weapon_field, e=True, visible=is_checked)
		if is_checked:
			ExportLogger.debug('Weapon field is now visible.')
		else:
			ExportLogger.debug('Weapon field is now hidden.')

	def toggle_prefix_field(self, *args):
		# Enable/disable prefix text field when checkbox changes
		try:
			val = mc.checkBox(self.prefix_check, q=True, v=True)
		except:
			val = False
		if mc.control(self.prefix_field, exists=True):
			mc.textField(self.prefix_field, e=True, en=val)

	#... New method to toggle the joint file text field
	def toggle_joint_file_field(self, *args):
		"""Toggle the enabled state of the joint file text field and button."""
		is_checked = mc.checkBox(self.import_joint_check, q=True, value=True)
		if mc.textFieldButtonGrp(self.joint_file_field, exists=True):
			#... Enable or disable the control based on checkbox state
			mc.textFieldButtonGrp(self.joint_file_field, e=True, enable=is_checked, buttonCommand=self._browse_joint_file)
			
	#... New method to handle browsing for the joint list file
	def _browse_joint_file(self, *args):
		"""Callback to open a file dialog and update the joint file Path text field."""
		try:
			#... Open file dialog for a .txt file
			file_path = mc.fileDialog2(
				fileMode=1, # 1 for single file selection
				caption="Select Joint List (.txt) File",
				fileFilter="Text Files (*.txt);;All Files (*.*)",
				dialogStyle=2,
				okCaption="Select"
			)
			if file_path:
				mc.textFieldButtonGrp(self.joint_file_field, edit=True, text=file_path[0])
		except (IndexError, TypeError):
			ExportLogger.info("User canceled the joint file browse operation.")





	def build_prefix_row(self):
		# Call this while the intended parent layout is set
		if mc.rowLayout(PREFIX_ROW, exists=True):
			mc.deleteUI(PREFIX_ROW)
		mc.rowLayout(PREFIX_ROW, numberOfColumns=2, adjustableColumn=2)
		mc.checkBox(self.prefix_check, l='Prefix', v=False, cc=self.toggle_prefix_field)  # unchecked by default
		mc.textField(self.prefix_field, tx='A_', en=False, w=120)  # disabled by default
		mc.setParent('..')			



	def _delete_existing_window(self):
		"""Delete existing UI window if it exists."""
		if mc.window(self.window_name, exists=True):
			mc.deleteUI(self.window_name)

	def _get_initial_values(self):
		"""Retrieve and return path, name, start time, and end time."""
		scene_anim = fileTools.Scene()
		scene_anim.get_scene_name()

		#... get scene name
		name = scene_anim.sceneNameShort_noExt

		#... get path name
		# path = os.path.normpath(fileTools.findCurrentPath()).replace('\\', '/')
		path_raw = fileTools.findCurrentPath() + f'{EXPORTED_FBX}\\'
		path = os.path.normpath(path_raw).replace('\\', '/')

		start_time, end_time = self.function.get_scene_start_end_times()

		return path, name, start_time, end_time

	def _add_label_and_textfield(self, label, field_name, value, height=25):
		"""Create a label and a text field in a row."""
		mc.text(label=label, h=height)
		mc.textField(field_name, fi=value, h=height)

	def _add_texfield_button(self, path):
		mc.textFieldButtonGrp (	self.path_field, 
								cw = [(1, 40), (2, 370), (3, 40)], 
								label="Path ",fi = path, 
								buttonLabel = "Browse", 
								buttonCommand=self._browse_dir)

	def _browse_dir(self, *args):
		"""Callback to open a file dialog and update the Path text field."""
		try:
			current_file = mc.file(query=True, sceneName=True)
			initial_dir = os.path.dirname(current_file) if current_file else os.path.expanduser("~")
			#... Open file dialog
			# file_name_dir = mc.fileDialog2(dialogStyle=2, fileMode=3, okCaption="Select")[0]
			file_name_dir = mc.fileDialog2(dialogStyle=2, fileMode=3, okCaption="Select", startingDirectory=initial_dir)[0]
			#... Update the text field with the selected path
			mc.textFieldButtonGrp(self.path_field, edit=True, text=file_name_dir)
		except (IndexError, TypeError):
			#... Handle case where user cancels the dialog
			ExportLogger.info("User canceled the browse operation.")




	def _create_timeline_section(self, start_time, end_time):
		"""Create the timeline input section with Start and End in the same row."""
		mc.rowColumnLayout(numberOfColumns=4, 
						   columnWidth=[(1, 50), (2, 100), (3, 50), (4, 100)],
						   columnSpacing=[(2, 10), (4, 10)])
		
		#... Start Label and Field
		mc.text(label="Start:", h=20)
		mc.textField(self.start_field, tx=start_time, h=20)
		
		#... End Label and Field
		mc.text(label="End:", h=20)
		mc.textField(self.end_field, tx=end_time, h=20)

		mc.setParent("..")  # Exit rowColumnLayout
		
		#... Buttons in a separate row
		mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 150), (2, 150)])
		mc.button(label="GetTime", command=self.function.getTimeLine, h=30)
		mc.button(label="SetTime", command=self.function.setTimeLine, h=30)

		mc.setParent("..")  # Exit rowColumnLayout
		mc.separator(h=30, style='out')

	def _create_reference_menu(self):
		"""Create the reference dropdown menu and refresh button."""
		mc.text(h=20, l="Assign to an existing Reference:")
		
		#... Create the optionMenu with a changeCommand callback
		mc.optionMenu(self.ref_menu, label="References", width=self.winWidth, 
					  changeCommand=self._on_reference_selected)
		
		#... Add a refresh button
		mc.button(label="Refresh", command=self.function.refreshReferences)

		#... Populate initial references
		self.function.referenceInScene()
			

	def _on_reference_selected(self, selected_item):
		"""
		Callback for when a reference is selected in the dropdown menu.
		
		Args:
			selected_item (str): The selected item's label.
		"""
		print(f"Selected reference: {selected_item}")

		
		ExportLogger.info(f'Namespace is: {selected_item}')
		model_grp = _check_case_with_namespace(selected_item, MODEL_GRP)
		rig_grp = _check_case_with_namespace(selected_item, RIG_GRP)

		try:

			#... if 'model_grp' not found find 'rig_grp' instead
			if model_grp != None:
				ExportLogger.info(f'Namespace is: {model_grp}')
				if mc.objExists(model_grp):
					mc.select(model_grp, r=True) #... selected for make hi-light in scene

			elif mc.objExists(rig_grp):		
				mc.select(rig_grp, r=True) #... selected for make hi-light in scene
			else:
				mc.error(f'This reference {selected_item} is not proper for export. Please consult Dadode')
				# rig_grp = _check_case_with_namespace(selected_item, RIG_GRP)
				# if mc.objExists(rig_grp):
				# 	mc.select(rig_grp, r=True) #... selected for make hi-light in scene
		except Exception as e:
			ExportLogger.error(f"Error during export: {e}\nThis reference {selected_item} is not proper for export. Please consult Dadode")



	def createGUI(self, *args):
			"""Main function to build the Maya UI."""
			#... Delete old window
			self._delete_existing_window()

			#... Get initial values
			path, name, start_time, end_time = self._get_initial_values()

			#... Create window
			mc.window(
			self.window_name,
			title=f"{PROJECT_NAME} {version}",
			widthHeight=(300, 300),
			sizeable=False,                  # prevent manual resizing
			resizeToFitChildren=True         # auto-fit to layout content
	)


			mc.frameLayout(label="Export Options", collapsable=False, mw=5, mh=5)
			mc.columnLayout(adjustableColumn=True)

			# ------------------------------------------------------------------
			# Timeline Section (with new Refresh Button)
			# ------------------------------------------------------------------
			mc.rowColumnLayout(numberOfColumns=5, 
							   columnWidth=[(1, 50), (2, 50), (3, 50), (4, 50), (5, 80)],
							   columnSpacing=[(2, 5), (4, 5)])
			
			#... Start Label and Field
			mc.text(label="Start:", h=20)
			mc.textField(self.start_field, tx=start_time, h=20)
			
			#... End Label and Field
			mc.text(label="End:", h=20)
			mc.textField(self.end_field, tx=end_time, h=20)

			#... Refresh Button added here
			mc.button(label="Refresh", command=self.function.refreshUI, h=20)

			mc.setParent("..")  # Exit rowColumnLayout
			
			#... Time Buttons in a separate row
			mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 150), (2, 150)])
			mc.button(label="GetTime", command=self.function.getTimeLine, h=30)
			mc.button(label="SetTime", command=self.function.setTimeLine, h=30)
			mc.setParent("..") 
			
			mc.separator(h=10, style='out')
			# ------------------------------------------------------------------


			#... Joint Import from File Section
			mc.columnLayout(adjustableColumn=True)
			mc.checkBox(self.import_joint_check, 
						label='Import joint name', 
						value=False,
						annotation="Check to import a list of joints for baking from an external file, overriding default joint finding.",
						onCommand=self.toggle_joint_file_field,
						offCommand=self.toggle_joint_file_field)
			mc.textFieldButtonGrp(	self.joint_file_field, 
									cw = [(1, 0), (2, 230), (3, 70)], 
									label="", 
									fi = "", 
									buttonLabel = "browse",
									enable = False,
									buttonCommand=self._browse_joint_file) 
									
			mc.setParent("..")
			mc.separator(h=10, style='out')
			# ------------------------------------------------------------------

			#... Bake Weapon for Cutscene Checkbox
			mc.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, self.winWidth)], columnAlign=(1, 'center'))
			mc.checkBox('bakeCutscene', label='Bake Weapon for Cutscene', value=False, 
						annotation="Enable this option for baking animations intended for cutscene exports.",
						onCommand=self.toggle_weapon_field, offCommand=self.toggle_weapon_field)
			mc.setParent("..")

			# Ensure the parent layout is the Export Options section
			self.build_prefix_row()


			#... Path to textfield button 
			self._add_texfield_button(path)

			#... Path and Name Section
			mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 60), (2, 400)])
			self._add_label_and_textfield("Name ", self.name_field, name)
			mc.setParent("..")


			#... Hidden Weapon Section
			mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 60), (2, 400)])
			mc.text(self.weapon_label, visible=False)
			mc.textField(self.weapon_field, tx="", visible=False)
			mc.setParent("..")


			#... Buttons
			mc.separator(h=20, style='in')
			mc.button(label="Remove Weapon Character", command=self.function.noWeapon, h=30) # <-- ย้ายปุ่มนี้ขึ้นมา

			mc.separator(h=20, style='in')
			
			#... Reference Menu
			self._create_reference_menu()
			
			mc.separator(h=20, style='in')

			#... Core Action Buttons (Import, Bake, Export)
			mc.button(label="Import Reference", command=self.function.importRef, h=50)
			mc.button(label="Bake Anim", command=self.function.bakeAnim, h=50)
			mc.button(label="Export Anim", command=self.function.exportFBX, h=50)

			# ------------------------------------------------------------------
			# Manual Export Section (MOVED TO BOTTOM)
			# ------------------------------------------------------------------
			mc.separator(h=15, style='out')
			mc.button(label="Manual Export Selection", command=self.function.exportSelectionFBX, h=30)
			mc.separator(h=15, style='out')
			# ------------------------------------------------------------------


			#... Show window
			mc.showWindow(self.window_name)

#... Manual run
# run = Ui()
# run.createGUI()


# from function.asset import RegulusAnimExporter
# reload(RegulusAnimExporter)

# run = RegulusAnimExporter.Ui()
# run.createGUI()