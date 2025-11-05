import maya.cmds as mc

def mirror_selCtrl():

	sels = mc.ls( sl = True )
	for sel in sels:
		if 'LFT' in sel:
			side = 'LFT'
			otherSide = 'RGT'
			mirror = True
		elif 'RGT' in sel:
			side = 'RGT'
			otherSide = 'LFT'
			mirror = True
		else:
			mirror = False

		if mirror == True:	

			copyCtrl = sel
			pasteCtrl = sel.replace(side,otherSide)

			attrs = [ 'tx','ty','tz','rx','ry','rz' ]

			if 'Stick' in copyCtrl:
				extraAttrs = [ 'fist', 'roll', 'relax' ]
				for extra in extraAttrs:
					attrs.append( extra )

			for attr in attrs:
				lock = mc.getAttr( '{0}.{1}'.format(copyCtrl,attr), l=1)
				if lock == False:
					attrVal = mc.getAttr('{0}.{1}'.format(copyCtrl,attr) )
					if attr == 'ty' or attr == 'tx' or attr == 'tz' :
						attrVal = attrVal * ( -1 )

					mc.setAttr('{0}.{1}'.format(pasteCtrl,attr), attrVal )


#mirror_selCtrl()


