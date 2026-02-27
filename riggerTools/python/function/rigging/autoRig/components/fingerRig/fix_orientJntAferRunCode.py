fingerList = ('thumb','index','middle','ring','pinky')
side = 'RGT'

for finger in fingerList:
	for num in range(1,4):
		#print(f'thumb{num:02}LFT_ctrl')
		print(f'{finger}{num}{side}_ctrl')
		print(f'{finger}{num}{side}_bJnt')
		mc.parentConstraint(f'{finger}{num:02}{side}_ctrl', f'{finger}{num:02}{side}_bJnt', name = f'{finger}{num:02}{side}_parCons')
