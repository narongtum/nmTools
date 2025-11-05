import maya.cmds as mc
import pymel.core as pm
import re

#... Assuming core module and classes (Dag, CoreLogger, Null) and PlusMinusAverage are available
from function.pipeline import logger
reload(logger)

from function.rigging.autoRig.base import core
reload(core)

class PinPolyLogger(logger.MayaLogger):
	LOGGER_NAME = "pin_locator_polygon"


poly_mesh = 'pSphere1'
vtxNum = '235'
locator_scale = 1.0
prefix = 'Rivet'
region = 'body'
side = 'C'
normalAxis = 'Z'
tangentAxis = 'X'










source_loc = f'{poly_mesh}.vtx[{vtxNum}]'



#... 1. Validate inputs
if not mc.objExists(poly_mesh):
	PinPolyLogger.error(f'Polygon mesh "{poly_mesh}" does not exist. Terminating.')
	#return None

if not mc.objExists(source_loc):
	PinPolyLogger.error(f'Source "{source_loc}" does not exist. Terminating.')
	#return None

#... 2. Determine base name and get world position

if '.' in source_loc:
	#... If source is a component
	match = re.search(r'\.(\w+)\[', source_loc)
	comp_type = match.group(1) if match else 'comp'
	world_pos = mc.pointPosition(source_loc, world=True)
	#... Clean name for node creation
	clean_name = source_loc.replace('.', '_').replace('[', '_').replace(']', '')
	base_name = f'{region}_{clean_name}_{side}'
	
else:
	#... If source is a transform
	world_pos = mc.xform(source_loc, query=True, worldSpace=True, translation=True)
	base_name = f'{region}_{source_loc}_{side}'


#... 3. Setup PyNodes and validate mesh shape
try:
	oMesh = pm.PyNode(poly_mesh)
	oShape = oMesh.getShape()
	if not isinstance(oShape, pm.nodetypes.Mesh):
		PinPolyLogger.error(f'"{poly_mesh}" is not a valid Polygon Mesh. Terminating.')
		#return None
except Exception as e:
	PinPolyLogger.error(f'Failed to process Polygon Mesh PyNode: {e}. Terminating.')
	#return None


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# A. Find the closest UV point on the mesh
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

oNode = pm.createNode('closestPointOnMesh', name = f'{base_name}_closePInfo_tmp')
oShape.worldMesh.connect(oNode.inMesh, force=True)
oNode.inPosition.set(world_pos)

uPos = oNode.parameterU.get()
vPos = oNode.parameterV.get()

pm.delete(oNode)

PinPolyLogger.info(f'Found closest UV on {poly_mesh}: U={uPos:.4f}, V={vPos:.4f}')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# B. Create PMA for UV input control
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#... Create a PlusMinusAverage node to hold and control UV coordinates
uv_pma = core.PlusMinusAverage( name = f'{base_name}_UVslide_pma' )

#... Set operation to 'None' (0) or 'Sum' (1) if you want to add multiple inputs
#... Using 'None' is simplest for just storing initial values.
uv_pma.attr('operation').value = 1 # Set to sum

#... Set the initial UV coordinates to Input 2D [0]
#... We use the core.Dag.attr() access style to set the U and V values
uv_pma.attr('input2D[0].input2Dx').value = uPos
uv_pma.attr('input2D[0].input2Dy').value = vPos

#... The user can now connect controls to input2D[1] onwards for UV sliding control
uv_pma.addAttribute( at='double2', ln='uvSlide', k=True)
uv_pma.addAttribute( at='double', ln='uSlide', parent='uvSlide', k=True)
uv_pma.addAttribute( at='double', ln='vSlide', parent='uvSlide', k=True)

uv_pma.attr('uSlide') >> uv_pma.attr('input2D[1].input2Dx')
uv_pma.attr('vSlide') >> uv_pma.attr('input2D[1].input2Dy')




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# C. Create uvPin node and connect the PMA
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

uvPin = pm.createNode('uvPin', name = f'{base_name}_{prefix}_uvPin')


#... Dictionary ที่แมปชื่อแกน (string) ไปยังค่า Index (integer)
AXIS_TO_INDEX_DICT = {
	'X': 0,
	'Y': 1,
	'Z': 2,
	'-X': 3,
	'-Y': 4,
	'-Z': 5,

}

uvPin.normalAxis.set(4)

normalAxis_index = AXIS_TO_INDEX_DICT.get(normalAxis)
tangentAxis_index = AXIS_TO_INDEX_DICT.get(tangentAxis)

uvPin.normalAxis.set(normalAxis_index)
uvPin.tangentAxis.set(tangentAxis_index)


#... Connect WorldMesh (from the shape node) to uvPin's originalGeometry
oShape.worldMesh.connect(uvPin.deformedGeometry, force=True) 










#... find orig shape

#... oShape คือ pSphereShape1 (Mesh Shape Node ที่มีการ Deform)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# D. Find the Original Geometry Node (ShapeOrig)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 1. Look for the node connected to the inMesh of the Deformed Shape (oShape)
#    We look for the SOURCE of the connection
#    Use mc.listConnections for robustness

# Get the name of the deformed shape (e.g., 'pSphereShape1')
oShape_name = oShape.name()

# Find the node feeding into the 'inMesh' of the deformed shape
# This is usually the last deformer (e.g., skinCluster) or a history node.
# However, for uvPin, we need the *undeformed* geometry source.

# The simplest way to reliably get the undeformed mesh is often 
# to look for the first node in the construction history that is a mesh/geometry source,
# OR, check if the *Original* attribute exists on the Shape Node (e.g., pSphereShape1.original)
# If a deformer is present, Maya often uses a parallel shape node (e.g., pSphereShape1Orig) 
# or a specific history attribute (e.g., "pSphereShape1.inMesh").

# Let's try the simple approach: check for a history node feeding into inMesh
# The correct source for uvPin.originalGeometry should be the output of the node *before* any deformation
# e.g., 'pSphereShape1Orig.outMesh' or 'initialShadingGroup.inMesh' if no deformer exists.

# Find the shape node that represents the original mesh (usually ending in 'Orig')
# This is a common pattern when a BlendShape is applied, or if a history node is present.

# First, try listing connections feeding *into* the inMesh
history_nodes = mc.listConnections(f'{oShape_name}.inMesh', source=True, destination=False)

if history_nodes:
	# The first history node is usually the last deformer in the chain.
	# The Original Geometry required by uvPin should be the *base* mesh,
	# often provided by the 'Orig' shape node if a blendShape is applied.
	
	# We will look for an intermediate object name ending in "Orig"
	# This is often the node that holds the undeformed mesh data for the deformer stack.
	all_history = mc.listHistory(oShape_name, future=False, allConnections=True) or []
	
	# Filter the history for shape nodes with the 'Orig' suffix.
	orig_shapes = [n for n in all_history if mc.nodeType(n) in ['mesh', 'nurbsSurface'] and n.endswith('Orig')]

	if not orig_shapes:
		# If no Orig shape found, we assume the deformed shape itself holds the clean geometry 
		# (This is rare/unsafe if deformers are present, but handles cases with no deformers)
		PinPolyLogger.warning(f'Could not find a standard "Orig" shape node for {poly_mesh}. Terminate Progress.')
		original_geometry_source = oShape_name
		#return False
	else:
		# Use the first found Orig shape name as the source
		shape_orig_name = orig_shapes[0]
		PinPolyLogger.info(f'Found Original Geometry Source: {shape_orig_name}.')
		original_geometry_source = shape_orig_name

else:
	# If no connections to inMesh, the shape is the original geometry (no history)
	PinPolyLogger.info(f'No deformer history found on {poly_mesh}. Using current shape as Original Geometry.')
	original_geometry_source = oShape_name


# Determine the output attribute: use 'outMesh' if it's a mesh node
if mc.nodeType(original_geometry_source) == 'mesh':
	original_geometry_attr = f'{original_geometry_source}.outMesh'
elif mc.nodeType(original_geometry_source) == 'nurbsSurface':
	original_geometry_attr = f'{original_geometry_source}.worldSpace[0]'
else:
	# If it's a deformer node, we need to trace back further (too complex for a simple step)
	# For simplicity here, we assume the found node has an outMesh attribute.
	# Note: In a robust rig, you would need complex logic to find the *undeformed* mesh.
	original_geometry_attr = f'{original_geometry_source}.outMesh'


# Final result variable
PinPolyLogger.info(f'Final Original Geometry Attribute to connect: {original_geometry_attr}.')
# Stop execution here as requested.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #







#... CONNECT PMA Output to uvPin Coordinates
#... This connection automatically solves the 'Dynamic Array' problem by creating Coordinate[0]
#uv_pma.attr('output2D') >> uvPin.attr('Coordinate[0]')

uvpin_core = core.Dag(uvPin.name())


shapeOrig = core.Dag(original_geometry_source)
shapeOrig.attr('outMesh') >> uvpin_core.attr('originalGeometry')


uv_pma.attr('output2D.output2Dx') >> uvpin_core.attr('coordinate[0].coordinateU')
uv_pma.attr('output2D.output2Dy') >> uvpin_core.attr('coordinate[0].coordinateV')




#... Create the output locator
pName = f'{base_name}_{prefix}_loc'

#... Create a new locator
pinned_loc = core.Locator(pName)

#... Set locator scale
pinned_loc.attr('localScaleX').value = locator_scale
pinned_loc.attr('localScaleY').value = locator_scale
pinned_loc.attr('localScaleZ').value = locator_scale

#... Connect uvPin's Output Matrix to the locator's offsetParentMatrix (Matrix Constraint)
# uvPin.outputMatrix.connect(pinned_loc.attr('offsetParentMatrix'), force=True)


uvpin_core.attr('outputMatrix[0]') >> pinned_loc.attr('offsetParentMatrix')



PinPolyLogger.info(f'Successfully pinned "{pinned_loc.name}" to "{poly_mesh}" using uvPin and PMA control.')

# return pinned_loc.name