#... source ...\research_and_developement\22.11.Nov.16.Wed.15_Round value

from function.rigging.skin import autoReadWriteSkin as skin
reload (skin)

def roundSkinWeight(digit=3,selection=''):

	selection = mc.ls(sl = True, fl = True)
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
			extractNum = []
			for i in range (len(eachVtx)):
				extractNum.append(eachVtx[i][1])
				

			#... go to round number
			VtxWeight=extractNum
			
			
			total = 0
			diff = 0
			VtxWeightNum=len(VtxWeight)
			VtxWeightValue=[]

			if len(VtxWeight) > 0:
				for each in range(len(VtxWeight)):
					float_num = round(VtxWeight[each], digit)
					VtxWeightValue.append(float_num)
					print(VtxWeightValue)

			for each in range(len(VtxWeightValue)):
				total = total + VtxWeightValue[each]
					
			if total > 1:
				biggest = 0
				for each in range(len(VtxWeightValue)):
					if VtxWeightValue[each] > VtxWeightValue[biggest]:
						biggest = each
						
					diff = round(1 - total)
					VtxWeightValue[biggest] = round((VtxWeightValue[biggest] + diff), digit)
					
			elif total < 1:
				biggest = 0
				for each in range(len(VtxWeightValue)):
					if VtxWeightValue[each] > VtxWeightValue[biggest]:
						biggest = each
						
					diff = round(1-total,digit)
					VtxWeightValue[biggest] = round((VtxWeightValue[biggest] + diff), digit)		
				
			total=0
			for each in range(len(VtxWeightValue)):
				total = total + VtxWeightValue[each]
				
			if total != 1:
			    print(mc.warning('The value is more than 1 why.'))



			#... assign round value to the dict
			for i in range (len(eachVtx)):
				
				eachVtx[i]=list(eachVtx[i])
				eachVtx[i][1] = VtxWeightValue[i]
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