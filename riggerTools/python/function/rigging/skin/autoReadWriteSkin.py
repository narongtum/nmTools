#!/usr/bin/python
# utils.py [part 3/4]
# mod from Andrew Glisinski
# Returns a list of requested object strings

from function.framework.reloadWrapper import reloadWrapper as reload
import maya.cmds as mc
import os
import json



'''
from function.rigging.skin import autoReadWriteSkin as skin
reload (skin)

'''
import maya.mel as mel

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload (wcd)

from function.pipeline import fileTools as fileTools 
reload (fileTools)

from function.rigging.util import misc as misc
reload(misc)

hashSign = '#' * 25

'''
from function.rigging.skin  import autoReadWriteSkin as skin
reload(skin)

geoData = skin.geoInfo(vtx=True, geo=True, skinC=True)
'''

MAYA_VERSION = mc.about(v=True)	



def selectBJntFromSameMesh():
	""" select bind joint from the mesh that was skinCluster before """
	try:
		selected = mc.ls(sl = True, flatten = True)[0]
	except:
		mc.error('Please select something')
		return False

	dirPath 	= 	_processPath()
	filePath  	= 	dirPath + '%s_generalData.json' %selected

	try:
		vertexData 	= 	wcd.loadData(filePath)
	except:
		print ('File skin data does not exists. terminate progress')
		return False

	print ('%s < = is sel var' %selected)

	skinJntLst = vertexData['skinJnt']

	return mc.select( skinJntLst ,r=True )

		







######################## core function

# wirteSkin.py [part 1/4]
# get neccessry data , vertex , geo name , shapename , skincluster name
def geoInfo(vtx = False, geo = False, shape = False, skinC = False): 
	# if user select geo
	if mc.ls(sl = True):
		returnValues = []
		# list compherehension
		# is mean each for mc.ls and appen to selVTX
		# if vertex in list 
		selVTX = [x for x in mc.ls(sl = True , fl = True) if ".vtx" in x]
		
		if len(selVTX) == 0:
			print ('No select vertex')

			
			selGEO = mc.ls(sl = True, objectsOnly = True)[0]

			try:
				geoShape = mc.listRelatives(selGEO, shapes = True)[0]
				print ('this is geoShape {0}'.format(geoShape))
			except:
				print ('There is no mesh selected.')

		
		else:
			# if len is more than 0 that mean user select vertex
			print ('Please do not select vertices')

		
		
		if vtx == True:
			print ('\nExporting vertex...')
			if len(selVTX) != 0: # if vertices are already selected, then we can take that list whole-sale.
				returnValues.append(selVTX)
			else:
				vtxIndexList = [ "{0}.vtx[{1}]".format(geoShape, x) for x in mc.getAttr ( geoShape + ".vrts", multiIndices=True) ]
				returnValues.append(vtxIndexList)
		
		
		if geo == True:
			
			returnValues.append(selGEO)
			print ('\nAppend geometry name... %s' %selGEO)
		
		
		if shape == True:
			returnValues.append(geoShape)
			print ('\nAppend shape name... %s' %geoShape)
		
		
		if skinC == True:
			skinClusterNM = [x for x in mc.listHistory(geoShape) if mc.nodeType(x) == "skinCluster" ][0]
			print ('\nAppend skinCluster name... %s' %skinClusterNM)
			returnValues.append(skinClusterNM)
			
		return returnValues

	else:
		print ('Please select something')


	'''
	index of geo info
	vertexList 		= 	geoData[0]
	selGEO 			= 	geoData[1]
	shapeName 		= 	geoData[2]
	skinCluster 	= 	geoData[3]
	'''
# wirteSkin.py [part 2/4]
# recived value from geoInfo to get the vertex weight
def getVertexWeights( vertexList = [], skinCluster = '', thresholdValue = 0.001 ):
	# check if have any vertex and skinCluster
	if len(vertexList) != None and skinCluster != None:
		# declate dictionary
		verticeDict = {}

		for vtx in vertexList:
			# return vale
			influenceVals = mc.skinPercent(skinCluster, vtx, q=True, v = True, ib = thresholdValue )

			# return joint name
			jointName = mc.skinPercent(skinCluster, vtx, transform = None, q =True, ib = thresholdValue)

			# conbine to vertex dict with the key is vtx

			# Python 3 has change data type of zip method from list of tuples to zip
			# Should be converted to a list
			
			if MAYA_VERSION == '2018':
				verticeDict[vtx] = zip(jointName , influenceVals)
			elif MAYA_VERSION == '2022' or MAYA_VERSION == '2023':
				verticeDict[vtx] = list(zip(jointName , influenceVals))


		return verticeDict

	else:
		mc.error('No Vertices or SkinCluster')

# 1 skin data
# 2 full file path with file name
def writeJsonFile( dataWrite , filePath , step ):
	print(type(dataWrite))
	with open(filePath, "w") as jsonFile:
		try:
			json.dump( dataWrite , jsonFile , indent = 2)
		except:
			print ('To prevent JSON seializable.')
			json.dumps( dataWrite , jsonFile, indent=2, default=dict(dataWrite))


	print ('File was save at: %s' %filePath)
	print ('\n')
	print (hashSign + ' witre data complete ' + hashSign)

#... solution
#... https://github.com/agiliq/django-graphos/issues/36 

#... get skin joint list
#... input full path
#... must put r for raw string
#... Input: write skinCluster
#... Result: skinname and skinjointlist
def getSkinJntLst():
	filePath = raw_input( "\nInput Data Path:	" )
	
	clean_path = filePath.replace('\\','\\\\')
	#clean_path = os.path.abspath( filePath )
	print (clean_path)


	vertexData 	= 	wcd.loadData( clean_path )
	for key in vertexData.keys():
		if ( key == 'skinCluster' ):
			skinName = vertexData['skinCluster']
		elif ( key == 'skinJnt' ):
			skinJntList = vertexData['skinJnt']
	return skinName,skinJntList





'''
#... Run command manual 
'''


'''
# get skin data
skinData = skin.getSkinJntLst()
skcName = skinData[0]
jntLst = skinData[1]
'''


def _processPath():
	dataRaw = fileTools.getAssetData()
	mayaFileName = dataRaw[0][-1]

	if 'hero' in mayaFileName:
		print ('This is hero file')
		filePath  = fileTools.desinatePath('\\RIG\\data\\skinData\\')

	else:
		print ('This is version file')
		filePath  = fileTools.desinatePath('\\data\\skinData\\')


	fileTools.currentFilePath(filePath)
	return filePath


#... include joint skin list
def exportWeightData():


	selection = mc.ls(sl = True, fl = True)

	if selection:

		for each in selection:
			mc.select( each , r = True)


			# get vertex data
			geoData = geoInfo( vtx = True, geo = True, skinC = True )
			vertexDict	=	{}
			vertexList 			= 		geoData[0]
			selGEO 				= 		geoData[1]
			skinClusterNam 		= 		geoData[2]

			# got dictionary of namejoint vertexnumber skinpercent
			vertexDict = getVertexWeights( vertexList , skinClusterNam )



			# get joint in skin cluster list data 
			jointSet = []
			for each in vertexList:
			
				jointName = mc.skinPercent( skinClusterNam, each, transform = None, q =True, ib = 0.0001)
				jointSet.extend( jointName )

			skinJntList = []

			for each in jointSet:
				if each not in skinJntList:
					skinJntList.append( each )

			#print skinJntList



			# add  skin cluster name to the dictionarty
			vertexDict['skinCluster'] = skinClusterNam
			# add skin joint cluster list to the dictionarty
			vertexDict['skinJnt'] = skinJntList
			# geo name
			vertexDict['geoName'] = selGEO 
			# print vertexDict



			# define path
			dirPath = _processPath()
			filePath  = dirPath + '%sData.json' %selGEO
			writeJsonFile( vertexDict , filePath , 'weight')

	else:
		mc.error("Nothing to select function terminate.")
		return False







def importWeightData():

	#	read json format
	# 	Flattens the returned list of objects so that each component is identified individually.
	selection = mc.ls(sl = True, flatten = True)

	if selection:

		for sel in selection:

			dirPath 	= 	_processPath()
			filePath  	= 	dirPath + '%sData.json' %sel

			try:
				vertexData 	= 	wcd.loadData(filePath)
			except:
				print ('File skin data does not exists. terminate progress')
				return False

			print ('%s < = is sel var' %sel)


			# Check is having skincluster of not
			relatives = mc.listRelatives( sel, type = "shape" )
			sCluster = mc.listConnections( relatives, type = "skinCluster" )

			if sCluster == None:
				'''
				check if skinCluster is already exists
				if not auto create skincluster with joint list
				if yes skip to load skinWeight
				'''
				
				print ('There are no skinCluster Then import weight Na.')

				# Select geo first for qury geo data function
				# for multiple selection 
				mc.select( sel , r = True)

				if vertexData['geoName'] != sel :
					print ('geo name may not match Bye')
					return False

				
				skinClusterNam = vertexData['skinCluster']
				skinJntLst = vertexData['skinJnt']
				geoName = vertexData['geoName']


				# assign skincluster with list
				newSkin = mc.skinCluster( skinJntLst, geoName,  name = skinClusterNam ,  toSelectedBones = True )[0]

			else:
				print ('There are already skinCluster Na.')
				selectGeoData = geoInfo(vtx = False, geo = False, shape = True, skinC = True)

				geoName			= 	selectGeoData[0]
				skinClusterNam 	= 	selectGeoData[1]

			misc.makeHeader('Load SkinCluster Complete.')

	else:
		mc.error("Nothing to select function terminate.")
		return False




	# dirPath 	= 	_processPath()

	# read json format
	# file path with skc name 
	# filePath  	= 	dirPath + '%sData.json' %skinClusterNam
	# vertexData 	= 	wcd.loadData(filePath)

	# .......................#
	# Import skinWeight data #
	# .......................#

	if len(vertexData) > 0:
		
		for key in vertexData.keys():
			# skipt skinJnt and skinCluster and geoName
			if ( key != 'skinCluster' ) and ( key != 'skinJnt' ) and ( key != 'geoName' ):
				try:
					# disable it for make it faster
					# print '\nImporting %s to skin data...' %key
					
					# use skc name, shapeName.vtx[number]
					mc.skinPercent( skinClusterNam, key, transformValue = vertexData[key], zeroRemainingInfluences = True )
				except:
					mc.error("Error , %s Skin Joint name may mistmatch or SkinCluster joint list not exists ..." %key)
					continue

				

			else:
				print("key, values pair have a problem")
				continue
		print ("\n{0} Vertices were set to vertex weight values. ".format(	len(vertexData.keys())	))
		print ("\n{0}{0} Import SkinCluster Complete {0}{0}".format( hashSign ))
	else:
		mc.error("JSON File was empty ")
	mc.select( deselect = True )




#broswe file skin data
def _jsonGetFileName(*args):
	jsonFilter = "*.json"
	print (jsonFilter)
	try:
		fileNameDir = mc.fileDialog2( fileFilter = jsonFilter, dialogStyle = 2, fileMode = 1, okCaption = 'Open')[0]
		if fileNameDir != "":
			if '/' in fileNameDir:
				clean_file = fileNameDir.replace('/','\\\\')
				print (clean_file)
				vertexData 	= 	wcd.loadData( clean_file )
				#print vertexData
				for key in vertexData.keys():
					if ( key == 'skinCluster' ):
						
						skinName = vertexData['skinCluster']
					elif ( key == 'skinJnt' ):
						
						skinJntList = vertexData['skinJnt']

			return skinName,skinJntList
				
	except:
		print ('Cancle progress...')




# automate import weight
def browseWeight():

	sJntList = _jsonGetFileName()
	skinName = sJntList[0]
	skinJntList = sJntList[1]


	geo = mc.ls(sl = True)
	# ask what is shape name
	shpName = wcd.validateCurve(geo)[0]

	# if already have skin then unbind
	if mc.listConnections( shpName, type = 'skinCluster' ):
		print ('there art having skincluster unbind skin')
		mel.eval('doDetachSkin "2" { "1","1" }')

	else:
		print ('there are no connection')

	mc.skinCluster( skinJntList , geo , name = skinName )
	mc.select( geo , r = True )
	importWeightData()
