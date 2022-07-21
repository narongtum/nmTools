
#
# auto naming file name
#



#  naming file texture name
textureSelect = mc.ls(sl=True)

if textureSelect:
	for each in textureSelect:

		if mc.nodeType(each) == 'file':
			print 'This texture file'
			matNam = mc.listConnections(each)[0]
			print matNam

			#print materialName
			if matNam.endswith('_mat'):
				print 'This material is naming already'
				# convert name
				# fileMatNam = matNam.strip('_mat') + '_file'
				fileMatNam = matNam.replace('_mat','_file')
				print fileMatNam
				mc.rename( each , fileMatNam )
			else:
				print 'This is not naming'

		elif mc.nodeType(each) == 'place2dTexture':
			print 'This place2dTexture file'
			matNam = mc.listConnections(each)[0]
			print matNam

			#print materialName
			if matNam.endswith('_file'):
				print 'This material is naming already'
				# convert name
				# fileMatNam = matNam.strip('_file') + '_plce2d'
				fileMatNam = matNam.replace('_file','_plce2d')
				print fileMatNam
				mc.rename( each , fileMatNam )
			else:
				print 'This place2dTexture is not naming'

else:
	mc.warning('Please select file texture.')
	
	


listFile = mc.ls(type = 'file')


for each in listFile:
	matNam = mc.listConnections(each)[0]
	#print materialName
	if matNam.endswith('_mat'):
		print 'This is naming already'
		fileMatNam = matNam.split('_mat')[0] + '_file'
		print fileMatNam
		mc.rename( each , fileMatNam )
	else:
		print 'This is not naming'
		continue
		
		
		
listFile = mc.ls(type = 'place2dTexture')
for each in listFile:
	matNam = mc.listConnections(each)[0]
	#print materialName
	if matNam.endswith('_file'):
		print 'This is naming already'
		fileMatNam = matNam.split('_file')[0] + '_plce2d'
		print fileMatNam
		mc.rename( each , fileMatNam )
	else:
		print 'This is not naming'
		continue
