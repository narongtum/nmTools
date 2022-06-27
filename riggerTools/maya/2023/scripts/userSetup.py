# Reload module

BUILD = 'mayaTools'
sys.path.append(r'D:\sysTools\nmTools\{0}\python'.format(BUILD))

# import mayaEnviron as ENV

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




# userSetup for maya2022 is not load, I donno how to fix it

# import module
import maya.cmds as mc
import sys
import maya.utils


cmds.evalDeferred( runThis ) 






# import importlib for maya2022
import importlib

# append path
sys.path.append(r'{0}\\python'.format(ENV.PROJECT_PATH))


from axionMenu import axionMenu2022 as axm
importlib.reload(axm)


# for Zv
import axionTools.animation 

'''
check to see if we re in batch or interactive mode. 
In interactive it runs maya.utils.executeDeferred  
and if we re in batch mode  it just executes the function
run menu
'''

maya.utils.executeDeferred('axm.runMenu()') 
print 'Create Axion menu...'



# Active port 7002 to recived message from Sublime to Maya
try:
	mc.commandPort(name=":7002", sourceType="python")
except :
	mc.warning('Could not active port 7002 (maybe it already opened.)')




