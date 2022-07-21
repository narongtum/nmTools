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

ctrl.addAttribute( longName = 'eyebrow_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'eyebrow_IO' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'inner_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'mid_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )
ctrl.addAttribute( longName = 'outer_UD' ,min = -10 , max = 10, defaultValue = 0 , keyable = True )

# ctrl.snap('eyebrowBaseLFT_crv')
# ctrl.scaleShape( scale = ( 0.05,0.05,0.05 ) )
# ctrl.rotateShape( rotate = (90,0,0) )
# ctrl.moveShape( move = (0,0,0.1) )

# ctrl.color = 'yellow'
# ctrlZro_grp = rigTools.zeroGroup( ctrl )
# ctrlZro_grp.name = part + side + 'Zro_' + 'grp'
# ctrl.lockHideAttrLst('rx','ry','rz','sx','sy','sz','v')
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


# make base_crv rotate and scale to the ctrl
base_crv = core.Dag('eyebrowBase%s_crv' %side)
ctrl.attr('rotate') >> base_crv.attr('rotate')
ctrl.attr('scale') >> base_crv.attr('scale')


'''
root_jnt = core.Dag('head_bJnt')
baseCrv_grp = core.Dag('faceZro_grp')
controller_parCons = core.parentConstraint( root_jnt , baseCrv_grp ,mo = True)
'''
print '##### End of %s part #####'%part