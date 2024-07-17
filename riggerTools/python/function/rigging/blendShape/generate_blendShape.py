#... generate blendshape 


#... 1. cut head poly name it  "facialBase_ply"
#... 2. to the grp name it "facialBshBase_grp"
#... 3. exe this function 

'''
from function.rigging.blendShape import generate_blendShape as gbs
reload(gbs)
gbs.duplicateForBlendshape( blendshapeAtEnd = True,blendshape_dict = mnd.facial_dict_ARKit, multiplier = 2.0 )
'''


import maya.cmds as mc

from function.rigging.util import boundingBox as bBox
from function.framework.reloadWrapper import reloadWrapper as reload
reload(bBox)

import pprint

from function.rigging.util import generic_maya_dict as mnd
reload(mnd)





'''
for mocap project
@param bsh_dict: Global dictionary from this module
@type bsh_dict: dictionary

'''



def duplicateForBlendshape( blendshapeAtEnd = False,blendshape_dict = 'dict', multiplier = 2.0, blendshapeName = 'facial_bsh' ):

	
			
	side = ''

	bshMember = []
	getBshGrp = []

	if mc.objExists('facialBshBase_grp'):
		baseBsh_grp = 'facialBshBase_grp'
	else:
		mc.error('There is no polygon group for blendShape use name :facialBshBase_grp ')
		return False


	# Get size (Use new method to find size)

	if mc.objExists('facialBase_ply'):
		boundBox = bBox.geoBoundingBox( 'facialBase_ply' )
	else:
		mc.warning('There is no polygon group for blendShape please use ply name: facialBase_ply')
		return False


	xVal = 0
	yVal = 0
	mulVal = 2
	xOffset = 0
	yOffset = 0


	bbY = int(	abs(boundBox[1] - boundBox[4])	)
	bbX = int(	abs(boundBox[0] - boundBox[3])	)

	if side == 'RGT':
		yOffset = 	bbY * 6.5 * multiplier
		xOffset = 	bbX * 1.5 * multiplier

	elif side == 'LFT':
		yOffset = 	bbY * 6.5 * multiplier
		xOffset = 	bbX * 3.0 * multiplier

	else:
		yOffset = 	bbY * 3.0 * multiplier
		xOffset = 	bbX * 5.0 * multiplier

	# xOffset = 0.5



	xVal += xOffset

	bshGrp = '%sBsh%s_grp' %(blendshape_dict['facialRegion'],side)
	mc.group( em = True , n = bshGrp )

	getBshGrp.append(bshGrp)
	bshMember = []
	bshInbName = []
	base_crvName=[]

	all_bsh = []

	i = 0



	member = mc.listRelatives( baseBsh_grp ,children=1)



	for i in range (len(blendshape_dict['name_all'])):

		eachAtt = blendshape_dict['name_all'][i]
		
		currBshNode = '%s' %eachAtt

		currBshSub = eachAtt + '_ply'

		# dup grp
		duppedNode = mc.duplicate( baseBsh_grp , rr = True )[0]
		mc.rename( duppedNode , currBshNode )

		# change memeber name
		# update another method

		for each in range(len(member)):
			mc.rename(eachAtt+'|'+ member[each] , eachAtt +'_'+ member[each])
		
			
		mc.parent(currBshNode , bshGrp)

		if eachAtt == blendshape_dict['name_all'][0]:
			mc.move( xOffset*multiplier*-0.1 , 0 , 0 , currBshNode , r = True)
		else:
			mc.move( xOffset , yVal , 0 , currBshNode , r = True)

		yVal += yOffset*0.2

		print ('currBshNode is :%s' %currBshNode)
		print ('xOffset is :%d' %xOffset)
		print ('yVal is :%d' %yVal)


		if i%5 == 0 :
			mul = i//5
			yVal = 0
			xOffset = 50*mul*1.25

		all_bsh.append(currBshNode)
			


			
	mc.move(blendshape_dict['posiBlock'][1] * 0.6 * xOffset, 0, 0, bshGrp, r = True)

	mc.select(deselect = True)

	# hide unused bsh
	if blendshape_dict['name_exclude']:
		for each in blendshape_dict['name_exclude']:
			mc.setAttr('{0}.visibility'.format(each), 0)

	# return all_bsh 
	blendshapeAtEnd = True
	if blendshapeAtEnd:
		mc.blendShape( all_bsh , 'facialBshBase_grp', topologyCheck = True, name = blendshapeName)
	

	print ('''\n
	# ========================
	# - End of function -
	# ========================
	''')
	return all_bsh



# execute
#duplicateForBlendshape( blendshapeAtEnd = True,blendshape_dict = mnd.facial_dict_ARKit, multiplier = 2.0 )