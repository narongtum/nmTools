#... Reload module

#... import mayaEnviron as ENV

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

#... userSetup for maya2022 is not load, I donno how to fix it
import sys
import maya.utils
import importlib
import maya.cmds as mc

# import importlib for maya2022
from importlib import reload as reload

'''
check to see if we re in batch or interactive mode. 
In interactive it runs maya.utils.executeDeferred  
and if we re in batch mode  it just executes the function
run menu
'''

sys.path.append('D:/sysTools/nmTools_github/riggerTools/python')
from nmMenu import nmMenu2023
importlib.reload(nmMenu2023)
maya.utils.executeDeferred('nmMenu2023.runMenu()')


#... Import module from start
# from function.framework.reloadWrapper import reloadWrapper as reload


from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )

if mc.pluginInfo("bifrostGraph", query=True, loaded=True):
	print("BifrostGraph loaded: True")
else:
	mc.loadPlugin("bifrostGraph")
	print("BifrostGraph was not loaded. It has now been loaded.")
