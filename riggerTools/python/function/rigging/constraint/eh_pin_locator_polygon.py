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

def pin_locator_polygon(poly_mesh='for_dup_hair',
                        vtx_list=[49],
                        locator_scale=1.0,
                        side='C',   #... Side argument restored as requested
                        normalAxis='Z',
                        tangentAxis='X'):
    """
    Pin locators to specific vertices on a polygon mesh using uvPin.
    
    Args:
        poly_mesh (str): Name of the polygon mesh.
        vtx_list (list/tuple/int): List of vertex indices to pin.
        locator_scale (float): Scale of the output locator.
        side (str): Side prefix for naming (e.g., 'C', 'L', 'R'). Placed at the very left.
        normalAxis (str): Axis to align with the normal ('X', 'Y', 'Z', '-X', '-Y', '-Z').
        tangentAxis (str): Axis to align with the tangent.
    """

    #... 1. Validate inputs
    if not mc.objExists(poly_mesh):
        PinPolyLogger.error(f'Polygon mesh "{poly_mesh}" does not exist. Terminating.')
        return None

    #... Ensure vtx_list is iterable (list or tuple)
    if isinstance(vtx_list, (int, str)):
        vtx_list = [vtx_list]

    #... 2. Analyze Naming using core.check_name_style
    #... We take index [4] which is 'nameNoSide' (Clean name without Side prefix/suffix and Extension)
    try:
        #... Returns: (base_name, side, reverse_side, isDefault, nameNoSide, name_reverse_side)
        name_info = core.check_name_style(poly_mesh)
        
        #... Grab index 4 as requested: Base name stripped of side and extension
        clean_base_name = name_info[4]
        
        #... Safety check: if index 4 is None/Empty (e.g. naming doesn't fit convention), fallback to index 0 or raw name
        if not clean_base_name:
             clean_base_name = name_info[0] if name_info[0] else poly_mesh.split('_')[0]

    except Exception as e:
        PinPolyLogger.warning(f"Could not analyze name style: {e}. Using raw mesh name as base.")
        clean_base_name = poly_mesh

    #... 3. Setup PyNodes and validate mesh shape (Do this once)
    try:
        oMesh = pm.PyNode(poly_mesh)
        oShape = oMesh.getShape()
        if not isinstance(oShape, pm.nodetypes.Mesh):
            PinPolyLogger.error(f'"{poly_mesh}" is not a valid Polygon Mesh. Terminating.')
            return None
    except Exception as e:
        PinPolyLogger.error(f'Failed to process Polygon Mesh PyNode: {e}. Terminating.')
        return None

    #... 4. Find Original Geometry (Do this once)
    oShape_name = oShape.name()
    history_nodes = mc.listConnections(f'{oShape_name}.inMesh', source=True, destination=False)
    
    original_geometry_source = oShape_name # Default
    if history_nodes:
        #... Attempt to find the 'Orig' shape node to pin to undeformed geometry
        all_history = mc.listHistory(oShape_name, future=False, allConnections=True) or []
        orig_shapes = [n for n in all_history if mc.nodeType(n) in ['mesh', 'nurbsSurface'] and n.endswith('Orig')]
        if orig_shapes:
            original_geometry_source = orig_shapes[0]
            PinPolyLogger.info(f'Found Original Geometry Source: {original_geometry_source}.')
        else:
             PinPolyLogger.warning(f'Could not find a standard "Orig" shape node for {poly_mesh}. Using deformed shape.')
    else:
        PinPolyLogger.info(f'No deformer history found on {poly_mesh}. Using current shape as Original Geometry.')

    #... Prepare return list
    created_locators = []

    #... 5. Iterate through Vertex List
    for vtxNum in vtx_list:
        
        #... Construct source location string
        source_loc = f'{poly_mesh}.vtx[{vtxNum}]'
        
        if not mc.objExists(source_loc):
            PinPolyLogger.error(f'Vertex "{source_loc}" does not exist. Skipping.')
            continue

        #... Get World Position
        world_pos = mc.pointPosition(source_loc, world=True)

        #... Naming Construction: {side}_{clean_base_name}_vtx{num}_loc
        #... Example: C_spine01_vtx10_loc
        loc_base_name = f'{side}_{clean_base_name}_vtx{vtxNum}'
        
        PinPolyLogger.info(f'Processing: {source_loc} -> {loc_base_name}')

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # A. Find the closest UV point on the mesh
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        oNode = pm.createNode('closestPointOnMesh', name=f'{loc_base_name}_closePInfo_tmp')
        oShape.worldMesh.connect(oNode.inMesh, force=True)
        oNode.inPosition.set(world_pos)

        uPos = oNode.parameterU.get()
        vPos = oNode.parameterV.get()
        pm.delete(oNode)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # B. Create PMA for UV input control
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        uv_pma = core.PlusMinusAverage(name=f'{loc_base_name}_UVslide_pma')
        uv_pma.attr('operation').value = 1 # Sum
        uv_pma.attr('input2D[0].input2Dx').value = uPos
        uv_pma.attr('input2D[0].input2Dy').value = vPos

        uv_pma.addAttribute(at='double2', ln='uvSlide', k=True)
        uv_pma.addAttribute(at='double', ln='uSlide', parent='uvSlide', k=True)
        uv_pma.addAttribute(at='double', ln='vSlide', parent='uvSlide', k=True)

        uv_pma.attr('uSlide') >> uv_pma.attr('input2D[1].input2Dx')
        uv_pma.attr('vSlide') >> uv_pma.attr('input2D[1].input2Dy')

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # C. Create uvPin node and connect the PMA
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        uvPin = pm.createNode('uvPin', name=f'{loc_base_name}_uvPin')

        AXIS_TO_INDEX_DICT = {
            'X': 0, 'Y': 1, 'Z': 2,
            '-X': 3, '-Y': 4, '-Z': 5,
        }

        #... Set Axis
        uvPin.normalAxis.set(AXIS_TO_INDEX_DICT.get(normalAxis, 2))
        uvPin.tangentAxis.set(AXIS_TO_INDEX_DICT.get(tangentAxis, 0))

        #... Connect Original Geometry
        oShape.worldMesh.connect(uvPin.deformedGeometry, force=True) 
        
        uvpin_core = core.Dag(uvPin.name())
        shapeOrig = core.Dag(original_geometry_source)
        
        #... Connect Orig Shape OutMesh
        if mc.nodeType(original_geometry_source) == 'nurbsSurface':
             shapeOrig.attr('worldSpace[0]') >> uvpin_core.attr('originalGeometry')
        else:
             shapeOrig.attr('outMesh') >> uvpin_core.attr('originalGeometry')

        #... Connect PMA to UVPin Coordinate[0]
        uv_pma.attr('output2D.output2Dx') >> uvpin_core.attr('coordinate[0].coordinateU')
        uv_pma.attr('output2D.output2Dy') >> uvpin_core.attr('coordinate[0].coordinateV')

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # D. Create the output locator
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        pName = f'{loc_base_name}_loc'

        pinned_loc = core.Locator(pName)
        pinned_loc.attr('localScaleX').value = locator_scale
        pinned_loc.attr('localScaleY').value = locator_scale
        pinned_loc.attr('localScaleZ').value = locator_scale

        pinned_loc.setLocColor('white')

        #... Connect Matrix
        uvpin_core.attr('outputMatrix[0]') >> pinned_loc.attr('offsetParentMatrix')
        
        #... Reset transform values since we use offsetParentMatrix
        pinned_loc.attr('tx').value = 0
        pinned_loc.attr('ty').value = 0
        pinned_loc.attr('tz').value = 0
        pinned_loc.attr('rx').value = 0
        pinned_loc.attr('ry').value = 0
        pinned_loc.attr('rz').value = 0

        created_locators.append(pinned_loc.name)
        PinPolyLogger.info(f'Successfully pinned "{pinned_loc.name}" to "{poly_mesh}".')

    return created_locators