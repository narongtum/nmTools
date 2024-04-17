'''
Path				: 
Title				: adjust all about controller 
Description			: do all about controller
Author				: narongtum
Date				: 19 aug 2018
Notes				: strange controller is fine base ctrl like 'circle' is maya error

createController()
createZroGrp()
createGimbal()

from function.rigging.controllerBox import adjustController as adjust
reload(adjust)


'''
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.constraint import matrixConstraint as mtc
reload(mtc)



try:
	reload  # Python 2.7
	print('This might be python 2.7')
except NameError:
	try:
		from importlib import reload  # Python 3.4+
		print('Python 3.4+')
	except ImportError:
		from imp import reload  # Python 3.0 - 3.3
		print('Python 3.0 - 3.3')


from function.enviroment import enviromentPath as env
reload(env)

# define ctrl LIBRARY path
# SHAPE_LIBRARY_PATH = 'D:\\sysTools\\nmTools\\riggerTools\\python\\function\\rigging\\ctrlSizeLibrary\\'


SHAPE_LIBRARY_PATH = env.SHAPE_LIBRARY_PATH


import maya.cmds as mc
# from function.rigging import aimCon as ac
# reload(ac)

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)

from function.rigging.util import misc 
reload(misc)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)



# =================================
# - Create Controller fix for use both as assign parameter and selected
# =================================

#... outdate using fkRig instead
def creControllerFunc( 		selected = [], scale = 1, ctrlShape = 'circle_ctrlShape', color = 'yellow', 
							constraint = True, matrixConst = False, mo = False, translate=True, 
							rotate = True, scaleConstraint = True, rotateOrder = 'xzy', parentUnder = False):
	'''
	Create Controller at selected object.
	@param scale: A dictionary of template component and items.
	@type template: dict
	'''
	print (scaleConstraint)
	rawName = ''
	rawNamLst = []
	storeNamLst = []
	# list selection
	# selected = mc.ls(sl = True)

	return_list = []

	if selected:
		if selected[0].split('_')[0] == 'L' or selected[0].split('_')[0] == 'R':
			if selected[0].count('_') == 1:
				for each in selected:
					rawName = each
					
					storeNamLst.append( rawName )
					rawNamLst.append( each )

			elif selected[0].count('_') > 1:
				# mc.error('selected[0]')
				for each in selected:
					parts = each.split('_')
					rawName = '_'.join(parts[:-1])
					storeNamLst.append( rawName )
					rawNamLst.append( each )

					print('I am here\n\n{}\n\n\n'.format(rawName))



		#... If having one underscore 'something_ctrl'
		elif selected[0].count('_') == 1:
			for each in selected:
				rawName = each.split('_')[0]
				# name with first index
				storeNamLst.append( rawName )
				# full name
				rawNamLst.append( each )
		elif selected[0].count('_') == 0:
			for each in selected:
				rawName = each
				storeNamLst.append( rawName )
				rawNamLst.append( each )

		#... for naming that use underscore more than one
		elif selected[0].count('_') > 2: 
			for each in selected:
				# each_split = each.split('_')
				# rawName = each_split[0] + each_split[1]
				parts = each.split('_')
				rawName = '_'.join(parts[:-1])

				storeNamLst.append( rawName )
				rawNamLst.append( each )

		# elif selected[0].count('_') > 2:
		# 	for each in selected:
		# 		storeNamLst.append( each ) 
		# 		rawNamLst.append( each )



		for i in range(len(storeNamLst)):

				
				#name = str( storeNamLst[i] )

				# Create  controller
				child_ctrl = core.Dag( storeNamLst[i] + '_ctrl' )
				child_ctrl.nmCreateController(ctrlShape)
				child_ctrl.editCtrlShape( axis = scale * 1.2 )
				child_ctrl.color = color
				child_ctrl.rotateOrder = rotateOrder
				child_ctrl.hideArnoldNode()

				print ('create gimbal controller/n')
				print (child_ctrl.name)
				gimbal_ctrl = core.createGimbal( child_ctrl )
				gimbal_ctrl.hideArnoldNode()

				# Create zero group
				# mc.error(child_ctrl.name)
				childZro_grp = rigTools.zroGrpWithOffset( child_ctrl )


				childZro_grp.matchPosition( rawNamLst[i] )
				childZro_grp.matchRotation( rawNamLst[i] )

				return_list.append(childZro_grp.name)
				return_list.append(child_ctrl.name)
				return_list.append(gimbal_ctrl.name)
				
				#... set RotationOrder
				child_ctrl.rotateOrder = rotateOrder 
				gimbal_ctrl.rotateOrder = rotateOrder
				
				if constraint == True:
					if matrixConst == False:
						# Making joint parent of controller
						joint_parCons = core.parentConstraint( gimbal_ctrl , rawNamLst[i] )
						joint_parCons.name = storeNamLst[i] + '_parCons'

						joint_ScalCons = core.scaleConstraint( gimbal_ctrl , rawNamLst[i] )
						joint_ScalCons.name = storeNamLst[i] + '_scalCons'
					else:
						print ('type(rawNamLst[i])type(rawNamLst[i])type(rawNamLst[i])type(rawNamLst[i])type(rawNamLst[i])type(rawNamLst[i])')
						print (type(rawNamLst[i]))

						print(gimbal_ctrl)
						print(rawNamLst[i])


						mtc.parentConMatrix( gimbal_ctrl, rawNamLst[i], mo = mo, translate = translate, rotate = rotate, scale = scaleConstraint)
						# misc.parentMatrix( gimbal_ctrl, rawNamLst[i] , mo = mo, translate = translate, rotate = rotate, scaleCon = scaleConstraint)

				else:
					continue

		if parentUnder:
			print('\nParent {0} to {1}\n'.format(childZro_grp.name, selected[i]))

			mc.parent(childZro_grp.name, selected[i])




		return return_list
	else:
		mc.warning('Please select something.')




# create controllder at selected
def createController():
	
	jntName = mc.ls(sl=True)[0]
	normalName = jntName.split('_')[0]
	ctrlName = jntName.split('_')[0] + '_ctrl'
	gmblName = jntName.split('_')[0] + 'Gmbl_ctrl'
	zroGrpName = jntName.split('_')[0] + 'Zro_grp'
	offsetGrpName = jntName.split('_')[0] + 'Offset_grp'

	ctrl = mc.circle( ch = 0, name = ctrlName, radius = 2 )[ 0 ]
	gmbl = mc.circle( ch = 0, name = gmblName, radius = 1.75 )[ 0 ]

	# catch shapeNode
	ctrlShape = mc.listRelatives( ctrl , s = True )[ 0 ]
	gmblShape = mc.listRelatives( gmbl , s = True )[ 0 ]

	mCls = mc.cluster( ctrlShape )[1]
	cls = mc.cluster( gmblShape )[1]

	print (cls)
	# rotate 90 make them flatten
	mc.setAttr( mCls + '.rx', -90 )
	mc.setAttr( cls + '.rx', -90 )


	# delete history
	mc.delete( ctrlShape, ch = True )
	mc.delete( gmblShape, ch = True )


	mc.parent( gmbl , ctrlName )
	ofsGrp = mc.group( ctrl , name = offsetGrpName)
	zGrp = mc.group( ofsGrp , name = zroGrpName)

	misc.snapParentCon( jntName, zGrp )


	mc.addAttr( ctrlName , ln = 'gmbl' , min = 0 , max = 1 , dv = 1 , k = True )
	mc.connectAttr( '%s.gmbl' % ctrlName , '%s.v' % gmblShape )


	attrs = ( 'tx' , 'ty' , 'tz' , 'sx' , 'sy' , 'sz' , 'v' )
	for attr in attrs :
		mc.setAttr( '%s.%s' % ( gmbl , attr ) , l = True , k = False )
		
	mc.parentConstraint ( gmblName, jntName , maintainOffset = True, name = gmblName + 'parCon')

	mc.setAttr( '%s_ctrl.gmbl' %normalName,0 )








def createZroGrpWithFlexName(selected):

	selected = mc.ls( sl = True )

	for each in selected:

		rawName = misc.check_name_style(name = each)

		zroGrpName = rawName[0] + 'Zro_grp'
		offsetGrpName = rawName[0] + 'Offset_grp'

		print (zroGrpName)
		print (offsetGrpName)

		mc.group(empty = True, name = zroGrpName)
		mc.group(empty = True, name = offsetGrpName)

		misc.snapParentCon( each, zroGrpName )
		misc.snapParentCon( each, offsetGrpName )

		mc.parent( each , offsetGrpName )
		mc.parent( offsetGrpName , zroGrpName )



# create zero group
def createZroGrp(offset = False):

	if offset == False:

		jntName = mc.ls( sl = True )

		for each in jntName:

			zroGrpName = each.split('_')[0] + 'Zro_grp'

			print (zroGrpName)

			mc.group(empty = True, name = zroGrpName)

			misc.snapParentCon(each,zroGrpName)

			mc.parent( each , zroGrpName )

			return zroGrpName


	elif offset == True:

		jntName = mc.ls( sl = True )

		for each in jntName:

			zroGrpName = each.split('_')[0] + 'Zro_grp'
			offsetGrpName = each.split('_')[0] + 'Offset_grp'

			print (zroGrpName)

			mc.group(empty = True, name = zroGrpName)
			mc.group(empty = True, name = offsetGrpName)

			misc.snapParentCon( each, zroGrpName )
			misc.snapParentCon( each, offsetGrpName )

			mc.parent( each , offsetGrpName )
			mc.parent( offsetGrpName , zroGrpName )

			return zroGrpName, offsetGrpName
	else:
		mc.warning('Please select something.')






# create gimbal Controller
# list name
def createGimbal():

	ctrlName = mc.ls(sl=True)[0]

	ctrlShape = mc.listRelatives( ctrlName , shapes = True )[ 0 ]

	if mc.nodeType(ctrlShape) == 'nurbsCurve':

		print ('This is might be Controller')
	
		shapes = wcd.getShape(ctrlShape)

		# change ctrl data 75 percent smaller
		data = wcd.modifiyCtrlShape( shapes,axis=[0.75, 0.75, 0.75])

		print (data[0])

		# create new controller
		gmblCtrl = mc.curve(ctrlName, p = data[0]["points"], k=data[0]["knots"], d=data[0]["degree"], per=bool(data[0]["form"]))

		# case if 
		#gmblCtrl = mc.curve(ctrlName, p = data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]))

		# add gimbal attr
		#mc.addAttr( ctrlName , ln = 'gimbal' , min = 0 , max = 1 , dv = 1 , k = True )
		mc.addAttr( ctrlShape , ln = 'gimbal' , min = 0 , max = 1 , dv = 1 , k = True )

		gmblShape = mc.listRelatives( gmblCtrl , s = True )[ 0 ]

		# set white color
		mc.setAttr( '%s.overrideEnabled' % gmblShape , 1 )
		mc.setAttr( '%s.overrideColor' % gmblShape , 16 )

		# snap
		misc.snapParentCon( ctrlName, gmblCtrl )
		mc.parent( gmblCtrl , ctrlName )

		# connect attr
		print  ( '%s.gimbal' % ctrlName , '%s.v' %gmblCtrl )
		
		# mc.connectAttr( '%s.gmbl' % ctrlName , '%s.v' %gmblShape )
		# mc.setAttr( '%s.gmbl' % ctrlName , 0 )
		mc.connectAttr( '%s.gimbal' % ctrlShape , '%s.v' %gmblShape )
		mc.setAttr( '%s.gimbal' % ctrlShape , 0 )

		#split name
		spName = misc.splitName(ctrlName)

		# hide hideArnoldNode
		parent_ctrl = core.Dag( ctrlName )
		parent_ctrl.hideArnoldNode()
		
		# rename gmbl ctrl
		mc.rename( gmblCtrl, spName[0] + 'Gmbl' + '_ctrl' )

		mc.select( deselect = True )

		return spName[0] + 'Gmbl' + '_ctrl'

	else:
		mc.warning( "This is not Controller" )





def createController( shapeName ):
		data = wcd.loadData(path = SHAPE_LIBRARY_PATH + shapeName + '.json')
		curveName = mc.curve(  p=data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]))
		
		mc.setAttr( '%s.overrideEnabled'	% curveName , 1 )
		mc.setAttr( '%s.overrideColor' 		% curveName , data['colour'] )




def assignColor( color = '' , arg = None ) :
	
	colorDict = { 	'yellow'		: 17 	, 'red' 			: 13 ,
					'softBlue' 		: 18 	, 'blue' 			: 6 ,
					'white' 		: 16 	, 'brown'			: 11 ,
					'black' 		: 1 	, 'gray' 			: 2 ,
					'softGray'		: 3 	, 'darkRed' 		: 4 ,
					'darkBlue' 		: 5 	, 'darkGreen'		: 7 ,
					'green' 		: 14 	, 'none' 			: 0 	}
				
	colorID = colorDict[ color ]
	selected = mc.ls( sl=True )
	
	for each in selected :
		# find shape node
		shapes = mc.listRelatives( each , shapes = True )
		
		if shapes :
			
			for shape in shapes :
				
				if color == 'none' :
					# set the 'none' color for user click none
					mc.setAttr( '%s.overrideColor'	 	% shape , colorID )
					mc.setAttr( '%s.overrideEnabled' 	% shape , 0 )
				else :
					mc.setAttr( '%s.overrideEnabled'	% shape , 1 )
					mc.setAttr( '%s.overrideColor' 		% shape , colorID )


