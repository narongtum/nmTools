'''
# skin utility
# - -/__ module path __/- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



from function.rigging.skin import skinUtil
reload(skinUtil)

'''


from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline import fileTools 
reload(fileTools)

import maya.cmds as mc
import json
import pymel.core as pm
import maya.mel as mm

def getJntData():
	joints = pm.selected(type='joint')
	for j in joints:
		skinClusters = j.worldMatrix[0].connections(type='skinCluster')
		for s in skinClusters:
			geo = s.getGeometry()[0]
			print ('%s influences %s via %s'%(j,geo,s))



def selectBindJnt(naming = '*_bind_jnt',**kwargs):
	if mc.ls(naming):
		mc.select(naming,**kwargs)
	else:
		mc.select('*_bJnt',**kwargs)



#... rename all skin cluster in scene
def renameSkinCluster():
	skinClusterList = mc.ls(type = 'skinCluster')
	ext = '_skc'
	for each in skinClusterList:
		if '_skc' not in each:
			geoName = mc.listConnections( each , type = 'mesh' )
			try:
				newName = mc.rename(each, str(geoName[0]) + ext)
				print ('changing name to %s'%newName)
			except:
				print ('%s has something wrong skiped.' %geoName)
				pass
		else:
			print ('%s already change name' %each)
			continue

	_renameAllBindpose()


#... rename all bindpose in scene
def _renameAllBindpose(ext = '_bindPose'):
	dagPoseList = mc.ls(type = 'dagPose')
	for each in dagPoseList:
		if ext not in each:
			skc_name  = mc.listConnections(each, type='skinCluster')[0]
			if skc_name:
				try:
					newName = mc.rename(each, f"{skc_name}{num:02d}{ext}")
					print(f'Changing name to {newName}')
					num = num + 1

				except Exception as e:
					print(f'{each} rename failed: {e}')
					num = num + 1
					continue
			else:
				print(f'{each} has no skinCluster connection, skipped.')
		else:
			print(f'{each} already renamed')
			continue

			
			




def _listJntSkinCluster():
	'''get the skin cluster and the joint'''

	try:
		selection = mc.ls(sl = True, fl = True)[0]
		# JointSelection = mc.ls( sl = True , type = "joint" )
		# We need the shape node to get the skincluster connection
		relatives = mc.listRelatives( selection, type = "shape" )
		sCluster = mc.listConnections( relatives, type = "skinCluster" )
		#get the joints in the skincluster
		#get skinCluster
		skinInfluences = mc.skinCluster( sCluster[0] , q = True,inf = True )

		# get tri count
		triCount = mc.polyEvaluate( selection ,triangle=True )

		num = 0
		# number of joint
		for each in skinInfluences:
			num = num + 1


		skcDict = 	{
			'skcName'	:	[]	,
			'number'	:	[]	,
			'listJnt'	:	[]	,
			'tris'		:	[]	,
			'polyName'	:	[]
					}

		skcDict['skcName'] = sCluster[0]
		skcDict['skinJnt'] = skinInfluences
		skcDict['number'] = num
		skcDict['tris'] = triCount
		skcDict['polyName'] = selection

		return skcDict

	except:	
		mc.warning('Please select geometry.')

# this function is redundance with auto export skin weight
def writeRigData():
	 # write skin joint list data 
	 # using for new naming condition only

	partFileName = mc.file( q = True , sn = True )
	splitfileName = partFileName.split('/')
	preName = splitfileName[len(splitfileName)-1]

	name = preName.split('.ma')[0]
	# PART FINDER
	folderPath = partFileName.split('/'+name)[0]

	
	DATA = _listJntSkinCluster()
	FILE_NAME = DATA['polyName'] + '_generalData' + '.json'

	if fileTools.ifHero():
		
		SAVE_PATH  = fileTools.desinatePath('\\data\\skinData\\')
		print ('this is a book'+SAVE_PATH)
	else:
		SAVE_PATH  = fileTools.desinatePath('\\data\\skinData\\')
		# if not exists create folder
		fileTools.checkExistFolder(SAVE_PATH)

	print (SAVE_PATH)
	FILE_PATH = SAVE_PATH + FILE_NAME

	f = open(	FILE_PATH, "w"	)
	f.write(	json.dumps( DATA , sort_keys=2, indent=4, )	)
	f.close()

	print ('File was save at: %s' %FILE_PATH)
	print ('\n')
	fileTools.makeHeader('Write complete')
	

'''
	f = open(SAVE_PATH, "w")
	f.write(json.dumps(list , sort_keys=2, indent=4, ))
	f.close()'''


# Parent joint to joint
def connectProxyJnt( master = 'bind_jnt' , slave = 'proxy_jnt' ):
	proxyJnt = mc.ls( '*'+ slave )
	for each in proxyJnt:
		bindJnt = each.replace( slave , master )
		#print bindJnt
		print ('constraint %s with %s' %(each,bindJnt))
		mc.parentConstraint(each, bindJnt)
		mc.scaleConstraint(each, bindJnt)
	print ('### CONNECT COMPLETE ###')
	 
		




#... copy selected weight
#... select source and destination
#... move from skin weight

def copyWeight():
	sels = mc.ls(sl=True)
	# query influence joint
	jnts = mc.skinCluster(sels[0], query=True, influence=True)
	# find skincluster in destination skin
	oldSkin = mm.eval('findRelatedSkinCluster("%s")' % sels[1])

	# check if have skin
	if oldSkin:
		# use arg for editable
		mc.skinCluster(oldSkin, edit = True, unbind = True)
	else:
		print ('%s is not have any skincluster' % sels[1])

	# toSelectedBones(tsb) = geometry will be bound to the selected bones only.
	# assign same skin cluster to destination
	newSkin = mc.skinCluster(jnts, sels[1], toSelectedBones=True)[0]

	# select source and destination
	mc.select(sels[0], replace=True)
	mc.select(sels[1], add=True)

	# copy weight
	mc.copySkinWeights(noMirror = True, surfaceAssociation = 'closestPoint',
					   influenceAssociation ='closestJoint')


#####################################################
#       multiple copyweight     
#####################################################

def mulWeight(source = ''):
	# select destination and source
	selection = mc.ls(sl=True)
	# destination = selection[1:]
	# source = selection[-1]
	#print 'source is %s, destination is %s' %selection,destination
	
	for each in selection:
		mc.select(source ,r=True)
		mc.select(each ,add=True)
		print ('%s has copied' %each)
		copyWeight()



# Convert selection to vertex
def creJntAtVertex():
	mc.select( mc.polyListComponentConversion( tv = True) )
	cluster = mc.cluster( relative = True, envelope = 1.0 )
	mc.select( clear = True )
	joint = mc.joint( scaleCompensate = False )
	snapPointConst(cluster[1], joint)
	mc.delete(cluster)