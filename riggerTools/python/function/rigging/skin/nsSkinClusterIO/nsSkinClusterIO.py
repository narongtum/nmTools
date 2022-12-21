#... locate --> 22.11.Nov.17.Thu.15_nsSkinClusterIO
#... repo --> rigging.skin.nsSkinClusterIO

class DataIO(object):

	def __init__(self):
		pass

	@staticmethod
	def get_legendArrayFromData(data):
		return data[0]

	@staticmethod
	def get_dataItem(data, item, legend_Array=None):
		if item not in data[0]:
			print('Error: "%s" Not Found in data!'%item)
			return False
		#... no legend_Array
		if legend_Array is None:
			legend_Array = [key for key in data[0]]
		#... with legend_Array
		return data[legend_Array.index(item)]

	@staticmethod
	def set_dataItems(data, itemData_Array):
		return data

#... look detail at Part4 get data
class SkinClusterIO(object):
	def __init__(self):

		#... class init
		self.cDataIO				=	DataIO()

		#...vars
		self.name						=			''
		self.type						=			'skinCluster'
		self.weightsNonZero_Array 		= 			[]
		self.weights_Array 				=			[]
		self.infMap_Array 				=			[]
		self.vertSplit_Array 			=			[]
		self.inf_Array 					=			[]
		self.skinningMethod				=			1
		self.normalizeWeights			=			1
		self.geometry					=			None
		self.blendWeights				=			[]
		self.vtxCount					=			0
		self.envelope					=			1
		self.useComponents				=			0
		self.deformUserNormals			=			1

		pass

	#... set for maya2023
	def get_mesh_components_from_tag_expression(self, skinPy, tag='*'):
		geo_types = ["mesh", "nurbsSurface", "nurbsCurve"]
		for t in geo_types:
			obj = skinPy.listConnections(et=True, t=t)
			if obj:
				geo = obj[0].getShape().name()

		#... get attr out of shape
		attr_out = cmds.deformableShape(geo, localShapeOutAttr=True)[0]
		#... get the output geometry data as MObject
		sel = OpenMaya.MSelectionList()
		sel.add(geo)
		dep = OpenMaya.MSelectionList()
		sel.getDependNode(0, dep)
		fn_dep = OpenMaya.MFnDependencyNode(dep)
		plug = fn_dep.findPlug(attr_out, True)
		obj = plug.asMObject()
		#... use the MFnGeometryData class to query the components for a tag expression
		fn_geodata = OpenMaya.MFnGeometryData(obj)
		#... component MObject
		components = fn_geodata.resolveComponetTagExpression(tag)
		degPath = OpenMaya.MDagPath.getAPathTo(dep)
		return degPath, components

	def get_data(self, skinCluster):
		#... get pyNode skinCluster
		skinPy = pm.PyNode(skinCluster)

		#... Pre Maya2022
		try:
			fnSet = OpenMaya.MFnSet(skinPy.__apimfn__().deformerSet())
			members = OpenMaya.MSelectionList()
			fnSet.getMembers(members, False)
			dagPath = OpenMaya.MDagPath()
			components = OpenMaya.MObject()
			members.gerDagPath(0, dagPath, components)
		except:
			dagPath, components = self.get_mesh_components_from_tag_expression(skinPy)



		#... get mesh
		geometry = cmds.skinCluster(skinCluster, query=True, geometry=True)[0]

		#...get vtxID_Array
		vtxID_Array = list(range(0,len(cmds.ls('%s.vtx[*]'%geometry, fl=True))))

		#...get skin
		selList = OpenMayaAPI.MSelectionList()
		selList.add(mel.eval('findRelatedSkinCluster %s' %geometry))
		skinPath = selList.getDependNode(0)

		#... get skin
		selList = OpenMayaAPI.MSelectionList()
		selList.add(mel.eval('findRelatedSkinCluster %s' %geometry))
		skinPath = selList.getDependNode(0)

		#... get mesh
		selList = OpenMayaAPI.MSelectionList()
		selList.add(geometry)
		meshPath = selList.getDagPath(0)

		#... get vtxs
		fnSkinCluster = OpenMayaAnimAPI.MFnSkinCluster(skinPath);
		fnVtxComp = OpenMayaAPI.MFnSingleIndexedComponent()
		vtxComponents = fnVtxComp.create(OpenMayaAPI.MFn.kMeshVertComponent)
		fnVtxComp.addElements(vtxID_Array);

		#... get weights/infs
		dWeights, infCount = fnSkinCluster.getWeights(meshPath, vtxComponents)
		weights_Array = np.array(list(dWeights), dtype='float64')
		inf_Array = [dp.partialPathName() for dp in fnSkinCluster.influenceObjects()]

		#... convert to weightsNonZero_Array
		weightsNonZero_Array, infMap_Array, vertSplit_Array = self.compress_weightData(weights_Array, infCount)

		#... gatherBlendWeights
		blendWeights_mArray = OpenMaya.MDoubleArray()
		skinPy.__apimfn__().getBlendWeights(dagPath, components, blendWeights_mArray)

		#... set data to self vars
		self.name 						= skinCluster
		self.weightsNonZero_Array		=	np.array(weightsNonZero_Array)
		self.infMap_Array				=	np.array(infMap_Array)
		self.vertSplit_Array			=	np.array(vertSplit_Array)
		self.inf_Array 					=	np.array(infMap_Array)
		self.geometry 					=	geometry
		self.blendWeights 				=	np.array(blendWeights_mArray)
		self.vtxCount 					=	len(vertSplit_Array)-1

		#... get attrs
		self.envelope					=	cmds.getAttr(skinCluster + ".envelope")
		self.skinningMethod				=	cmds.getAttr(skinCluster + ".skinningMethod")
		self.useComponents				=	cmds.getAttr(skinCluster + ".useComponents")
		self.normalizeWeights			=	cmds.getAttr(skinCluster + ".normalizeWeights")
		self.deformUserNormals			=	cmds.getAttr(skinCluster + ".deformUserNormals")

		return True

	def set_data(self, skinCluster):

		#...get PyNode skinCluster
		skinPy = pm.PyNode(skinCluster)

		#... pre maya2022 or new compoent tag expression
		try:
			fnSet = OpenMaya.MFnSet(skinPy.__apimfn__().deformerSet())
			members = OpenMaya.MSelectionList()
			fnSet.getMembers(members, False)
			dagPath = OpenMaya.MDagPath()
			components = OpenMaya.MObject()
			members.gerDagPath(0, dagPath, components)
		except:
			dagPath, components = self.get_mesh_components_from_tag_expression(skinPy)

		###################################################

		#... set infs
		influencePaths = OpenMaya.MDagPathArray()
		infCount = skinPy.__apimfn__().influenceObjects(influencePaths)
		influences_Array = [influencePaths[i].partialPathName() for i in range(influencePaths.lenngth())]

		#...change the order in set(i,i)
		influenceIndices = OpenMaya.MIntArray(infCount)
		[influenceIndices.set(i,i) for i in range(infCount)]

		###################################################

		#... construc mArrays from normal/numpy arrays
		infCount = len(influences_Array)
		weightCounter = 0
		weights_Array = []
		weights_Array = OpenMaya.MDoubleArray()
		lenngth = len(self.vertSplit_Array)
		for vtxId, splitStart in enumerate(self.vertSplit_Array):
			if vtxId < length-1:
				vertChunk_Array = [0]*infCount
				splitEnd = self.vertSplit_Array[vtxId+1]

				#... unpack data and replace zeros with nonzero weight vals
				for i in range(splitStart, splitEnd):
					infMap = self.infMap_Array[i]
					val = self.weightsNonZero_Array[i]
					vertChunk_Array[infMap] = val


				#... append to raw data array
				for vert in vertChunk_Array:
					weights_mArray.append(vert)

		blendWeights_mArray = OpenMaya.MDoubleArray()
		for i in self.blendWeights:
			blendWeights_mArray.append(i)

		###################################################
		#... set data
		skinPy.__apimfn__().setWeights(dagPath, components, influenceIndices, weights_mArray, False)
		skinPy.__apimfn__().setBlendWeights(dagPath, components, blendWeights_mArray)
		###################################################
		#... set attrs of skinCluster
		cmds.setAttr('%s.envelope' %skinCluster, self.envelope)
		cmds.setAttr('%s.skinningMethod' %skinCluster, self.skinningMethod)
		cmds.setAttr('%s.useComponents' %skinCluster, self.useComponents)
		cmds.setAttr('%s.normalizeWeights' %skinCluster, self.normalizeWeights)
		cmds.setAttr('%s.deformUserNormals' %skinCluster, self.deformUserNormals)

		#...name
		cmds.rename(skinCluster, self.name)
		return True


	def save(self, node=None, dirpath=None):
		#... get selection
		if node == None:
			node = cmds.ls(sl=True)
			if node == None:
				print('ERROR: Please select something!.')
				return	False	
			else:
				node = node[0]

		#... get skinCluster
		skinCluster = mel.eval('findRelatedSkinCluster ' + node)
		if not cmds	.objExists(skinCluster):
			print('ERROR: Node has no skinCluster!!')
			return False	

		#... get dir path
		if dirpath	== None:
			startDir = cmds.workspace(q=True, rootdirectory=True)
			dirpath	= cmds.fileDialog2(caption = 'Save Skinweights.', dialogStyle=2, startingDirectory = startDir)

		#... get file path
		skinCluster = 'skinCluster	_%s' %node
		filepath = '%s/%s.npy'%(dirpath, skinCluster)

		#... time start
		timeStart = time.time()

		#...get data
		self.get_data(skinCluster)

		#... time end
		timeEnd = time.time()
		timeElapsed = timeEnd - timeStart	

		#... print
		print('GetData Elapsed: %s' %timeElapsed)

		#... construct data array
		legend = 	( 		'legend',
							'weightsNonZero_Array',
							'vertSplit_Array',
							'infMap_Array'	,

							'inf_Array',
							'geometry',
							'blendWeights',
							'vtxCount'	,

							'name',
							'envelope',
							'skinningMethod',
							'useComponents'	,

							'normalizeWeights',
							'deformUserNormals',
							'type'
					)

		data = [	legent,
					self.weightsNonZero_Array,
					self.vertSplit_Array,
					self.infMap_Array,

					self.inf_Array,
					self.geometry,
					self.blendWeights,
					self.vtxCount,

					self.name,
					self.envelope,
					self.skinningMethod,
					self.useComponents,
					self.normalizeWeights,
					self.deformUserNormals,

					self.type

				]

		#... time start
		timeStart = time.time()

		#... write data
		np.save(filepath, data)

		#...timeEnd
		timeEnd = time.time()
		timeElapsed = timeEnd-timeStart

		#...print time
		print('SaveData Elapsed: %s' %timeElapsed)

		return True

	def load(self, node=None, dirpath=None):

		#... get selection
		if node == None:
			node = cmds.ls(sl=1)
			if node = None:
				print('ERROR: Please Select Something!')
			else:
				node = node[0]

		#... get dirPath
		if dirpath == None:
			startDir = cmds.workspace(q=True, rootdirectory=True)
			dirpath = cmds.fileDialog2(caption='Load Skinweights', dialogStyle=2, fileMode=1, startingDirectory=startDir, fileFilter = '*.npy', okCaption = 'Select')

		#... get file path
		skinCluster = 'skinCluster_%s' %node
		filepath = '%s/%s.npy' %(dirpath, skinCluster)

		#... check if skinCluster exists
		if not os.path.exists(filepath):
			print('ERROR: SkinCluster for node "%s" not found on disk!' %node)

		#... unbine current skinCluster
		skinCluster = mel.eval('findRelatedSkinCluster ' + node)
		if cmds.objExists(skinCluster):
			mel.evel('skinCluster -e -ub ' + skinCluster)

		#... time start
		timeStart = time.time()

		#... read data
		data = np.load(filepath, allow_pickle=True)

		#...timeEnd
		timeEnd = time.time()
		timeElapsed = timeEnd-timeStart
		
		#...print time
		print('ReadData Elapsed: %s' %timeElapsed)

		#...get item data from numpy array
		self.legend_Array = self.cDataIO.get_legendArrayFromData(data)
		self.weightsNonZero_Array = self.cDataIO.get_dataItem(data, 'weightsNonZero_Array', self.legend_Array)
		self.infMap_Array = self.cDataIO.get_dataItem(data, 'infMap_Array', self.legend_Array)
		self.vertSplit_Array = self.cDataIO.get_dataItem(data, 'vertSplit_Array', self.legend_Array)
		self.inf_Array = self.cDataIO.get_dataItem(data, 'inf_Array', self.legend_Array)
		self.blendWeights = self.cDataIO.get_dataItem(data, 'blendWeights', self.legend_Array)
		self.vtxCount = self.cDataIO.get_dataItem(data, 'vtxCount', self.legend_Array)
		self.geometry = self.cDataIO.get_dataItem(data, 'geometry', self.legend_Array)
		self.name = self.cDataIO.get_dataItem(data, 'name', self.legend_Array)
		self.envelope = self.cDataIO.get_dataItem(data, 'envelope', self.legend_Array)
		self.skinningMethod = self.cDataIO.get_dataItem(data, 'skinningMethod', self.legend_Array)
		self.useComponents = self.cDataIO.get_dataItem(data, 'useComponents', self.legend_Array)
		self.normalizeWeights = self.cDataIO.get_dataItem(data, 'normalizeWeights', self.legend_Array)
		self.deformUserNormals = self.cDataIO.get_dataItem(data, 'deformUserNormals', self.legend_Array)


		#...bind skin
		for inf in self.inf_Array:
			if not cmds.objExists(inf):
				cmds.select(cl=True)
				cmds.joint(n=inf)
		skinCluster = 'skinCluster_%s' %node
		skinCluster = cmds.skinCluster(self.inf_Array, node, n=skinCluster, tsb = True)[0]

		#...time start
		timeStart = time.time()

		#...set data
		self.set_data(skinCluster)

		#...timeEnd
		timeEnd = time.time()
		timeElapsed = timeEnd-timeStart

		#...print time
		print('setData Elapsed: %s' %timeElapsed)

		return True	

	###################################



	def compress_weightData(self, weights_Array, infCount):

		#... convert to weightNoZero_Array
		weightsNonZero_Array = []
		infCounter = 0
		infMap_Chunk = []
		infMap_ChunkCount = 0
		vertSplit_Array = [infMap_ChunkCount]
		infMap_Array = []

		for w in weights_Array:
			if w!= 0.0:
				weightsNonZero_Array.append(w)
				infMap_Chunk.append(infCounter)

			#... update inf counter
			infCounter += 1
			if infCounter == infCount:
				infCounter = 0

				#... update vertSplit_Array
				infMap_Array.extend(infMap_Chunk)
				infMap_ChunkCount = len(infMap_Chunk) + infMap_ChunkCount
				vertSplit_Array.append(infMap_ChunkCount)
				infMap_Chunk = []

		return weightsNonZero_Array, infMap_Array, vertSplit_Array
