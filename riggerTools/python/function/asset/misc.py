'''
from function.asset import misc 
reload(misc)
'''

#... Reload module
from function.framework.reloadWrapper import reloadWrapper as reload

from function.pipeline import logger 
reload(logger)

import maya.cmds as mc

#... Instance logger module
class MiscLogger(logger.MayaLogger):
	LOGGER_NAME = "asset.misc"

def sortOutliner():
	selected = mc.ls(sl=True)
	if selected:
		resorted = sorted(selected)

		for each in resorted:
			mc.reorder(each,back=True)
			MiscLogger.info('{0} has been sorted.'.format(each))
	else:
		MiscLogger.warning('There are no selection.')





