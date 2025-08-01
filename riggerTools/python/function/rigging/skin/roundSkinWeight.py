#... source ...research_and_developement\22.11.Nov.16.Wed.15_Round value
#... destination ...function.rigging.skin



'''
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.skin import roundSkinWeight as rsw
reload(rsw)
selected = mc.ls(sl=True)[0]
rsw.roundSkinWeight(digit=3, selection=selected)

'''
from function.framework.reloadWrapper import reloadWrapper as reload

import logging 

from function.pipeline import logger 
reload(logger)

import maya.cmds as mc
import time

from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.skin import autoReadWriteSkin as skin
reload (skin)

class roundSkinLogger(logger.MayaLogger):
	LOGGER_NAME = "roundSkin"


import traceback


def has_skin_cluster(mesh):
    # Get the history of the mesh
    history = mc.listHistory(mesh)
    
    # Check if any of the nodes in the history are skinCluster nodes
    skin_clusters = mc.ls(history, type='skinCluster')
    
    if skin_clusters:
        return True
    else:
        return False









def roundSkinWeight(digit=3, selection=''):

	roundSkinLogger.set_level(logging.DEBUG)
	roundSkinLogger.info('Start function.')

	roundSkinLogger.info('[ROUND] CALLED')
	roundSkinLogger.info('Traceback:\n' + ''.join(traceback.format_stack()))
	
	#...timeStart
	timeStart = time.time()

	# selection = mc.ls(sl = True, fl = True)
	mc.select( selection, r = True)

	selection = mc.ls(sl = True)[0]
	if selection == []:
		mc.warning("No valid selection made. Exiting roundSkinWeight.")
		return False
	# each = selection[0]

	

	#... check there are having skin
	round_mesh = mc.ls(sl=True)[0]
	if has_skin_cluster(round_mesh):
		roundSkinLogger.info('There are having skincluster.')
	else:
		return False



	# get vertex data
	geoData = skin.geoInfo( vtx = True, geo = True, skinC = True )
	vertexDict	=	{}
	vertexList 			= 		geoData[0]
	selGEO 				= 		geoData[1]
	skinClusterNam 		= 		geoData[2]

	# got dictionary of namejoint vertexnumber skinpercent
	vertexDict = skin.getVertexWeights( vertexList , skinClusterNam )


	#... if you want to run each line
	# eachVtxNum = 'Iberian_Lynx_Body_plyShape.vtx[99]'

	for eachVtxNum in vertexList:

		

		eachVtx = vertexDict[eachVtxNum]
		
		#... case# 1 there are only one skin jnt
		if len(eachVtx) == 1:

			#... there is just one joint in vtx so I assign 1
			eachVtx[0] = list(eachVtx[0])
			eachVtx[0][1] = 1
			eachVtx[0] = tuple(eachVtx[0])

			continue


		else:

			#... case# 2 is normal weight
			VtxWeight = []
			for i in range (len(eachVtx)):
				#... get only number
				VtxWeight.append(eachVtx[i][1])
				

			#... go to round number
			# VtxWeight=extractNum
			
			
			total = 0
			diff = 0
			VtxWeightNum=len(VtxWeight)
			vtxWeightValueList=[]


			# roundSkinLogger.info(f'Weight before adjust: {VtxWeight}')
			# print(f'Weight before adjust: {VtxWeight}')




			# Step 1: Round each value
			rounded_VtxWeight = [round(value, 3) for value in VtxWeight]

			# Step 2: Calculate the sum of the rounded values
			total_sum = sum(rounded_VtxWeight)

			# Step 3: Adjust the max value if the sum is not exactly 1
			if total_sum != 1.0:
			    max_value = max(rounded_VtxWeight)
			    max_index = rounded_VtxWeight.index(max_value)
			    
			    # Calculate the difference needed to make the sum 1
			    difference = 1.0 - total_sum
			    # Adjust the max value
			    rounded_VtxWeight[max_index] += difference

			# Output the results
			new_total_sum = sum(rounded_VtxWeight)
			# rounded_VtxWeight, new_total_sum


			if new_total_sum == 1:
				roundSkinLogger.info(f'{eachVtxNum} Sum of value is: 1 That OK.')
			elif new_total_sum > 1:
				roundSkinLogger.warning( 'THE {0} VALUE IS {1} MORE THAN ONE WHY!!!!!.'.format(eachVtxNum, new_total_sum) )
			elif new_total_sum < 1: 
				roundSkinLogger.warning( 'THE {0} VALUE IS {1} MORE THAN ONE WHY!!!!!.'.format(eachVtxNum, new_total_sum) )







			'''
			#... round value logic  here
			if len(VtxWeight) > 0:
				for each in range(len(VtxWeight)):
					float_num = round(VtxWeight[each], digit)
					vtxWeightValueList.append(float_num)
					

			#... sum value
			
			for each in range(len(vtxWeightValueList)):
				total = total + vtxWeightValueList[each]
					
			if total > 1:
				#... change the condition
				#... find index of max value
				max_index = vtxWeightValueList.index(max(vtxWeightValueList))

				diff = max(vtxWeightValueList) - (total - 1.00)
				diff = format(diff,".3f")
				
				vtxWeightValueList[max_index] = float(diff)
				

				# biggest = 0
				# for each in range(len(vtxWeightValueList)):
				# 	if vtxWeightValueList[each] > vtxWeightValueList[biggest]:
				# 		biggest = each
						
				# 	diff = round(1 - total)
				# 	vtxWeightValueList[biggest] = round((vtxWeightValueList[biggest] + diff), digit)
					
			elif total < 1:
				#... change the condition
				#... find index of max value
				max_index = vtxWeightValueList.index(max(vtxWeightValueList))
				diff = max(vtxWeightValueList) + (1.00 - total)
				diff = format(diff,".3f")
				vtxWeightValueList[max_index] = float(diff)

				# biggest = 0
				# for each in range(len(vtxWeightValueList)):
				# 	if vtxWeightValueList[each] > vtxWeightValueList[biggest]:
				# 		biggest = each
						
				# 	diff = round(1-total,digit)
				# 	vtxWeightValueList[biggest] = round((vtxWeightValueList[biggest] + diff), digit)		
				

			total = 0
			for each in range(len(vtxWeightValueList)):
				total = total + vtxWeightValueList[each]



				
			if total != 1:
				roundSkinLogger.warning( 'THE {0} VALUE IS {1} MORE THAN ONE WHY!!!!!.'.format(eachVtxNum, total) )
				#return False

			'''


			#... assign round value to the dict
			for i in range (len(eachVtx)):
				
				eachVtx[i]=list(eachVtx[i])
				eachVtx[i][1] = rounded_VtxWeight[i]
				eachVtx[i]=tuple(eachVtx[i])


			#... next assign that new each vtx to dicionary value
			vertexDict[eachVtxNum] = eachVtx

	#...timeEnd
	timeEnd = time.time()
	timeElapsed = timeEnd-timeStart

	roundSkinLogger.info('Round value has complete.\n')
	roundSkinLogger.info('SetData Elapsed: %s'%timeElapsed)











	# # # # # # # #
	#.... import
	# # # # # # # #

	#selectGeoData = skin.geoInfo(vtx = False, geo = False, shape = True, skinC = True)

	#geoName			= 	selectGeoData[0]
	#skinClusterNam 	= 	selectGeoData[1]



	if len(vertexDict) > 0:
		
		for key in vertexDict.keys():
			# skipt skinJnt and skinCluster and geoName
			if ( key != 'skinCluster' ) and ( key != 'skinJnt' ) and ( key != 'geoName' ):
				try:
					# disable it for make it faster
					roundSkinLogger.debug('\nImporting %s to skin data...' %key)
					
					# use skc name, shapeName.vtx[number]
					mc.skinPercent( skinClusterNam, key, transformValue = vertexDict[key], zeroRemainingInfluences = True )
				except:
					mc.error("Error , %s Skin Joint name may mistmatch or SkinCluster joint list not exists ..." %key)
					continue		
			else:
				print("key, values pair have a problem")
				continue
		roundSkinLogger.info("\n{0} Vertices were set to vertex weight values. ".format(len(vertexDict.keys())	))
		roundSkinLogger.info("\n{0}{0} Import SkinCluster Complete {0}{0}".format('--------------' ))
	else:
		mc.error("JSON File was empty ")
	roundSkinLogger.info('# # # Complete # # #')
	mc.select( deselect = True )