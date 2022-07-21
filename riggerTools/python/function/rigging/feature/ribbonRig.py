# create ribbon rig

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

from function.rigging.util import misc as misc
reload(misc)






# Global gather infomation
width = 10				
numJoints = 5			
prefix = 'top' 		
side = 'LFT'			
aim = 'y+'				
jointTop = 'upperArmLFT_bJnt'			
jointBtm = 'lowerArmLFT_bJnt'
part = 'upArm'
charScale = 1
types = 'Rbn'
noTouch_grp = 'noTouch_grp'
elem = ''

partElem = part + elem
position = ( 'Top' , 'Mid' ,'Btm' )
ctrl_grp = 'armRigLFT_grp'












topPart = core.Dag( jointTop )
btmPart = core.Dag( jointBtm )

topPart_rbnJnt = rigTools.jointAt( topPart )
btmPart_rbnJnt = rigTools.jointAt( btmPart )

# armARbnTopLFT_rbnJnt
topPart_rbnJnt.name = partElem + types + position[0] + side + '_rbnJnt' 
topPart_rbnJnt.attr('radius').value = 5
topPart_rbnJnt.attr('overrideEnabled').value = 1
topPart_rbnJnt.attr('overrideColor').value = 3

btmPart_rbnJnt.name = partElem + types + position[2] + side + '_rbnJnt' 
btmPart_rbnJnt.attr('radius').value = 5
btmPart_rbnJnt.attr('overrideEnabled').value = 1
btmPart_rbnJnt.attr('overrideColor').value = 3





if aim == 'y+':
	# start from LFT > RGT
	topPoint  = (width/2*-1)
	endPoint  = (width/2)

elif aim == 'y-':
	endPoint  = (width/2*-1)
	topPoint  = (width/2)





# Create temp base NURBS-plane 
tmpPlane = core.nurbPlane( axis = (0,1,0), width = width, lengthRatio = (1.0/width) , u = 2 , v = 1,  degree = 3 , ch = 0)
tmpPlane.name = 'tmpPlane_nrb'

# Create wire deformer
deformCrv = core.curve( p = [(topPoint , 0 , 0) , (endPoint, 0, 0)], degree = 1	)
deformCrv.name = 'deform_crv'
wireDef = mc.wire(	tmpPlane, dds = (0,15), wire = deformCrv	)

# Create Clusters : 
clsTop = core.cluster(	( deformCrv.name + '.cv[0]'),  relative = 1 )
clsEnd = core.cluster(	( deformCrv.name + '.cv[1]'),  relative = 1 )
clsTop.maSnap( jointTop )
clsEnd.maSnap( jointBtm )

# Duplicate
name = partElem + types + side
mc.duplicate( tmpPlane.name ,  name =  name + '_nrb')


# makeTheNurb to object
ribbon_nrb = core.Dag( name + '_nrb' )
ribbon_nrb.attr('visibility').value = 0

tmpPlane.deleteName()
clsTop.deleteName()
clsEnd.deleteName()
deformCrv.deleteName()





name = partElem + types

# Create group and Parenting to Main grp
# follicle grp
flc_grp = core.Null( name +'Flc' + side +'_grp')
# detail controller
detail_grp = core.Null( name +'Detail' + side + '_grp')
# nurb grp
nrb_grp = core.Null( name +'Nrb' + side + '_grp')
# For main ribbon 
rbnCtrl_grp = core.Null( name +'Ctrl' + side + '_grp')




# Create inbetween flc and joint 
# For main ribbon 
proxyJntList = []
for each in range (0 , numJoints ):

	if not numJoints == 5:
		mc.warning('You must use only 5 joint.')
		
	else:
		midJnt = 3


	num =  each + 1
	# Common name
	name =  partElem + types + '%02d'%num + side

	# Create Follicle
	folicle = core.Null( name + '_flc')
	folicle.follicle( name = folicle.name + 'Shape_flc', ss = True )
	folicleShape = core.Dag( folicle.shape )
	ribbon_nrb.attr('local') >> folicleShape.attr('inputSurface')
	ribbon_nrb.attr('worldMatrix[0]') >> folicleShape.attr('inputWorldMatrix')

	# Connected armALFTShape.outRotate to armALFT.rotate
	folicleShape.attr('outRotate') >> folicle.attr('rotate')
	folicleShape.attr('outTranslate') >> folicle.attr('translate')

	# Inbetween formula
	uVal = ((0.5 / numJoints) * (each + 1) * 2) - ((0.5 / (numJoints * 2)) * 2)
	folicleShape.attr('parameterU').value = uVal
	folicleShape.attr('parameterV').value = 0.5
	ribbon_jnt = core.Joint()
	ribbon_jnt.name = name + '_pxyJnt'
	ribbon_jnt.maSnap( folicle )
	

	# Adjust rotation for proper Axis
	if aim == 'y+':
		ribbon_jnt.attr('rotateX').value += 90

	elif aim == 'y-':
		ribbon_jnt.attr('rotateX').value -= 90

	
	ribbon_jnt.attr('radius').value = 2.5
	ribbon_jnt.attr('overrideEnabled').value = 1
	# Make it gray
	ribbon_jnt.attr('overrideColor').value = 3
	ribbon_ctrl = core.Dag( name + '_ctrl' )
	ribbon_ctrl.nmCreateController('circle_ctrlShape')
	ribbonZro_grp = rigTools.zeroGroupNam( ribbon_ctrl )
	
	ribbon_ctrl.editCtrlShape( axis = charScale * 4 )
	ribbon_ctrl.rotateShape( rotate = ( 0 , 0 , -90 ) )
	ribbon_ctrl.color = 'softBlue'

	# Constraint
	ribbonZro_grp.maSnap( ribbon_jnt )
	folicle_parCons = core.parentConstraint( folicle , ribbonZro_grp ,mo = True)
	folicle_parCons.name = name + '_parCons'

	
	# Lock and hide
	ribbon_ctrl.lockHideAttrLst( 'rx' , 'ry' , 'rz' ,  'v' )
	ribbon_jnt.parent( ribbon_ctrl )

	# Parenting Group
	folicle.parent( flc_grp )
	ribbonZro_grp.parent( detail_grp )


	proxyJntList.append( ribbon_jnt.name )



	
	
ribbon_nrb.parent( nrb_grp )
# Create Middle ribbon joint

name =  partElem + types + '%02d'%midJnt + side

middle_ctrl = core.Dag( name + '_ctrl' )

middle_rbnJnt = core.Joint()
middle_rbnJnt.name = partElem + 'Mid' + side + '_rbnJnt'
middle_rbnJnt.maSnap( middle_ctrl )

middle_rbnJnt.attr('radius').value = 5
middle_rbnJnt.attr('overrideEnabled').value = 1
middle_rbnJnt.attr('overrideColor').value = 3


#								#
# Create middle square ctrl
#								#

name = partElem + 'Mid' 
ribbonMid_ctrl = core.Dag( name + types + side + '_ctrl')
ribbonMid_ctrl.nmCreateController('square_ctrlShape')
ribbonMid_ctrl.editCtrlShape( axis = charScale * 7.5 )

# Add attr
ribbonMid_ctrl.addAttribute( longName = 'Bar' , niceName = '-'   , at ='enum', en = 'Twist' , keyable = True )
ribbonMid_ctrl.addAttribute( longName = 'Upper_Twist' , defaultValue = 0 , keyable = True )
ribbonMid_ctrl.addAttribute( longName = 'Lower_Twist' , defaultValue = 0 , keyable = True )
ribbonMid_ctrl.addAttribute( attributeType = 'short' , longName = 'Detail' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )
ribbonMid_ctrl.addAttribute( attributeType = 'short' , longName = 'Auto_Twist' , minValue = 0 , maxValue = 1 , defaultValue = 0 , keyable = True )

ribbonMid_ctrl.color = 'yellow'
ribbonMid_ctrl.rotateShape(rotate = ( 0 , 0 , -90))

ribbonMidLocate_loc = core.Locator( name + types + side + '_loc' )
ribbonMidAim_grp = core.Null( name + types + 'Aimed' + side + '_grp')
ribbonMidAim_grp.parent( ribbonMidLocate_loc )
ribbonMid_ctrl.parent( ribbonMidAim_grp )
ribbonMidLocate_loc.maSnap( middle_rbnJnt )



# Use parent insted ParCon
middle_rbnJnt.parent( ribbonMid_ctrl )

# Create up aim for middle ribbon
midAimUp_loc = core.Locator( name + types + 'AimUp' + side + '_loc' )
midAimUp_loc.snap( middle_rbnJnt )
aimUpZro_grp = rigTools.zeroGroupNam( midAimUp_loc )
midAimUp_loc.attr('translateY').value +=10
midAimUp_loc.attr('v').value = 0


# AimCons for make it look at
middle_aimCons = core.aimConstraint(  jointTop , ribbonMidAim_grp ,  mo = True , worldUpObject = midAimUp_loc.name)
middle_aimCons.attr('worldUpType').value = 1
middle_aimCons.name = name + types + '_AimUp' + side + '_aimCons'



# Could not uset method skinCluster it will crash
skinName = mc.skinCluster(  topPart_rbnJnt.name , middle_rbnJnt.name ,btmPart_rbnJnt.name , ribbon_nrb.name ,dr = 7 , mi = 2 )[0]
#ribbon_skc = core.SkinCluster( topPart_rbnJnt.name , middle_rbnJnt.name ,btmPart_rbnJnt.name , ribbon_nrb.name ,dr = 7 , mi = 2 )

for each in range (0,4):
	print each
	mc.skinPercent( skinName, ribbon_nrb.name + '.cv[0][%d]' %each , transformValue=[( topPart_rbnJnt.name , 1), ( middle_rbnJnt.name, 0)])
	mc.skinPercent( skinName , ribbon_nrb.name + '.cv[1][%d]' %each , transformValue=[( topPart_rbnJnt.name , 0.8), ( middle_rbnJnt.name, 0.2 )])
	mc.skinPercent( skinName, ribbon_nrb.name + '.cv[3][%d]' %each , transformValue=[( middle_rbnJnt.name , 0.2), ( btmPart_rbnJnt.name, 0.8 )])



# Create up aim for upper ribbon
name = partElem + position[0]
topLocate_loc = core.Locator(  name + types + side + '_loc' )
topAimed_grp = core.Null( name + types +'Aimed'+ side + '_grp' )
topUpObj_loc = core.Locator( name + types + 'UpObj' + side + '_loc' )

topAimed_grp.parent( topLocate_loc )
topUpObj_loc.parent( topLocate_loc )

topLocate_loc.maSnap( jointTop )
# because it orient from
topUpObj_loc.attr('translateX').value = -10
topPart_rbnJnt.parent( topAimed_grp )
topUpObj_loc.attr('v').value = 0


# Create up aim for lower ribbon
name = partElem + position[2]
lowerLocate_loc = core.Locator( name + types + side + '_loc' )
lowerAimed_grp = core.Null( name + types +'Aimed'+ side + '_grp' )
lowerUpObj_loc = core.Locator( name + types + 'UpObj' + side + '_loc' )

lowerAimed_grp.parent( lowerLocate_loc )
lowerUpObj_loc.parent( lowerLocate_loc )

lowerLocate_loc.snap( jointBtm )
lowerUpObj_loc.attr('translateX').value = -10
lowerUpObj_loc.attr('v').value = 0
btmPart_rbnJnt.parent( lowerAimed_grp )

# Point constraint Point for make locate  it follow 
rbnUpper_poinCons = core.pointConstraint(  jointTop , topLocate_loc , mo = True )
rbnUpper_poinCons.name = partElem + types + position[0] + side + '_pointCons'

# Point constraint Point for make locate  it follow 
rbnLower_poinCons = core.pointConstraint(  jointBtm , lowerLocate_loc , mo = True )
rbnLower_poinCons.name = partElem + types + position[2] + side + '_pointCons'

# AimCons for make it look at
upper_aimCons = core.aimConstraint(  lowerLocate_loc , topAimed_grp ,  mo = True , worldUpObject = topUpObj_loc.name)
upper_aimCons.attr('worldUpType').value = 1
upper_aimCons.name = partElem + types + position[0] + side + '_aimCons'

lower_aimCons = core.aimConstraint(  topLocate_loc , lowerAimed_grp ,  mo = True , worldUpObject = lowerUpObj_loc.name)
lower_aimCons.attr('worldUpType').value = 1
lower_aimCons.name = partElem + types + position[2] + side + '_aimCons'

middleRbn_poinCons = core.pointConstraint( jointTop , jointBtm , ribbonMidLocate_loc,mo = True)
middleRbn_poinCons.name = partElem + types + position[1] + side + '_pointCons'

middleRbn_poinCons.attr( '%s'%jointTop + 'W0'  ).value = 0.5
middleRbn_poinCons.attr( '%s'%jointBtm + 'W1'  ).value = 0.5

aimUpZro_grp.parent( ribbonMidLocate_loc )

# Parent  Parent
flc_grp.parent( noTouch_grp )

# Spicific name Need to be fix later
detail_grp.parent( ctrl_grp )
nrb_grp.parent(noTouch_grp)

# snap grp
rbnCtrl_grp.maSnap( jointTop )
topLocate_loc.parent( rbnCtrl_grp )
lowerLocate_loc.parent( rbnCtrl_grp )
ribbonMidLocate_loc.parent( rbnCtrl_grp )


rbnCtrl_grp.parent( ctrl_grp )
rbnCtrl_parCons = core.parentConstraint( jointTop , rbnCtrl_grp , mo = True )
rbnCtrl_parCons.name = partElem + types + 'Ctrl' + side + '_parCons'

# Connect Upper Attr
ribbonMid_ctrl.attr('Upper_Twist') >> topPart_rbnJnt.attr('rotateY')
# Connection Detail to visibility
ribbonMid_ctrl.attr('Detail') >> detail_grp.attr('visibility')

# Connect Lower twsit
addTwistVal = core.AddDoubleLinear( partElem + 'Twist' + side + '_adl' )
ribbonMid_ctrl.attr('Lower_Twist') >> addTwistVal.attr('input1')
addTwistVal.attr('output') >> btmPart_rbnJnt.attr('rotateY')


# Create condition
condTwistVal = core.Condition( partElem + 'Twist' + side + '_cond' )
ribbonMid_ctrl.attr('Auto_Twist') >> condTwistVal.attr('firstTerm')
condTwistVal.attr('secondTerm').value = 1
condTwistVal.attr('colorIfFalseR').value = 0
btmPart.attr('rotateY') >> condTwistVal.attr('colorIfTrueR')
condTwistVal.attr('outColorR') >> addTwistVal.attr('input2')





print proxyJntList

bindJntList = []
for each in  proxyJntList :
    rawNam = misc.splitName(each)[0]
    bind_jnt = mc.joint( name = rawNam + '_bJnt')
    mc.select(deselect = True)
    misc.snapParentConstr( each ,  bind_jnt , mo = False)
    bindJntList.append(bind_jnt)
    print rawNam



for each in range( len(bindJntList) ):
    if each == 1:
        mc.parent( bindJntList[1] , bindJntList[0])          
    if each > 1:
        mc.parent( bindJntList[each] , bindJntList[each-1])
        
    
               
mc.parent( bindJntList[0] , jointTop )
mc.select(deselect = True)  
    

    
    