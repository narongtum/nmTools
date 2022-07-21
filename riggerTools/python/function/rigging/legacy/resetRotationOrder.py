
#
# reset the rotation order
#


ctrl_lst = mc.ls('*_ctrl')


for each in ctrl_lst:
	try:
		mc.setAttr("%s.rotateOrder" %each, 0)
	except:
		continue





#
# relink animatin to the old style channal
#

nameSpace = 'b_0070_evandriaBoss_rig_hero'
fingers = ('thumb','index','middle','ring','pinky')
side = 'RGT'

for x in xrange(1,4):
	for finger in fingers:
		# print '{0}{1:02d}{2}_ctrl_rotateZ'.format(finger, x, side)
		mc.connectAttr('{0}{1:02d}{2}_ctrl_rotateZ.output'.format(finger, x, side) , '{3}:{0}{1:02d}{2}_ctrl.rotateX'.format(finger, x, side, nameSpace) , f = True)
		mc.disconnectAttr('{0}{1:02d}{2}_ctrl_rotateZ.output'.format(finger, x, side) , '{3}:{0}{1:02d}{2}_ctrl.rotateZ'.format(finger, x, side, nameSpace) )
		
		
		mc.setAttr('{3}:{0}{1:02d}{2}_ctrl.rotateZ'.format(finger, x, side, nameSpace), 0 )



