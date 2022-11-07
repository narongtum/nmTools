
###########################

#Title: skinClusterIO.py
#Author: Noah Schnapp
#LinkedIn: https://www.linkedin.com/in/wnschnapp/

###########################
####### IMPORTS ###########
###########################

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as OpenMayaAPI
import maya.api.OpenMayaAnim as OpenMayaAnimAPI
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMaya as OpenMaya
import os

import numpy as np
import json

import time

from function.rigging.util import misc
from function.framework.reloadWrapper import reloadWrapper as reloader
reloader(misc)


#...SCRIPT EDITOR USE

'''
import sys 
import imp 
dirpath = r"D:\narongtum\research_and_developement\my tutorial\22.08.Aug.26.Fri.17_The Fastest SkinCluster ExportImport- A Studio Workflow The Art of Compression"
sys.path.insert(0, dirpath) 
import nmSkinClusterIO_v001 as skinClusterIO
reload(skinClusterIO)
skinClusterIO.create_sphereSkin()
'''

def create_sphereSkin():

	#...vars
	mesh = 'mesh'
	smoothDivisions = 4
	jntCount = 100

	#...file new
	cmds.file(new=True, f=True)
	#...create sphere
	cmds.polySphere(n=mesh, r=5)
	#...smooth
	cmds.polySmooth(mesh, divisions=smoothDivisions)
	cmds.delete(mesh, ch=True)
	#...create joints
	cmds.select(cl=True)
	jnt_Array = [cmds.joint() for j in range(jntCount)]
	#...bind
	skinCluster = cmds.skinCluster(jnt_Array, mesh, n='skinCluster_mesh', tsb = True)[0]


def devSave():

	#...init class
	cSkinClusterIO_json = SkinClusterIO_jason()

	#...vars
	mesh = 'mesh'

	#...timeStart
	timeStart = time.time()

	#...run
	cSkinClusterIO_json.save(mesh, dirpath=dirpath)

	#...timeEnd
	timeEnd = time.time()
	timeElapsed = timeEnd - timeStart

	#...print time
	print('Total Elapsed: %s' %timeElapsed)

	return True




































def devLoad():

	#...init class
	cSkinClusterIO_json - SkinClusterIO_jason()
	cSkinClusterIO = SkinClusterIO()

	#...vars
	mesh = 'mesh'

	#...timeStart
	timeStart = time.time()

	#...run
	cSkinClusterIO.load(mesh, dirpath=dirpath)

	#...timeEnd
	timeEnd = time.time()
	timeElapsed = timeEnd - timeStart

	#...print time
	print('Total Elapsed: %s' %timeElapsed)

	return True


def devSaveLoad():

	#...create demo
	# create_sphereSkin()
	devSave()
	devLoad()

	return True

class SkinClusterIO_jason(object):

	def __init__(self):

		#...class init
		self.cDataIO		=	DataIO()

		#... vars
		self.name			=	''
		self.type			=	'skinCluster'
		self.weightsNonZero_Array	=	[]
		self.weights_Array 			=	[]
		self.infMap_Array			=	[]
		self.vertSplit_Array		=	[]
		self.inf_Array 				=	[]
		self.skinningMethod			=	1
		self.normalizeWeights		=	1
		self.geometry				=	None
		self.blendWeights			=	[]
		self.vtxCount				=	0
		self.evelope				=	1
		self.skinningMethod			=	1
		self.useComponents			=	0
		self.normalizeWeights		=	1
		self.deformUserNormals		=	1

		pass


	def get_data(self, skinCluster):
		#... get the MFnSkinCluster for skinCluster
		selList = OpenMaya.MSelectionList()
		selList.add(skinCluster)
		clusterNode = OpenMaya.MObject()
		selList.getDependNode(0, clusterNode)
		skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)

		#...get components
		fnSet = OpenMaya.MFnSet(skinFn.deformerSet())
		members = OpenMaya.MSelectionList()
		fnSet.getMembers.(members, False)
		dagPath = OpenMaya.MDagPath()
		components = OpenMaya.MObject()
		members.getDagPath(0, dagPath, components)

	#...get selection
	def save(self, node=None, dirpath=None):
		if node==None:
			node = cmds.ls(sl=True)
			if node == None:
				print('ERROR: Select Something!')
				return False
			else:
				node = node[0]

	#...get skinCluster
	skinCluster = mel.eval('findRelatedSkinCluster ' + node)
	if not cmds.objExists(skinCluster):
		print('ERROR: Node has no skinCluster!')

	#...get dirpath
	if dirpath == None:
		startDir = cmds.workspace(q=True, rootDirectory=True)
		dirpath = cmds.fileDialog2(caption='Save Skinweights', dialogStyle=2, fileMode=3, startingDirectory=startDir, okCaption = 'Select')

	#...get filepath
	skinCluster='skinCluster_%s' %node
	filepath = '%s/%s' %(dirpath, skinCluster)

	#...timeStart (how long to take the data)
	timeStart = time.time()

	#...get skin data
	data = {}
	shape = cmds.listRelatives(node, c=True)[0]
	vtx_Array = ["{0}.vtx[{1}]".format(shape, x) for x in cmds.getAttr(shape + '.vrts', multiIndices=True)]
	for vtx in vtx_Array:
		inf_Array = cmds.skinPercent(skinCluster, vtx, transform=None, q=1)
		weights = cmds.skinPercent(skinCluster, vtx, q=1, v=1)
		data[vtx] = zip(inf_Array, weights)

	#...timeEnd
	timeEnd = time.time()
	timeElapsed = timeEnd - timeStart

	#...print time
	print('GetData Elapsed: %s' %timeElapsed)

	#...timeStart (how long to take the data)
	timeStart = time.time()

	#...write data 
	fh = open(filepath, 'w')
	json = dump(data, fh, 0)
	fh.close()

	#...timeEnd
	timeEnd = time.time()
	timeElapsed = timeEnd-timeStart

	#...print time
	print('SaveData Elapsed: %s'%timeElapsed)

	# return True