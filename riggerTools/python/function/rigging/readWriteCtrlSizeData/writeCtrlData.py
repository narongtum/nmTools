'''
// date : 10 aug 2018
//----------------------------------------------------------------------------
// read / write controller data
//----------------------------------------------------------------------------
// mod from: vshotarv :https://github.com/vshotarov/controlShapeManager
//
// DESCRIPTION:		
//		
// REQUIRES:	to install this menu just copy
//	D:\\True_Axion\\Tools\\riggerTools\\maya
// 	to C:\\Users\\<user>\\Documents\\maya
//
// 
//	from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
//----------------------------------------------------------------------------

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd

'''



import os
import json
import re
import functools
from maya import cmds as mc, OpenMaya as om

# global variable
SHAPE_LIBRARY_PATH = None
ext = ".json"


# is
# ok
# to run

# find address of maya file only
def whereAreMe(path = None):
	path = mc.file(q=True, sn = True)
	return path


# auto find propery folder
def validCtrlData():
	where = whereAreMe()
	clean_path = os.path.normpath(where)
	spPath = clean_path.split("\\")

	try:
		reElem = "\\"+spPath[-2]+"\\"+spPath[-1]
		dataPath = 	clean_path.replace(reElem,'') 
		global SHAPE_LIBRARY_PATH
		SHAPE_LIBRARY_PATH = dataPath + "\\data\\ctrlSizeData\\"
		return SHAPE_LIBRARY_PATH

	except Exception as e:
		raise e









# check if folder is exists
def filePath(filename = None):
	if not os.path.exists(os.path.dirname(filename)):
		try:
			os.makedirs(os.path.dirname(filename))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise



# 1 validateCurve
# define shapaNode


def validateCurve( crv = None ):
	'''Checks whether the transform we are working with is actually a curve and returns it's shapes'''
	# print 'validate :%s'%crv
	
	if mc.nodeType(crv) == "transform" and mc.nodeType(mc.listRelatives(crv, c=1, s=1)[0]) == "nurbsCurve":
		crvShapes = mc.listRelatives(crv, c=1, s=1)

	elif mc.nodeType(crv) == "nurbsCurve":
		crvShapes = mc.listRelatives(mc.listRelatives(crv, p=1)[0], c=1, s=1)

	elif mc.nodeType(crv) == "transform":
		crvShapes = mc.listRelatives(crv, shapes=True)


	else:
		mc.error("The object " + crv + " passed to validateCurve() is not a curve")

	return crvShapes




# 2 getshape
# create dictionary template
def getShape(crv = None):
	'''Returns a dictionary containing all the necessery information for rebuilding the passed in crv.'''
	crvShapes = validateCurve(crv)

	crvShapeList = []

	for crvShape in crvShapes:
		crvShapeDict = {
			"name":crv,
			"points": [],
			"knots": [],
			"form": mc.getAttr(crvShape + ".form"),
			"degree": mc.getAttr(crvShape + ".degree"),
			"colour": mc.getAttr(crvShape + ".overrideColor")
		}
		points = []
		# get CV point data
		for i in range(	mc.getAttr(	crvShape + ".controlPoints", s = 1	)	):# number of CV
			points.append(	mc.getAttr(	crvShape + ".controlPoints[%i]" %i)	[0]	)# %i is mean int

		crvShapeDict["points"] = points
		# get knots , what is knots
		crvShapeDict["knots"] = getKnots(crvShape)

		crvShapeList.append(crvShapeDict)

	#return crvShapeDist instead
	return crvShapeDict
	
# 2.5 get knot  , what is knot  ?
def getKnots( crvShape = None ):
	mObj = om.MObject()
	sel = om.MSelectionList()
	sel.add(crvShape)
	sel.getDependNode(0, mObj)

	fnCurve = om.MFnNurbsCurve(mObj)
	tmpKnots = om.MDoubleArray()
	fnCurve.getKnots(tmpKnots)

	return [ tmpKnots[i] for i in range(tmpKnots.length()) ]




# 3 saveToLib

'''Saves the shape data to a shape file in the SHAPE_LIBRARY_PATH directory'''
def saveToLib( crv = None, shapeName = None ):
	'''Saves the shape data to a shape file in the SHAPE_LIBRARY_PATH directory'''
	crvShape = getShape(crv=crv)
	# automate naming of shapeNode
	path = os.path.join(SHAPE_LIBRARY_PATH , re.sub("\s", "", shapeName) + ".json")
	for shapeDict in crvShape:
		# so why you delete colour
		shapeDict.pop("colour", None)
	saveData(path, crvShape)




# not JSON anymore
def saveData(path = None, data = None):
	'''Saves a dictionary as JSON in a file'''
	# if validatePath(path):
	f = open(path, "w")
	f.write(json.dumps(data, sort_keys=1, indent=4, separators=(",", ":")))
	f.close()
	return 1
	





def validatePath(path=None):
	'''Checks if the file already exists and provides a dialog to overwrite or not'''
	if os.path.isfile(path):
		confirm = mc.confirmDialog(title='Overwrite file?',
								   message='The file ' + path + ' already exists.Do you want to overwrite it?',
								   button=['Yes', 'No'],
								   defaultButton='Yes',
								   cancelButton='No',
								   dismissString='No')
		if confirm == "No":
			mc.warning("The file " + path + " was not saved")
			return 0
	return 1


def loadFromLib(shape=None):
	'''Loads the shape data from the shape file in the SHAPE_LIBRARY_PATH directory'''
	path = os.path.join(SHAPE_LIBRARY_PATH, shape + ".json")
	print (path)
	data = loadData(path)
	
	return data



def loadData( path = None ):
	'''Loads raw JSON data from a file and returns it as a dict'''
	# if this file  exist
	if os.path.isfile(path):
		f = open(path, "r")
		data = json.loads(f.read())
		f.close()
		return data
	else:
		mc.error("The file " + path + " doesn't exist. Please check")




	# Assigns args[0] as the shape of the selected curves
	'''
	def assignControlShape(*args):
		
		sel = mc.ls(sl=1, fl=1)
		for each in sel:
			setShape(each, loadFromLib(args[0]))
		mc.select(sel)
	'''

def setShape(crv, crvShapeList):
	''' Creates a new shape on the crv transform, by using the properties in the crvShapeDict. '''
	crvShapes = validateCurve(crv)

	oldColour = mc.getAttr(crvShapes[0] + ".overrideColor")
	# delete old shape and create new one
	mc.delete(crvShapes)

	for i, crvShapeDict in enumerate(crvShapeList):
		tmpCrv = mc.curve( p = crvShapeDict["points"], k = crvShapeDict["knots"], d = crvShapeDict["degree"], per = bool(crvShapeDict["form"] ) )
		
		newShape = mc.listRelatives( tmpCrv, s=1 )[0]
		mc.parent(newShape, crv, r=1, s=1)

		mc.delete(tmpCrv)

		#newShape = mc.rename(newShape, crv + "Shape" + str(i + 1).zfill(2)	)
		# assign name by the object and +'Shape'
		newShape = mc.rename( newShape , crv + "Shape" 	)

		mc.setAttr(newShape + ".overrideEnabled", 1)

		if "colour" in crvShapeDict.keys():
			setColour(newShape, crvShapeDict["colour"])
		else:
			setColour(newShape, oldColour)
		



def setColour(crv, colour):

	'''
	Sets the overrideColor of a curve
	@param : A dictionary of template component and items.
	@type : dict
	@return 
	'''



	if mc.nodeType(crv) == "transform":
		crvShapes = mc.listRelatives(crv)
	else:
		crvShapes = [crv]
	for crv in crvShapes:
		mc.setAttr(crv + ".overrideColor", colour)



def flipCtrlShape( sel , axis=[-1, -1, -1] ):
	sel = mc.ls(sl=True)
	print ('new mod axis is %s' %axis)
	shapes = getShape(sel[0])
	print (shapes)	
	newShapes = []


	for i, each in enumerate(shapes["points"]):
		shapes["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
	newShapes.append(shapes)
	# this is mean
	# for each number of joint [i] 1,2,3,4,5,..... number of point
	# for each is value (-0.12885414399848572, 3.9327916631783624, 12.533662558110011)
	# that mean make this multiply with -1
	# and append that to new shape

	# specifiy the shape that u went to make
	return newShapes




def modifiyCtrlShape(shapesData , axis=[-1, -1, -1] ):
	newShapes = []
	for i, each in enumerate(shapesData["points"]):
		shapesData["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
	newShapes.append(shapesData)
	return newShapes




'''
sys.path.append(r'D:\noman')

import writeCtrlData_draft_v010 as wcd
reload(wcd)

# write controller size data
allCtrl = mc.ls('*_ctrl')
allShapeName = []
for each in allCtrl:
    shapeName = wcd.validateCurve(each)
    
    crvShapeList = wcd.getShape(each)
    
    SHAPE_LIBRARY_PATH = r"D:/noman/ctrlData/"
    shape = shapeName[0]
    allShapeName.append(shape)
    ext = ".json"
    path = SHAPE_LIBRARY_PATH + shape + ext
    
    # save data 
    wcd.saveData(path , data = crvShapeList)
    
# load controller size data
for each in allShapeName:
    data = wcd.loadFromLib(each)
    mc.curve(data["name"],r=True,p=data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]))
 
# another benefit it can 'replace' curve shape to another by loading desinate control data to spicifie curve
# example
# using hip ctrl data
data = wcd.loadFromLib('hip_ctrlShape') 

# replace is importance

# specifile 'spine_ctrl' and change spine to   shape of hipCtrl 
mc.curve('spine_ctrl',replace = True,p=data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]))

# you can specifie by nameing it i add name to key at this dict already 
Ex


data["name"]
it will return name 'cog_ctrl' 
'''
