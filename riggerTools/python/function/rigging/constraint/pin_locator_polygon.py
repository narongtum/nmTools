import maya.cmds as mc
import pymel.core as pm
import re

from function.framework.reloadWrapper import reloadWrapper as reload

#... Assuming core module and classes (Dag, CoreLogger, Null) and PlusMinusAverage are available
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



import maya.cmds as mc
import pymel.core as pm
from function.rigging.autoRig.base import core
from function.pipeline import logger

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
						tangentAxis='X'):
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
		PinPolyLogger.info(f'Success: {pinned_loc.name}')

	return created_locators