'''
from function.rigging.feature import autoSkirtRig
reload(autoSkirtRig)
'''


import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

"""
Tune Clamp for proper behaivor
Tune MDV for proper behaivor

move to feature

"""



# a raw name of this controller
# name = ''
# blind joint name
# jointName = ''
# Name of controller that want to add attr
# attrPlace = ''

def autoSkirt( name = 'skirtBack01', jointName = 'upperLegRGT_bJnt', attrPlace = 'skirtBackCurl_ctrl' ):
	parent_jnt = core.Dag( jointName )
	autoSkirt_ctrl = core.Dag( '%s_ctrl' %name )
	# Warning solid variable
	offset_grp = core.Dag( '%sOffset_grp' %name )



	autoSkirt_cmp = core.Clamp(name)
	autoSkirt_cmp.attr('minR').value = -90
	autoSkirt_cmp.attr('minG').value = -90
	autoSkirt_cmp.attr('minB').value = -90

	autoSkirt_cmp.attr('maxR').value = 360
	autoSkirt_cmp.attr('maxG').value = 360
	autoSkirt_cmp.attr('maxB').value = 360

	parent_jnt.attr('rotate') >> autoSkirt_cmp.attr( 'input' )



	# create mdv for decrease value 76 percent
	resisVal_mdv = core.MultiplyDivine(name+'Resis' + '_mdv')
	resisVal_mdv.attr('input2X').setVal(0.76)
	resisVal_mdv.attr('input2Y').setVal(0.76)
	resisVal_mdv.attr('input2Z').setVal(0.76)
	# connect value
	autoSkirt_cmp.attr('output') >> resisVal_mdv.attr( 'input1' )


	# For spread value
	multiplier_mdv = core.MultiplyDivine(name + 'MulVal_mdv')
	resisVal_mdv.attr('output') >> multiplier_mdv.attr( 'input1' )
	multiplier_mdv.attr('input2X').setVal(1)
	multiplier_mdv.attr('input2Y').setVal(1.1)
	multiplier_mdv.attr('input2X').setVal(1.2)




	# Create blendColor Node
	switch_blc = core.BlendColors(name+'Switch')
	switch_blc.suffix
	switch_blc.attr('blender').setVal(0)
	multiplier_mdv.attr( 'output.outputX' ) >> switch_blc.attr( 'color1.color1R' )
	multiplier_mdv.attr( 'output.outputZ' ) >> switch_blc.attr( 'color1.color1B' )


	switch_blc.attr( 'output' ) >> offset_grp.attr( 'rotate' )


	if attrPlace:
		attrPlace_ctrl = core.Dag( attrPlace )
		attrPlace_shape = core.Dag( attrPlace_ctrl.shape )
		attrPlace_shape.addAttribute( longName = 'autoSkirt' , min = 0 , max = 1 , defaultValue = 0 , keyable = True )
		attrPlace_shape.attr( 'autoSkirt' ) >> switch_blc.attr( 'blender' ) 
