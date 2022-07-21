# use path as arg to import asset
'''
from function.rigging.autoRig.reference import templateJoint as tpJnt
reload(tpJnt)
tpJnt.importTemplete('D:/True_Axion/Tools/riggerTools/python/axionTools/rigging/autoRig/reference/EH_tmpRig.ma')


'''
import maya.cmds as mc

# import template joint with no namespace using clashing node
def importTemplate( templatePath = '' ):
	#prefix = "EH_tmpRig"
	mc.file(templatePath, i = True, type = 'mayaAscii', ignoreVersion = True, mergeNamespacesOnClash = False, renamingPrefix = '' , options = 'v=0', preserveReferences = True, importFrameRate = True,importTimeRange = "override" )
	# mc.delete("%s_defaultRenderLayer" %prefix)
# open file in arg
def openTemplete( templatePath = '' ):
	mc.file(templatePath, force = True, options = 'v=0', ignoreVersion = True, type = 'mayaAscii', open = True)