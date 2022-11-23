#... 
from function.rigging.autoRig.base import core
reload(core)

source = 'upperLegLFT_bJnt'
side = 'LFT'

sensitive = (0,1,0,50)
direction = ('forward','rear','backward')
direction =  direction[1]
baseName = 'along' + direction
#...					[for dynamic source pointMatrix]	[for still matrix ]
axisGuide = { 	'forward': 	((0,1,0), 				(0,0,1))	,
				'rear': 	((0,1,0), 				(1,0,0))	,	
				'backward': ((0,1,0), 				(0,0,-1))		
					}

destination = 'objectA01'

for each in axisGuide.keys():
    if each == direction:
        print(axisGuide[each])
        sourcePtx_mtx = axisGuide[each][0]
        still_mtx = axisGuide[each][1]
        
        
    

source_pMtx = core.PointMatrixMult(name = baseName, enable = True, inPoint = sourcePtx_mtx )

source_joint = core.Dag(source)
source_joint.attr('worldMatrix') >> source_pMtx.attr('inMatrix')

forward_vector = core.VectorProduct(name = baseName + 'Forward' + side, operator = 0)
forward_vector.attr('input1X').value = still_mtx[0]
forward_vector.attr('input1Y').value = still_mtx[1]
forward_vector.attr('input1Z').value = still_mtx[2]

#... for make dot product
forward_dot = core.VectorProduct(name = baseName + 'ForwardDot' + side, operator = 1)

forward_vector.attr('output') >> forward_dot.attr('input1')
source_pMtx.attr('output') >> forward_dot.attr('input2')
forward_dot.attr('normalizeOutput').value = 1

remap_value = core.RemapCurve(name = baseName + '_sentsitive',positive = True, defaultValue = sensitive)


forward_dot.attr('outputZ') >> remap_value.attr('inputValue')
input_min = remap_value.attr('inputValue').value
remap_value.attr('inputMin').value = input_min