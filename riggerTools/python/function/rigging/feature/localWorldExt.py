#... Update version for local/world not make it cycle with curl rig

from function.rigging.autoRig.base import core
reload(core)


ctrl = 'spine02FK_ctrl' 
localObj = 'spineRig_grp' 
worldObj = 'ctrl_grp'  
baseGrp = 'spine02FKOffset_grp' 
bodyPart = 'spine02FK' 


#... Switching world and local object.
locGrp = core.Null()
worGrp = core.Null()
locGrp.snap( baseGrp )
worGrp.snap( baseGrp )
# Store null1 null2
oldLoc = str( locGrp.name )
oldWor = str( worGrp.name )

if bodyPart == None:
	# Assign new name
	locGrp.name =  'local'
	worGrp.name =  'world'
else:
	locGrp.name = bodyPart +'_local'
	worGrp.name = bodyPart + '_world'



# Orient constraint
worldGrpCons = core.orientConstraint( worldObj , worGrp , mo = True )
baseGrpBaseCons = core.orientConstraint(locGrp , worGrp , baseGrp )
reverseNode_rev = core.Reverse()
reverseNode_rev.name = bodyPart + '_rev'

# Change name back to null1 null2 for return
#locGrp.name = oldLoc
#worGrp.name = oldWor

controller_transform = core.Dag( ctrl )
controller_shape = core.Dag( controller_transform.shape )


attr = 'localWorld'
controller_shape.addAttribute( ln = attr , k = True , min = 0 , max = 1 )
controller_shape.attr(attr) >> baseGrpBaseCons.attr('w1')
# i = input , o = output
controller_shape.attr(attr) >> reverseNode_rev.attr('ix')
reverseNode_rev.attr( 'ox' ) >> baseGrpBaseCons.attr( 'w0' )



locGrp.parent( localObj )
worGrp.parent( localObj )

#... if not do this is not work why??
locGrp.parent( 'spine02FKZro_grp' )
worGrp.parent( 'spine02FKZro_grp' )



core.clearSel()

