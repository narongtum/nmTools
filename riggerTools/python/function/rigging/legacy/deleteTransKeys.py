# use for delete translate key from existing animation.fbx
import maya.cmds as mc
def deleteKey():

	ignorPosList = [ 'Root','hips_bind_jnt','upperArmArmorLFT_bind_jnt','upperArmArmorRGT_bind_jnt','handLFT_prop_jnt','handRGT_prop_jnt','lowerArmLFT_prop_jnt','lowerArmRGT_prop_jnt','tessetArmorLFT_bind_jnt','tessetArmorRGT_bind_jnt']
	noTransList = []
	for each in ignorPosList:
		transX = each + '_translateX'
		transY = each + '_translateY'
		transZ = each + '_translateZ'
		
		noTransList.append(transX)
		noTransList.append(transY)
		noTransList.append(transZ)
		
	print noTransList

	mc.select('*translate*')
	allkey = mc.ls(sl=True)
	for jnt in allkey:
		if jnt in noTransList:
			print 'let them be   ' + jnt + '-------------------------'
		elif jnt == 'translateFilter':
			print ' justFilter '
		else:
			print jnt
			mc.delete( jnt )



	# get last key
	keyIndex = (mc.keyframe('Root.tx', indexValue=True, q=True))[-1]
	lastKey = keyIndex+1

	# set timeline
	#mc.playbackOptions(animationStartTime = 1)
	#mc.playbackOptions(animationEndTime = lastKey)

#test
#deleteKey()