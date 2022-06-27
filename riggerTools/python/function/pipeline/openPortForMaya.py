# open port for sublime
try :
	mc.commandPort(name=":7002", close=True)
	mc.commandPort(name=":7001", close=True)
except RuntimeError as e:
	print (e)

# now open a new port
try :
	mc.commandPort(name=":7002", sourceType="python")
except RuntimeError as e:
	print (e)

# or open some random MEL port (make sure you change it to this port in your config file)
try :
	mc.commandPort(name=":7001", sourceType="mel")
except RuntimeError as e:
	print (e)



import maya.cmds as cmds


# if it was already open under another configuration
cmds.commandPort(name=":7002", close=True)

# now open a new port
cmds.commandPort(name=":7002", sourceType="python")

# or open some random MEL port (make sure you change it to this port in your config file)
cmds.commandPort(name=":10000", sourceType="mel")