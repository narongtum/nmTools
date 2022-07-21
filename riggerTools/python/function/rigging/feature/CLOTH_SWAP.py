# Untimate CLOTH SWAP
# NAME GIVING
import maya.cmds as mc
mainCtrl = 'char_ctrl'
giveType = 'hat','ub','lb','fw'
#giveName = 'boy01','girl01','adventure01','alien01','astronaut01','ballerina01','cat01','cheerleader01','classy01','clown01','cowboy01','detective01','dinosaur01','generic01','generic02','generic03','generic04','knight01','maid01','plague01','princess01','rich01','robot01','vacation01','vampire01','victorian01','winter01'
giveName = ['unicorn01'] # ADD NAME
enAttr = 'none:all:hat:ub:lb:fw'

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



# select helper
'''
mc.select('maleFace01_pma',r=True)
mc.select(ubCon,r=True)
'''