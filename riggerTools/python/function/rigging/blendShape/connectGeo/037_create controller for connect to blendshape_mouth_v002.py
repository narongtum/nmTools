'''
04 mouth part
'''
from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

from function.rigging.blendShape import blendshapeTools as bshTools
reload(bshTools)


	# ============
	# mouth part
	# - up Lip UD All -
	# ============


part = 'upLib'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipUpAll_bsh'
behv = 'Up'
attrName = 'translateY'

print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipUpAll%s_bsh' %behv , 
						positive = True , amp = 1 )



behv = 'Dn'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipUpAll%s_bsh' %behv , 
						positive = False , amp = 1 )






	# ============
	# - lo Lip UD All -
	# ============


part = 'loLib'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipLoAll_bsh'
behv = 'Up'
attrName = 'translateY'

print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipLoAll%s_bsh' %behv , 
						positive = True , amp = 1 )



behv = 'Dn'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipLoAll%s_bsh' %behv , 
						positive = False , amp = 1 )









	# ============
	# - up Lip IO All -
	# ============


part = 'upLib'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipUpAll_bsh'
behv = 'In'
attrName = 'translateX'

print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipUpAll%s_bsh' %behv , 
						positive = False , amp = 1 )



behv = 'Out'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipUpAll%s_bsh' %behv , 
						positive = True , amp = 1 )





	# ============
	# - lo Lip IO All -
	# ============


part = 'loLib'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipLoAll_bsh'
behv = 'In'
attrName = 'translateX'

print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipLoAll%s_bsh' %behv , 
						positive = False , amp = 1 )


part = 'loLib'
behv = 'Out'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipLoAll%s_bsh' %behv , 
						positive = True , amp = 1 )













	# ============
	# - up Lip forward All - (using connect attr)
	# ============


part = 'allLibPull'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipUpAll_bsh'
behv = 'In'
attrName = 'translateZ'

# make base_crv rotate and scale to the ctrl
base_crv = core.Dag('lipUpBase_crv')
multiply = core.MultiDoubleLinear(part)

ctrl.attr('translateZ') >> multiply.attr('input1')
multiply.attr('input2').value = 0.08
multiply.attr('output') >> base_crv.attr('translateZ')

part = 'allLibPush'
# make base_crv rotate and scale to the ctrl
base_crv = core.Dag('lipLoBase_crv')
multiply = core.MultiDoubleLinear(part)

ctrl.attr('translateZ') >> multiply.attr('input1')
multiply.attr('input2').value = 0.08
multiply.attr('output') >> base_crv.attr('translateZ')











	# ============
	# - up Lip FC All -
	# ============


part = 'upLib'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipUpAll_bsh'
behv = 'FC'
attrName = 'rotateZ'
amp = 0.1
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipUpAll%s_bsh' %behv , 
						positive = False , amp = amp )


part = 'upLib'
behv = 'CC'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipUpAll%s_bsh' %behv , 
						positive = True , amp = amp )





	# ============
	# - lo Lip IO All -
	# ============


part = 'loLib'
side = ''
# make connect to template controller
ctrl = core.Dag( 'midLibBsh_ctrl' )
eyebrowBaseBsh = 'lipLoAll_bsh'
behv = 'FC'
attrName = 'rotateZ'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipLoAll%s_bsh' %behv , 
						positive = False , amp = amp )


behv = 'CC'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = 'lipLoAll%s_bsh' %behv , 
						positive = True , amp = amp )



	# ============
	# coner LFT & RGT
	# - up Lip cnr  -
	# ============

	# ============
	# change the pattern
	# - up Lip cnr  -
	# Up ,Dn ,In ,Out
	# ============

# corner
part = 'upLip'
side = 'RGT'
# make connect to template controller
ctrl = core.Dag( 'lipBsh%s_ctrl' %side )
eyebrowBaseBsh = 'lipUpAll_bsh' 
behv = 'Up'
attrName = 'translateY'
amp = 0.7



print '%s  all going up' %part
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s%s_bsh' %(part,behv,side) , 
						positive = True , amp = amp )

behv = 'Dn'
print '%s  all going up' %part
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s%s_bsh' %(part,behv,side) , 
						positive = False , amp = amp )




behv = 'In'
attrName = 'translateX'
amp = 0.7


print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s_bsh' %(part,behv) , 
						positive = False , amp = amp )



behv = 'Out'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s_bsh' %(part,behv) , 
						positive = True , amp = amp )





	# ============
	# change the pattern
	# - lo Lip cnr  -
	# Up ,Dn ,In ,Out
	# ============
part = 'loLip'
side = ''
# make connect to template controller
ctrl = core.Dag( 'lipBshLFT_ctrl' )
eyebrowBaseBsh = 'lipLoAll_bsh'
behv = 'Up'
attrName = 'translateY'
amp = 0.7


print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s_bsh' %(part,behv) , 
						positive = True , amp = amp )



behv = 'Dn'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s_bsh' %(part,behv) , 
						positive = False , amp = amp )



behv = 'In'
attrName = 'translateX'
amp = 0.7


print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName, side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s_bsh' %(part,behv) , 
						positive = False , amp = amp )



behv = 'Out'
print '%s eyebrow all going up' %behv
bshTools.connectCtrlToBsh( 		ctrlNam = ctrl.name , part = part, behv = behv,
						attr = attrName,side = side, 
						bshBase = eyebrowBaseBsh , bshMember = '%sCnr%s_bsh' %(part,behv) , 
						positive = True , amp = amp )