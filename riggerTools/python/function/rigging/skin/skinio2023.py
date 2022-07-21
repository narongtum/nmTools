# source: nomanTools\21.05.May.11.Tue_skin export API method
# Skin Import / Export 
# from Chad Vernon
# Noman EDIT version


'''
# direct run
from function.rigging.skin import skinio
reload(skinio)


skinio.show()

'''

from function.framework.reloadWrapper import reloadWrapper as reload

from functools import partial

try:
	import cPickle as pickle
except:
	import pickle as pickle

import maya.cmds as mc
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI
import maya.OpenMayaAnim as OpenMayaAnim

from function.rigging.util import misc
reload(misc)

from function.framework.Qtpy.Qt import QtCore, QtGui, QtWidgets

try:
	from shiboken2 import wrapInstance
except:
	from sid import wrapInstance as wrapInstance

from function.pipeline import fileTools as fileTools 
reload(fileTools)





# change from QtGui to QtWidgets


# from function.framework.Qtpy.Qt import *

'''try:
	from PySide import QtGui
	from PySide import QtCore
	from shiboken import wrapInstance
	
except:
	# from PyQt4 import QtGui
	# from PyQt4 import QtCore
	from sid import wrapInstance as wrapInstance'''








# set logging for debug from justin isral
import logging

logger = logging.getLogger('debug_text')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


# prevent logging from bubbling up to maya's logger
logger.propagate=0

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')



# for disable logging
# logging.disable(logging.CRITICAL)

logger.debug('Start of program')


def show():
	dialog = SkinIODialog(getMayaWindow())
	dialog.show()


# import skinio
# skinio.show()


# get this window on top
# said about parent window on top at 1:16 (crateing the remapping dialog)

def getMayaWindow():
	ptr = OpenMayaUI.MQtUtil.mainWindow()
	try:
		return wrapInstance(long(ptr), QtWidgets.QMainWindow)
	except:
		return wrapInstance(int(ptr), QtWidgets.QMainWindow) # python 3 format

def getShape(node,intermediate=False):
	"""
	get the shape from specified node.
	@param[in] node Name of a transform or shape nodeType
	@param[in] intermediate True to get the intermediate shape, False to get the visible shape visible
	@return the name fo the desired shape node
	"""

	if mc.nodeType(node) == 'transform':
		shapes = mc.listRelatives(node,shapes=True,path=True)
		if not shapes:
			shapes = []

		for shape in shapes:
			isIntermediate = mc.getAttr('%s.intermediateObject' %shape)
			# sometimes there art left over intermediate shapes that are not used so
			# check the connections to make sure we get the one that is used.is
			if intermediate and isIntermediate and mc.listConnections(shape,source=False):
				return shape
			elif not intermediate and not isIntermediate:
				return shape

		if shapes:
			return shapes[0]

	elif mc.nodeType(node) in ['mesh','nurbeCurve','nurbeSurface']:
		return node

	return None











class SkinCluster(object):

	kFileExtension = '.skin'


	@classmethod
	def createAndImport(cls, filePath=None, shape=None):
		"""Creates a skinCluster on the specified shape if one does not already exist
		and then import the weight data."""
		if not shape:
			try:
				shape = mc.ls(sl=True)[0]
			except:
				raise RuntimeError('No shape selected')

		if filePath == None:
			startDir = mc.workspace(q=True, rootDirectory=True)

			# add another folder
			startDir += r'skin/' 

			# check if that folder exists
			fileTools.checkExistFolder(filename = startDir)

			# add name from selection
			selected = mc.ls(sl=True)[0]
			startDir += selected

			filePath = mc.fileDialog2(dialogStyle=2, fileMode=1, startingDirectory=startDir,
										fileFilter='Skin Files (*%s)' % SkinCluster.kFileExtension)

		if not filePath:
			return
		if not isinstance(filePath, basestring):
			filePath = filePath[0]

		# Read in the file
		fh = open(filePath, 'rb')
		data = pickle.load(fh)
		fh.close()

		# Make sure the vertex count is the same
		meshVertices = mc.polyEvaluate(shape, vertex=True)
		importedVertices = len(data['blendWeights'])
		if meshVertices != importedVertices:
			raise RuntimeError('Vertex counts do not match. %d != %d' %
					(meshVertices, importedVertices))

		# Check if the shape has a skinCluster
		if SkinCluster.getSkinCluster(shape):
			skinCluster = SkinCluster(shape)
		else:
			# Create a new skinCluster
			joints = data['weights'].keys()

			# Make sure all the joints exist
			unusedImports = []
			noMatch = set([SkinCluster.removeNamespaceFromString(x)
						  for x in mc.ls(type='joint')])
			for j in joints:
				if j in noMatch:
					noMatch.remove(j)
				else:
					unusedImports.append(j)
			# If there were unmapped influences ask the user to map them
			if unusedImports and noMatch:
				mappingDialog = WeightRemapDialog(getMayaWindow())
				mappingDialog.setInfluences(unusedImports, noMatch)
				mappingDialog.exec_()

				# print 'this is dict: '+mappingDialog.mapping.items()

				for src, dst in mappingDialog.mapping.items():

					# Swap the mapping
					# alway error here dunno why
					data['weights'][dst] = data['weights'][src]
					del data['weights'][src]

			# Create the skinCluster with post normalization so setting the weights does not
			# normalize all the weights
			joints = data['weights'].keys()
			skinCluster = mc.skinCluster(joints, shape, tsb=True, nw=2, n=data['name'])
			skinCluster = SkinCluster(shape)

		skinCluster.setData(data)
		print ('Imported %s' % filePath)



	@classmethod
	def getSkinCluster(cls, shape):
		"""Get the skinCluster node attached to the specified shape.

		@param[in] shape Shape node name
		@return The attached skinCluster name or None if no skinCluster is attached."""
		shape = getShape(shape)
		history = mc.listHistory(shape, pruneDagObjects=True, il=2)
		if not history:
			return None
		skins = [x for x in history if mc.nodeType(x) == 'skinCluster']
		if skins:
			return skins[0]
		return None


	@classmethod
	def export(cls, filePath=None, shape=None):
		skin = SkinCluster(shape)
		logger.debug(filePath)
		skin.exportSkin(filePath)


	@classmethod
	def removeNamespaceFromString(cls, value):
		# error type 'From' wrong
		"""remove name space from a namespaceFormString
		Changes NAMESPACE:joint1:NAMESPACE:joint2 to joint1:joint2

		@Param[in] string name with a namespaceFormString
		@return the name without namespace

		"""

		tokens = value.split('|')
		result = ''


		for i, token in enumerate(tokens):
			if i > 0:
				result += '|'
			result += token.split(':')[-1]
		return result


	def __init__(self, shape=None):
		"""Constructor"""
		if not shape:
			try:
				shape = mc.ls(sl=True)[0]
			except:
				raise RuntimeError('No shape selected.')


		# get shape node
		self.shape = getShape(shape)
		if not self.shape:
			raise RuntimeError('No shape connected to %s' %shape)


		# get the skinCluster node attached to the shape
		self.node = SkinCluster.getSkinCluster(shape)
		if not self.node:
			raise RuntimeError('No skinCluster attached to %s' %self.shape)


		# get the skinCluster MObject 
		selectionList = OpenMaya.MSelectionList()# get the MObject
		selectionList.add(self.node)

		self.mobject = OpenMaya.MObject()
		selectionList.getDependNode(0, self.mobject)
		# looking at http://docs.autodesk.com/MAYAUL/2014/ENU/Maya-API-Documentation/index.html
		self.fn = OpenMayaAnim.MFnSkinCluster(self.mobject)
		self.data = {
				'weights' : {},
				'blendWeights' : [],
				'name' : self.node
				}

	def gatherData(self):
		dagPath, components = self.__getGeometryComponents()
		self.gatherInfluenceWeights(dagPath, components)
		self.gatherBlendWeights(dagPath, components)

		for attr in ['skinningMethod', 'normalizeWeights']:
			self.data[attr] = mc.getAttr('%s.%s' %(self.node, attr))


	def __getGeometryComponents(self):
		# get dagPath and member components of skin shape
		# myError 1. "MFnset" is wrong 
		# "MFnSet" is correct 
		fnSet = OpenMaya.MFnSet(self.fn.deformerSet())
		members = OpenMaya.MSelectionList()
		fnSet.getMembers(members, False)
		dagPath = OpenMaya.MDagPath()
		components = OpenMaya.MObject()
		members.getDagPath(0, dagPath, components)
		# myError 2. forget to return
		return dagPath, components




	def gatherInfluenceWeights(self, dagPath, components):
		# gather all the Influence Weights
		weights = self.__getCurrentWeights(dagPath,components)

		influencePaths = OpenMaya.MDagPathArray()
		numInfluences = self.fn.influenceObjects(influencePaths)

		numComponentsPerInfluence = weights.length() / numInfluences

		for ii in range(influencePaths.length()):
			influenceName = influencePaths[ii].partialPathName()
			# we want to store the weights by influence withoit the namespace so it is easier
			# to import if the namesapce is diffenrenct
			influenceWithoutNamespace = SkinCluster.removeNamespaceFromString(influenceName)
			# store data
			self.data['weights'][influenceWithoutNamespace] = \
					[weights[jj*numInfluences+ii] for jj in range(numComponentsPerInfluence)]


	# https://help.autodesk.com/view/MAYAUL/2017/ENU/?guid=__cpp_ref_class_m_fn_skin_cluster_html
	# look under
	# Member Function Documentation

	def __getCurrentWeights(self, dagPath, components):
		"""Get the current weight array"""
		weights = OpenMaya.MDoubleArray()
		util = OpenMaya.MScriptUtil()
		util.createFromInt(0)
		# error wrong attr 'asUinPtr'
		pUInt = util.asUintPtr()
		self.fn.getWeights(dagPath, components, weights, pUInt)
		return weights


	def gatherBlendWeights(self, dagPath, components):
		""" gather the blend wiehgts """

		weights = OpenMaya.MDoubleArray()
		# type error 
		self.fn.getBlendWeights(dagPath, components, weights)
		self.data['blendWeights'] = [weights[i] for i in range(weights.length())]



	def exportSkin(self, filePath=None):
		"""export the skinCluster data to disk
		@param[in] filePath file path"""

		if filePath == None:
			# dir that set project
			startDir = mc.workspace(q=True, rootDirectory=True)

			# add another folder
			startDir += r'skin/' 

			# check if that folder exists
			fileTools.checkExistFolder(filename = startDir)

			# add name from selection
			selected = mc.ls(sl=True)[0]
			startDir += selected

			filePath = mc.fileDialog2(dialogStyle=2, fileMode=0, startingDirectory=startDir,
										fileFilter='Skin Files (*%s)' % SkinCluster.kFileExtension)						

		if not filePath:
			logger.debug('Shape not found please check.')
			return
		filePath = filePath[0]
		if not filePath.endswith(SkinCluster.kFileExtension):
			filePath += SkinCluster.kFileExtension

		self.gatherData()

		# call the pickle function
		fh = open(filePath, 'wb')
		pickle.dump(self.data, fh, pickle.HIGHEST_PROTOCOL)
		logger.info('Export the skin DONE yeah')
		fh.close()

		print('Exported skinCluster (%d influences, %d vertices)%s' %(
				len(self.data['weights'].keys()), len(self.data['blendWeights']), filePath))



	def setData(self, data):
		""" sets the data and stores it in the Maya skinCluster node. 

		@param[in] data Data dictionary"""

		self.data = data

		dagPath, components = self.__getGeometryComponents()
		self.setInfluenceWeights(dagPath, components)
		self.setBlendWeights(dagPath, components)

		for attr in ['skinningMethod', 'normalizeWeights']:
			mc.setAttr('%s.%s' %(self.node, attr), self.data[attr])


	def setInfluenceWeights(self, dagPath, components):
		""" sets all the influences weights"""
		weights = self.__getCurrentWeights(dagPath,components)
		influencePaths = OpenMaya.MDagPathArray()
		numInfluences = self.fn.influenceObjects(influencePaths)
		numComponentsPerInfluence = weights.length() / numInfluences

		# keep track of whicg imported influences aren't unused
		unusedImports = []

		# keep track of whick existing influences don't get anyrhing imported
		noMatch = [influencePaths[ii].partialPathName() for ii in range(influencePaths.length())]




		
		for importedInfluence, importedWeights in self.data['weights'].items():
			for ii in range(influencePaths.length()):
				influenceName = influencePaths[ii].partialPathName() # partialpath is fullpath name
				influenceWithoutNamespace = SkinCluster.removeNamespaceFromString(influenceName)

				if influenceWithoutNamespace == importedInfluence:
					# store the imported weights into the MDoubleArray
					for jj in range(numComponentsPerInfluence):
						weights.set(importedWeights[jj], jj*numInfluences+ii)
					noMatch.remove(influenceName)
					break
			else:
				unusedImports.append(importedInfluence)

		
		if unusedImports and noMatch:
			mappingDialog = WeightRemapDialog(getMayaWindow())
			mappingDialog.setInfluences(unusedImports, noMatch)
			mappingDialog.exec_()

			for src, dst in mappingDialog.mapping.items():
				for ii in range(influencePaths.length()):
					if influencePaths[ii].partialPathName() == dst:
						for jj in range(numComponentsPerInfluence):
							weights.set(self.data['weights'][src][jj], jj*numInfluences+ii)
						break
		



		influenceIndices = OpenMaya.MIntArray(numInfluences)
		for ii in range(numInfluences):
			influenceIndices.set(ii, ii)
		self.fn.setWeights(dagPath, components,influenceIndices,weights,False)



	def setBlendWeights(self, dagPath, components):
		""" set the blendWeights"""
		blendWeights = OpenMaya.MDoubleArray(len(self.data['blendWeights']))
		for i,w in enumerate(self.data['blendWeights']):
			blendWeights.set(w, i)

		self.fn.setBlendWeights(dagPath, components, blendWeights)





 
class WeightRemapDialog(QtWidgets.QDialog):


	def __init__(self, parent=None):
		super(WeightRemapDialog, self).__init__(parent)
		self.setWindowTitle('Remap Weights')
		self.setObjectName('remapWeightsUI')
		self.setModal(True)
		self.resize(600,400)
		self.mapping={}

		mainVbox = QtWidgets.QVBoxLayout(self)
		label = QtWidgets.QLabel('The following influences have no corresponding influence from the imported file you can enither remap the influences or skip them')

		label.setWordWrap(True)
		mainVbox.addWidget(label)

		hbox = QtWidgets.QHBoxLayout()
		mainVbox.addLayout(hbox)


		# The existing influences that didn't have weight imported
		vbox = QtWidgets.QVBoxLayout()
		hbox.addLayout(vbox)
		vbox.addWidget(QtWidgets.QLabel('Unmapped influences'))
		self.existingInfluences = QtWidgets.QListWidget()
		vbox.addWidget(self.existingInfluences)


		# the existing influence that didnl't have weight importedInfluences
		vbox = QtWidgets.QVBoxLayout()
		hbox.addLayout(vbox)
		vbox.addWidget(QtWidgets.QLabel('Available imported influences'))
		scrollArea = QtWidgets.QScrollArea()
		widget = QtWidgets.QScrollArea()
		self.importedInfluenceLayout = QtWidgets.QVBoxLayout(widget)

		

		vbox.addWidget(widget)

		hbox = QtWidgets.QHBoxLayout()
		mainVbox.addLayout(hbox)
		hbox.addStretch()
		btn = QtWidgets.QPushButton('Ok')
		btn.released.connect(self.accept)
		hbox.addWidget(btn)


	def setInfluences(self, importedInfluences, existingInfluences):
		infs = list(existingInfluences)
		infs.sort()
		self.existingInfluences.addItems(infs)
		width = 200
		for inf in importedInfluences:
			# row = QtWidgets.QLayout(inf)
			row = QtWidgets.QHBoxLayout()
			self.importedInfluenceLayout.addLayout(row)
			label = QtWidgets.QLabel(inf)
			row.addWidget(label)
			toggleBtn = QtWidgets.QPushButton('>')
			toggleBtn.setMaximumWidth(30)
			row.addWidget(toggleBtn)
			label = QtWidgets.QLabel('')
			label.setMaximumWidth(width)
			label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
			row.addWidget(label)
			toggleBtn.released.connect(partial(self.setInfluenceMapping, src=inf, label=label)) # partial is callback allow to pass in arg
		self.importedInfluenceLayout.addStretch()


	def setInfluenceMapping(self, src, label):
		selectedInfluence = self.existingInfluences.selectedItems()
		if not selectedInfluence:
			return
		dst = selectedInfluence[0].text()
		label.setText(dst)
		self.mapping[src] = dst
		# Remove the item from the list
		index = self.existingInfluences.indexFromItem(selectedInfluence[0])
		item = self.existingInfluences.takeItem(index.row())
		del item



# class SkinIODialog(QtWidgets.QDialog):
class SkinIODialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(SkinIODialog, self).__init__(parent)
		self.setWindowTitle('Skin IO')
		self.setObjectName('skiniowidget')
		self.setModal(False)
		self.setFixedSize(200,80)

		vbox = QtWidgets.QVBoxLayout(self)
		btn = QtWidgets.QPushButton('Export')
		btn.released.connect(SkinCluster.export)
		vbox.addWidget(btn)
		btn = QtWidgets.QPushButton('Import')
		btn.released.connect(SkinCluster.createAndImport)
		vbox.addWidget(btn)


logger.debug('End of program')