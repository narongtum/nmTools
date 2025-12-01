import maya.cmds as mc
import pymel.core as pm
import re

from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline import logger
reload(logger)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)

class PinPolyLogger(logger.MayaLogger):
	LOGGER_NAME = "pin_locator_polygon"




	

'''
from function.rigging.constraint import eh_pin_locator_polygon as plp
reload(plp)

plp.pin_locator_polygon(poly_mesh='spine01_L02_ply',
						vtx_list=[9,10],
						locator_scale=1.0,
						side='C',   #... Side argument restored as requested
						normalAxis='Z',
						tangentAxis='X')

'''







class PinPolyLogger(logger.MayaLogger):
	LOGGER_NAME = "pin_locator_polygon"

import maya.cmds as mc
import pymel.core as pm
from function.rigging.autoRig.base import core
from function.pipeline import logger

class PinPolyLogger(logger.MayaLogger):
	LOGGER_NAME = "pin_locator_polygon"

def pin_locator_polygon(poly_mesh='for_dup_hair',
						vtx_list=[49],
						locator_scale=1.0,
						side='C',
						normalAxis='Z',
						tangentAxis='X',
						createJoint=False):
	"""
	Pin locators to specific vertices using uvPin.
	Fixed: Works on Transformed Static Meshes without Freeze Transform.
	"""

	#... 1. Validate inputs
	if not mc.objExists(poly_mesh):
		PinPolyLogger.error(f'Polygon mesh "{poly_mesh}" does not exist. Terminating.')
		return None

	if isinstance(vtx_list, (int, str)):
		vtx_list = [vtx_list]

	#... 2. Analyze Naming
	try:
		name_info = core.check_name_style(poly_mesh)
		clean_base_name = name_info[0] 
		if not clean_base_name:
			 clean_base_name = name_info[0] if name_info[0] else poly_mesh.split('_')[0]
	except Exception as e:
		PinPolyLogger.warning(f"Could not analyze name style: {e}. Using raw mesh name.")
		clean_base_name = poly_mesh

	#... 3. Setup PyNodes
	try:
		oMesh = pm.PyNode(poly_mesh)
		oShape = oMesh.getShape()
		if not isinstance(oShape, pm.nodetypes.Mesh):
			PinPolyLogger.error(f'"{poly_mesh}" is not a valid Polygon Mesh. Terminating.')
			return None
	except Exception as e:
		PinPolyLogger.error(f'Failed to process PyNode: {e}. Terminating.')
		return None

	#... 4. Determine UV Set & History
	oShape_name = oShape.name()
	
	#... Get Current UV Set (Fixes the "Corner/Zero" bug)
	try:
		current_uv_set = mc.polyUVSet(poly_mesh, query=True, currentUVSet=True)[0]
	except:
		current_uv_set = 'map1'

	#... Check for Deformer History
	history_nodes = mc.listConnections(f'{oShape_name}.inMesh', source=True, destination=False)
	
	original_geometry_source = None # Default to None for Static Mesh
	use_orig_node = False

	if history_nodes:
		all_history = mc.listHistory(oShape_name, future=False, allConnections=True) or []
		orig_shapes = [n for n in all_history if mc.nodeType(n) in ['mesh', 'nurbsSurface'] and n.endswith('Orig')]
		if orig_shapes:
			original_geometry_source = orig_shapes[0]
			use_orig_node = True
			PinPolyLogger.info(f'Found Deformer History. Will use Orig Source: {original_geometry_source}.')
	
	if not use_orig_node:
		PinPolyLogger.info(f'Static Mesh detected. Will NOT connect originalGeometry to avoid Double Transform.')

	created_locators = []

	#... 5. Iterate
	for vtxNum in vtx_list:
		source_loc = f'{poly_mesh}.vtx[{vtxNum}]'
		
		if not mc.objExists(source_loc):
			continue

		#... Get World Position
		world_pos = mc.pointPosition(source_loc, world=True)

		loc_base_name = f'{clean_base_name}_vtx{vtxNum}'
		PinPolyLogger.info(f'Processing: {source_loc} -> {loc_base_name}')

		#... A. Find Closest UV
		oNode = pm.createNode('closestPointOnMesh', name=f'{loc_base_name}_closePInfo_tmp')
		oShape.worldMesh.connect(oNode.inMesh, force=True)
		oNode.inPosition.set(world_pos)

		uPos = oNode.parameterU.get()
		vPos = oNode.parameterV.get()
		pm.delete(oNode)

		#... B. Create PMA
		uv_pma = core.PlusMinusAverage(name=f'{loc_base_name}_UVslide_pma')
		uv_pma.attr('operation').value = 1 
		uv_pma.attr('input2D[0].input2Dx').value = uPos
		uv_pma.attr('input2D[0].input2Dy').value = vPos

		uv_pma.addAttribute(at='double2', ln='uvSlide', k=True)
		uv_pma.addAttribute(at='double', ln='uSlide', parent='uvSlide', k=True)
		uv_pma.addAttribute(at='double', ln='vSlide', parent='uvSlide', k=True)

		uv_pma.attr('uSlide') >> uv_pma.attr('input2D[1].input2Dx')
		uv_pma.attr('vSlide') >> uv_pma.attr('input2D[1].input2Dy')

		#... C. Create uvPin
		uvPin = pm.createNode('uvPin', name=f'{loc_base_name}_uvPin')
		
		#... Set UV Set Explicitly
		uvPin.uvSetName.set(current_uv_set)

		AXIS_TO_INDEX_DICT = {'X': 0, 'Y': 1, 'Z': 2, '-X': 3, '-Y': 4, '-Z': 5}
		uvPin.normalAxis.set(AXIS_TO_INDEX_DICT.get(normalAxis, 2))
		uvPin.tangentAxis.set(AXIS_TO_INDEX_DICT.get(tangentAxis, 0))

		#... CONNECT GEOMETRY
		#... 1. Deformed Geometry = World Mesh
		oShape.worldMesh.connect(uvPin.deformedGeometry, force=True) 
		
		uvpin_core = core.Dag(uvPin.name())
		
		#... 2. Original Geometry logic (The Fix)
		if use_orig_node:
			# Only connect Original Geometry if we have a Deformation Chain (Orig node)
			shapeOrig = core.Dag(original_geometry_source)
			if mc.nodeType(original_geometry_source) == 'nurbsSurface':
				 shapeOrig.attr('worldSpace[0]') >> uvpin_core.attr('originalGeometry')
			else:
				 shapeOrig.attr('outMesh') >> uvpin_core.attr('originalGeometry')
		else:
			# [CRITICAL FIX] For Static Mesh: DO NOT connect originalGeometry.
			# Let uvPin calculate purely based on deformedGeometry (World Mesh).
			pass 

		#... Connect PMA to Coordinate
		uv_pma.attr('output2D.output2Dx') >> uvpin_core.attr('coordinate[0].coordinateU')
		uv_pma.attr('output2D.output2Dy') >> uvpin_core.attr('coordinate[0].coordinateV')


		if createJoint == True:
			pre_jnt = core.Joint(f'{loc_base_name}_jnt')
			uvpin_core.attr('outputMatrix[0]') >> pre_jnt.attr('offsetParentMatrix')
			created_locators.append(pre_jnt.name)
		else:

			#... D. Output Locator
			pName = f'{loc_base_name}_loc'
			pinned_loc = core.Locator(pName)
			pinned_loc.attr('localScaleX').value = locator_scale
			pinned_loc.attr('localScaleY').value = locator_scale
			pinned_loc.attr('localScaleZ').value = locator_scale
			pinned_loc.setLocColor('white')

			#... Matrix Connection
			uvpin_core.attr('outputMatrix[0]') >> pinned_loc.attr('offsetParentMatrix')

			
			#... Reset Transforms
			for attr in ['tx','ty','tz','rx','ry','rz']:
				pinned_loc.attr(attr).value = 0

			created_locators.append(pinned_loc.name)

		PinPolyLogger.info(f'Success: {created_locators}')

	return created_locators





# ... imports remain the same ...

def pin_locator_polygon_from_guides(poly_mesh='head_geo',
									guide_list=[], 
									locator_scale=1.0,
									side='C',
									normalAxis='Z',
									tangentAxis='X',
									createJoint=False,
									naming_suffix='pin'):
	"""
	Pin locators (or joints) to a mesh using existing Locator Guides to determine position.
	
	Args:
		poly_mesh (str): The target mesh name.
		guide_list (list): List of locator names used as guides.
	"""

	#... 1. Validate inputs
	if not mc.objExists(poly_mesh):
		PinPolyLogger.error(f'Polygon mesh "{poly_mesh}" does not exist.')
		return None

	if not guide_list:
		PinPolyLogger.warning('Guide list is empty.')
		return None

	#... 2. Setup Mesh PyNode
	try:
		oMesh = pm.PyNode(poly_mesh)
		oShape = oMesh.getShape()
	except Exception as e:
		PinPolyLogger.error(f'Failed to process Mesh: {e}')
		return None

	#... 3. Determine UV Set & History (Logic เดิม)
	oShape_name = oShape.name()
	try:
		current_uv_set = mc.polyUVSet(poly_mesh, query=True, currentUVSet=True)[0]
	except:
		current_uv_set = 'map1'

	#... Check Deformer History logic (Logic เดิม)
	history_nodes = mc.listConnections(f'{oShape_name}.inMesh', source=True, destination=False)
	original_geometry_source = None
	use_orig_node = False

	if history_nodes:
		all_history = mc.listHistory(oShape_name, future=False, allConnections=True) or []
		orig_shapes = [n for n in all_history if mc.nodeType(n) in ['mesh', 'nurbsSurface'] and n.endswith('Orig')]
		if orig_shapes:
			original_geometry_source = orig_shapes[0]
			use_orig_node = True
			PinPolyLogger.info(f'Found Deformer History. Using Orig: {original_geometry_source}')

	created_objects = []

	#... 4. Iterate through GUIDES instead of Vertex IDs
	for guide in guide_list:
		if not mc.objExists(guide):
			PinPolyLogger.warning(f'Guide "{guide}" not found. Skipping.')
			continue

		#... [KEY CHANGE] Get World Position from Guide Locator
		world_pos = mc.xform(guide, query=True, worldSpace=True, translation=True)

		#... Naming Logic: Use guide name as base
		# Ex: 'eyeLeft_guide_loc' -> base: 'eyeLeft'
		guide_short = guide.split(':')[-1] # Remove namespace if any
		
		# Try to clean name using core or simple split
		try:
			# Assuming core.check_name_style returns (base, side, ...)
			name_info = core.check_name_style(guide_short)
			clean_base_name = name_info[0]
		except:
			 # Fallback if check_name_style fails or returns unexpected format
			clean_base_name = guide_short.replace('_loc', '').replace('_guide', '')

		loc_base_name = f'{clean_base_name}_{naming_suffix}'
		PinPolyLogger.info(f'Processing Guide: {guide} -> {loc_base_name}')

		#... A. Find Closest UV (ใช้ Position จาก Guide)
		oNode = pm.createNode('closestPointOnMesh', name=f'{loc_base_name}_closePInfo_tmp')
		oShape.worldMesh.connect(oNode.inMesh, force=True)
		oNode.inPosition.set(world_pos) # <--- ใส่ Position ตรงนี้

		uPos = oNode.parameterU.get()
		vPos = oNode.parameterV.get()
		pm.delete(oNode)

		#... B. Create PMA (Logic เดิม)
		uv_pma = core.PlusMinusAverage(name=f'{loc_base_name}_UVslide_pma')
		uv_pma.attr('operation').value = 1 
		uv_pma.attr('input2D[0].input2Dx').value = uPos
		uv_pma.attr('input2D[0].input2Dy').value = vPos

		uv_pma.addAttribute(at='double2', ln='uvSlide', k=True)
		uv_pma.addAttribute(at='double', ln='uSlide', parent='uvSlide', k=True)
		uv_pma.addAttribute(at='double', ln='vSlide', parent='uvSlide', k=True)

		uv_pma.attr('uSlide') >> uv_pma.attr('input2D[1].input2Dx')
		uv_pma.attr('vSlide') >> uv_pma.attr('input2D[1].input2Dy')

		#... C. Create uvPin (Logic เดิม)
		uvPin = pm.createNode('uvPin', name=f'{loc_base_name}_uvPin')
		uvPin.uvSetName.set(current_uv_set)

		AXIS_TO_INDEX_DICT = {'X': 0, 'Y': 1, 'Z': 2, '-X': 3, '-Y': 4, '-Z': 5}
		uvPin.normalAxis.set(AXIS_TO_INDEX_DICT.get(normalAxis, 2))
		uvPin.tangentAxis.set(AXIS_TO_INDEX_DICT.get(tangentAxis, 0))

		# Connect Geometry
		oShape.worldMesh.connect(uvPin.deformedGeometry, force=True) 
		uvpin_core = core.Dag(uvPin.name())
		
		if use_orig_node:
			shapeOrig = core.Dag(original_geometry_source)
			if mc.nodeType(original_geometry_source) == 'nurbsSurface':
				 shapeOrig.attr('worldSpace[0]') >> uvpin_core.attr('originalGeometry')
			else:
				 shapeOrig.attr('outMesh') >> uvpin_core.attr('originalGeometry')

		# Connect UV coords
		uv_pma.attr('output2D.output2Dx') >> uvpin_core.attr('coordinate[0].coordinateU')
		uv_pma.attr('output2D.output2Dy') >> uvpin_core.attr('coordinate[0].coordinateV')

		#... D. Output (Joint or Locator)
		if createJoint:
			# Create Joint logic
			final_obj = core.Joint(f'{loc_base_name}_jnt')
			# Reset transforms just in case
			for attr in ['tx','ty','tz','rx','ry','rz']:
				final_obj.attr(attr).value = 0
			
			uvpin_core.attr('outputMatrix[0]') >> final_obj.attr('offsetParentMatrix')
			created_objects.append(final_obj.name)
		else:
			# Create Locator logic
			pName = f'{loc_base_name}_loc'
			final_obj = core.Locator(pName)
			final_obj.attr('localScaleX').value = locator_scale
			final_obj.attr('localScaleY').value = locator_scale
			final_obj.attr('localScaleZ').value = locator_scale
			final_obj.setLocColor('white')

			uvpin_core.attr('outputMatrix[0]') >> final_obj.attr('offsetParentMatrix')
			
			# Reset Transforms
			for attr in ['tx','ty','tz','rx','ry','rz']:
				final_obj.attr(attr).value = 0

			created_objects.append(final_obj.name)

	PinPolyLogger.info(f'Pin from guides success: {created_objects}')
	return created_objects