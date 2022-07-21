'''
03 eye lid part
'''

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.blendShape import blendshapeTools as bshTools
reload(bshTools)









	# ============
	# - up Lid UD -
	# ============


part = 'upLid'
side = 'LFT'
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



	# ============
	# - create invert matrix -
	# ============
inv_grp = core.Dag( '%sBsh%sOffset_grp'%(part,side) )
zro_grp = core.Dag( '%sBsh%sZro_grp'%(part,side) )
decom = core.DecomposeMatrix( part+side )

ctrl.attr('inverseMatrix') >> decom.attr('inputMatrix')
decom.attr('outputTranslate') >> inv_grp.attr('translate')
decom.attr('outputRotate') >> inv_grp.attr('rotate')

# mid locator specific name fix later
lid_parCons = core.parentConstraint( 'eyeLidUpBase02%s_loc' %side , zro_grp , mo = True)
lid_parCons.name = part + side
lid_parCons.suffix







	# ============
	# - lo Lid UD -
	# ============

part = 'loLid'
ctrl = core.Dag( '%sBsh%s_ctrl' %(part,side)	)
eyebrowBaseBsh = 'eyeLidLoAll%s_bsh' %side
behv = 'Up'
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




	# ============
	# - create invert matrix -
	# ============
inv_grp = core.Dag( '%sBsh%sOffset_grp'%(part,side) )
zro_grp = core.Dag( '%sBsh%sZro_grp'%(part,side) )
decom = core.DecomposeMatrix( part+side )

ctrl.attr('inverseMatrix') >> decom.attr('inputMatrix')
decom.attr('outputTranslate') >> inv_grp.attr('translate')
decom.attr('outputRotate') >> inv_grp.attr('rotate')

# mid locator specific name fix later
lid_parCons = core.parentConstraint( 'eyeLidLoBase02%s_loc' %side , zro_grp , mo = True)
lid_parCons.name = part + side
lid_parCons.suffix

