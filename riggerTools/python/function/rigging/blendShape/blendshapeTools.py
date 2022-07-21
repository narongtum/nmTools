# Step



# 1. prepare "facialBase_ply" and set grp name "facialBshBase_grp"

# 1. cut head poly to the grp name it "facialBshBase_grp"
# name polygon "facialBase_ply"


# 2. exe this function 
# 3. run duplicate ply for blendshape
# 4. make blendshape
# 5. import facial controller and reprositioning controller for each facial part



'''

from function.rigging.blendShape import blendshapeTools as bshTools
reload(bshTools)



# Eyebrow
eyeBrowLFT_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYEBROW_DICT , side = 'LFT')
eyeBrowRGT_dict  = bshTools.createBshToPly( bsh_dict = bshTools.EYEBROW_DICT , side = 'RGT')

# Eyelid All
eyelidAll_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELIDALL_DICT , side = 'LFT')
eyelidAll_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELIDALL_DICT , side = 'RGT')




'''
import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.util import boundingBox as bBox
reload(bBox)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

import pprint

# Base name type

# Eye
upLid = ['upLid' ]
loLid = ['loLid' ]

# Name of Position
upDown = ['Up' , 'Dn']
# up down inbetween
upDwnInb = ['UpInbA' , 'DnInbA']

inOut = ['In' , 'Out']
leftRight = ['LFT' , 'RGT']
twist = ['FC' , 'CC']
position = ['Inner' , 'Mid' , 'Outer']


# name of side
SIDES = ['LFT' , 'RGT' ]
separater = '#'*25



# - - - - - - - - Eyebrow - - - - - - - - # 
EYEBROW_DICT = { 	'facialRegion'	:	'eyebrow',
					'attrBshNam' 	:	[ 'eyebrowAll' , 'eyebrowInn' , 'eyebrowMid' , 'eyebrowOut' ]	,
					'bshBeheavior'	:	[ upDown+inOut , upDown , upDown , upDown ] 			,
					'posiBlock'		:	(1,1)															,
					'side'			:	True																}


# - - - - - - - - Eyeball - - - - - - - - # 
EYELID_ALL_DICT = { 	'facialRegion'	:	'eyeBall',
					'attrBshNam' 	:	['eyeBall' ,'eyeCnrInn' ,'eyeCnrOut']		,
					'bshBeheavior'	:	[ upDown+inOut+twist , upDown , upDown ] 			,
					'posiBlock'		:	(3,1)															,
					'side'			:	True}


# - - - - - - - - Eyelid upper - - - - - - - - # 
EYELID_UP_DICT = { 	'facialRegion'	:	'eyeLidUp',
					'attrBshNam' 	:	[ 'upLid', 'upLidInn', 'upLidMid', 'upLidOut']	,
					'bshBeheavior'	:	[ upDown+upDwnInb+twist ,['Dn']+['DnInbA'] ,['Dn']+['DnInbA'] ,['Dn']+['DnInbA'] ] 			,
					'posiBlock'		:	(4,1)															,
					'side'			:	True																}


# - - - - - - - - Eyelid lower - - - - - - - - # 
EYELID_LO_DICT = { 	'facialRegion'	:	'eyeLidLo',
					'attrBshNam' 	:	[ 'loLid', 'loLidInn', 'loLidMid', 'loLidOut']	,
					'bshBeheavior'	:	[  upDown+upDwnInb+twist ,['Up']+['UpInbA'] ,['Up']+['UpInbA'] ,['Up']+['UpInbA'] ] 			,
					'posiBlock'		:	(5,1)															,
					'side'			:	True																}


# - - - - - - - - Mounth - - - - - - - - # 
# mounth middle
LIP_ALL_DICT = { 	'facialRegion'	:	'mounthMid',
					'attrBshNam' 	:	[ 'mounth','upLipMid'   ,'loLipMid','mounthCurl' ,'mounthClench' ,'mounthPull','mounthU' ]	,
					'bshBeheavior'	:	[ upDown+leftRight+twist ,upDown    ,upDown      ,inOut  ,inOut ,inOut ,inOut] 			,
					'posiBlock'		:	(7,1)															,
					'side'			:	False																}



# mounth side 
LIP_SIDE_DICT = { 	'facialRegion'	:	'lip',
					'attrBshNam' 	:	['upLip' ,'loLip' ,'mounthCnr' ,'lipPart']			,
					'bshBeheavior'	:	[upDown ,upDown ,upDown+inOut ,inOut] 		,
					'posiBlock'		:	(8,1)		,
					'side'			:	True	}






# - - - - - - - - Jaw - - - - - - - - # 
# jaw
JAW_DICT = { 	'facialRegion'	:	'jaw',
					'attrBshNam' 	:	[ 'jaw' ]	,
					'bshBeheavior'	:	[ ['Sq','St'] ] 			,
					'posiBlock'		:	(10,1)				,
					'side'			:	False	}



# - - - - - - - - Cheek - - - - - - - - # 
# cheek
CHEEK_DICT = { 	'facialRegion'	:	'cheek',
					'attrBshNam' 	:	[ 'cheekUp' , 'cheekLo' ,'puff']	,
					'bshBeheavior'	:	[ inOut ,inOut ,inOut] 			,
					'posiBlock'		:	(11,1)				,
					'side'			:	True	}


# - - - - - - - - Nose - - - - - - - - # 
# nose all
NOSE_ALL_DICT = { 	'facialRegion'	:	'nose',
					'attrBshNam' 	:	[ 'nose']	,
					'bshBeheavior'	:	[ ['Sq','St'] ] 			,
					'posiBlock'		:	(12,1)				,
					'side'			:	False	}


# nose side
NOSE_SIDE_DICT = { 	'facialRegion'	:	'nose',
					'attrBshNam' 	:	[ 'nose']	,
					'bshBeheavior'	:	[ upDown+twist ] 			,
					'posiBlock'		:	(13,1)				,
					'side'			:	True	}			







def createBshToPly( bsh_dict, side):
	'''
	Duplicate base geometry for each facial in dict in the same collum

	@param bsh_dict: dictionary from this module
	@type bsh_dict: dictionary

	@param side: side
	@type side: string

	'''

	bshMember = []
	getBshGrp = []

	# ==========
	# - Checks - match of attribure name and bsh beheavior ?
	# ==========

	if not len(bsh_dict['attrBshNam']) == len(bsh_dict['bshBeheavior']):
		raise Exception('The number of attrBshNam and bshBeheavior is not match.')
		mc.error('The number of attrBshNam and bshBeheavior is not match.')

	xVal = 0


	if mc.objExists('facialBshBase_grp'):
		baseBsh_grp = 'facialBshBase_grp'
	else:
		mc.error('There is no group polygon for blendShape')


	basePoly_bsh = core.Dag( baseBsh_grp )
	# Get base name



	# Get size (old)
	# boundBox = mc.exactWorldBoundingBox(basePoly_bsh)
	# xmin, ymin, zmin, xmax, ymax, zmax.

	# Get size (Use new method to find size)
	boundBox = bBox.geoBoundingBox( 'facialBase_ply' )


	mulVal = 2
	xOffset = 0
	yOffset = 0
	yVal = 0


	bbY = int(	abs(boundBox[1] - boundBox[4])	)
	bbX = int(	abs(boundBox[0] - boundBox[3])	)

	if side == 'RGT':
		yOffset = 	bbY * 6.5  
		xOffset = 	bbX * 1.5

	elif side == 'LFT':
		yOffset = 	bbY * 6.5 
		xOffset = 	bbX * 3.0

	else:
		yOffset = 	bbY * 6.5  
		xOffset = 	bbX * 3.0

	# xOffset = 0.5

	print 'boundBox X is :%i' %bbX
	print 'boundBox Y is :%i' %bbY
	print 'This is %s part\n' %basePoly_bsh
	print 'This is %s posiBlock\n' %bsh_dict['posiBlock'][0]


	xVal += xOffset

	bshGrp = '%sBsh%s_grp' %(bsh_dict['facialRegion'],side)
	mc.group( em = True , n = bshGrp )

	getBshGrp.append(bshGrp)
	bshMember = []
	bshInbName = []
	base_crvName=[]

	i = 0

	for i in range (len(bsh_dict['attrBshNam'])):

		# yVal = 0
		eachAtt = bsh_dict['attrBshNam'][i]

		for eachBehav in bsh_dict['bshBeheavior'][i]:
			# print eachAtt + eachBehav + side + '_bsh'

			currBshNode = '%s%s%s_bsh' %(eachAtt,eachBehav,side)
			currBshSub = '%s%s%s_ply' %(eachAtt,eachBehav,side)

			# print currBshNode
			duppedNode = mc.duplicate( basePoly_bsh , rr = True )[0]
			mc.rename(duppedNode , currBshNode )

			mc.select(currBshNode , r = True)
			
			# rename member of this group is may cause error if member is more than 1
			mc.pickWalk(direction = 'down')
			headSel = mc.ls(sl=True)[0]
			mc.rename( headSel , currBshSub )
			
			mc.parent(currBshNode , bshGrp)
			mc.move( xOffset , yVal , 0 , currBshNode , r = True)
			# Skipt the inbetween blendshape
			if 'InbA' in currBshNode or 'InbB' in currBshNode :
				#currInb_bsh = core.Dag( currBshNode )
				#currInb_bsh.color = 'softGray'
				bshInbName.append(currBshNode)
			else:
				bshMember.append(currBshNode)
			
			# print '%s has move yVal to ' %currBshNode
			# print yVal

			yVal += yOffset*0.2


			
	print 'xVal is ' + '%i' %xOffset


	base_crvName.append( bsh_dict['facialRegion'] + 'All%s_bsh' %side )
	# mc.move( xVal , 0 , 0, bshGrp , r = True )


	bshData = { 'facialPart'	: bsh_dict['facialRegion'] 						,
				'baseBsh'		: basePoly_bsh 										,
				'bshBaseName'	: bsh_dict['facialRegion'] + 'All%s_bsh' %side 	,
				'bshMember'		: bshMember										,
				'bshInbName'	: bshInbName									,
				'bshGrp'		: bshGrp 										,
				'posiBlock'		: bsh_dict['posiBlock']							,
				'side' 			: bsh_dict['side']										}

	print '####################'
	print  bsh_dict['attrBshNam']
	print '####################'
	print '\n'
	print 'Position Block: ' + str(bsh_dict['posiBlock'][0])
	print '####################'
	mc.move( bshData['posiBlock'][0]*60 , 0 , 0 , bshData['bshGrp'] , r = True)

	mc.select(deselect = True)
	# add the last member 
	# bshMember.append(base_crv)


	# continue to write it on monday
	# xVal , yVal = bBox.getGeoRatio( bshData['baseBsh'] )
	bshList = bshData['bshMember'] + [ bshData['baseBsh'] ]
	# add parallel blendshape make chain to any existing deformers in the history of the object. A blendShape is inserted to blend the parallel results together. 
	bshMember = mc.blendShape( bshList , name =  bshData['bshBaseName'] ,parallel = True)
	return bshData





def _duplicateForBsh( bsh_dict ,side = '', nameSpace=None ):
	'''
	Duplicate curve prepare for blendshape
	@param bsh_dict: Global dictionary from this module
	@type bsh_dict: dictionary
	@param nameSpace: prepare for just in case
	@type nameSpace: str
	'''

	bshMember = []
	getBshGrp = []

	# ==========
	# - Checks - the number of pair data is equal ?
	# ==========

	if not len(bsh_dict['attrBshNam']) == len(bsh_dict['bshBeheavior']):
		raise Exception('The number of attrBshNam and bshBeheavior is not match.')


	xVal = 0

	try:
		base_crv = bsh_dict['facialRegion'] + 'Base%s'%side + '_crv'
	except:
		raise Exception('Object not exist! Please Checks at reference')

	base_bsh = core.Dag( base_crv )
	# Get base name

	# Get size
	boundBox = mc.exactWorldBoundingBox(base_crv)
	# xmin, ymin, zmin, xmax, ymax, zmax.

	# set the offset value
	# ymin - ymax
	yOffset = 	float(abs(boundBox[1] - boundBox[4]  * 1.025 ))
	# yOffset = 0.25	
	# xmin - xmax
	xOffset = 	float(abs(boundBox[0] - boundBox[3]  * 2 ))
	# xOffset = 0.5
	yVal = 0

	print 'This is %s part\n' %base_crv

	if bsh_dict['side']:

		if side == 'LFT':
			base_bsh.color = 'red'
		else:
			base_bsh.color = 'blue'
			xOffset = xOffset*0.65

		xVal += xOffset

		bshGrp = '%sBsh%s_grp' %(bsh_dict['facialRegion'],side)
		mc.group( em = True , n = bshGrp )

		getBshGrp.append(bshGrp)
		bshMember = []
		bshInbName = []
		base_crvName=[]


		for i in range (len(bsh_dict['attrBshNam'])):

			# yVal = 0
			eachAtt = bsh_dict['attrBshNam'][i]

			for eachBehav in bsh_dict['bshBeheavior'][i]:
				# print eachAtt + eachBehav + side + '_bsh'

				currBshNode = '%s%s%s_bsh' %(eachAtt,eachBehav,side)

				# print currBshNode
				duppedNode = mc.duplicate( base_crv , rr = True )[0]
				mc.rename(duppedNode , currBshNode )
				mc.parent(currBshNode , bshGrp)
				mc.move( 0 , yVal , 0 , currBshNode , r = True)
				# Skipt the inbetween blendshape
				if 'InbA' in currBshNode or 'InbB' in currBshNode :
					currInb_bsh = core.Dag( currBshNode )
					currInb_bsh.color = 'softGray'
					bshInbName.append(currBshNode)
				else:
					bshMember.append(currBshNode)
				
				# print '%s has move yVal to ' %currBshNode
				# print yVal

				yVal += yOffset

		# add the last member 
		# bshMember.append(base_crv)


		# print bshMember

		base_crvName.append( bsh_dict['facialRegion'] + 'All%s_bsh' %side )
		# Create blendshape
		# mc.blendShape( bshMember , name = bsh_dict['facialRegion'] + 'All%s_bsh' %side)

		mc.move( xVal , 0 , 0, bshGrp , r = True )
		print '%s has move to ' %bshGrp
		print xVal

		# grpBsh = mc.group( em = True , name = bsh_dict['facialRegion'] + 'Bsh_grp'  )
		# mc.parent( getBshGrp , grpBsh)
		# mc.move( bsh_dict['num']*1.2 , 0 , 0, grpBsh , r = True )

		bshData = { 'facialPart'	: bsh_dict['facialRegion'] 						,
					'baseBsh'		: base_crv 										,
					'bshBaseName'	: bsh_dict['facialRegion'] + 'All%s_bsh' %side 	,
					'bshMember'		: bshMember										,
					'bshInbName'	: bshInbName									,
					'bshGrp'		: bshGrp 										,
					'posiBlock'		: bsh_dict['posiBlock']							,
					'side' 			: bsh_dict['side']										}
		
		#print bshData
		print '### connect blend shape complete ###\n'
		return bshData

	# in case not side
	else:
		xVal += xOffset

		bshGrp = '%sBsh_grp' %(bsh_dict['facialRegion'] )
		mc.group( em = True , n = bshGrp )

		getBshGrp.append(bshGrp)
		bshMember = []
		bshInbName = []
		base_crvName=[]


		for i in range (len(bsh_dict['attrBshNam'])):

			# yVal = 0
			eachAtt = bsh_dict['attrBshNam'][i]

			for eachBehav in bsh_dict['bshBeheavior'][i]:
				# print eachAtt + eachBehav + side + '_bsh'

				currBshNode = '%s%s_bsh' %(eachAtt,eachBehav)

				# print currBshNode
				duppedNode = mc.duplicate( base_crv , rr = True )[0]
				mc.rename(duppedNode , currBshNode )
				mc.parent(currBshNode , bshGrp)
				mc.move( 0 , yVal , 0 , currBshNode , r = True)
				# Skipt the inbetween blendshape
				if 'InbA' in currBshNode or 'InbB' in currBshNode :
					bshInbName.append(currBshNode)
				else:
					bshMember.append(currBshNode)
				
				# print '%s has move yVal to ' %currBshNode
				# print yVal

				yVal += yOffset

		# add the last member 
		# bshMember.append(base_crv)


		# print bshMember

		base_crvName.append( bsh_dict['facialRegion'] + 'All_bsh' )
		# Create blendshape
		# mc.blendShape( bshMember , name = bsh_dict['facialRegion'] + 'All%s_bsh' %side)

		mc.move( xVal , 0 , 0, bshGrp , r = True )
		print '%s has move to ' %bshGrp
		print xVal

		# grpBsh = mc.group( em = True , name = bsh_dict['facialRegion'] + 'Bsh_grp'  )
		# mc.parent( getBshGrp , grpBsh)
		# mc.move( bsh_dict['num']*1.2 , 0 , 0, grpBsh , r = True )

		bshData = { 'facialPart'	: bsh_dict['facialRegion'] 						,
					'baseBsh'		: base_crv 										,
					'bshBaseName'	: bsh_dict['facialRegion'] + 'All%s_bsh' %side 	,
					'bshMember'		: bshMember										,
					'bshInbName'	: bshInbName									,
					'bshGrp'		: bshGrp 										,
					'posiBlock'		: bsh_dict['posiBlock']							,
					'side' 			: bsh_dict['side']										}
		
		#print bshData
		print '### connect blend shape complete ###\n'
		return bshData




def createBshToCurve( bsh_dict , posiBlock = (1,1) ):

	# Check is single or pair
	if not bsh_dict['side']:
		result_dict = _duplicateForBsh( bsh_dict )
		result_dict = _singleConnectBsh( result_dict )
		return result_dict
		# raise Exception('Target geometry has no side.')


	LFTdict = _duplicateForBsh( bsh_dict , side = 'LFT')
	RGTdict = _duplicateForBsh( bsh_dict , side = 'RGT')

	# Merge 2 dictionary together
	PAIR_DICT = LFTdict , RGTdict
	result_dict = _pairConnectBsh( PAIR_DICT )
	return result_dict





def _singleConnectBsh( singleBsh_dict ):
	'''
	connect blendshape from pair dictionary (just copy paste from pair connect blendshape )
	@param bsh_dict: Global dictionary from this module
	@type bsh_dict: dictionary

	'''

	# Get the bbox of the curve
	# Move it to here becase of blendshape is not work if place after it.
	xVal , yVal = bBox.getGeoRatio( singleBsh_dict['baseBsh'] )


	bshList = singleBsh_dict['bshMember'] + [ singleBsh_dict['baseBsh'] ]

	# ==================
	# - Add Blendshape -
	# ==================

	bshMember = mc.blendShape( bshList , name =  singleBsh_dict['facialPart'] + 'All_bsh' )

	print 'blendshape the %s' %'something'
	
	# grpBsh = mc.group( em = True , name = singleBsh_dict['facialPart'] + 'SosoBsh_grp'  )

	# mc.parent( singleBsh_dict['bshGrp'] , grpBsh)
	# mc.parent( singleBsh_dict['bshGrp'] , grpBsh)

	mc.move( xVal*singleBsh_dict['posiBlock'][0]*3  ,  singleBsh_dict['posiBlock'][1]   ,0, singleBsh_dict['bshGrp'] , r = True )
	mc.select(clear = True)
	
	return singleBsh_dict




def _pairConnectBsh( pairBsh_dict ):
	'''
	connect blendshape from pair (LFT,RGT) dictionary
	@param bsh_dict: Global dictionary from this module
	@type bsh_dict: dictionary

	'''

	side = ['LFT' , 'RGT']

	# Get the bbox of the curve
	# Move it to here becase of blendshape is not work if place after it.
	xVal , yVal = bBox.getGeoRatio( pairBsh_dict[0]['baseBsh'] )

	for i in range (0,2):
		bshList = pairBsh_dict[i]['bshMember'] + [ pairBsh_dict[i]['baseBsh'] ]

		# ==============
		# - Add Blendshape -
		# ==============

		bshMember = mc.blendShape( bshList , name =  pairBsh_dict[i]['facialPart'] + 'All%s_bsh' %side[i] )

		print 'blendshape the %s' %side[i]
	
	grpBsh = mc.group( em = True , name = pairBsh_dict[0]['facialPart'] + 'Bsh_grp'  )

	mc.parent( pairBsh_dict[0]['bshGrp'] , grpBsh)
	mc.parent( pairBsh_dict[1]['bshGrp'] , grpBsh)

	mc.move(     xVal*pairBsh_dict[0]['posiBlock'][0]*1.5  ,  pairBsh_dict[1]['posiBlock'][1]   ,0, grpBsh , r = True )
	mc.select(clear = True)
	
	return pairBsh_dict



def create( baseGeo,targetGeo=[],origin='local',deformOrder=None,prefix=None,blendShapeName = '' ):
	'''
	Create a blendShape deformer for the specified base geometry(reference from glmaster).
	@param baseGeo: Geometry to apply blendShape deformer to.
	@type baseGeo: str
	@param targetGeo: List of blendShape target models.
	@type targetGeo: list
	@param origin: Create a local or world space belndShape deformer. Accepted values - "local" or "world".
	@type origin: str
	@param deformOrder: Deformer order. Accepted values - "after", "before", "parallel", "split" or "foc".
	@type deformOrder: str
	@param prefix: Naming prefix
	@type prefix: str
	'''

	# =====================
	# - Create BlendShape -
	# =====================
	
	if deformOrder == 'after':
		blendShape = mc.blendShape(baseGeo,name=blendShapeName,origin=origin,after=True)[0]
	elif deformOrder == 'before':
		blendShape = mc.blendShape(baseGeo,name=blendShapeName,origin=origin,before=True)[0]
	elif deformOrder == 'parallel':
		blendShape = mc.blendShape(baseGeo,name=blendShapeName,origin=origin,parallel=True)[0]
	elif deformOrder == 'split':
		blendShape = mc.blendShape(baseGeo,name=blendShapeName,origin=origin,split=True)[0]
	elif deformOrder == 'foc':
		blendShape = mc.blendShape(baseGeo,name=blendShapeName,origin=origin,foc=True)[0]
	else:
		blendShape = mc.blendShape(baseGeo,name=blendShapeName,origin=origin)[0]


	# ===============
	# - Add Targets -
	# ===============
	
	for target in targetGeo:
		addTarget( blendShape=blendShape,target=target,base=baseGeo )

	# =================
	# - Return Result -
	# =================
	
	return blendShape


def addTarget(blendShape,target,base='',targetIndex=-1,targetAlias='',targetWeight=0.0,topologyCheck=False):
	'''
	Add a new target to the specified blendShape
	@param blendShape: Name of blendShape to remove target from
	@type blendShape: str
	@param target: New blendShape target geometry
	@type target: str
	@param base: BlendShape base geometry. If empty, use first connected base geomtry
	@type base: str
	@param targetIndex: Specify the target index. If less than 0, use next available index. 
	@type targetIndex: str
	@param targetAlias: Override the default blendShape target alias with this string
	@type targetAlias: str
	@param targetWeight: Set the target weight value
	@type targetWeight: float
	'''

	
	# ==============
	# - Add Target -
	# ==============
	

	if targetIndex < 0: 
		targetIndex = nextAvailableTargetIndex(blendShape)
	
	# Add Target
	mc.blendShape(blendShape,e=True,t=(base,targetIndex,target,1.0),topologyCheck=topologyCheck)
	
	# Get Target Name
	targetName = getTargetName(blendShape,target)
	
	# Override Target Alias
	if targetAlias:
		targetIndex = getTargetIndex(blendShape,targetName)
		mc.aliasAttr(targetAlias,blendShape+'.weight['+str(targetIndex)+']')
		targetName = targetAlias
	
	# =====================
	# - Set Target Weight -
	# =====================
	
	if targetWeight: mc.setAttr(blendShape+'.'+targetName,targetWeight)
	
	# =================
	# - Return Result -
	# =================
	
	return (blendShape+'.'+targetName)


def nextAvailableTargetIndex(blendShape):
	'''
	Get the next available blendShape target index
	@param blendShape: Name of blendShape to get next available target index for
	@type blendShape: str
	'''

	
	# Get blendShape target list
	targetList = getTargetList(blendShape)
	if not targetList: return 0
	
	# Get last index
	lastIndex = getTargetIndex(blendShape,targetList[-1])
	nextIndex = lastIndex + 1
	
	# Return result
	return nextIndex


def getTargetList(blendShape):
	'''
	Return the target list for the input blendShape
	@param blendShape: Name of blendShape to get target list for
	@type blendShape: str
	'''

	
	# Get attribute alias
	targetList = mc.listAttr(blendShape+'.w',m=True)
	if not targetList: targetList = []
	
	# Return result
	return targetList


def getTargetIndex(blendShape,target):
	'''
	Get the target index of the specified blendShape and target name
	@param blendShape: Name of blendShape to get target index for
	@type blendShape: str
	@param target: BlendShape target to get the index for
	@type target: str
	'''

	# Get attribute alias
	aliasList = mc.aliasAttr(blendShape,q=True)
	aliasIndex = aliasList.index(target)
	aliasAttr = aliasList[aliasIndex+1]

	# Get index
	# Break 4 off from 'weight[4]'
	targetIndex = int(aliasAttr.split('[')[-1].split(']')[0])

	# Return
	return targetIndex


def addTatgetInbetween( blendShape,targetGeo,targetName,base='',targetWeight='0.5' ):
	'''
	Add a new target inbetween to the specified blendShape target
	@param blendShape: Base Blendshape name
	@type blendShape: str
	@param targetGeo: Inbetween object name
	@type targetGeo: str
	@param targetName: BlendShape target name that want to add inbetween to
	@type targetName: str
	@param base: Base geometry or curve . If empty, use first connected base geomtry
	@type base: str
	@param targetWeight: target weight value
	@type targetWeight: str
	'''

	# ==========
	# - Checks -
	# ==========
	
	# Target
	if not mc.objExists(targetGeo):
		raise Exception('Target geometry "'+target+'" does not exist!')
	# Base
	if base and not mc.objExists(base):
		raise Exception('Base geometry "'+base+'" does not exist!')

	# Get Target Index
	targetIndex = getTargetIndex(blendShape,targetName)

	# Add Target
	mc.blendShape(blendShape,e=True,t=(base,targetIndex,targetGeo,targetWeight))
	
	# =================
	# - Return Result -
	# =================
	
	return (blendShape+'.'+targetName)


def getTargetName(blendShape,targetGeo):
	'''
	Get blendShape target alias for specified target geometry
	@param blendShape: BlendShape node to get target name from
	@type blendShape: str
	@param targetGeo: BlendShape target geometry to get alia name for
	@type targetGeo: str
	'''
	# ==========
	# - Checks -
	# ==========
	

	
	# Target
	if not mc.objExists(targetGeo):
		raise Exception('Target geometry "'+targetGeo+'" does not exist!')
	
	# ===================
	# - Get Target Name -
	# ===================
	
	# Get Target Shapes
	# targetShape = glTools.utils.shape.getShapes(targetGeo,nonIntermediates=True,intermediates=False)

	targetShape = mc.listRelatives(targetGeo,s=True,ni=True,pa=True) 
	if not targetShape: targetShape = mc.ls(mc.listRelatives(targetGeo,ad=True,pa=True),shapes=True,noIntermediate=True)
	if not targetShape: raise Exception('No shapes found under target geometry "'+targetGeo+'"!')
	
	# Find Target Connection
	targetConn = mc.listConnections(targetShape,sh=True,d=True,s=False,p=False,c=True)
	if not targetConn.count(blendShape):
		raise Exception('Target geometry "'+targetGeo+'" is not connected to blendShape "'+blendShape+'"!')
	targetConnInd = targetConn.index(blendShape)
	targetConnAttr = targetConn[targetConnInd-1]
	targetConnPlug = mc.listConnections(targetConnAttr,sh=True,p=True,d=True,s=False)[0]
	
	# Get Target Index
	targetInd = int(targetConnPlug.split('.')[2].split('[')[1].split(']')[0])
	# Get Target Alias
	targetAlias = mc.aliasAttr(blendShape+'.weight['+str(targetInd)+']',q=True)
	
	# =================
	# - Return Result -
	# =================
	
	return targetAlias


def addBshInbetween( bsh_dict , bshName , bshInbName , targetWeight=0.5 ):
	'''
	Get blendShape target alias for specified target geometry
	@param bsh_dict: BlendShape data 
	@type blendShape: dictionary
	@param bshName: name of blendshape that want to insert inb
	@type bshName: str
	@param bshInbName: name of inb blendshape 
	@type bshInbName: str
	@param targetWeight: weight value 
	@type targetWeight: float
	'''

	if bsh_dict[0]['side'] == True:
		for side in range(0,2):
			# collect name for create inbetween
			bshBaseName = bsh_dict[side]['bshBaseName']

			# curve or geo name
			objBshName = bsh_dict[side]['baseBsh']

			# create inbetween
			addTatgetInbetween( bshBaseName , bshInbName , bshName , objBshName ,targetWeight)

			bshName=bshName.replace('LFT' , 'RGT')
			bshInbName=bshInbName.replace('LFT' , 'RGT')
			bshBaseName=bshBaseName.replace('LFT' , 'RGT')
			objBshName=objBshName.replace('LFT' , 'RGT')

			print 'Change side from LFT to RGT...'
			print bshName
			print bshInbName
			print bshBaseName
			print objBshName
			print separater + ' Blendshape Complete ' + separater	



# warp it up to function
def connectInbetween( bsh_dict , MembIndex , inbIndex ,weight):
	'''
	Connect inbetween blendshape  
	@param bsh_dict: dictionary return from previous function
	@type bsh_dict: dictionary
	@param targetIndex: index of inbetween 
	@type targetIndex: int tuple
	@param weight: target weight
	@type weight: float ( limit to 0 - 1 )
	'''

	# indexNum = len(bsh_dict[0]['bshInbName'])
	# for i in range(0,indexNum)


	# add inb for eyebrow
	for side in range(0,2):
		# collect name for create inbetween
		bshBaseName = bsh_dict[side]['bshBaseName']

		# curve or geo name
		objBshName = bsh_dict[side]['baseBsh']

		# blendshape that want to be inserted (must specify)
		bshMemName = bsh_dict[side]['bshMember'][MembIndex]

		# name of inbetween blendshape (must specify)
		bshInbName = bsh_dict[side]['bshInbName'][inbIndex]

		# create inbetween
		addTatgetInbetween( bshBaseName , bshInbName , bshMemName , objBshName , weight)

		print 'inserted %s to %s at weight %f' %(bshInbName,bshMemName,weight)




def connectInbetweenForPly( bsh_dict , MembIndex , inbIndex ,weight):
	'''
	Connect inbetween blendshape usable for Connection single each blendshape invidualy

	@param bsh_dict: dictionary return from previous function
	@type bsh_dict: dictionary

	@param MembIndex: index of bshMember 
	@type MembIndex: int

	@param inbIndex: index of bshInbMember 
	@type inbIndex: int

	@param targetIndex: index of inbetween 
	@type targetIndex: int tuple

	@param weight: target weight
	@type weight: float ( limit to 0.0 - 1.0 )
	'''

	# indexNum = len(bsh_dict[0]['bshInbName'])
	# for i in range(0,indexNum)


	# collect name for create inbetween
	bshBaseName = bsh_dict['bshBaseName']

	# curve or geo name
	objBshName = bsh_dict['baseBsh']

	# blendshape that want to be inserted (must specify)
	bshMemName = bsh_dict['bshMember'][MembIndex]

	# name of inbetween blendshape (must specify)
	bshInbName = bsh_dict['bshInbName'][inbIndex]

	# create inbetween
	addTatgetInbetween( bshBaseName , bshInbName , bshMemName , objBshName , weight)

	print 'inserted %s to %s at weight %f' %(bshInbName,bshMemName,weight)




def connectCtrlToBsh(ctrlNam,part,behv,attr,side,bshBase,bshMember,positive = True , amp = 5):
	'''
	connection value from [ controller >>> MDL >>> animCurve >>> blendshape ]
	@param ctrlNam: controller that want to pass value
	@type ctrlNam: str
	@param part: part of the blendshape such as eyeLidUp , lidDown
	@type part: str
	@param behv: behavior of the blendshape such as going up , roll in roll out 
	@type behv: str
	@param attr: attrbute name of controller that you want connect to blendshape
	@type attr: str
	@param side: side
	@type side: str
	@param bshBase: blendshape name base 
	@type bshBase: str	
	@param bshMember: name of member that you want to connect
	@type bshMember: str	
	@param positive: type of value 'negative' or 'positive'
	@type positive: boolean	
	@param amp: amplifier blendshape value 
	@type amp: int		
	'''
	# print 'part %s is %s' %(part,behv)
	bshNode = core.Dag(bshBase)
	ctrl = core.Dag(ctrlNam)
	
	if positive:
		animCurve = core.AnimCurvePos( part + behv + 'Pos' + side )
		mulVal = core.MultiDoubleLinear( part + behv + 'Pos' + side )
	else:
		animCurve = core.AnimCurveNeg( part + behv + 'Neg' + side )
		mulVal = core.MultiDoubleLinear( part + behv + 'Neg' + side )

	
	mulVal.attr('input2').value = amp
	ctrl.attr( attr ) >> mulVal.attr( 'input1' )
	mulVal.attr( 'output' ) >> animCurve.attr( 'input' )
	animCurve.attr( 'output' ) >> bshNode.attr( bshMember )
	print '### Connect value success ###\n'
	return True