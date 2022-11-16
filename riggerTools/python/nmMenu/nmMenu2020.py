# coding: utf-8
'''
// date : 30.Mar.2022
//----------------------------------------------------------------------------
// nomanMenu - Python Script - version 0.4
//----------------------------------------------------------------------------
//
// DESCRIPTION:
//
// REQUIRES:	to install this menu just copy
//	D:\\sysTools\\nmTools\\riggerTools\\maya
// 	to C:\\Users\\<user>\\Documents\\maya
//
//
//
//----------------------------------------------------------------------------
'''

# MAIN Menu
import pymel.core as pm
import maya.cmds as mc
import maya.OpenMaya as om
import maya.mel as mel
import sys
import os.path


# find variable enviroment
path = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.normpath(path)
PROJECT_PATH = abs_path.replace(r'\python\nmMenu','')


# add path
PLUGINS_PATH = PROJECT_PATH + "\\python\\function\\plugin\\2018\\"

# load plugins
mc.loadPlugin( PLUGINS_PATH + "AnimSchoolPicker.mll", quiet = True)

# naming
PROJECT_NAME = 'nmMenu'

# append path
#sys.path.append(r'D:\sysTools\nmTools\riggerTools\python')
iconPath = PROJECT_PATH + r'\\image'




def reloadMenu():
	if pm.menu( 'MayaWindow|%s' %PROJECT_NAME, exists = True):
		mc.deleteUI('MayaWindow|%s' %PROJECT_NAME)


# run menu
def runMenu():
	# Delete exists menu
	if pm.menu( 'MayaWindow|%s' %PROJECT_NAME, exists = True):
		mc.deleteUI('MayaWindow|%s' %PROJECT_NAME)


	# Name of the global variable for the Maya window
	MainMayaWindow = pm.language.melGlobals['gMainWindow']

	# Build a menu and parent under to that Maya Window
	TAI = pm.menu( PROJECT_NAME, to = True, parent = MainMayaWindow )




	'''

	MENU Body Part

	'''




	'''

	 Asset Tools

	'''
	#----------------------------------------------------------------------------------------------------------------------
	mc.menuItem( label = 'Asset' , subMenu = True, tearOff = True)


	mc.menuItem( label = 'Publish file', divider = True )

	mc.menuItem( label = "Commit To SVN",	command = "from function.pipeline import svnMaya\nreload(svnMaya)\nsvnMaya.commitCurrentPath()", ann = "Commit current file to SVN.(Make sure this file already add.)" , image = iconPath + '\\svn-commit-small.png')	

	mc.menuItem( label = "Local Publish",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfileTools.localPublish()", ann = "Clean file and commit to local department.", image = iconPath + '\\localPublish.png')

	mc.menuItem( label = "Global Publish",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfileTools.globalPublish()", ann = "Clean file and commit to Global Library.", image = iconPath + '\\worldIcon.png')


	#mc.menuItem( label = 'Exporting Tools', divider = True )

	mc.menuItem( label = "Export with Path", command = "from function.asset import exportPathTool as exportPathTool\nreload(exportPathTool)\nrun = exportPathTool.Ui()\nrun.createGUI()" , ann = "export To Path From Selected Object" )

	mc.menuItem( label = "Export Skeleton Mesh", command = "from function.asset import export_skelMesh as esm \nreload(esm)\nesm.exportRig_fbx()" , ann = "Export Skeleton Mesh" )

	mc.menuItem( label = "Export FBX file to current folder.",	command = "from function.asset import exportFBX\nreload(exportFBX)\nexportFBX.noCareExporter()", ann = "Automate export FBX file to curren maya folder.( select mesh and run )")

	#-----------------------------

	mc.menuItem( label = 'Asset', divider = True )

	mc.menuItem( label = "Create Thumbnails",	command = "from function.pipeline import fileTools as fileTools\nreload(fileTools)\nfileTools.createThumbnail()", ann = "Create Thumbnails at current location.")

	mc.menuItem( label = "Remove selected reference",	command = "from function.rigging.util import misc as misc\nreload(misc)\nmisc.removeSelectedReference()", ann = "Remove Selected Reference")

	mc.menuItem( label = "Import And Remove Namespace",	command = "from function.asset import assetTools as ast\nreload(ast)\nast.impRem()", ann = "Import and remove namespace")

	mc.menuItem( label = "Replace Texture",	command = "from function.asset import assetTools as ast\nreload(ast)\nast.replaceTex()", ann = "Replace All Texture in scene.")
	
	mc.menuItem( label = "Open Containing Folder",	command = "from function.pipeline import fileTools\nreload(fileTools)\nfolder = fileTools.currentBackFolder()\nfileTools.openContainerFile(path = folder)", ann = "Open Containing Folder.")

	





	#-----------------------------
	mc.menuItem( label = 'Naming', divider = True )
	# use cometJointOrient
	mel.eval('source "D:/sysTools/nmTools/riggerTools/mel/cometTools/cometRename.mel"')
	mc.menuItem(label="cometRename",	command = "mel.eval('cometRename()')",ann = "Set JointOrient" )

	mc.menuItem( label = "Renamer",	command = "from function.framework.Qtpy.Qt import QtCore, QtGui, QtWidgets\nfrom function.asset.renamer import nomanRenamer_ui\nreload(nomanRenamer_ui)\nForm = QtWidgets.QWidget()\nui = nomanRenamer_ui.Ui_ReNameUi()\nui.setupUi(Form)\nForm.show()", ann = "Renamer")

	mc.menuItem( label = "Auto add suffix",	command = "from function.rigging.util import misc as msc\nreload(msc)\nmsc.selAutoSuffix()", ann = "Select and click.")

	mc.menuItem( label = "Transfer Selected Shading.",	command = "from function.asset import assetTools as ast\nreload(ast)\nast.transferShade()", ann = "Select Parent then Child.")
	mc.setParent( '..', menu = True )
	#----------------------------------------------------------------------------------------------------------------------


	'''

	 Modeling Tools

	'''
	#----------------------------------------------------------------------------------------------------------------------
	mc.menuItem( label = 'Modeling' ,subMenu = True, tearOff = True)

	# Export Asset
	#mc.menuItem( label="xExport Asset", ann = "Export Asset.." )

	mc.menuItem( label = "Create Shader", command = "from function.rigging.tools import createShdFromSel as shdFromSel\nreload(shdFromSel)\nrun = shdFromSel.Ui()\nrun.createGUI()" , ann = "Create Shader From Selected Object" )

	# mc.menuItem( label = "Connect BSH :select model", command = "from function.modelling import InvictusBSH as INVBSH\nreload(INVBSH)\nINVBSH.connectExpression()" , ann = "Connect Blendshape From Selected Helmet" )
	
	# mc.menuItem( label = "Connect BSH :select BSH", command = "from function.modelling import InvictusBSH as INVBSH\nreload(INVBSH)\nINVBSH.connectBshToCtrl()" , ann = "Connect Blendshape From Selected blendshapes" )

	mc.setParent( '..', menu = True )
	#----------------------------------------------------------------------------------------------------------------------




	'''

	 Animation Tools

	'''
	#----------------------------------------------------------------------------------------------------------------------
	# Animation Main Menu
	mc.menuItem( label = 'Animation' , subMenu = True , tearOff = True)
	# Animation sub menu

	# Studio Library
	mc.menuItem( label = "Studio Library", 			command = "from function.animation import studiolibrary\nreload(studiolibrary)\nstudiolibrary.main()" , ann = "Run animation Library" )

	# AnimSchoolPicker
	mc.menuItem( label = "AnimSchool Picker", 		command = "mel.eval('AnimSchoolPicker()')" , ann = "Run AnimSchool Picker" )

	# onionSkinRenderer
	mc.menuItem( label = "OnionSkinRenderer", 		command = "from function.animation.onionSkinRenderer import onionSkinRendererWindow as onionWindow\nreload(onionWindow)\nonionWindow.openOnionSkinRenderer()" , ann = "onionSkinRenderer" )

	# ZvParentMaster
	mc.menuItem( label = " ZvParentMaster", 		command = "from function.animation import ZvParentMaster\nreload(ZvParentMaster)\nZvParentMaster.ZvParentMaster()" , ann = "animation tool that helps you to animate objects in mutual contact or interaction with ease." )

	# ZvParentMaster Mod Ui
	mc.menuItem( label = " ZvParentMaster Ui", 		command = "from function.animation import zvParentMaster_tools_ui_mod as zv\nreload(zv)\nzv.createGUI()" , ann = "animation tool that helps you to animate objects in mutual contact or interaction with ease." )
	
	# tweener
	mc.menuItem( label = "Tweener", 	command = "from function.animation import tweenerUI\nreload (tweenerUI)\ntweenerUI.TweenWindow().show()" , ann = "adjust the slider and see the results immediately" )



	'''# ackDeleteRedundant
				mel.eval('source "D:/sysTools/nmTools/riggerTools/mel/ackDeleteRedundant.mel"')
				mc.menuItem(label = "ackDeleteRedundant", 		command = "mel.eval('ackDeleteRedundant')", ann = "Deletes keys that have the same value as it's two" )'''

	mc.menuItem(divider = True)
	#------------------------------------------------------------------------------------------------

	# Playblast tool
	mc.menuItem( label = "Playblast Tool", 			command = "from function.pipeline.playBlast import playblastTool\nreload(playblastTool)\nrun=playblastTool.Ui()\nrun.createGUI()" , ann = "Playblast tools" )

	mc.menuItem(divider = True)
	#------------------------------------------------------------------------------------------------

	mc.menuItem( label = "Export Animation", 		command = "from function.asset import genericAnimExporter as gae\nreload(gae)\nrun = gae.Ui()\nrun.createGUI()" , ann = "Bake Animation Export"  )
	
	# mc.menuItem( label = "SNAP IK/FK", 				command = "from function.animation import NewSnap as snp\nreload(snp)\nsnp.Snap()" , ann = "SNAP IK/FK" )

	# mc.menuItem( label = "SNAP IK/FK V3", 			command = "from function.animation import snapFKIKv3\nreload(snapFKIKv3)\nsnapFKIKv3.ikfkSnap()" , ann = "Newer SNAP IK/FK for new autoRig" )
	
	# mc.menuItem( label = "SNAP IK/FK v4", 			command = "from function.animation import snapFKIKv4\nreload(snapFKIKv4)\nsnapFKIKv4.ikfkSnap()" , ann = "2020 SNAP IK/FK for 2020+ autoRig" )

	# mc.menuItem( label = "BakeMocap", 				command = "from function.animation import bakeFromMocap as bfm\nreload(bfm)\nrun=bfm.Main()\nrun.bakeGUI()" , ann = "Bake Mocap Animation"  )

	# mc.menuItem( label = "BakeMocap 90", 			command = "from function.animation import bakeFromMocap90 as bfnine\nreload(bfnine)\nrun=bfnine.Main()\nrun.bakeGUI()" , ann = "Bake Mocap Animation footage that flip 90 degree."  )

	# mc.menuItem( label = "[EH] BakeAnim", 			command = "from function.animation import bakeAnimationEH as bae\nreload(bae)\nrun=bae.Ui()\nrun.createGUI()" , ann = "Bake Animation"    )

	# mc.menuItem( label = "[SS] BakeAnim", 			command = "from function.animation import bakeAnimationSS as bas\nreload(bas)\nrun=bas.Ui()\nrun.createGUI()" , ann = "Bake Animation SS"    )

	# mc.menuItem( label = "[2HR] BakeAnim",			command = "from function.animation import bakeAnimationRotateFor2Hero as bah\nreload(bah)\nrun=bah.Ui()\nrun.createGUI()" , ann = "Bake Animation For 2 Hero project"    )

	# mc.menuItem( label = "[PH] BakeExport", 		command = "from function.animation import bakeAnimationPH as bai\nreload(bai)\nrun=bai.Ui()\nrun.createGUI()" , ann = "Bake Animation for HOPE project"    )

	# mc.menuItem( label = "[PH] Delete Translate",	command = "from function.rigging.legacy import deleteTransKeys as deleteTransKeys\nreload(deleteTransKeys)\ndeleteTransKeys.deleteKey()" , ann = "Delete translate key from fbx file"  )

	mc.menuItem(divider = True)
	#------------------------------------------------
	mc.menuItem( label = "Reset all controller",	command = "from function.rigging import RESET as re\nreload(re)\nre.resetAllController(reference = True)" , ann = "Reset Character Pose ( reference only )"   )

	mc.menuItem( label = "Reset controller (nonRef)",	command = "from function.rigging import RESET as re\nreload(re)\nre.resetAllController(reference = False)" , ann = "Reset Character Pose ( for rigger )"   )
	
	mc.menuItem( label = "Select all controller", 	command = "from function.animation import animTools\nreload(animTools)\nanimTools.selectAllCtrl()" , ann = "Select all controller"    )

	mc.menuItem( label = "mirror controller", 		command = "from function.animation import mirrorSelCtrl\nreload(mirrorSelCtrl)\nmirrorSelCtrl.mirror_selCtrl()", ann = "Select LFT ctrl and auto copy to other side and vice versa"	)

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

	mc.menuItem( label = "Snap All Transforms", 	command = "from function.rigging.util import misc\nreload(misc)\nmisc.parentCon()" , ann = "Snaping All Transforms selected, Select parent and child." )

	mc.menuItem( label = "Snap Position", 		command = "from function.rigging.util import misc\nreload(misc)\nmisc.pointCon()" , ann = "Snaping Point selected, Select parent and child." )

	mc.menuItem( label = "Snap Rotation", 		command = "from function.rigging.util import misc\nreload(misc)\nmisc.orientCon()" , ann = "Select parent and child." )

	mc.setParent( '..', menu=True )




	
	# = = > Skeleton Submenu
	#------------------------------------------------
	mc.menuItem( label = 'Skeleton' ,subMenu = True, tearOff = True)

	# Create Joint at selected vertex
	mc.menuItem(label = "Create Joint at selected vertex", command = "from function.rigging.util import misc as misc\nreload(misc)\nmisc.creJntAtVertex()" , ann = "Create Joint at selected vertex" )

	# CometJointOrient
	OrientCmd = mel.eval('source "D:/sysTools/nmTools/riggerTools/mel/cometTools/cometJointOrient.mel"')
	mc.menuItem(label="cometJointOrient",	command = "mel.eval('cometJointOrient()')",ann = "Comet Set JointOrient" )

	# Create joint along curve
	mc.menuItem(label = "Create Joint Along Curve", command = "from function.rigging.skeleton import createJointAlongCurve as cjac\nreload(cjac)\ncjac.run()" , ann = "Create Joint at selected vertex" )

	mc.setParent( '..', menu=True )









	# = = > Skin Submenu
	#------------------------------------------------
	mc.menuItem( label = "Skin", 				ann = "Snap selected.",subMenu = True , tearOff = True)


	# Import weight
	mc.menuItem( label = "Load weight", command = "from function.rigging.skin import autoReadWriteSkin\nreload(autoReadWriteSkin)\nautoReadWriteSkin.importWeightData()" , ann = "Select source and import." )

	# Export weight
	mc.menuItem( label = "Save weight", command = "from function.rigging.skin import autoReadWriteSkin\nreload(autoReadWriteSkin)\nautoReadWriteSkin.exportWeightData()" , ann = "Select source and export.", image = iconPath + '\\bullet_interactivePlayback.png' )
	
	# Browse weight
	mc.menuItem( label = "Browse weight", command = "from function.rigging.skin import autoReadWriteSkin\nreload(autoReadWriteSkin)\nautoReadWriteSkin.browseWeight()" , ann = "Browse source and import skin." )

	# Browse weight
	mc.menuItem( label = "Export mesh general data", command = "from function.rigging.skin import exportImportMeshGeneralData as IMG\nreload(IMG)\nIMG.run()" , ann = "Browse source and import skin general data." )
	
	# Chad vernon skin weight import / export
	mc.menuItem( label = "Skin Import / Export", command = "from function.rigging.skin import skinio\nreload(skinio)\nskinio.show()" , ann = "Just another skinweight Import/Export thank to chad vernon." )

	# Export mesh general data
	# mc.menuItem( label = "Export mesh general data", command = "from function.rigging.skin import skinUtil\nreload(skinUtil)\nskinUtil.writeRigData()" , ann = "Write geneal skin data to txt file." )

	# Select bind joint from same mesh
	# mc.menuItem( label = "Select bind joint from same mesh", command = "from function.rigging.skin import autoReadWriteSkin\nreload(autoReadWriteSkin)\nautoReadWriteSkin.selectBJntFromSameMesh()" , ann = "Select bind joint from mesh that was skinCluster before." )

	mc.menuItem(divider = True)
	#------------------------------------------------

	# skinWrangler
	mc.menuItem( label = "SkinWrangler", command = "from function.rigging.skin.skinWrangler import skinWrangler as sw\nreload(sw)\nskinWranglerWindow = sw.show()" , ann = "By Christopher Evans, https://github.com/chrisevans3d/skinWrangler" )

	mc.menuItem(divider = True)
	#------------------------------------------------

	# dora weight
	DoraCmd = mel.eval('source "D:/sysTools/nmTools/riggerTools/mel/DoraSkinWeightImpExp.mel"')

	mc.menuItem( label = "DoraWeight", 	command = "mel.eval('DoraSkinWeightImpExp()')", ann = "Read and Write skin weight" )

	mc.menuItem( label = "Copyweight", 	command = "from function.rigging.skin import copySkinWeight as ckw\nreload(ckw)\nckw.copyWeight()" , ann = "Select source and destination and copyWeight." )

	mc.menuItem( label = "tf_smoothSkinWeight", command = "from function.rigging import tf_smoothSkinWeight\nreload(tf_smoothSkinWeight)\ntf_smoothSkinWeight.paint()", ann = "select a skinned mesh and execute" )

	mc.menuItem( label = "Select bind joint", command = "from function.rigging.skin import skinUtil as skinUtil\nreload(skinUtil)\nskinUtil.selectBindJnt()", ann = "select a bind joint" )

	mc.menuItem( label = "ml_copySkin", command = "from function.rigging.skin import ml_copySkin\nreload(ml_copySkin)\nml_copySkin.ui()", ann = "Copy a skinCluster from one mesh to another, or to a selection of vertices." )

	mc.menuItem( label = "CopySkin from Ref", command = "from function.rigging.skin import copySkinFromRef as cpr\nreload(cpr)\ncpr.runUi()", ann = "Likewise above but can use as Reference." )

	mc.menuItem(divider = True)
	#------------------------------------------------

	mc.menuItem( label = "Rename all skinCluster", command = "from function.rigging.skin import skinUtil as skinUtil\nreload(skinUtil)\nskinUtil.renameSkinCluster()", ann = "rename all skinCluster" )


	mc.setParent( '..', menu=True )



	# = = > Controller Submenu
	#------------------------------------------------

	mc.menuItem( label = "Controller", ann = "Snap selected.", subMenu = True , tearOff = True)

	mc.menuItem( label = "Create Master Group", 	command = "from function.rigging.autoRig.bodyRig import rootRig\nreload(rootRig)\nrootRig.createMasterGrp(charScale=1)" )

	mc.menuItem( label = "Create ZroGrp", 	command = "from function.rigging.controllerBox import adjustController as ccr\nreload(ccr)\nccr.createZroGrp()" )

	mc.menuItem( label = "Create Controller at Selected" , command = "from function.rigging.controllerBox import adjustController as ccr\nreload(ccr)\nccr.creControllerFunc()", ann = "create Controller selected.")

	mc.menuItem( label = "rrRigBox CreateController" , command = "from function.rigging.Rigbox_Reborn_Curves_Tool import rr_main_curves as rrCurves\nreload(rrCurves)\nrrCurves.window_creation()", ann = "A Maya tool to help with control icon creation and other basic rig construction tasks from Jennifer Conley.")

	mc.menuItem( label = "mz ctrlCreator" , command = "from function.rigging.controllerBox.mz_ctrlCreator import mz_ctrlCreator as mzcc\nreload(mzcc)\nmzcc.mz_ctrlCreator()", ann = "Scirpt uses to create controllers by Mingquan Zhou.")

	mc.menuItem(divider = True)
	#------------------------------------------------

	mc.menuItem( label = "Save Controller Data" , command = "from function.rigging.readWriteCtrlSizeData import run\nreload(run)\nrun.savingData()", ann = "Save Controller Size Data.")

	mc.menuItem( label = "Load Controller Data" , command = "from function.rigging.readWriteCtrlSizeData import run\nreload(run)\nrun.loadingData()", ann = "Load Controller Size Data." , image = iconPath + '\\bullet_interactivePlayback.png')

	mc.menuItem(divider = True)
	#------------------------------------------------

	mc.menuItem( label = "Create Controller" , command = "from function.rigging.controllerBox import createController\nreload(createController)\ncreateController.run()", ann = "Create Controller and Assign Color.")

	mc.menuItem( label = "Create Gimbal Controller" , command = "from function.rigging.controllerBox import adjustController\nreload(adjustController)\nadjustController.createGimbal()", ann = "createGimbal .")

	mc.menuItem(divider = True)

	mc.menuItem( label = "Edit Controller Shape" , command = "from function.rigging.controllerBox import flipController\nreload(flipController)\nflipController.run()", ann = "Select source and destination.")

	mc.menuItem(divider = True)

	mc.setParent( '..', menu=True )
	mc.menuItem(divider = True)
	#------------------------------------------------





	# = = > Blendshape Submenu
	#------------------------------------------------

	mc.menuItem( label = "Blendshape", subMenu = True , tearOff = True)

	mel.eval('source "D:/sysTools/nmTools/riggerTools/python/function/rigging/blendShape/abSymMesh.mel"')
	mc.menuItem(label = "abSymMesh",	command = "mel.eval('abSymMesh')",ann = "A useful little script for building symmetrical and asymmetrical blendshapes." )

	mel.eval('source "D:/sysTools/nmTools/riggerTools/python/function/rigging/blendShape/shapeTools/mirrorShape.mel"')
	mc.menuItem(label = "MirrorShape",	command = "mel.eval('mirrorShape')",ann = "A useful little script for building symmetrical and asymmetrical blendshapes." )

	mel.eval('source "D:/sysTools/nmTools/riggerTools/python/function/rigging/blendShape/shapeTools/copyShape.mel"')
	mc.menuItem(label = "CopyShape",	command = "mel.eval('copyShape')",ann = "A useful little script for building symmetrical and asymmetrical blendshapes." )


	mc.setParent( '..', menu=True )

	mc.menuItem(divider = True)
	#------------------------------------------------






	# = = > AutoRig Submenu
	#------------------------------------------------
	mc.menuItem( label = 'AutoRig' ,subMenu = True, tearOff = True)

	mc.menuItem(label = "Import Biped Joint",		command = "from function.rigging.autoRig.reference import templateJoint as tpJnt\nreload(tpJnt)\ntpJnt.importTemplate('D:/sysTools/nmTools/riggerTools/python/function/rigging/autoRig/reference/templateJoint_biped.ma')\nmc.delete('EH_tmpRig_defaultRenderLayer')" , ann = "Import Template joint project." )

	mc.menuItem(label = "Import Quaruped Joint",		command = "from function.rigging.autoRig.reference import templateJoint as tpJnt\nreload(tpJnt)\ntpJnt.importTemplate('D:/sysTools/nmTools/riggerTools/python/function/rigging/autoRig/reference/templateJoint_quaruped.ma')" , ann = "Import Template quaruped joint project." )

	mc.setParent( '..', menu=True )
	mc.menuItem(divider = True)
	#------------------------------------------------




	# = = > Cleanup
	#------------------------------------------------

	mc.menuItem( label = 'Cleanup' , subMenu = True, tearOff = True )

	mel.eval('source "D:/sysTools/nmTools/riggerTools/mel/zooNameSpacey.mel"')
	mc.menuItem(label = "zooNameSpacey",	command = "mel.eval('zooNameSpacey()')",ann = "remove namespace" )

	mc.setParent( '..', menu=True )




	# reset controller
	mc.menuItem( label = "Reset all controller", command = "from function.rigging import RESET as re\nreload(re)\nre.resetAllController(reference = False)" , ann = "Reset Character Pose" )

	# unhide attirbute
	#mc.menuItem(label="xUnhide Attr", 		command = snapRun , ann = "Snap selected.")

	# create local world switch controller
	mc.menuItem(label="Create Local/World Orient", command = "from function.rigging import LOCAL_WORLD_Orient as lwo\nreload(lwo)\nlwo.localWorldOrient()" , ann = "Snap selected." )

	mel.eval('source 	"D:/sysTools/nmTools/riggerTools/mel/mFollicle.mel"	')
	mc.menuItem( label = "mFollicle",	command = "mel.eval('mFollicle()')", ann = "Create Follicle at selected vertex" )

	mc.menuItem( label = "Rig Tools",	command = "from function.rigging.tools import rigtool\nreload(rigtool)\nrun=rigtool.Ui()\nrun.createGUI()", ann = "Just Rig Box" )
	
	mc.menuItem( label = "Color Tools",	command = "from function.rigging.tools import colorTool\nreload(colorTool)\nrun=colorTool.Ui()\nrun.createGUI()", ann = "Just Color Box" )



	mc.setParent( '..', menu=True )

	mc.setParent( '..', menu=True )
	#----------------------------------------------------------------------------------------------------------------------

	mc.menuItem(divider = True)
	
	# comment because it cause of maya crash
	#mc.menuItem(label = 'Reload Menu',		command = "from nmMenu import nmMenu as axm\nreload(axm)\naxm.reloadMenu()\naxm.runMenu()" , ann = "Re-Creates this menu, and does a rehash to pick up any new scripts.",image = iconPath + '\\VariableInstance.bmp')
	
	mc.menuItem(label = 'Sync userSetup',	command = "from function.pipeline import fileTools as fileTools\nreload(fileTools)\nfileTools.copyMayaFiles()" , ann = "Copy userSetup to User", image = iconPath + '\\VariableInstance.bmp')







# backup
# cometCmd = mel.eval('source "D:/mayaTools/mel/cometTools/cometJointOrient.mel"')

#runMenu()
