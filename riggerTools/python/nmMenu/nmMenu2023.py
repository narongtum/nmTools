# coding: utf-8
'''
// date : 06.May.2022
//----------------------------------------------------------------------------
// noman Menu - Python Script - version 0.4
//----------------------------------------------------------------------------
//
// DESCRIPTION:
//
// REQUIRES:	to install this menu copy to
//	D:\\sysTools\\nmTools\\riggerTools\\maya
// 	to C:\\Users\\<user>\\Documents\\maya
//
//
//
//----------------------------------------------------------------------------
'''



# Reload module

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
		
# Import library
import pymel.core as pm
import maya.cmds as mc
import maya.OpenMaya as om
import maya.mel as mel
import sys
import importlib
import os.path



PROJECT_PATH = "D:/sysTools/nmTools_github/riggerTools"
abs_path = os.path.normpath(PROJECT_PATH)

# naming
PROJECT_NAME = 'nmMenu_g'

# append path

ICON_PATH = os.path.normpath(PROJECT_PATH + r'\\image')


# add path
PLUGINS_PATH = os.path.normpath(PROJECT_PATH + r"\\python\\function\\plugin\\2023")


# animlibrary

ANIMLIB_PATH = os.path.normpath(PROJECT_PATH + r'\\python\\function\\animation\\studiolibrary2023\\src')
if not os.path.exists(ANIMLIB_PATH):
	raise IOError(r'The source path {0} does not exist!'.format(ANIMLIB_PATH))
if ANIMLIB_PATH not in sys.path:
	sys.path.insert(0, ANIMLIB_PATH)



#... load plugins
# mc.loadPlugin( PLUGINS_PATH + "\\AnimSchoolPicker.mll", quiet = True)

def reloadMenu():
	if pm.menu( 'MayaWindow|%s' %PROJECT_NAME , exists = True):
		mc.deleteUI('MayaWindow|%s' %PROJECT_NAME )


#... Add DreamWallPicker
DW_PATH = PROJECT_PATH + r'/python/function/animation/dwpicker-1.0.2-2025.02.11'

def launch_dwpicker(*args):
	if DW_PATH not in sys.path:
		sys.path.insert(0, DW_PATH)
	import dwpicker
	dwpicker.show()

#... runmenu
def runMenu():
	try:
		# Delete exists menu
		if pm.menu( 'MayaWindow|%s' %PROJECT_NAME , exists = True):
			mc.deleteUI('MayaWindow|%s' %PROJECT_NAME )


		# Name of the global variable for the Maya window
		MainMayaWindow = pm.language.melGlobals['gMainWindow']

		# Build a menu and parent under to that Maya Window
		TAI = pm.menu( PROJECT_NAME, to = True, parent = MainMayaWindow )

	except Exception as e:
		print("Error:", e)



	'''

	MENU Body Part

	'''



	'''

	 File Manager

	'''
	mc.menuItem( label = "File Manager",	command = "from function.pipeline.file_manager import run_ui\nreload(run_ui)\nrun_ui.run_file_manager()", ann = "Open File Manager(test)" )

	#-----------------------------
	mc.menuItem(divider = True)




	'''

	 Asset Tools

	'''
	#----------------------------------------------------------------------------------------------------------------------
	mc.menuItem( label = 'Asset' , subMenu = True, tearOff = True)


	mc.menuItem( label = 'Publish file', divider = True )

	#----------------------------------------------------------------------------------------------------------------------
	

	# mc.menuItem( label = "Commit To SVN",	command = "from function.pipeline import svnMaya\nimportlib.reload(svnMaya)\nsvnMaya.commitCurrentPath()", ann = "Commit current file to SVN.(Make sure this file already add.)" , image = ICON_PATH + '\\svn-commit-small.png')	

	# mc.menuItem( label = "Local Publish",	command = "from function.pipeline import fileTools\nimportlib.reload(fileTools)\nfileTools.localPublish()", ann = "Clean file and commit to local department.", image = ICON_PATH + '\\localPublish.png')

	# mc.menuItem( label = "Global Publish",	command = "from function.pipeline import fileTools\nimportlib.reload(fileTools)\nfileTools.globalPublish()", ann = "Clean file and commit to Global Library.", image = ICON_PATH + '\\worldIcon.png')

	#mc.menuItem( label = 'Exporting Tools', divider = True )

	# mc.menuItem( label = "Export with Path", command = "from function.asset import exportPathTool as exportPathTool\nimportlib.reload(exportPathTool)\nrun = exportPathTool.Ui()\nrun.createGUI()" , ann = "export To Path From Selected Object" )
	
	# mc.menuItem( label = "Export FBX file to current folder.",	command = "from function.asset import exportFBX\nimportlib.reload(exportFBX)\nexportFBX.noCareExporter()", ann = "Automate export FBX file to curren maya folder.( select mesh and run )")

	#-----------------------------


	mc.menuItem( label = "Create Thumbnails",	command = "from function.pipeline import fileTools as fileTools\nimportlib.reload(fileTools)\nfileTools.createThumbnail()", ann = "Create Thumbnails at current location.")

	mc.menuItem( label = "Remove selected reference",	command = "from function.rigging.util import misc as misc\nimportlib.reload(misc)\nmisc.removeSelectedReference()", ann = "Remove Selected Reference")

	mc.menuItem( label = "Import And Remove Namespace",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfileTools.impRem()", ann = "Import and remove namespace")

	mc.menuItem( label = "Sort Selected Outliner",	command = "from function.asset import misc\nreload(misc)\nmisc.sortOutliner()", ann = "Sort Selected Outliner")

	mc.menuItem( label = "Replace Texture",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfileTools.replaceTex()", ann = "Replace All Texture in scene.")

	mc.menuItem( label = "Print Texture Path",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfileTools.printTexturePath()", ann = "Print All Texture in scene.")
	
	mc.menuItem( label = "Open Containing Folder",	command = "from function.pipeline import fileTools\nimportlib.reload(fileTools)\nfolder = fileTools.currentBackFolder()\nfileTools.openContainerFile(path = folder)", ann = "Open Containing Folder.")

	mc.menuItem( label = "Export Selection",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfileTools.exportSel()", ann = "Export selected to Maya file.")





	#-----------------------------
	mc.menuItem( label = 'Naming', divider = True )

	# use cometJointOrient
	FUNCTION_PATH = "/mel/cometTools/cometRename.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem(label="cometRename", command = "mel.eval('cometRename()')",ann = "comet Rename" )

	mc.menuItem( label = "Renamer",	command = "from function.framework.Qtpy.Qt import QtCore, QtGui, QtWidgets\nfrom function.asset.renamer import nomanRenamer_ui\nimportlib.reload(nomanRenamer_ui)\nForm = QtWidgets.QWidget()\nui = nomanRenamer_ui.Ui_ReNameUi()\nui.setupUi(Form)\nForm.show()", ann = "Renamer")

	mc.menuItem( label = "Auto add suffix",	command = "from function.rigging.util import misc as msc\nimportlib.reload(msc)\nmsc.selAutoSuffix()", ann = "Select and click.")

	mc.menuItem( label = "Transfer Selected Shading.",	command = "from function.pipeline import fileTools as ast\nimportlib.reload(ast)\nast.transferShade()", ann = "Select Parent then Child.")
	mc.setParent( '..', menu = True )
	#----------------------------------------------------------------------------------------------------------------------


	# '''

	#  Modeling Tools

	# '''
	# #----------------------------------------------------------------------------------------------------------------------
	# mc.menuItem( label = 'Modeling' ,subMenu = True, tearOff = True)

	# # Export Asset
	# #mc.menuItem( label="xExport Asset", ann = "Export Asset.." )

	# mc.menuItem( label = "Create Shader", command = "from function.rigging.tools import createShdFromSel as shdFromSel\nimportlib.reload(shdFromSel)\nrun = shdFromSel.Ui()\nrun.createGUI()" , ann = "Create Shader From Selected Object" )

	# mc.menuItem( label = "Connect BSH :select model", command = "from function.modelling import InvictusBSH as INVBSH\nimportlib.reload(INVBSH)\nINVBSH.connectExpression()" , ann = "Connect Blendshape From Selected Helmet" )
	
	# mc.menuItem( label = "Connect BSH :select BSH", command = "from function.modelling import InvictusBSH as INVBSH\nimportlib.reload(INVBSH)\nINVBSH.connectBshToCtrl()" , ann = "Connect Blendshape From Selected blendshapes" )

	# mc.setParent( '..', menu = True )
	# #----------------------------------------------------------------------------------------------------------------------




	'''

	 Animation Tools

	'''
	#----------------------------------------------------------------------------------------------------------------------
	# Animation Main Menu
	mc.menuItem( label = 'Animation' , subMenu = True , tearOff = True)
	# Animation sub menu

	# Studio Library
	mc.menuItem( label = "Studio Library", 			command = "import studiolibrary\nstudiolibrary.main()" , ann = "Run animation Library" )

	# AnimSchoolPicker
	# mc.menuItem( label = "AnimSchool Picker", 		command = "mel.eval('AnimSchoolPicker()')" , ann = "Run AnimSchool Picker" )

	#... DreamWall Picker
	mc.menuItem(label = "DreamWall Picker", 		command = launch_dwpicker, ann="Launch DreamWall Picker")

	# onionSkinRenderer
	mc.menuItem( label = "OnionSkinRenderer", 		command = "from function.animation.onionSkinRenderer import onionSkinRendererWindow as onionWindow\nimportlib.reload(onionWindow)\nonionWindow.openOnionSkinRenderer()" , ann = "onionSkinRenderer" )

	# ZvParentMaster
	mc.menuItem( label = " ZvParentMaster", 		command = "from function.animation import ZvParentMaster\nimportlib.reload(ZvParentMaster)\nZvParentMaster.ZvParentMaster()" , ann = "animation tool that helps you to animate objects in mutual contact or interaction with ease." )
	
	# ZvParentMaster Mod Ui
	mc.menuItem( label = " ZvParentMaster Ui", 		command = "from function.animation import zvParentMaster_tools_ui_mod as zv\nreload(zv)\nzv.createGUI()" , ann = "animation tool that helps you to animate objects in mutual contact or interaction with ease." )

	# tweener
	mc.menuItem( label = "Tweener", 	command = "from function.animation import tweenerUI\nimportlib.reload (tweenerUI)\ntweenerUI.TweenWindow().show()" , ann = "adjust the slider and see the results immediately" )



	'''# ackDeleteRedundant
				mel.eval('source "D:/sysTools/nmTools/riggerTools/mel/ackDeleteRedundant.mel"')
				mc.menuItem(label = "ackDeleteRedundant", 		command = "mel.eval('ackDeleteRedundant')", ann = "Deletes keys that have the same value as it's two" )'''

	mc.menuItem(divider = True)
	#------------------------------------------------------------------------------------------------

	# Playblast tool
	mc.menuItem( label = "Playblast Tool", 			command = "from function.pipeline.playBlast import playblastTool\nimportlib.reload(playblastTool)\nrun=playblastTool.Ui()\nrun.createGUI()" , ann = "Playblast tools" )

	mc.menuItem(divider = True)
	
	#------------------------------------------------------------------------------------------------

	mc.menuItem( label = "Export Animation", 		command = "from function.asset import genericAnimExporter as gae\nimportlib.reload(gae)\nrun = gae.Ui()\nrun.createGUI()" , ann = "Bake Animation Export"  )

	mc.menuItem(divider = True)

	#------------------------------------------------------------------------------------------------
	
	mc.menuItem( label = "SNAP IK/FK v4", 			command = "from function.animation import snapFKIKv4\nimportlib.reload(snapFKIKv4)\nsnapFKIKv4.ikfkSnap()" , ann = "2020 SNAP IK/FK for 2020+ autoRig" )

	# mc.menuItem( label = "BakeMocap 90", 			command = "from function.animation import bakeFromMocap90 as bfnine\nimportlib.reload(bfnine)\nrun=bfnine.Main()\nrun.bakeGUI()" , ann = "Bake Mocap Animation footage that flip 90 degree."  )


	mc.menuItem(divider = True)
	#------------------------------------------------
	mc.menuItem( label = "Reset all controller",	command = "from function.rigging import RESET as re\nimportlib.reload(re)\nre.resetAllController(reference = True)" , ann = "Reset Character Pose ( reference only )"   )

	mc.menuItem( label = "Reset controller (nonRef)",	command = "from function.rigging import RESET as re\nimportlib.reload(re)\nre.resetAllController(reference = False)" , ann = "Reset Character Pose ( for rigger )"   )
	
	mc.menuItem( label = "Select all controller", 	command = "from function.animation import animTools\nimportlib.reload(animTools)\nanimTools.selectAllCtrl()" , ann = "Select all controller"    )

	mc.menuItem( label = "mirror controller", 		command = "from function.animation import mirrorSelCtrl\nimportlib.reload(mirrorSelCtrl)\nmirrorSelCtrl.mirror_selCtrl()", ann = "Select LFT ctrl and auto copy to other side and vice versa"	)

	mc.setParent( '..', menu=True )
	#----------------------------------------------------------------------------------------------------------------------





	'''

	 Rigging tools

	'''
	#----------------------------------------------------------------------------------------------------------------------
	# Rigging Main Menu

	mc.menuItem( label = 'Rigging' ,subMenu = True, tearOff = True)

	# Rigging Sub menu
	# = = > Snap Submenu
	mc.menuItem( label = "Snap" , ann = "Snap selected.",subMenu = True , tearOff = True)

	mc.menuItem( label = "Snap All Transforms", 	command = "from function.rigging.util import misc\nimportlib.reload(misc)\nmisc.parentCon()" , ann = "Snaping All Transforms selected, Select parent and child." )

	mc.menuItem( label = "Snap Position", 		command = "from function.rigging.util import misc\nimportlib.reload(misc)\nmisc.pointCon()" , ann = "Snaping Point selected, Select parent and child." )

	mc.menuItem( label = "Snap Rotation", 		command = "from function.rigging.util import misc\nimportlib.reload(misc)\nmisc.orientCon()" , ann = "Select parent and child." )

	mc.setParent( '..', menu=True )




	
	# = = > Skeleton Submenu
	#------------------------------------------------
	mc.menuItem( label = 'Skeleton' ,subMenu = True, tearOff = True)

	#... Create Joint at selected vertex
	mc.menuItem(label = "Create Joint at selected vertex", command = "from function.rigging.util import misc as misc\nimportlib.reload(misc)\nmisc.creJntAtVertex()" , ann = "Create Joint at selected vertex" )

	#... CometJointOrient
	
	FUNCTION_PATH = "/mel/cometTools/cometJointOrient.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem(label="cometJointOrient",	command = "mel.eval('cometJointOrient()')",ann = "Comet Set JointOrient" )

	#... Select Body Joint
	mc.menuItem(label = "Select Body Joint", command = "from function.rigging.skeleton import jointTools as jntTools\nimportlib.reload(jntTools)\njntTools.select_body_jnt()", ann = "Selected the body joint that exists in scene." )

	#... Create joint along curve
	mc.menuItem(label = "Create Joint Along Curve", command = "from function.rigging.skeleton import createJointAlongCurve as cjac\nimportlib.reload(cjac)\ncjac.run()" , ann = "Create Joint at selected vertex" )
	
	mc.setParent( '..', menu=True )









	# = = > Skin Submenu
	#------------------------------------------------
	mc.menuItem( label = "Skin", 				ann = "Snap selected.",subMenu = True , tearOff = True)


	#... Import weight(use Noah instead)
	mc.menuItem( label = "Load weight Default", command = "from function.rigging.skin import autoReadWriteSkin\nimportlib.reload(autoReadWriteSkin)\nautoReadWriteSkin.importWeightData()" , ann = "Select source and import." )
	mc.menuItem( label = "Load weight", command = "from function.framework.reloadWrapper import reloadWrapper as reload\nfrom function.rigging.skin.nsSkinClusterIO import nsSkinClusterIO_reFunc as skinIO\nreload(skinIO)\nskinIO.loadSkin()" , ann = "Select source and import By Noah Schnapp." )

	# Export weight
	mc.menuItem( label = "Save weight Default", command = "from function.rigging.skin import autoReadWriteSkin\nimportlib.reload(autoReadWriteSkin)\nautoReadWriteSkin.exportWeightData()" , ann = "Select source and export.", image = ICON_PATH + '\\bullet_interactivePlayback.png' )
	mc.menuItem( label = "Save weight", command = "from function.framework.reloadWrapper import reloadWrapper as reload\nfrom function.rigging.skin.nsSkinClusterIO import nsSkinClusterIO_reFunc as skinIO\nreload(skinIO)\nskinIO.saveSkin()" , ann = "Select source and export By Noah Schnapp.", image = ICON_PATH + '\\bullet_interactivePlayback.png' )
		
	# Browse weight
	mc.menuItem( label = "Browse weight", command = "from function.rigging.skin import autoReadWriteSkin\nimportlib.reload(autoReadWriteSkin)\nautoReadWriteSkin.browseWeight()" , ann = "Browse source and import skin." )

	# Browse weight
	mc.menuItem( label = "Export mesh general data", command = "from function.rigging.skin import exportImportMeshGeneralData as IMG\nimportlib.reload(IMG)\nIMG.run()" , ann = "Browse source and import skin general data." )

	#... not work in 2023
	# Chad vernon skin weight import / export
	# mc.menuItem( label = "Skin Import / Export", command = "from function.rigging.skin import skinio2023\nimportlib.reload(skinio2023)\nskinio2023.show()" , ann = "Just another skinweight Import/Export thank to chad vernon." )

	mc.menuItem(divider = True)
	#------------------------------------------------

	# skinWrangler
	mc.menuItem( label = "SkinWrangler", command = "from function.rigging.skin.skinWrangler import skinWrangler_2023 as sw\nimportlib.reload(sw)\nskinWranglerWindow = sw.show()" , ann = "By Christopher Evans, https://github.com/chrisevans3d/skinWrangler" )
	#... copy paste weight
	mc.menuItem( label = "Copy Paste Weight", command = "from function.rigging.skin import copyPasteSkinUI as cpu\nreload(cpu)\nui = cpu.BuildUI()\nui.show()", ann = "Copy and Paste Weight." )
	#... Round skin weight
	mc.menuItem( label = "Round Skin Weight", command = "from function.framework.reloadWrapper import reloadWrapper as reload\nfrom function.rigging.skin import roundSkinWeight as rsw\nreload(rsw)\nselected = mc.ls(sl=True)\nrsw.roundSkinWeight(digit=3, selection=selected)" , ann = "Convert from MEL" )

	mc.menuItem(divider = True)
	#------------------------------------------------

	# dora weight
	FUNCTION_PATH = "/mel/DoraSkinWeightImpExp.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem( label = "DoraWeight", 	command = "mel.eval('DoraSkinWeightImpExp()')", ann = "Read and Write skin weight" )

	mc.menuItem( label = "Copyweight", 	command = "from function.rigging.skin import copySkinWeight as ckw\nimportlib.reload(ckw)\nckw.copyWeight()" , ann = "Select source and destination and copyWeight." )

	mc.menuItem( label = "tf_smoothSkinWeight", command = "from function.rigging import tf_smoothSkinWeight\nimportlib.reload(tf_smoothSkinWeight)\ntf_smoothSkinWeight.paint()", ann = "select a skinned mesh and execute" )

	mc.menuItem( label = "Select bind joint", command = "from function.rigging.skin import skinUtil as skinUtil\nimportlib.reload(skinUtil)\nskinUtil.selectBindJnt()", ann = "select a bind joint" )

	mc.menuItem( label = "ml_copySkin", command = "from function.rigging.skin import ml_copySkin\nimportlib.reload(ml_copySkin)\nml_copySkin.ui()", ann = "Copy a skinCluster from one mesh to another, or to a selection of vertices." )

	mc.menuItem( label = "CopySkin from Ref", command = "from function.rigging.skin import copySkinFromRef as cpr\nimportlib.reload(cpr)\ncpr.runUi()", ann = "Likewise above but can use as Reference." )

	mc.menuItem(divider = True)
	#------------------------------------------------

	mc.menuItem( label = "Rename all skinCluster", command = "from function.rigging.skin import skinUtil as skinUtil\nimportlib.reload(skinUtil)\nskinUtil.renameSkinCluster()", ann = "rename all skinCluster" )


	mc.setParent( '..', menu=True )



	# = = > Controller Submenu
	#------------------------------------------------

	mc.menuItem( label = "Controller", ann = "Snap selected.", subMenu = True , tearOff = True)

	mc.menuItem( label = "Create Master Group", 	command = "from function.rigging.autoRig.bodyRig import rootRig\nimportlib.reload(rootRig)\nrootRig.createMasterGrp(charScale=1)" )

	mc.menuItem( label = "Create ZroGrp", 	command = "from function.rigging.controllerBox import adjustController as ccr\nimportlib.reload(ccr)\nselected = mc.ls(sl=True)\nccr.createZroGrpWithFlexName(selected)" )

	mc.menuItem( label = "Create Controller at Selected" , command = "from function.rigging.controllerBox import adjustController as ccr\nimportlib.reload(ccr)\nselected = mc.ls(sl=True)\nccr.creControllerFunc(selected)", ann = "create Controller selected.")

	mc.menuItem( label = "rrRigBox CreateController" , command = "from function.rigging.Rigbox_Reborn_Curves_Tool import rr_main_curves as rrCurves\nimportlib.reload(rrCurves)\nrrCurves.window_creation()", ann = "A Maya tool to help with control icon creation and other basic rig construction tasks from Jennifer Conley.")

	mc.menuItem( label = "mz ctrlCreator" , command = "from function.rigging.controllerBox.mz_ctrlCreator import mz_ctrlCreator as mzcc\nimportlib.reload(mzcc)\nmzcc.mz_ctrlCreator()", ann = "Scirpt uses to create controllers by Mingquan Zhou.")

	mc.menuItem(divider = True)
	#------------------------------------------------

	mc.menuItem( label = "Save Controller Data" , command = "from function.rigging.readWriteCtrlSizeData import run\nimportlib.reload(run)\nrun.savingData()", ann = "Save Controller Size Data.")

	mc.menuItem( label = "Load Controller Data" , command = "from function.rigging.readWriteCtrlSizeData import run\nimportlib.reload(run)\nrun.loadingData()", ann = "Load Controller Size Data." , image = ICON_PATH + '\\bullet_interactivePlayback.png')

	mc.menuItem(divider = True)
	#------------------------------------------------

	mc.menuItem( label = "Create Controller" , command = "from function.rigging.controllerBox import createController\nimportlib.reload(createController)\ncreateController.run()", ann = "Create Controller and Assign Color.")

	mc.menuItem( label = "Create Gimbal Controller" , command = "from function.rigging.controllerBox import adjustController\nimportlib.reload(adjustController)\nadjustController.createGimbal()", ann = "createGimbal .")

	mc.menuItem(divider = True)

	mc.menuItem( label = "Edit Controller Shape" , command = "from function.rigging.controllerBox import flipController\nimportlib.reload(flipController)\nflipController.run()", ann = "Select source and destination.")

	mc.menuItem(divider = True)

	mc.setParent( '..', menu=True )
	mc.menuItem(divider = True)
	#------------------------------------------------





	# = = > Blendshape Submenu
	#------------------------------------------------

	mc.menuItem( label = "Blendshape", subMenu = True , tearOff = True)


	FUNCTION_PATH = "/python/function/rigging/blendShape/abSymMesh.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem(label = "abSymMesh",	command = "mel.eval('abSymMesh')",ann = "A useful little script for building symmetrical and asymmetrical blendshapes." )

	FUNCTION_PATH = "/python/function/rigging/blendShape/shapeTools/mirrorShape.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem(label = "MirrorShape",	command = "mel.eval('mirrorShape')",ann = "A useful little script for building symmetrical and asymmetrical blendshapes." )

	FUNCTION_PATH = "/python/function/rigging/blendShape/shapeTools/copyShape.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem(label = "CopyShape",	command = "mel.eval('copyShape')",ann = "A useful little script for building symmetrical and asymmetrical blendshapes." )


	mc.setParent( '..', menu=True )

	mc.menuItem(divider = True)
	#------------------------------------------------






	# = = > AutoRig Submenu
	#------------------------------------------------
	mc.menuItem( label = 'AutoRig' ,subMenu = True, tearOff = True)

	# mc.menuItem(label = "Import Biped Joint",		command = "from function.rigging.autoRig.reference import templateJoint as tpJnt\nimportlib.reload(tpJnt)\ntpJnt.importTemplate('{0}/python/function/rigging/autoRig/reference/templateJoint_biped.ma')\nmc.delete('EH_tmpRig_defaultRenderLayer')".format(PROJECT_PATH) , ann = "Import Template joint project." )

	mc.menuItem(label = "RefDup Biped Joint",		command = "from function.rigging.autoRig.reference import templateJoint as tpJnt\nimportlib.reload(tpJnt)\ntpJnt.refTempRemove('{0}/python/function/rigging/autoRig/reference/templateJoint_biped.ma')".format(PROJECT_PATH) , ann = "Import Template joint project." )

	mc.menuItem(label = "RefDup Quaruped Joint",	command = "from function.rigging.autoRig.reference import templateJoint as tpJnt\nimportlib.reload(tpJnt)\ntpJnt.refTempRemove('{0}/python/function/rigging/autoRig/reference/templateJoint_quaruped.ma')".format(PROJECT_PATH) , ann = "Import Template quaruped joint project." )

	mc.setParent( '..', menu=True )
	mc.menuItem(divider = True)
	#------------------------------------------------




	# = = > Cleanup
	#------------------------------------------------

	mc.menuItem( label = 'Cleanup' , subMenu = True, tearOff = True )

	FUNCTION_PATH = "/mel/zooNameSpacey.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem(label = "zooNameSpacey",	command = "mel.eval('zooNameSpacey()')",ann = "remove namespace" )

	mc.setParent( '..', menu=True )




	# reset controller
	mc.menuItem( label = "Reset all controller", command = "from function.rigging import RESET as re\nimportlib.reload(re)\nre.resetAllController(reference = False)" , ann = "Reset Character Pose" )

	# unhide attirbute
	#mc.menuItem(label="xUnhide Attr", 		command = snapRun , ann = "Snap selected.")

	# create local world switch controller
	mc.menuItem(label="Create Local/World Orient", command = "from function.rigging import LOCAL_WORLD_Orient as lwo\nimportlib.reload(lwo)\nlwo.localWorldOrient()" , ann = "Snap selected." )

	FUNCTION_PATH = "/mel/mFollicle.mel"
	mel.eval('source "%s%s"' %(PROJECT_PATH,FUNCTION_PATH))
	mc.menuItem( label = "mFollicle",	command = "mel.eval('mFollicle()')", ann = "Create Follicle at selected vertex" )

	# mc.menuItem( label = "Rig Tools",	command = "from function.rigging.tools import rigtool\nimportlib.reload(rigtool)\nrun=rigtool.Ui()\nrun.createGUI()", ann = "Just Rig Box" )
	
	# mc.menuItem( label = "Color Tools",	command = "from function.rigging.tools import colorTool\nimportlib.reload(colorTool)\nrun=colorTool.Ui()\nrun.createGUI()", ann = "Just Color Box" )



	mc.setParent( '..', menu=True )

	mc.setParent( '..', menu=True )
	#----------------------------------------------------------------------------------------------------------------------

	mc.menuItem(divider = True)
	
	
	mc.menuItem(label = 'Sync userSetup',	command = "from function.pipeline import fileTools as fileTools\nimportlib.reload(fileTools)\nfileTools.copyMayaFiles()" , ann = "Copy userSetup to User", image = ICON_PATH + '\\VariableInstance.bmp')







# backup
# cometCmd = mel.eval('source "D:/mayaTools/mel/cometTools/cometJointOrient.mel"')

#runMenu()
