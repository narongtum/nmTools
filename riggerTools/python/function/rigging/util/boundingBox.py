'''
Reference from glTools



from function.rigging.util import boundingBox as bBox
reload(bBox)




'''
import maya.cmds as mc
import maya.OpenMaya as OpenMaya


def geoBoundingBox( geometry , worldSpace = True , noIntermediate = True , visibleOnly = True ):
	'''
	get bounding box value from geometry 
	@param geometry: return bounding box
	@type geometry: str or list
	'''
	# Initialize Object Classes
	geoDagPath = OpenMaya.MDagPath()
	selectionList = OpenMaya.MSelectionList()

	# Initialize empty bounding box
	bbox = OpenMaya.MBoundingBox()

	# Get Visible Geometry
	geoShapes = mc.ls(mc.listRelatives(geometry,ad=True,pa=True),noIntermediate=noIntermediate,geometry=True,visible=visibleOnly)

	for shape in geoShapes:
		selectionList.clear()
		OpenMaya.MGlobal.getSelectionListByName(shape,selectionList)
		selectionList.getDagPath(0,geoDagPath)
		bboxShape = OpenMaya.MFnDagNode(geoDagPath).boundingBox()

		if worldSpace: 
			bboxShape.transformUsing(geoDagPath.inclusiveMatrix())
			bbox.expand(bboxShape)

	# Get Bounding Box Min/Max (as MPoint)
	mn = bbox.min()
	mx = bbox.max()

	# Return Formatted Result
	return [mn.x,mn.y,mn.z,mx.x,mx.y,mx.z]



def getGeoRatio( select , xVal = 1.25 , yVal = 2 ):
	'''
	I don't know what is for
	'''
	boundBox = mc.exactWorldBoundingBox(select)
	yOffset = 	float(abs(boundBox[1] - boundBox[4]  * xVal )	)
	xOffset = 	float(abs(boundBox[0] - boundBox[3]  * yVal )	)

	return xOffset,yOffset



