#... source ...research_and_developement\22.11.Nov.16.Wed.15_Round value
#... destination ...function.rigging.skin



'''
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.skin import roundSkinWeight as rsw
reload(rsw)
selected = mc.ls(sl=True)[0]
rsw.roundSkinWeight(digit=3, selection=selected)

'''


import maya.cmds as mc


from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.skin import autoReadWriteSkin as skin
reload (skin)

def roundSkinWeight(digit=3, selection=''):

	selection = mc.ls(sl = True, fl = True)
	if selection == None:
		return False
	each = selection[0]
	mc.select( each , r = True)
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
		
		if len(eachVtx) == 1:

			#... there is just one joint in vtx so I assign 1
			eachVtx[0] = list(eachVtx[0])
			eachVtx[0][1] = 1
			eachVtx[0] = tuple(eachVtx[0])

			continue


		else:
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
			#... round value here
			if len(VtxWeight) > 0:
				for each in range(len(VtxWeight)):
					float_num = round(VtxWeight[each], digit)
					vtxWeightValueList.append(float_num)
					print(vtxWeightValueList)

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
				
			total=0
			for each in range(len(vtxWeightValueList)):
				total = total + vtxWeightValueList[each]
				
			if total != 1:
				print(mc.warning('THE {0} VALUE IS {1} MORE THAN ONE WHY!!!!!.'.format(eachVtxNum, total)))
				#return False



			#... assign round value to the dict
			for i in range (len(eachVtx)):
				
				eachVtx[i]=list(eachVtx[i])
				eachVtx[i][1] = vtxWeightValueList[i]
				eachVtx[i]=tuple(eachVtx[i])


			#... next assign that new each vtx to dicionary value
			vertexDict[eachVtxNum] = eachVtx








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
					print ('\nImporting %s to skin data...' %key)
					
					# use skc name, shapeName.vtx[number]
					mc.skinPercent( skinClusterNam, key, transformValue = vertexDict[key], zeroRemainingInfluences = True )
				except:
					mc.error("Error , %s Skin Joint name may mistmatch or SkinCluster joint list not exists ..." %key)
					continue		
			else:
				print("key, values pair have a problem")
				continue
		print ("\n{0} Vertices were set to vertex weight values. ".format(	len(vertexDict.keys())	))
		print ("\n{0}{0} Import SkinCluster Complete {0}{0}".format('--------------' ))
	else:
		mc.error("JSON File was empty ")
	print('\n### Complete ###')
	mc.select( deselect = True )