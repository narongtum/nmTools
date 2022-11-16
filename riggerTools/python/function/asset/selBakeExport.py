import maya.cmds as mc
import maya.mel as mel

from function.pipeline import fileTools as fileTools 
reload(fileTools)

from function.asset import exportFBX 
reload(exportFBX)

# export or bake before submit tools
def keySelObj( name = '*bJnt' ):
	bJntSet = mc.ls( name )
	#attrs = ('tx','ty','tz','rx','ry','rz')
	for bJnt in bJntSet:
		mc.bakeResults( bJnt, simulation = True, t= (0,1), at=["tx","ty","tz","rx","ry","rz"] )

def unparentSel():
	if len(mc.ls(sl=True)) > 0: # lens if something in select print TRUE
		print 'selected'
		sel = mc.ls(sl=True)
		for obj in sel:
			print obj
			try:
				mc.parent( obj ,world = True)
			except Exception as error:
				print error
				pass

		return sel

def deleteGrpRigGrp( ):
	# in case already delete rig_grp
	if mc.objExists('rig_grp'):
		mc.delete( 'rig_grp' )
		print 'Deleting rig_grp...'

def deleteObjType( objType = 'animCurve' ):
	animCurves = mc.ls(type= objType )
	for key in animCurves:
		print key
		mc.delete( key )
		print '_____been Delete____'

def cleanConstraints():

	print 'I will clean scene Cons'
	forDelList = []

	try:
		cons = mc.ls( '*Cons' )
		forDelList.append( cons )
		for each in forDelList:
			mc.delete( each )
	except Exception as error:
		print error
		pass

def exportModule( sel = '', rootJnt = 'root' ): # borrow from Noman <<<
	# brake sel to each
	for polySelected in sel:

		mc.select( polySelected, replace = True )    
		mc.select( rootJnt , add = True )   
			
		# Export obj	
		exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '

		# Get file name
		fileName = polySelected
		# fileName = fileTools.getAssetData()[-1][0]

		# Get path
		path =fileTools.findCurrentPath()
		path = path.replace('\\','/')
		path = path.replace('rig','fbx')

		exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
		exportCommand += exportFBXPath
		
		# Exec
		mel.eval( exportCommand )
		print '>>> %s has been export.'%polySelected
		print '>>> at PATH :  %s ' %exportFBXPath
		
		# Deselect
		mc.select(deselect = True)

	fileTools.openContainerFile( path = path )
	print '# # # Export Complete # # #'



def namingFilter():
	dag = mc.ls( dag = True )
	if 'root' in dag:
		rootJnt = 'root'
		suffix = '*_bJnt'

	elif 'Root' in dag:
		rootJnt = 'Root'
		suffix = '*_bind_jnt'
	else:
		print '>>>  no Root or root here  <<<'

	return rootJnt, suffix

 	

def toFBXFolder():
	rootJnt, suffix = namingFilter()

	sel = unparentSel()
	keySelObj( suffix )
	deleteGrpRigGrp()
	deleteObjType( 'animCurve' )
	cleanConstraints()
	exportModule( sel,  rootJnt )

def toHereFolder():
	rootJnt, suffix = namingFilter()
	exportFBX.noCareExporter( suffix = suffix , rootJnt = rootJnt )