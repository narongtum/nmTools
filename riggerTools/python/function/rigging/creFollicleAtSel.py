# -*- coding: utf-8 -*-
""" Create follicle at selected

Todo:
	* Select
	* run function


Direct run:
from function.rigging import creFollicleAtSel as cfa
reload(cfa)

cfa.createFollicleAtSel()


"""



from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import core
reload(core)

import maya.cmds as mc


def createFollicleAtSel( flcGrp = 'follicleGroup', flcName = 'follicle', side = '', usePartName = False, selected = [] ):
	# selected = mc.ls(sl=True)

	partName = ('Inn', 'Mid', 'Out')
	if mc.objExists('follicleGroup') == False:
		mc.select( cl = True )
		flc_grp = core.Null( flcGrp )
		flc_grp.lockHideAttrLst( 'tx' , 'ty' , 'tz' , 'rx' ,'ry' , 'rz' , 'sx' ,'sy' , 'sz' )
		
	folicle_list = []
	num = 1
	for vtxSel in selected:

		inObj = vtxSel.split('.')
		shapeObj = misc.shapeName(inObj[0])

		follShape = mc.createNode( 'follicle')

		if usePartName == False:
			newName = flcName + '%02d'%(num) + side +'_flc'
		elif usePartName == True:
			newName = flcName + partName[num-1] + side +'_flc'

		print (newName)
		mc.select(follShape,r=1)
		mc.pickWalk( d = 'up')
		follTran = mc.ls(sl=True)[0]

		if mc.objExists('%s.outMesh' %inObj[0]):
			print 'This is polygon na.'

			mc.connectAttr('%s.outMesh' %shapeObj ,  '%s.inputMesh' %follShape , f = True)
			mc.connectAttr('%s.worldMatrix' %shapeObj ,  '%s.inputWorldMatrix' %follShape , f = True)
			
			mc.connectAttr('%s.outRotate' %follShape ,  '%s.rotate' %follTran , f = True)
			mc.connectAttr('%s.outTranslate' %follShape ,  '%s.translate' %follTran , f = True)
				
			
			mapNum = mc.polyListComponentConversion( vtxSel ,toUV = True )[0]
			uvPos = mc.polyEditUV(mapNum, query=True)
			print uvPos

			mc.setAttr( '%s.parameterU' %follShape ,uvPos[0])
			mc.setAttr( '%s.parameterV' %follShape ,uvPos[1])

			mc.rename(follTran , newName)
			num = num + 1

		elif mc.objExists('%s.local' %inObj[0]):
			# I don no how to find UV coordinate from nurb
			print 'This is nurb Use create controller for Surface instead.'

		else:
			print 'maybe something not right.'

		# // parents the follicle into the follicleGroup //
		mc.parent( newName , flcGrp )

		folicle_list.append(newName)
		# print folicle_list

	return folicle_list

	mc.select(cl=True)



# create locator and pxyJnt under folicle


