from function.rigging.tools import dTool as dc
reload(dc)
from function.rigging.tools import proc as pc 
reload(pc)
from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)
# Prop RIG

def propRig( jnt = '' ): # will duplicate 'ctrl' in scene
	name = jnt.split('_')[0]
	grp = name + 'Zro' + '_grp'
	#off = name + 'Offset' + '_grp'
	ctrl = name + '_ctrl'
	ctrlShape = ctrl + 'Shape'
	gmblCtrl = name + 'Gmbl' + '_ctrl'
	# create
	mc.duplicate( 'ctrl', name = ctrl )
	#mc.group( name = off, em=True)
	mc.group( name = grp, em=True )
	
	# gimbal
	shapes = wcd.getShape( ctrlShape )
	data = wcd.modifiyCtrlShape( shapes , axis = [0.75, 0.75, 0.75] )
	gmblCtrl = mc.curve( name = gmblCtrl, p = data[0]["points"], k = data[0]["knots"], d = data[0]["degree"], per = bool(data[0]["form"]) )
	dc.ctrlColor( gmblCtrl, 'white' )

	# hide Vis for gimbal
	ctrlShp = mc.listRelatives( ctrl, shapes = True)
	gmblShp = mc.listRelatives( gmblCtrl, shapes = True)
	mc.addAttr ( ctrlShp[0], sn = 'gmb' ,ln = 'Gimbal', min = 0, max = 1, dv = 0, k = True)
	mc.connectAttr ( ctrlShp[0] + '.Gimbal',gmblShp[0] + '.visibility' )

	# lock and hide attr
	mc.setAttr( ctrl + '.v' , keyable = 0, lock = 1)
	mc.setAttr( gmblCtrl + '.v', keyable = 0, lock = 1)

	# adjust
	mc.parent( gmblCtrl, ctrl)
	mc.parent( ctrl, grp )
	#mc.parent( off, grp )
	dc.allMat( grp, jnt )


	dc.parCon( ctrl, jnt, mo=1 )
#else:
#	print ">>>>>   create ctrl in scene first  <<<<<"


propRig( jnt = 'propLFT_bJnt' )
propRig( jnt = 'propRGT_bJnt' )
