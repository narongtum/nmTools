# corrective joint chain
# by Mateusz Matejczyk
# https://vimeo.com/295232753
# destination rigging.corrective

# Source file
# D:\narongtum\research_and_developement\_Archive_2021\21.06.Jun.11.Fri_corrective joint chain

'''
# direct run
from function.rigging.corrective import correctiveJointChain as cjc
reload(cjc)
'''

# Logs
# 1. Create 3 corrective joint and parent it
# 2. Change outliner color can't use afer Maya 2023

# TODO
# try to use MTcon instead _psCons

from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.util import misc as misc
reload(misc)

from function.rigging.autoRig.base import core
reload(core)


from function.pipeline import logger 
reload(logger)

class correctiveJntLog(logger.MayaLogger):
	LOGGER_NAME = "correctiveJointChain"

# import logging
# logger = logging.getLogger('debug_text')
# logger.setLevel(logging.DEBUG)




def correctiveJointChain(	skinJntA = 'A_jnt'	,
							skinJntB = 'B_jnt'	,
							correctiveJntA = 'ACorr_jnt',
							correctiveJntB = 'BCorr_jnt',
							correctiveJntC = 'CCorr_jnt',
							nameSpace = ''		,				
							baseName = 'arm'	,				
							charScale = 1		,					
							side = 'LFT'		,
							section = 'outer'	,
							offsetValue = 1):





	core.makeHeader('Start of %s module' %__name__)

	skinJntA = core.Dag(skinJntA)
	skinJntB = core.Dag(skinJntB)


	section = section.capitalize()

	if not correctiveJntA:
		mc.error('Please create corrective joint first.')
		
	corr_a_jnt = core.Dag(correctiveJntA)
	corr_b_jnt = core.Dag(correctiveJntB)
	corr_c_jnt = core.Dag(correctiveJntC)


	# make it white
	corr_a_jnt.attr('overrideEnabled').value = 1
	corr_a_jnt.attr('overrideColor').value = 16


	corr_a_jnt.attr('segmentScaleCompensate').value = 0
	corr_b_jnt.attr('segmentScaleCompensate').value = 0
	corr_c_jnt.attr('segmentScaleCompensate').value = 0

	# create null grp for make zero out
	correctiveJnt_grp = core.Null(nameSpace + baseName + 'Corr' + 'Jnt'+ section + side + '_grp')
	correctivePositonJnt_grp = core.Null(nameSpace + baseName + 'Corr' + 'JntPosition'+ section + side + '_grp')
	correctivePositonJnt_grp.parent(correctiveJnt_grp)

	correctiveJnt_grp.snap(corr_b_jnt)

	corr_a_jnt.parent(correctivePositonJnt_grp)

	posiExt_loc = core.Locator(nameSpace + baseName + 'Position' + 'Extract'+ section + side + '_loc')
	rotExt_loc = core.Locator(nameSpace + baseName + 'Rotation' + 'Extract'+ section + side + '_loc')


	rotExt_loc.parent(posiExt_loc)
	posiExt_loc.snap(corr_b_jnt)
	rotExt_loc.snap(corr_c_jnt)

	posiExt_loc.parent(correctiveJnt_grp)


	# psCon to the locator
	corr_a_psCon = core.parentConstraint( skinJntA, skinJntB, posiExt_loc, mo=True, skipRotate = ['x','y','z'] )
	corr_a_psCon.name = nameSpace + baseName + 'CorrA' + section + side + '_psCons'
	corr_b_psCon = core.parentConstraint( skinJntA, skinJntB, rotExt_loc, mo=True, skipRotate = ['x','y','z'] )
	corr_b_psCon.name = nameSpace + baseName + 'CorrB' + section + side + '_psCons'


	# create vector product
	position_normal_dot = core.VectorProduct(nameSpace + baseName + 'PositionNormalDot'+ section + side + '_vpr')
	normal_dot = core.VectorProduct(nameSpace + baseName + 'NormalDot'+ section + side + '_vpr')

	# connect value
	posiExt_loc.attr('translate') >> position_normal_dot.attr('input1')
	rotExt_loc.attr('translate') >> position_normal_dot.attr('input2')

	rotExt_loc.attr('translate') >> normal_dot.attr('input2')

	# get the offset value from corrective b joint
	# offsetValue = corr_b_jnt.attr('translateY').value
	# cancle

	# pass value
	normal_dot.attr('input1Y').value = offsetValue


	intersection_mdv = core.MultiplyDivine(nameSpace + baseName + 'Intersection'+ section + side + '_mdv')
	intersection_mdv.attr('operation').value = 2

	position_normal_dot.attr('output') >> intersection_mdv.attr('input1')
	normal_dot.attr('output') >> intersection_mdv.attr('input2')


	distance_mdv = core.MultiplyDivine(nameSpace + baseName + 'Distance'+ section + side + '_mdv')
	intersection_mdv.attr('output') >> distance_mdv.attr('input2')


	if side == 'LFT':
		i = 1
	else:
		i = -1

	value_slide = (round(offsetValue,2)/2) * i
	distance_mdv.attr('input1Y').value = value_slide
	distance_mdv.attr('output') >> correctivePositonJnt_grp.attr('translate')

	# orient con to corrective joint
	corrective_oriCons = core.orientConstraint(skinJntB, correctiveJntB, mo=True)
	corrective_oriCons.name = (nameSpace + baseName + 'Orient'+ section + side + '_oriCons')

	# make constraint to follow
	allMov_psCons = core.parentConstraint( skinJntA, correctiveJnt_grp, mo=True )
	allMov_psCons.name = nameSpace + baseName + 'AllMove'+ section + side + '_psCons'

	allMov_psCons = core.scaleConstraint( skinJntA, correctiveJnt_grp, mo=True )
	allMov_psCons.name = nameSpace + baseName + 'AllMove'+ section + side + '_scaleCons'


	# create value slide attr at grp for easy to adjust
	correctiveJnt_grp.addAttribute( at = 'float', longName = 'vector_offset', keyable = True )
	correctiveJnt_grp.addAttribute( at = 'float', longName = 'value_slide', keyable = True )
	# correctiveJnt_grp.setOutlineColor('white')

	# assign value
	correctiveJnt_grp.attr( 'vector_offset' ).value = offsetValue
	correctiveJnt_grp.attr( 'value_slide' ).value = value_slide

	# connect back to node
	correctiveJnt_grp.attr( 'vector_offset' ) >> normal_dot.attr('input1Y')
	correctiveJnt_grp.attr( 'value_slide' ) >> distance_mdv.attr('input1Y')

	# lock and hide 'TRS' attr
	correctiveJnt_grp.lockHideAttrLst( 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy' , 'sz' , 'v' )

	# sent value
	# misc.parentMatrix( skinJntA.name, correctiveJnt_grp.name, mo = True, t = True, r = True, s = True)


	# hide Locator
	posiExt_loc.attr('v').value = 0
	rotExt_loc.attr('v').value = 0

	core.makeHeader('End of correctiveJointChain function.')
	return correctiveJnt_grp, corr_a_jnt




'''


from function.rigging.corrective import correctiveJointChain as cjc
reload(corJntChain)


oGap, oJnt = corJntChain.correctiveJointChain(		skinJntA = 'A_jnt'	,
							skinJntB = 'B_jnt'	,
							correctiveJntA = 'ACorrOuter_jnt',
							correctiveJntB = 'BCorrOuter_jnt',
							correctiveJntC = 'CCorrOuter_jnt',
							nameSpace = ''		,				
							baseName = 'arm'	,				
							charScale = 1		,					
							side = 'LFT'		,
							section = 'outer'				)
							
							
corJntChain.correctiveJointChain(		skinJntA = 'A_jnt'	,
							skinJntB = 'B_jnt'	,
							correctiveJntA = 'ACorrInner_jnt',
							correctiveJntB = 'BCorrInner_jnt',
							correctiveJntC = 'CCorrInner_jnt',
							nameSpace = ''		,				
							baseName = 'arm'	,				
							charScale = 1		,					
							side = 'LFT'		,
							section = 'inner'				)	


							

'''