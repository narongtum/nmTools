# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:40:43 2021

@author: Noman
"""

# using for wrap execute connect blendshape node >>> geo
# super sensitive not sure is okay to make it to function



from function.rigging.blendShape import blendshapeTools as bshTools
reload(bshTools)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.util import misc 
reload(misc)




# [controller] >> [blendshape]
	# ========================
	# - execute fundtion 
	# ========================

'''

from function.rigging.blendShape import blendshapeConnectGeo as bshCon
reload(bshCon)



bshCon.connectEyebrow(side = 'LFT')
bshCon.connectEyebrow(side = 'RGT')

bshCon.connectEyeLid(side = 'LFT')
bshCon.connectEyeLid(side = 'RGT')

bshCon.connectEyeBall(side = 'LFT')
bshCon.connectEyeBall(side = 'RGT')


bshCon.connectNose()
bshCon.connectWingNose(side = 'LFT')
bshCon.connectWingNose(side = 'RGT')


bshCon.connectCheek(side = 'LFT')
bshCon.connectCheek(side = 'RGT')
bshCon.connectMouth()
bshCon.connectLipSide(side = 'LFT')
bshCon.connectLipSide(side = 'RGT')


'''




# use this function to run connection between  

# [controller] >> [blendshape]
	# ========================
	# - Connect Value to controller -
	# ========================



# import ctrl and adjust proper prosition
# run this for connect value (sample)


def connectEyebrow( side = 'LFT' ):

	part = 'eyebrow' 
	if side == 'RGT':
		logicA = False
		logicB = True
	elif side == 'LFT':
		logicA = False
		logicB = True



	# make connect to template controller
	ctrl = core.Dag( 'eyebrowBsh%s_ctrl' %side)

	ctrl.addAttribute( longName = 'inner_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mid_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'outer_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.lockHideAttrLst('rx','ry','rz','sx','sy','sz','v')






		# ============
		# - Eyebrow -
		# ============


	part = 'eyebrow'
	eyebrowBaseBsh = 'eyebrowAll%s_bsh' %side

	behv = 'AllUp'
	attrName = 'eyebrow_UD'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = 'translateY', side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = 0.75 )


	behv = 'AllDn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = 'translateY',side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = 0.75 )




	# reverse with side
	behv = 'AllIn'
	attrName = 'eyebrow_IO'
	print '%s eyebrow all rolling up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = 'AllIn',
							attr = 'translateX', side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = logicA , amp = 0.75 )


	behv = 'AllOut'
	print '%s eyebrow all rolling up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = 'eyebrow', behv = behv,
							attr = 'translateX',side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = logicB , amp = 0.75 )



	if side == 'RGT':

		# reverse with side
		behv = 'AllPull'
		attrName = 'All_PP'
		bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
								attr = 'translateZ', side = side, 
								bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
								positive = False , amp = 1 )
		behv = 'AllPush'
		bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
								attr = 'translateZ',side = side, 
								bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
								positive = True , amp = 1 )


	else:

		# reverse with side
		behv = 'AllPull'
		attrName = 'All_PP'
		bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
								attr = 'translateZ', side = side, 
								bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
								positive = True , amp = 1 )
		behv = 'AllPush'
		bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
								attr = 'translateZ',side = side, 
								bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
								positive = False , amp = 1 )






	behv = 'InnUp'
	attrName = 'inner_UD'
	print '%s eyebrow all rolling up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv ,
							attr = attrName , side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = 0.1 )
	behv = 'InnDn'
	print '%s eyebrow all rolling up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = 0.1 )






	behv = 'MidUp'
	attrName = 'mid_UD'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = 0.1 )

	behv = 'MidDn'
	print '%s eyebrow all going down' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = 0.1 )
	print 'outer eyebrow all going up'







	behv = 'OutUp'
	attrName = 'outer_UD'
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = 0.1 )
	print 'outer all going up'
	behv = 'OutDn'
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = 0.1 )





	misc.makeHeader('End of %s %s part'%(part,side))






def connectEyeLid(side = 'RGT'):


	part = 'upLid'

	# make connect to template controller
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)

	eyebrowBaseBsh = 'eyeLidUpAll%s_bsh' %side
	amp = 1
	behv = 'Up'
	attrName = 'translateY'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = eyebrowBaseBsh , bshMember = 'upLidUp%s_bsh' %side  , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )


	behv = 'FC'
	attrName = 'translateX'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'CC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )



	ctrl.addAttribute( longName = 'inner_UD' ,min = 0 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mid_UD' ,min = 0 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'outer_UD' ,min = 0 , max = 10, defaultValue = 0 , keyable = True )

	ctrl.lockHideAttrLst('tz','rx','ry','rz','sx','sy','sz','v')





		# ============
		# - insert inn mid outer -
		# ============


	# behv = 'InnDn'
	# attrName = 'inner_UD'

	#behv = 'MidDn'
	#attrName = 'mid_UD'


	#behv = 'OutDn'
	#attrName = 'outer_UD'


	eyebrowBaseBsh = 'eyeLidUpAll%s_bsh' %side
	behv_Lst = [ 'InnDn' , 'MidDn' , 'OutDn' ]
	attrName_Lst = ['inner_UD' , 'mid_UD' , 'outer_UD' ]

	for i in range(len(behv_Lst)):
		print behv_Lst[i]
		print attrName_Lst[i]

		print '%s eyebrow all going up' %behv
		bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name, part = part, behv = behv_Lst[i],
								attr = attrName_Lst[i], side = side, 
								bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv_Lst[i],side)  , 
								positive = True , amp = amp )










		# ============
		# - lo Lid UD -
		# ============

	part = 'loLid'
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
	eyebrowBaseBsh = 'eyeLidLoAll%s_bsh' %side
	behv = 'Up'
	attrName = 'translateY'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )


	attrName = 'translateX'
	behv = 'FC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'CC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )


	ctrl.addAttribute( longName = 'inner_UD' ,min = 0 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mid_UD' ,min = 0 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'outer_UD' ,min = 0 , max = 10, defaultValue = 0 , keyable = True )

	ctrl.lockHideAttrLst('tz','rx','ry','rz','sx','sy','sz','v')





		# ============
		# - insert inn mid outer For loLid
		# ============


	#behv = 'InnUp'
	#attrName = 'inner_UD'

	#behv = 'MidUp'
	#attrName = 'mid_UD'


	behv = 'OutUp'
	attrName = 'outer_UD'





	eyebrowBaseBsh = 'eyeLidLoAll%s_bsh' %side
	behv_Lst = [ 'InnUp' , 'MidUp' , 'OutUp' ]
	attrName_Lst = ['inner_UD' , 'mid_UD' , 'outer_UD' ]

	for i in range(len(behv_Lst)):
		print behv_Lst[i]
		print attrName_Lst[i]

		print '%s eyebrow all going up' %behv
		bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name, part = part, behv = behv_Lst[i],
								attr = attrName_Lst[i], side = side, 
								bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv_Lst[i],side)  , 
								positive = True , amp = amp )

	misc.makeHeader('End of %s %s part'%(part,side))







def connectEyeBall(side = 'LFT'):





	part = 'eyeBall'

	if side == 'RGT':
		logicA = True
		logicB = False
	elif side == 'LFT':
		logicA = False
		logicB = True


	# make connect to template controller
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
	baseBsh = 'eyeBallAll%s_bsh' %side
	amp = 1
	behv = 'Up'
	attrName = 'translateY'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )





		# ============
		# - eyeBall roll in out -
		# ============

	attrName = 'translateX'

	behv = 'In'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'Out'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )







		# ============
		# - eyeBall roll in out -
		# ============

	attrName = 'rotateZ'
	amp = 0.01
	behv = 'FC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = amp )
	behv = 'CC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = True , amp = amp )





		# ============
		# - add cnr UD -
		# ============

	ctrl.addAttribute( longName = 'cnr_inner_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'cnr_outer_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )



	behv = 'InnUp'
	part = 'eyeCnr'
	attrName = 'cnr_inner_UD'
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'InnDn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )



		# ============
		# - add cnr Out UD -
		# ============

	behv = 'OutUp'
	part = 'eyeCnr'
	attrName = 'cnr_outer_UD'
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'OutDn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )





	ctrl.lockHideAttrLst('tz','rx','ry','rz','sx','sy','sz','v')
	misc.makeHeader('End of %s %s part'%(part,side))












def connectNose():

	# ============
	# - all nose this should run once -
	# ============


	amp = 1
	part = 'nose'


	behv = 'Sq'
	attrName = 'translateY'
	baseBsh = 'noseAll_bsh'
	side = 'LFT'
	ctrl = core.Dag( '%sBsh_ctrl' %part	)

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = 'noseBsh_ctrl' , part = part, behv = behv,
							attr = attrName, side = '', 
							bshBase = baseBsh , bshMember = 'noseSq_bsh'  , 
							positive = False , amp = amp )


	behv = 'St'
	attrName = 'translateY'
	baseBsh = 'noseAll_bsh'

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = 'noseBsh_ctrl' , part = part, behv = behv,
							attr = attrName, side = '', 
							bshBase = baseBsh , bshMember = 'noseSt_bsh'  , 
							positive = True , amp = amp )

	# ============
	# - adding nose slide left right -
	# ============


	behv = 'LFT'
	attrName = 'translateX'
	baseBsh = 'noseAll_bsh'

	print '%s %s all going up' %(behv,part)
	bshTools.connectCtrlToBsh( 		ctrlNam = 'noseBsh_ctrl' , part = part, behv = behv,
							attr = attrName, side = '', 
							bshBase = baseBsh , bshMember = 'noseLFT_bsh'  , 
							positive = True , amp = amp )


	behv = 'RGT'
	attrName = 'translateX'
	baseBsh = 'noseAll_bsh'

	print '%s %s all going up' %(behv,part)
	bshTools.connectCtrlToBsh( 		ctrlNam = 'noseBsh_ctrl' , part = part, behv = behv,
							attr = attrName, side = '', 
							bshBase = baseBsh , bshMember = 'noseRGT_bsh'  , 
							positive = False , amp = amp )



	ctrl.lockHideAttrLst('tz','rx','ry','rz','sx','sy','sz','v')
	misc.makeHeader('End of %s part'%part)




def connectWingNose( side = 'LFT' ):


	# ============
	# - all nose this should run twice -
	# ============





	# ============
	# - another controller for manipulate wing nose -
	# ============
	amp = 1
	behv = 'Up'
	part = 'nose'
	attrName = 'translateY'
	baseBsh = 'noseAll%s_bsh' %side
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )


	behv = 'Dn'
	attrName = 'translateY'
	baseBsh = 'noseAll%s_bsh' %side

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = amp )





	behv = 'FC'
	attrName = 'translateX'
	baseBsh = 'noseAll%s_bsh' %side
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )


	behv = 'CC'
	attrName = 'translateX'
	baseBsh = 'noseAll%s_bsh' %side

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = amp )



	ctrl.lockHideAttrLst('tz','rx','ry','rz','sx','sy','sz','v')
	misc.makeHeader('End of Wing nose')






def connectCheek(side = 'LFT'):

	part = 'cheek'

	# for eyelid up and lo 


		# ============
		# - Cheek -
		# ============


	
	
	# make connect to template controller
	ctrl = core.Dag( 'cheekBsh%s_ctrl' %side	)
	baseBsh = 'cheekAll%s_bsh' %side
	amp = 1

	behv = 'LoOut'
	attrName = 'translateZ'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = True , amp = amp )
	behv = 'LoIn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )






		# ============
		# - eyeBall roll up down -
		# ============


	part = 'cheek'

	# make connect to template controller
	ctrl = core.Dag( 'cheekBsh%s_ctrl' %side	)
	baseBsh = 'cheekAll%s_bsh' %side
	amp = 1
	attrName = 'translateY'
	behv = 'UpOut'


	if side == 'LFT':
		logicA = 'False'
		logicB = 'True'

	elif side == 'RGT':
		logicA = 'True'
		logicB = 'False'

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = logicA , amp = amp )
	behv = 'UpIn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = logicB , amp = amp )









		# ============
		# - eyeBall roll up down -
		# ============


	part = 'puff'

	# make connect to template controller
	ctrl = core.Dag( 'cheekBsh%s_ctrl' %side	)
	baseBsh = 'cheekAll%s_bsh' %side
	amp = 1
	attrName = 'translateX'
	behv = 'Out'

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )
	behv = 'In'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = True , amp = amp )







	ctrl.lockHideAttrLst('rx','ry','rz','sx','sy','sz','v')
	misc.makeHeader('End of %s %s part'%(part,side))









def connectMouth():
	side = 'Mid'
	part = 'mouth'
	# make connect to template controller
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
	baseBsh = 'mouthMidAll_bsh'
	amp = 1
	behv = 'Up'
	attrName = 'translateY'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = 'mouthUp_bsh'  , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = 'mouthDn_bsh' , 
							positive = False , amp = amp )





	behv = 'TurnR'
	attrName = 'translateX'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = 'mouthLFT_bsh'  , 
							positive = True , amp = amp )
	behv = 'TurnL'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = 'mouthRGT_bsh' , 
							positive = False , amp = amp )




	'''

	behv = 'TurnR'
	attrName = 'translateX'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = 'mouthLFT_bsh'  , 
							positive = True , amp = amp )
	behv = 'TurnL'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = 'mouthRGT_bsh' , 
							positive = False , amp = amp )


	'''



		# ============
		# - mouth roll in out -
		# ============

	attrName = 'rotateZ'
	amp = 0.1

	behv = 'FC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s_bsh' %(part,behv)  , 
							positive = False , amp = amp )
	behv = 'CC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s_bsh' %(part,behv) , 
							positive = True , amp = amp )





	'''


		# ============
		# - mouth roll in out -
		# ============

	attrName = 'rotateZ'
	amp = 0.1

	behv = 'FC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s_bsh' %(part,behv)  , 
							positive = False , amp = amp )
	behv = 'CC'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s_bsh' %(part,behv) , 
							positive = True , amp = amp )


	'''



	# ============
		# - add cnr UD -
		# ============

	ctrl.addAttribute( longName = 'upLip_mid_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'loLip_mid_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mouth_curl_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mouth_clench_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mouth_pull_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mouth_U_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'mouth_AU_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )






		# ============
		# - mouth roll in out -
		# ============

	behv = 'MidUp'
	part = 'upLip'
	attrName = 'upLip_mid_UD'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'MidDn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )















		# ============
		# - mouth roll in out -
		# ============

	behv = 'MidUp'
	part = 'loLip'
	attrName = 'loLip_mid_UD'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'MidDn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )





		# ============
		# - mouth roll in out -
		# ============

	behv = 'CurlIn'
	part = 'mouth'
	attrName = 'mouth_curl_IO'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'CurlOut'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )


		# ============
		# - mouth roll in out -
		# ============

	behv = 'ClenchIn'
	part = 'mouth'
	attrName = 'mouth_clench_IO'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'ClenchOut'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )







		# ============
		# - mouth roll in out -
		# ============

	behv = 'PullIn'
	part = 'mouth'
	# attrName = 'mouth_pull_IO'
	attrName = 'translateZ'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = False , amp = amp )
	behv = 'PullOut'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = True , amp = amp )









		# ============
		# - mouth U
		# ============

	behv = 'UIn'
	part = 'mouth'
	attrName = 'mouth_U_IO'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'UOut'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )




		# ============
		# - mouth AU
		# ============


	behv = 'AUIn'
	part = 'mouth'
	attrName = 'mouth_AU_IO'
	side = ''
	amp = 1

	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
							positive = True , amp = amp )
	behv = 'AUOut'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )





	ctrl.lockHideAttrLst('rx','ry','sx','sy','sz','v')
	misc.makeHeader('End of %s part'%part)



def connectLipSide(side = 'LFT'):



	part = 'lip' 
	if side == 'RGT':
		logicA = True
		logicB = False
	elif side == 'LFT':
		logicA = False
		logicB = True



	# make connect to template controller
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
	baseBsh = 'lipAll%s_bsh' %side
	amp = 1

	behv = 'Up'
	attrName = 'translateY'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = 'mouthCnr%s%s_bsh' %(behv,side) , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = 'mouthCnr%s%s_bsh' %(behv,side) , 
							positive = False , amp = amp )









		# ============
		# - lip or mouth roll up down -
		# ============


	part = 'lip'

	# make connect to template controller
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
	baseBsh = 'lipAll%s_bsh' %side
	amp = 1

	behv = 'Out'
	attrName = 'translateX'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = 'mouthCnr%s%s_bsh' %(behv,side) , 
							positive = True , amp = amp )
	behv = 'In'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = 'mouthCnr%s%s_bsh' %(behv,side) , 
							positive = False , amp = amp )






		# ============
		# - lip or mouth roll up down -
		# ============


	part = 'lip'

	# make connect to template controller
	ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
	baseBsh = 'lipAll%s_bsh' %side
	amp = 1

	behv = 'Out'
	attrName = 'translateZ'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = 'lipPart%s%s_bsh' %(behv,side) , 
							positive = True , amp = amp )
	behv = 'In'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = 'lipPart%s%s_bsh' %(behv,side) , 
							positive = False , amp = amp )




	# ============
		# - add cnr UD -
		# ============

	ctrl.addAttribute( longName = 'upLip_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
	ctrl.addAttribute( longName = 'loLip_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )




	part = 'upLip'



	amp = 1

	behv = 'Up'
	attrName = 'upLip_UD'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )






	part = 'loLip'

	# make connect to template controller

	amp = 1

	behv = 'Up'
	attrName = 'loLip_UD'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName, side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = True , amp = amp )
	behv = 'Dn'
	print '%s eyebrow all going up' %behv
	bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
							attr = attrName,side = side, 
							bshBase = baseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
							positive = False , amp = amp )





	ctrl.lockHideAttrLst('rx','ry','rz','sx','sy','sz','v')
	misc.makeHeader('End of %s %s part'%(part,side))


