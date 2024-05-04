from function.rigging.autoRig.base import core
reload(core)


zroGrp = 'spine03Zro_grp'
ctrl = 'spine03_ctrl' 
localObj = 'spine02_gmbCtrl' 
worldObj = 'ctrl_grp'  
baseGrp = 'spine03Offset_grp' 
bodyPart = 'spine03' 
attrOccur = 'spine03_ctrlShape'




#... create null grp under zro grp

localWorld_grp = core.Null(bodyPart + 'LocalWorld_grp')
localWorld_grp.snap( baseGrp )
localWorld_grp.parent(zroGrp)

#... parent ctrl under it
baseGrp = core.Dag(baseGrp)

baseGrp.parent(localWorld_grp)

# Switching world and local object.
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
baseGrpBaseCons = core.orientConstraint( locGrp , worGrp , localWorld_grp )
reverseNode_rev = core.Reverse()
reverseNode_rev.name = bodyPart + '_rev'

# Change name back to null1 null2 for return
#locGrp.name = oldLoc
#worGrp.name = oldWor


controller_shape = core.Dag( attrOccur )


attr = 'localWorld'
controller_shape.addAttribute( ln = attr , k = True , min = 0 , max = 1 )
controller_shape.attr(attr) >> baseGrpBaseCons.attr('w1')
# i = input , o = output
controller_shape.attr(attr) >> reverseNode_rev.attr('ix')
reverseNode_rev.attr( 'ox' ) >> baseGrpBaseCons.attr( 'w0' )



locGrp.parent( localObj )
worGrp.parent( localObj )

#... if not do this is not work why??
#locGrp.parent( 'spine03Zro_grp' ) #<<< this will cause cycle
#worGrp.parent( 'spine03Zro_grp' )



core.clearSel()

#return locGrp , worGrp , worldGrpCons , baseGrpBaseCons , reverseNode_rev