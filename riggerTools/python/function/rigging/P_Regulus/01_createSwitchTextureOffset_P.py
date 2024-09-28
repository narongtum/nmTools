# PORTABLE - createSwtichTextureOffset -

# ctrl must not have "mouth" Attr, if already had it will cancel

# place2dTexture is node that on the left side of Mouth texture




import maya.cmds as mc

# create and link facial switch texture
def createSwtichTextureOffset( ctrl = 'facialSwitch_ctrl', place2dTexture = 'M_C001_Ashford_01_Mouth_PT', attrName = 'mouth', addEnumList = [ 'Default', 'Happy', 'Argh', 'Angry', 'Excited' ] ):

	#addEnumList = [ 'Default', 'Happy', 'Argh', 'Angry', 'Excited' ] # will be loop

	maxEnum = len( addEnumList )
	enum = ''

	if mc.objExists( '{0}.{1}'.format( ctrl, attrName ) ):
		print( 'Attribute Name - {0} - Already Exists'.format( attrName ) )
		return

	for each in addEnumList:

		if each == addEnumList[0]:
			enum = '{0}{1}'.format( enum, each )

		else:
			enum = '{0}:{1}'.format( enum, each )

	# print( enum )
	attr = addEnum( ctrl, attrName, enum )


	for i, eachEnum in enumerate( addEnumList ):

		# get calculate offsetValue
		#rawOffsetValue = 1 + ( ( i - maxEnum ) / maxEnum )
		rawOffsetValue = 1 + ( ( i - 8 ) / 8 )

		offsetValue = round( rawOffsetValue, 4 ) # round at 4 digit 

		# create condition in loop
		cnd = mc.createNode( 'condition', name = '{0}_{1}_cnd'.format( attrName, eachEnum ) )
		cnd = str(cnd)
		#print (cnd)

		connectTo( attr, cnd, 'firstTerm' )
		setAttr( cnd, 'secondTerm', i ) # 0 1 2 3 4
		setAttr( cnd, 'colorIfTrueR', offsetValue ) # setOffsetValue 0 0.2 0.4 0.6 0.8

		if i > 0:
			connect( last_cnd, 'outColorR', cnd, 'colorIfFalseR' )

		if i == ( maxEnum - 1 ): # last index
			connect( cnd, 'outColorR', place2dTexture, 'offsetU' ) # offset U for X along texture
			setAttr( place2dTexture, 'coverageU', 8 )

		# make prior cndExist
		last_cnd = cnd

	print( "Create Swtich Texture Offset - Misson Accomplish" )

	return



# etc code

def addEnum( ctrl = '', name = '', enum = '' ):
	mc.addAttr( ctrl, longName = name, at = 'enum', enumName = enum, k = True  )
	attrName = '{0}.{1}'.format( ctrl , name )
	return attrName
# addEnum( ctrl, 'follow', 'cog:hip' )


def connectTo( attrA = '', objB = '', attrB = '' ):
	# input attrA might be [ addFKIK, addBooAttr ] return
	if attrB == '':
		mc.connectAttr( attrA , '{0}'.format( objB ) )
	else:
		mc.connectAttr( attrA , '{0}.{1}'.format( objB, attrB ) )
	
def setAttr( obj = '', attr = '', val = '' ):
	mc.setAttr( '{0}.{1}'.format( obj, attr ) , val )

def connect( objA = '' , attrA = '', objB = '', attrB = '' ):
	mc.connectAttr( '{0}.{1}'.format( objA, attrA ) , '{0}.{1}'.format( objB, attrB ) )




# RUN #

# RUN #

# RUN #

# RUN #

createSwtichTextureOffset( ctrl = 'facialSwitch_ctrl', place2dTexture = 'NPC003_Conrad_01_Mouth_PT', attrName = 'mouth', addEnumList = [ 'Default', 'A', 'E', 'I', 'O', 'U','Sp1','Sp2' ] )




#... create Separater
from function.rigging.autoRig.base import core
reload(core)


face_ctrl = core.Dag('facialSwitch_ctrl')
# face_ctrl.addAttribute( at = 'enum', keyable = True , en = 'FACIAL', longName = '-------' )
face_ctrl.addAttribute( longName = 'ctrlVis', at = 'enum', keyable = True, enumName = 'CTRL_VIS', niceName = '-------' )


'''
'addAttr -ln "FACIAL" -nn "-------" -at "enum" -en "FACIAL:"  |rig_grp|master_ctrl|placement_ctrl|ctrl_grp|headRig_grp|head01Zro_grp|head01_ctrl|head01_gmbCtrl|facialRig_grp|facialSwitchZro_grp|facialSwitch_ctrl;'
createSwtichTextureOffset( ctrl = 'facialSwitch_ctrl', place2dTexture = 'CH006_Dantalia_01_Mouth_place2dTexture', attrName = 'mouth', addEnumList = [ 'Default', 'A', 'E', 'I', 'O' , 'U', 'Sp1', 'Sp2'] )
'''