# userSetup for nmTools set


# import module
import maya.cmds as mc
import sys
import maya.utils



# append path
# sys.path.append(r'D:\True_Axion\Tools\riggerTools\python')
# sys.path.append(r'D:\True_Axion\Tools\riggerTools\python\axionTools\rigging\autoRig\bodyRig')
sys.path.append(r'D:\sysTools\nmTools\riggerTools\python')


# reload wrapper
from function.framework.reloadWrapper import reloadWrapper as reloader


from nmMenu import nmMenu as nmm
reloader(nmm)


# for Zv
import function.animation 

'''
check to see if we re in batch or interactive mode. 
In interactive it runs maya.utils.executeDeferred  
and if we re in batch mode  it just executes the function
run menu
'''

maya.utils.executeDeferred('nmm.runMenu()') 
print 'Create Axion menu...'



# Active port 7002 to recived message from Sublime to Maya
try:
	mc.commandPort(name=":7002", sourceType="python")
except :
	mc.warning('Could not active port 7002 (maybe it already opened.)')



