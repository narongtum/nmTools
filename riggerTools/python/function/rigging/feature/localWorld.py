import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.tools import dTool as dc 
reload(dc)

# LOCAL WORLD
def localWorld( fromSel = True, giveCtrl = [], ori = True, worldCtrl = 'ctrl_grp' ):
	if fromSel == True:
		sel = mc.ls(sl=1)
	elif fromSel == False:
		sel = giveCtrl

	for each in sel:
		mc.select(each)
		selZroGrp = mc.pickWalk(d='up')
		upSel = mc.pickWalk(d='up')
		preUpGrp = upSel[0]

		if 'Zro' in preUpGrp:
			upSel = mc.pickWalk(d='up')
			grp = preUpGrp
			mainParent = upSel[0]
			print ('Need more step')
		else:
			selGrp = selZroGrp
			grp = selGrp[0]
			mainParent = preUpGrp
			print ('Ok to use it')

		preName = each.split('_')
		name = preName[0]
		
		#grp = name + 'Zro_grp'  //// both preUpGrp, selZroGrp
		wor = name + 'Wor_grp'
		loc = name + 'Loc_grp'
		rev = name + '_rev'

		# Find if localWorld Exist or not
		attrs = mc.listAttr( each ,r = True )
		if 'localWorld' in attrs:
			print ('____________________________')
			print ('localWorld is Exist')
		else:
			mc.addAttr( each , ln = 'localWorld', sn = 'lcw', attributeType = 'float', k = True, min = 0, max = 1 )

		# Check is local world is already marriage
		listCon = mc.listConnections( each + '.localWorld', c = False)
		if mc.objExists(rev) == True:
			if rev in listCon:
				print ('_______________________________________')
				print ('localWorld is already marriage Dude!!!')
				print ('__________________')
				print ('find someone els!')
				break
		else:
			mc.group( em=1,n=wor )
			mc.group( em=1,n=loc )
			mc.createNode('reverse', n=rev )
			
			dc.allMat( wor, grp )
			dc.allMat( loc, grp )

			mc.parent( wor, loc, mainParent )
			if ori == True:
				# World to wor
				dc.oriCon( worldCtrl, wor, mo=1 )
				# oriCon to GRP
				cons = dc.oriCon( [loc,wor] , grp )
			elif ori == False:
				# World to wor
				dc.parCon( worldCtrl, wor, mo=1 )
				# parCon to GRP
				cons = dc.parCon( [loc, wor], grp)
			# Connect it baby
			mc.connectAttr( each + '.localWorld', rev + '.inputX' )
			mc.connectAttr( rev + '.outputX', cons + '.w0' )
			mc.connectAttr( rev + '.inputX', cons + '.w1' )


# run func from name
#localWorld( fromSel = False, giveCtrl = ['pCube1_ctrl'], ori = True, worldCtrl = 'ctrl_grp' )
# run from selection
#localWorld( fromSel = True, giveCtrl = [], ori = True, worldCtrl = 'ctrl_grp' )