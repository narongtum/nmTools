#... \rigging\autoRig\addRig\simpleAutoSkirt
#... todo
#... make skirt on/off
#... make limit angle condition
#... make for RGT side
#... set graph in remapValue 

from function.rigging.autoRig.base import core
reload(core)




source = 'upperLegRGT_bJnt'
side = 'RGT'

sensitive = (0,1,0,50)
direction = ('forward','rear','backward')
direction =  direction[2]
baseName = 'along' + direction.capitalize()
destination = 'skirtB01Offset_grp'


#...[for dynamic source pointMatrix]	[for still matrix ]
axisGuide = { 	'forward': 	((0,1,0), 				(0,0,1))	,
				'rear': 	((0,1,0), 				(1,0,0))	,	
				'backward': ((0,1,0), 				(0,0,-1))		
					}

# for RGT side
axisGuide = { 	'forward': 	((0,-1,0), 				(0,0,-1))	,
				'rear': 	((0,-1,0), 				(1,0,0))	,	
				'backward': ((0,-1,0), 				(0,0,1))		
					}




for each in axisGuide.keys():
    if each == direction:
        print(axisGuide[each])
        sourcePtx_mtx = axisGuide[each][0]
        still_mtx = axisGuide[each][1]
        
        
    
#... create just once
source_pMtx = core.PointMatrixMult(name = baseName + side , enable = True, inPoint = sourcePtx_mtx )

source_joint = core.Dag(source)
source_joint.attr('worldMatrix') >> source_pMtx.attr('inMatrix')

forward_vector = core.VectorProduct(name = baseName + side, operator = 0)
forward_vector.attr('input1X').value = still_mtx[0]
forward_vector.attr('input1Y').value = still_mtx[1]
forward_vector.attr('input1Z').value = still_mtx[2]

#... for make dot product
forward_dot = core.VectorProduct(name = baseName + 'Dot' + side, operator = 1)

forward_vector.attr('output') >> forward_dot.attr('input1')
source_pMtx.attr('output') >> forward_dot.attr('input2')
forward_dot.attr('normalizeOutput').value = 1

remap_value = core.RemapCurve(name = baseName + '_sentsitive' + side,positive = True, defaultValue = sensitive)

if side == 'LFT':
	forward_dot.attr('outputZ') >> remap_value.attr('inputValue')
	reverseVal_mdl = core.MDLWithMul(name = baseName + '_RevVal' + side,dv = 1)
elif side == 'RGT':
	reverseVal_mdl = core.MDLWithMul(name = baseName + '_RevVal' + side,dv = -1)

forward_dot.attr('outputZ') >> reverseVal_mdl.attr('input1')


input_min = remap_value.attr('inputValue').value
remap_value.attr('inputMin').value = input_min

reverseVal_mdl.attr('output') >> remap_value.attr('inputValue')




#... make pma for collect all value
collectValue_pma = core.PlusMinusAverage(name= baseName + '_collect' + side)
remap_value.attr('outValue') >> collectValue_pma.attr('input3D[0].input3Dx')


#mc.connectAttr('{0}.outValue'.format(remap_value.name), ' alongforward_collectRGT.input3D[0].input3Dx')





#... sandbox zone


