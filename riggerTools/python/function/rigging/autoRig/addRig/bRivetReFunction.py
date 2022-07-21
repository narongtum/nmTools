# to D:\True_Axion\Tools\riggerTools\python\axionTools\rigging\autoRig\addRig

from function.pipeline import fileTools as fileTools 
reload(fileTools)


"""
from function.rigging.autoRig.addRig import bRivetReFunction as brf
reload(brf)

"""



import maya.cmds as mc
import re

from function.rigging.autoRig.base import core
reload(core)

from function.pipeline import logger 
reload(logger)

class RivetLogger(logger.MayaLogger):
	LOGGER_NAME = "bRivet"


RivetLogger.info('# # # Starting function. # # #')

# loc = spaceRivet.name
# tmpLoc.attr( 'overrideEnabled' ).value = 1
# tmpLoc.attr( 'overrideDisplayType' ).value = 2




def _pair_evaluate():
	# select pair of edge
	input = mc.filterExpand(sm = 32)

	# if input and len(input) >=2:  
	if input and (len(input) % 2) == 0:
		print ('This is even number')
		ob = input[0].split('.')[0]
		edgeMax = mc.polyEvaluate(ob, e=True)
		shape = mc.listRelatives(ob, shapes=True)
		count = range(0,len(input))
		# doublet = zip(range(count-1),range(1, count))
		mc.undoInfo( ock=True )
		return input, count, edgeMax, shape
	else:
		mc.error('bRivet requires at least 2 edges to be selected')



def _remove_odd(number_list):
	odd_num = []
	even_num = []
	for i in number_list[:]:
		if i % 2 != 0:
			odd_num.append(i)
		elif i % 2 == 0:
			even_num.append(i)
	return even_num, odd_num





def _bRivetCreate(edge_number, baseName = 'rivetFace', side = 'LFT', fixedRotate = False, size = 0.25, color = 'white',count=0, edgeMax=500, shape='shapeName'):

	spaceRivet = core.Locator(baseName + side + '_loc')
	spaceRivet.setOutlineColor(color)
	spaceRivet.color = color
	spaceRivet.attr( 'localScaleX' ).value = size
	spaceRivet.attr( 'localScaleY' ).value = size
	spaceRivet.attr( 'localScaleZ' ).value = size


	var = [['pointOnSurfaceInfo','pos'],['loft','loft'],['fourByFourMatrix','mat'],['decomposeMatrix','dcp']]
	pnt = ['normal', 'tangentU.tangentU', 'tangentV.tangentV', 'position.position']
	xyz = ['X','Y','Z']
	uv = 'UV'

	# doublet = zip(range(count-1),range(1, count))
	locs = []




	#for n in range(4):
	#    var[n][1] = cN(var[n][0], name = var[n][1])
		
		
	# create node	
	var[0][1] = mc.createNode(var[0][0], name = baseName + side + '_poi')
	var[1][1] = mc.createNode(var[1][0], name = baseName + side + '_loft')
	var[2][1] = mc.createNode(var[2][0], name = baseName + side + '_fbfmat')
	var[3][1] = mc.createNode(var[3][0], name = baseName + side + '_decom')	
	 

	# loc = mc.spaceLocator(name = baseName + side + '_loc')	
	mc.setAttr('%s.turnOnPercentage' % var[0][1], 1)
	mc.setAttr('%s.degree' % var[1][1], 1)
	mc.addAttr(spaceRivet.name, at = 'float2', ln= uv) 


	for one in (0,1):
		# use regex to find edge number
		num = int(re.findall("\[(.*?)\]", edge_number[one])[0])
		mc.addAttr(spaceRivet.name, at = 'short' , ln = 'edgeIndex%d' % one, min = 0, max = edgeMax, k = True, dv = num)

		if one == 0:
			edge = 'first'
		elif one == 1:
			edge = 'second'

		ed = mc.createNode('curveFromMeshEdge', name = baseName + '_' + edge + '_' + side + '_cfm')
		# assign value
		mc.setAttr('%s.edgeIndex[0]' % ed, num)
		mc.connectAttr('%s.edgeIndex%d' % (spaceRivet.name,one), '%s.edgeIndex[0]' % ed)	
		mc.connectAttr('%s.worldMesh[0]' % shape[0] , '%s.inputMesh' % ed)
		mc.connectAttr('%s.outputCurve' % ed, '%s.inputCurve[%s]' % (var[1][1], one))
		mc.addAttr(spaceRivet.name, at = 'float' , ln = uv[one], k = True, p= uv, min = 0, max = 1)


	for UV in uv:
		mc.connectAttr('%s.UV.%s' % (spaceRivet.name, UV), '%s.parameter%s' % (var[0][1], UV))
		mc.setAttr('%s.UV.%s' % (spaceRivet.name, UV), 0.5)		  

		
	for i in range(4):
		for j in range(3):
			o =	 xyz[j]
			if i in [1,2]: o = o.lower()
			mc.connectAttr('%s.%s%s' %(var[0][1], pnt[i], o), '%s.in%s%s' % (var[2][1], i, j))

		
	mc.connectAttr('%s.outputSurface' % var[1][1], '%s.inputSurface' % var[0][1])
	mc.connectAttr('%s.output' % var[2][1], '%s.inputMatrix' % var[3][1])
	mc.connectAttr('%s.outputTranslate' % var[3][1], '%s.t' % spaceRivet.name)


	if fixedRotate:
		mc.connectAttr('%s.outputRotate' % var[3][1], '%s.r' % spaceRivet.name)

	locs.append(spaceRivet.name)
	mc.select(deselect=True)


	# return spaceRivet
	# bRivet('baseNameHaya', 'RGT')




###############
# execute
###############



def createRivet(	baseName = 'rivetFaceD',
					side = 'LFT',
					fixedRotate = False,
					size = 0.25,
					color = 'white'):



	edge_data = _pair_evaluate()
	reform_list = _remove_odd(edge_data[1])
	doublet = zip( (reform_list[0]),(reform_list[1]) )



	num = 0
	for each in range(len(doublet)):
		pair_edge = [ edge_data[0][doublet[each][0]], edge_data[0][doublet[each][1]] ]
		num = num+1 
		locName = baseName + '%02d'%num 
		print pair_edge
		
		_bRivetCreate(edge_number = pair_edge, baseName = locName, side = side , fixedRotate = fixedRotate, size =size, color = color,count = len(edge_data[1]),edgeMax = edge_data[2],shape = edge_data[3] )

		RivetLogger.info('# # # bRivet create complete. # # #')

	
	
'''brf.createRivet(	baseName = 'rivetFaceD',
					side = 'LFT',
					fixedRotate = True,
					size = 0.25,
					color = 'white')'''