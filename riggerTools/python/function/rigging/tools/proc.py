# Proc

import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.tools import dTool as dc 
reload(dc)
from function.rigging.feature import localWorld as lcw
reload( lcw )
# for CogPivot Only
from function.rigging.autoRig.base import core
reload(core)

def clearVis( suffix = '_ctrl' , hide = False):

	try :
		mc.select( cl = True)
		mc.select( '*' + suffix )
		sel = mc.ls(sl = True )
		if sel > 0 :
			for each in sel:
				if hide == True:
					if suffix == '_loc':
						locatorShp = each + 'Shape'
						print (locatorShp)
						dc.lockHideVis( locatorShp )
					else:
						dc.lockHideVis( each )
				elif hide == False:
					dc.lockVis( each )
		mc.select( cl = True )

	except:
		print (" there is no " )
		print (suffix)




def QuickProc( giveName = 'strap', side = 'LFT', switchCtrl = 'backCloth_ctrl'):
	for i in range(2):
		if i > 0:
			name = giveName + '%02d' %(i+1) + side
			ikJnt = name + '_ikJnt'
			fkSimGrp = name + 'Sim_grp'
			# connect
			con = dc.oriCon( ikJnt, fkSimGrp )
			mc.connectAttr( switchCtrl + '.autoStrap', con + '.w0' )



def renameShd( overideName = '' ):
	# Auto rename from mat
	# you have to select mat fist
	sel = mc.ls(sl=True)
	for each in sel:
		if overideName == '':
			name = each.split('_')[-1]
		else:
			name = overideName
		#print name
		shd = name + '_shd'
		mat = name + '_mat'
		file = name + '_file'
		bmp = name + '_bmp'
		bmpFile = name + '_bmp_file'
		# List connect of select
		connects = mc.listConnections( each , p = True )
		for plug in connects:
			node = plug.split('.')[0]
			nt = mc.nodeType( node )

			if nt == 'shadingEngine':
				print (node)
				mc.rename( node, shd )
			elif nt == 'bump2d':
				bmpConnected = mc.listConnections( node, p = True )
				for con in bmpConnected:
					if 'outAlpha' in con:
						print (con)
						bmpFileNode = con.split('.')[0]
						mc.rename( bmpFileNode, bmpFile )
				mc.rename( node, bmp )
			elif nt == 'file':
				print (node)
				mc.rename( node, file )
		mc.rename( each, mat )



def piston( masterA = 'Ankle_R_bJnt', masterB = 'AnkleBack_Flab_R_bJnt' ):
	sel = mc.ls(sl=1)
	#createJnt
	for s in range(len(sel)):
		if s == 0:
			master = masterA
			root = sel[0]
			tip = sel[1]
		elif s == 1:
			master = masterB
			root = sel[1]
			tip = sel[0]
		mc.select(cl=1)
		for i in range(2):
			bJnt = root + '_%02d_bJnt' %(i+1)
			mc.joint( name = bJnt )
			if i == 0:
				dc.posMat( bJnt, root )
			elif i == 1:
				dc.posMat( bJnt, tip )
				
		pistJnt = root + '_01_bJnt'
		delJnt = root + '_02_bJnt'
		
		mc.joint( pistJnt, e = True, oj = 'yzx', secondaryAxisOrient = 'zdown', ch = True, zso = True ) 
		mc.delete( delJnt )
		
		mc.parent( pistJnt, master )
		dc.parCon( master, root, mo=1 )
		mc.aimConstraint( tip, pistJnt, aimVector = (0,1,0), upVector = (1,0,0), worldUpType = "scene",  mo =1, w = 1)



def resetAllController( reference = False ):
	if reference:
		refStr = '*:*'
		print ('This is reference.')
	else:
		refStr = '*'
	print (refStr)

	#sel = mc.ls( '%s_ctrl' %refStr )

	sel = mc.ls('%s_ctrl' %refStr,'%s_gmbCtrl' %refStr)
	print (sel)
	for i in range( len(sel) ):

		name = sel[i]
		print ('Reset %s Ctrl Value to Zero.' %name)
		attr = 'tx','ty','tz','rx','ry','rz','sx','sy','sz'
		for a in range(len(attr)):
			attrName = name + '.' + attr[a]
			lock = mc.getAttr(attrName,l=1)
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
					mc.setAttr(attrName,0)

	# include condition for finger curl controller
	# noman edit

	curlBehav = ( 'fist' ,'roll' ,'relax' , 'spread')
	if reference :
		curlFinger = ('*:armStickRGT_ctrl' , '*:armStickLFT_ctrl')

		print (name)
		mc.select(name)
		nameSpace = misc.findNameSpace()


		for finger in curlFinger:
			for behav in curlBehav:
				if mc.objExists( nameSpace + finger + '.' + behav ):
					mc.setAttr( nameSpace + finger + '.' + behav, 0 )
	
	else:
		curlFinger = ('armStickRGT_ctrl' , 'armStickLFT_ctrl')
		print ('This is not reference.')

		for finger in curlFinger:
			for behav in curlBehav:
				print (finger + '.' + behav)
				if mc.objExists(   finger + '.' + behav ):
					
					mc.setAttr(  finger + '.' + behav, 0 )

		print ('Reset finger ....\n')

	mc.select(cl=True)
	print( "### RESET CTRL VALUE COMPLETE ###")



def boneCount():
	Sel = len(mc.ls(sl = True))
	if Sel == 0: # IF THIRE NO SELCTION
		if mc.joint('Root' , exists = True):
			mc.select('Root',hi=True)
			amountJnt = len(mc.ls(sl = True))
			amoutBindJnt = len(mc.ls('*bind_jnt'))
			numJnt = 'NUMBER OF JOINT >>> %d' %amountJnt
			bindJnt = 'BIND JOINT >>> %d' %amoutBindJnt
			mc.select(cl=True)
			print (numJnt)
			print (bindJnt)
		else:
			print ('No Object Select')
		
	else:
		mc.select(hi=True)
		amountJnt = len(mc.ls(sl = True))
		amoutBindJnt = len(mc.ls('*bind_jnt'))
		numJnt = 'NUMBER OF JOINT >>> %d' %amountJnt
		bindJnt = 'BIND JOINT >>> %d' %amoutBindJnt
		mc.select(cl=True)
		print (numJnt)
		print (bindJnt)
	


def twistNrbRig( nameSpace = '', stJnt = 'lowerArmLFT_bJnt', enJnt = 'handLFT_bJnt' , charScale = 1 ):

	# start with Name
	ns = nameSpace
	twist_grp = ns + 'twist_noTouch_grp'
	flc_grp = ns + 'twistFlc_grp'
	if mc.objExists( twist_grp ) == 0:
		dc.lock_grp( ns + 'twist_noTouch_grp' )
		dc.lock_grp( flc_grp )
		dc.hide( flc_grp )
		mc.parent( flc_grp, twist_grp )
		mc.parent( twist_grp, 'noTouch_grp' )

	# start here
	stName = stJnt.split('_')[0]
	print (stName)
	enName = enJnt.split('_')[0]
	print (enName)
	
	side = enName[-3:]
	print (side)

	preName = enName.split( side )[0]
	twName = preName + 'Twist' + side
	twJnt =  twName + '_bJnt' 
	# twist nrb
	nrb = twName + '_nrb'
	nrbSkin = core.Dag( nrb )
	mc.nurbsPlane( n = nrb, ch = False, v = 1, u = 4)
	dc.hide( nrb )
	mc.setAttr( nrb + '.ry', -90 )
	mc.setAttr( nrb + '.rx', 90 )
	mc.setAttr( nrb + '.ty', .5 )
	mc.makeIdentity( nrb, apply = True, t=1, r=1, s=1 )
	mc.makeIdentity( nrb, apply = False, t=1, r=1, s=1 )

	# MAT nrb to piorJnt
	dc.allMat( nrb, stJnt )
	mc.joint( n = twJnt )
	getScale = mc.getAttr( enJnt + '.ty' )
	mc.setAttr( nrb + '.sy', getScale )
	mc.makeIdentity( nrb, apply = True, t=1, r=1, s=1 )
	mc.parent( nrb, twist_grp )

	# nrb skinCluster
	stSkinJnt = core.Dag( stJnt )
	enSkinJnt = core.Dag( enJnt )
	nrb_skc = core.SkinCluster( stSkinJnt.name, enSkinJnt.name, nrbSkin.name, dr = 10 , mi = 2 )
	nrb_skc.name =  nrb + '_skc'


	flc = twName + '_flc'
	flcShp = flc + 'Shape'
	mc.createNode( 'follicle', n = flcShp )
	# flc
	mc.connectAttr( flcShp + '.outTranslate', flc + '.translate' )
	mc.connectAttr( flcShp + '.outRotate', flc + '.rotate' )
	# nrb
	mc.connectAttr( nrb + '.local' , flcShp + '.inputSurface' )
	mc.connectAttr( nrb + '.worldMatrix[0]' , flcShp + '.inputWorldMatrix' )
	# set
	mc.setAttr( flcShp + '.pv', 0.5 )
	mc.setAttr( flcShp + '.pu', 0.5 )

	dc.allMat( twJnt, flc)
	mc.makeIdentity( twJnt, apply = True, t=1, r=1, s=1 )
	dc.oriCon( flc, twJnt, mo = 1 )
	mc.parent( flc, flc_grp )
	mc.parent( twJnt, stJnt )

	#twistNrbRig( nameSpace = '', stJnt = 'lowerArmLFT_bJnt', enJnt = 'handLFT_bJnt' , charScale = 1 )
	#twistNrbRig( nameSpace = '', stJnt = 'lowerArmRGT_bJnt', enJnt = 'handRGT_bJnt' , charScale = 1 )


def twistRig( nameSpace = '', stJnt = 'lowerArmLFT_bJnt', enJnt = 'handLFT_bJnt' , charScale = 1 ):

	# start here
	stName = stJnt.split('_')[0]
	enName = enJnt.split('_')[0]
	side = enName[-3:]
	preName = enName.split( side )[0]
	twName = preName + 'Twist' + side
	twJnt =  twName + '_bJnt'
	twMdv = twName + '_mdv'

	# twJnt
	mc.joint( n = twJnt )
	dc.allMat( twJnt, stJnt )
	mc.parent( twJnt, stJnt )
	mc.makeIdentity( twJnt, apply = True, t=1, r=1, s=1 )

	# move
	enJntDist = mc.getAttr( enJnt + '.ty' )
	getDist = ( enJntDist/2 )
	mc.setAttr( twJnt + '.ty', getDist )

	# if rotate to match end joint
	dc.rotMat( twJnt, enJnt )
	mc.makeIdentity( twJnt, apply = True, t=1, r=1, s=1 )

	# link node and set
	mc.createNode( 'multiplyDivide' , n = twMdv )
	mc.connectAttr( enJnt + '.ry', twMdv + '.i1y' )
	mc.setAttr( twMdv + '.i2y', 0.5 )
	mc.connectAttr( twMdv + '.oy', twJnt + '.ry' )

	#twistRig( nameSpace = '', stJnt = 'lowerArmLFT_bJnt', enJnt = 'handLFT_bJnt' , charScale = 1 )
	#twistRig( nameSpace = '', stJnt = 'lowerArmRGT_bJnt', enJnt = 'handRGT_bJnt' , charScale = 1 )


# Armor_SWAP
def setupShowArmor(sex , digit , giveName  ):
	# NAME GIVING
	mainCtrl = 'nucleus_ctrl'
	giveType = 'helmet','chest','arms','hip','legs'
	enAttr = 'none:all:helmet:chest:arms:hip:legs'


	# Create Type List
	for n in range(len(giveName)):
		armorName = giveName
		mainAttr = mainCtrl + '.' + armorName
		name = sex + '_' + digit + '_' + giveName + '_1'
		set = name + '_set'
		ubCon = name + '_ub_con'
		lbCon = name + '_lb_con'
		colrFls = '.colorIfFalse.colorIfFalse'
		colrTru = '.colorIfTrue.colorIfTrue'
		colrOut = '.outColor.outColor'
		
		# add Attr
		mc.addAttr( mainCtrl, longName  = armorName, at = 'enum', keyable = True, en = enAttr)
		# Connect set Vis
		mc.connectAttr(mainAttr, set + '.v')

		# Create Node
		mc.createNode('condition', n = ubCon)
		mc.createNode('condition', n = lbCon)
		# Set Attr
		mc.setAttr(ubCon + '.secondTerm' ,1)
		mc.setAttr(lbCon + '.secondTerm' ,1)
		# Connect to Main
		mc.connectAttr(mainAttr, ubCon + '.firstTerm')
		mc.connectAttr(mainAttr, lbCon + '.firstTerm')

		for t in range(len(giveType)):
			type = giveType[t]
			armor = name + '_' + type
			amrCon = armor + '_con'
			count = t+2
			# Create and Set Node
			mc.createNode('condition', n = amrCon)
			mc.setAttr(amrCon + '.secondTerm', count)
			giveChanel = ('R','G','B')
			for a in range(len(giveChanel)):
				chanel = giveChanel[a]
				mc.setAttr(amrCon + colrTru + chanel,1)
				mc.setAttr(amrCon + colrFls + chanel,0)
			# Let Connect
			mc.connectAttr(mainAttr, amrCon + '.firstTerm')
			# IF is TYPE
			if t <= 2 :
				allCon = ubCon
				if t == 0:
					colr = 'R'
				elif t == 1:
					colr = 'G'
				elif t == 2:
					colr = 'B'
			elif t >= 3:
				allCon = lbCon
				if t == 3:
					colr = 'R'
				elif t == 4:
					colr = 'G'
			# Let Connect IN
			mc.setAttr(allCon + colrTru + colr, 1)
			# Let Connect OUT
			mc.connectAttr(amrCon + colrOut + 'R', allCon + colrFls + colr)
			mc.connectAttr(set + '.v', allCon + colrTru + colr)
			mc.connectAttr(allCon + colrOut + colr,armor + '.v')


#Armor_SWAP
def setupSelectedArmor():
	sel = mc.ls(sl = True)
	fullName = sel[0]
	nameList = fullName.split('_')
	sex = nameList[0]
	digit = nameList[1]
	giveName = nameList[2] + '_' + nameList[3]
	print (sex, digit, giveName)
	setupShowArmor(sex = sex, digit = digit, giveName = giveName )
	#setupShowArmor(sex = 'm', digit = '0070', giveName = 'evandria_var0' )
	#setupSelectedArmor()


# PH Export Armor
def exportSelArmor():
	ExportItem = mc.ls(sl=True)
	for i in range(len(ExportItem)):
		name = ExportItem[i]
		# Split by '_'
		sp = name.split('_')
		sex = sp[0]
		numName = sp[1] + '_' + sp[2]
		varNum = sp[3]
		catName = sp[5]
		if 'm' in sex[0]:
			gender = 'Male'
			
		if 'f' in sex[0]:
			gender = 'Female'
			
		mc.parent (ExportItem[i],w=True)
		mc.select(cl=True)
		mc.select('*Root', '*'+ name)
		# for SVN
		# D:\True_Axion\Project_HOPE\Content\3D_ART\Character\Player\f\Armor\0010_valiant\var0
		
		#filePath = 'D:/WORK/Hope/share/char/Player/' + gender + '/Export/' + numName + '/' + varNum + '/' # This Computer
		
		filePath = 'D:/True_Axion/Project_HOPE/Content/3D_ART/Character/Player/' + sex + '/Armor/' + numName + '/' + varNum + '/' # To SVN
		
		mc.select('*Root', name)
		sel = mc.ls(sl=True)
		fileName = sel[1]
		mc.file(filePath + fileName + '.fbx', f=True, op=('v=0'), typ='FBX export', pr=True, es = True)


# EH Export Outfit
def exportSelOutfit():
	items = mc.ls(sl=True)
	for s in range(len(items)):
	    # Find Name
	    giveName = items[s].split('_')
	    newName = giveName[1].split('0')
	    name = newName[0]
	    # ready for export
	    mc.parent(items[s],w=True)
	    mc.select(cl=True)
	    mc.select('*Root', items[s])
	    # file path
	    filePath = 'D:/True_Axion/Project_EVERGLEAM_HILL/3D_ART/Character/Player/clothes/' + name + '/fbx/' # To SVN
	    sel = mc.ls(sl=True)
	    fileName = items[s]
	    mc.file(filePath + fileName + '.fbx', f=True, op=('v=0'), typ='FBX export', pr=True, es = True)


# EH setup Outfit
def setupSelectedOutfit():
	#CLOTH SWAP With Click
	sel = mc.ls(sl=True)
	# NAME GIVING
	mainCtrl = 'char_ctrl'
	sepSel = sel[0].split('_')
	frontName = sepSel[0]
	endName = sepSel[1]

	#mc.listConnections('maleFace01_pma.input2D', destination = 0)
	#mc.attributeQuery('input2D[13].input2Dx', node = 'maleFace01_pma' , c =True)
	#mc.connectAttr('rev_01.output.outputX','maleFace01_pma.input2D[13].input2Dx' )

	if frontName == 'hat':
	    giveType = ['hat','ub','lb','fw']
	elif frontName == 'head':
	    giveType = ['head','ub','lb','fw']
	else:
	    print ('Please Select Head or Hat')
	    
	#giveName = ['assasin01'] # ADD NAME
	giveName = [endName] # SelectName
	enAttr = 'none:all:' + giveType[0] + ':ub:lb:fw'

	# Create Type List
	for n in range(len(giveName)):
	    name = giveName[n]
	    mainAttr = mainCtrl + '.' + name
	    set = 'cl_' + name
	    ubCon = name + '_ub_con'
	    lbCon = name + '_lb_con'
	    colrFls = '.colorIfFalse.colorIfFalse'
	    colrTru = '.colorIfTrue.colorIfTrue'
	    colrOut = '.outColor.outColor'
	    
	    # add Attr
	    mc.addAttr( mainCtrl, longName  = name, at = 'enum', keyable = True, en = enAttr)
	    # Connect set Vis
	    mc.connectAttr(mainAttr, set + '.v')
	    # Create Node
	    mc.createNode('condition', n = ubCon)
	    mc.createNode('condition', n = lbCon)
	    # Set Attr
	    mc.setAttr(ubCon + '.secondTerm' ,1)
	    mc.setAttr(lbCon + '.secondTerm' ,1)
	    # Connect to Main
	    mc.connectAttr(mainAttr, ubCon + '.firstTerm')
	    mc.connectAttr(mainAttr, lbCon + '.firstTerm')

	    for t in range(len(giveType)):
	        type = giveType[t]
	        armor =  type + '_' + name
	        amrCon = armor + '_con'
	        count = t+2
	        # Create and Set Node
	        mc.createNode('condition', n = amrCon)
	        mc.setAttr(amrCon + '.secondTerm', count)
	        giveChanel = ('R','G','B')
	        for a in range(len(giveChanel)):
	            chanel = giveChanel[a]
	            mc.setAttr(amrCon + colrTru + chanel,1)
	            mc.setAttr(amrCon + colrFls + chanel,0)
	        # Let Connect
	        mc.connectAttr(mainAttr, amrCon + '.firstTerm')
	        # IF is TYPE
	        if t <= 1 :
	            allCon = ubCon
	            if t == 0:
	                colr = 'R'
	            elif t == 1:
	                colr = 'G'
	            #elif t == 2:
	                #colr = 'B'
	        elif t >= 2:
	            allCon = lbCon
	            if t == 2:
	                colr = 'R'
	            elif t == 3:
	                colr = 'G'
	        # Let Connect IN
	        mc.setAttr(allCon + colrTru + colr, 1)
	        # Let Connect OUT
	        mc.connectAttr(amrCon + colrOut + 'R', allCon + colrFls + colr)
	        mc.connectAttr(set + '.v', allCon + colrTru + colr)
	        mc.connectAttr(allCon + colrOut + colr,armor + '.v')


# targetPov
def targetPov( ctrl = '', jnt = '' ):
	# name
	loc = ctrl + '_loc'
	ann = ctrl + '_ann'

	# create locator
	mc.spaceLocator( n = loc )
	#dc.hide( loc )
	mc.parent( loc, ctrl )
	dc.parCon( jnt, loc, mo = 0 )

	# create anno
	mc.annotate( loc, tx='', p=(0, 0, 0) )
	mc.rename( 'annotation1', ann )
	dc.allMat( ann, ctrl )
	mc.parent( ann, ctrl )
	dc.lock( ann )
	mc.setAttr( ann + '.ove', 1) # overrideEnabled
	mc.setAttr( ann + '.ovdt', 1) # overrideDisplayType

	# addAttr to Ctrl
	mc.addAttr( ctrl, sn = 'tgv' ,ln = 'targetVis', at = 'bool', dv = 1, k = True)
	mc.connectAttr( ctrl + '.tgv', ann + '.v' )

	# EXAMPLE
	#targetPov( ctrl = 'legLFT_pov_ctrl', jnt = 'lowerLegLFT_bind_jnt' )
	#targetPov( ctrl = 'legRGT_pov_ctrl', jnt = 'lowerLegRGT_bind_jnt' )
	#targetPov( ctrl = 'armLFT_pov_ctrl', jnt = 'lowerArmLFT_bind_jnt' )
	#targetPov( ctrl = 'armRGT_pov_ctrl', jnt = 'lowerArmRGT_bind_jnt' )

	mc.setAttr( loc + '.visibility', 0) 


def localWorldSel( ori = True ):
	if ori == True:
		style = True
	elif ori == False:
		style = False
	lcw.localWorld( fromSel = True, giveCtrl = [], ori = style, worldCtrl = 'ctrl_grp' )


def cogPivot( cog = 'cog_ctrl', cogZro = 'cogCtrlZro_grp', piorGrp = 'hipRig_grp', charScale = 1 ):

	# Snap null make for FK/IKmatcher
	cogPivot_grp = core.Null('cogPivot_grp' )
	# Create controller
	cogPivot_ctrl = core.Dag( 'cogPivot_ctrl'  )
	cogPivot_ctrl.nmCreateController( 'diamond_ctrlShape' )
	cogPivot_ctrl.editCtrlShape( axis = charScale*10 )
	#cogPivot_ctrl.renameShape( 'cogPivot_ctrl' )
	cogPivot_ctrl.setColor( 'yellow' )

	ctrl = cogPivot_ctrl.name
	grp = cogPivot_grp.name

	print (ctrl)
	print (grp)

	mc.parent( ctrl, grp )
	dc.allMat( grp, cog )
	mc.parent( grp, piorGrp )

	mc.connectAttr( ctrl + '.rotate', cogZro + '.rotate' )
	mc.connectAttr( ctrl + '.translate', cogZro + '.rotatePivot' )
	mc.connectAttr( ctrl + '.translate', cogZro + '.scalePivot' )


	ctrlShp = mc.listRelatives( cog, shapes = True)
	mc.addAttr(  ctrlShp[0], sn = 'cogpiv' ,ln = 'cogPivot', min = 0, max = 1, dv = 0, k = True )
	mc.connectAttr( ctrlShp[0] + '.cogPivot', grp + '.v' )