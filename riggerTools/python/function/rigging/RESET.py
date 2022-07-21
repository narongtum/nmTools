# reset all controller
from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging.util import misc as misc
reload(misc)

def resetAllController( reference = False ):
	name = ''
	if reference:
		refStr = '*:*'
		print ('This is reference.')
	else:
		refStr = '*'
	print (refStr)

	#sel = mc.ls( '%s_ctrl' %refStr )

	sel = mc.ls('%s_ctrl' %refStr,'%s_gmbCtrl' %refStr)
	for i in range( len(sel) ):

		name = sel[i]
		# DISABLE PRINT BECAUSE IT MAKE SLOWER
		# print 'Reset %s Ctrl Value to Zero.' %name
		attr = 'tx','ty','tz','rx','ry','rz','sx','sy','sz'
		for a in range(len(attr)):
			attrName = name + '.' + attr[a]
			lock = mc.getAttr( attrName , l = 1 )
			if lock == True:
				continue
			if lock == False:
				if attr[a] == 'sx':
					mc.setAttr(attrName,1)
				elif attr[a] == 'sy':
					mc.setAttr(attrName,1)
				elif attr[a] == 'sz':
					mc.setAttr(attrName,1)

				else:
					# if some controller having connection it will cast error.
					try:
						if mc.getAttr( attrName ) == 0:
							# DISABLE PRINT BECAUSE IT MAKE SLOWER
							# print 'It already 0 skipped.'
							continue
						else:
							mc.setAttr( attrName, 0 )
					except :
						print ('%s is can not reset, skipped.' %name)
						continue
					

	# include condition for finger curl controller
	# noman edit

	curlBehav = ( 'fist' ,'roll' ,'relax' , 'spread' , 'wide')

	curlFinger = ('armStickRGT_ctrl', 'armStickLFT_ctrl', 'handStickRGT_ctrl', 'handStickLFT_ctrl', 'stickLFT_ctrl', 'stickRGT_ctrl')

	print (name)
	print ('This is Reference si na.')
	mc.select(name)
	nameSpace = misc.findNameSpace()


	for finger in curlFinger:
		for behav in curlBehav:
			print (nameSpace + finger + '.' + behav)
			if mc.objExists( nameSpace + finger + '.' + behav ):
				mc.setAttr( nameSpace + finger + '.' + behav, 0 )
	


		print ('Reset finger ....\n')




	mc.select(cl=True)
	print( "### RESET CTRL VALUE COMPLETE ###")