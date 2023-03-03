# use path as arg to import asset
'''
from function.rigging.autoRig.reference import templateJoint as tpJnt
reload(tpJnt)
tpJnt.importTemplete('D:/True_Axion/Tools/riggerTools/python/axionTools/rigging/autoRig/reference/EH_tmpRig.ma')


'''
import maya.cmds as mc

from function.enviroment import enviromentPath as env
from function.framework.reloadWrapper import reloadWrapper as reload
reload(env)



# import template joint with no namespace using clashing node
def importTemplate( templatePath = '' ):
	#prefix = "EH_tmpRig"
	mc.file(templatePath, i = True, type = 'mayaAscii', ignoreVersion = True, mergeNamespacesOnClash = False, renamingPrefix = '' , options = 'v=0', preserveReferences = True, importFrameRate = True,importTimeRange = "override" )
	# mc.delete("%s_defaultRenderLayer" %prefix)
# open file in arg
def openTemplete( templatePath = '' ):
	mc.file(templatePath, force = True, options = 'v=0', ignoreVersion = True, type = 'mayaAscii', open = True)


#.. Using reference and duplicate instead

def refTempRemove(REF_PATH):
	
	namespace = "_temp_ref"

	mc.file(REF_PATH, 
			  r=True, 
			  type="mayaAscii", 
			  ignoreVersion=True, 
			  gl=True, 
			  mergeNamespacesOnClash=False, 
			  namespace=namespace, 
			  options="v=0;")

	mc.duplicate('_temp_ref:template_ctrl')
	mc.file( REF_PATH , rr=True )

