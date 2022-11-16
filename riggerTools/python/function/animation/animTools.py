'''
from function.animation import animTools 
reload( animTools )
'''
from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging.util import misc
reload(misc)

def selectAllCtrl():
	selected = mc.ls( sl = True )
	nameSpace = misc.findNameSpace()

	if nameSpace:
		# If selection is reference
		mc.select('%s*_ctrl' %nameSpace)
	elif selected:
		# If selection is controller
		mc.select( '*_ctrl' )
	else:
		# Nothing select 
		mc.warning( "No controller selected" )