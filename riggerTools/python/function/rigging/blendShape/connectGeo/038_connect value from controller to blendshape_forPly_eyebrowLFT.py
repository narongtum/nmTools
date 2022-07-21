'''
2. create controller for connect to blendshape
connnect to template face control instead

'''
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.blendShape import blendshapeTools as bshTools
reload(bshTools)


part = 'eyebrow'
side = 'LFT'

# make connect to template controller
ctrl = core.Dag( 'eyebrowBsh%s_ctrl' %side)
# ctrl.nmCreateController('circle_ctrlShape')
# ctrl.limitTrans( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1 ))

# ctrl.addAttribute( longName = 'eyebrow_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
# ctrl.addAttribute( longName = 'eyebrow_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'inner_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'mid_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'outer_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )


ctrl.lockHideAttrLst('rx','ry','rz','sx','sy','sz','v')
# ctrl.lockHideAttrLst('tx','ty','tz','rx','ry','rz','sx','sy','sz','v')




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


behv = 'AllIn'
attrName = 'eyebrow_IO'
print '%s eyebrow all rolling up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = 'AllIn',
						attr = 'translateX', side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side) , 
						positive = False , amp = 0.75 )


behv = 'AllOut'
print '%s eyebrow all rolling up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = 'eyebrow', behv = behv,
						attr = 'translateX',side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%s%s%s_bsh' %(part,behv,side)  , 
						positive = True , amp = 0.75 )



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






print '##### End of %s part #####'%part