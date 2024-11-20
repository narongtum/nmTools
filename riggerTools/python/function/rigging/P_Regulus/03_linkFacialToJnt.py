# this will link facial Switch ctrl to facial Offset jnt on the floor

# you need to link texture 2D first

import maya.cmds as mc

def linkFacialToJnt( ctrl = 'facialSwitch_ctrl', attr = 'mouth', facialJnt = 'facialOffset_jnt' ):

	# check
	if mc.objExists( '{0}.{1}'.format( ctrl, attr ) ):
		# check 
		if mc.objExists( facialJnt ):
			pass
		else:
			# create joint
			mc.select( cl = True )
			jnt = mc.joint( name = 'facialOffset_jnt' )
			mc.select( cl = True )
			if mc.objExists( 'root' ):
				mc.parent( jnt, 'root' )
				mc.select( cl = True )

		if mc.listConnections( '{0}.tx'.format( facialJnt )):
			print ( '{0} Already Connect'.format( facialJnt ) )
		else:
			mc.connectAttr( '{0}.{1}'.format( ctrl, attr ), '{0}.sx'.format( facialJnt ) )

	else:
		return

	print( 'Connection Accomplish' )

linkFacialToJnt( ctrl = 'facialSwitch_ctrl', attr = 'mouth', facialJnt = 'facialOffset_jnt' )
