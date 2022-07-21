import maya.cmds as mc

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload(rigTools)

def ikfkSnap():
	if len(mc.ls(sl=1)) > 0: # SELECT AND FINDING FUNCTION
		sel = mc.ls(sl=1) # list all select object
		for i in range(len(sel)):

			if 'Stick' in sel[i]: # if Stick in the select
				giveName =  sel[i]
				rawNam = giveName.split('_')
				if ':' in sel[i]: # find out is need to extrac namespace or not

					if len(rawNam) == 2:
						nn = rawNam[0]
						ns = nn.split(':')[0]
						namespace = ns + ':'
						selCtrl = giveName.split(':')[1] # IF have only _
						print "A:"
					
					elif len(rawNam) > 2:
						selCtrl = rawNam[-2]+'_'+rawNam[-1]
						namespace = giveName.split(selCtrl)[0]  # IF have more than 1 _
						print "B:"

					# func
					rigTools.ikfkSwitch( selCtrl, namespace = namespace, longAlias = selCtrl, item=None)
					print namespace
					print selCtrl

				elif ':' not in sel[i]: # there is no name space but have to find out is it have the preName or not
					print 'No nameSpace N/a'
					
					if len(rawNam) == 2:
						selCtrl = giveName
						namespace = ''
						print "A"
					
					elif len(rawNam) > 2:
						selCtrl = rawNam[-2]+'_'+rawNam[-1] # selCtrl = nn.split('_')[-1]
						namespace = giveName.split(selCtrl)[0]
						print "B"

					# func
					print namespace
					print selCtrl
					rigTools.ikfkSwitch( selCtrl, namespace = namespace, longAlias = selCtrl, item=None)
			else:
				print "Please Select any Stick" 

	else:
		print "pls select somthing"
