# ========== # 
# move from rigging.misc
# ========== #

from function.rigging.constraint import normalConstraint as nmCon
reload(nmCon)


#####################################################
#      constraint pair between proxy joint and bind joint old(naming)               
#####################################################
def constraintProxyJnt( child = 'bind_jnt', parent = 'proxy_jnt' ):
	naming = '*_' + parent
	proxyList = mc.ls( naming )
	
	for each in proxyList:
		spEach = each.split('_')
		childNam = spEach[0] + '_' + child
		mc.parentConstraint( each , childNam , maintainOffset = True)
		mc.scaleConstraint( each , childNam , maintainOffset = True)



#####################################################
#      multiple constraint new condition           
#####################################################
def multipleCon( child = '*_bJnt', parent = '*Gmbl_ctrl' ):
	naming = '*_' + parent
	proxyList = mc.ls( naming )
	
	for each in proxyList:
		spEach = each.split('_')
		childNam = spEach[0] + '_' + child
		mc.parentConstraint( each , childNam , maintainOffset = True)
		mc.scaleConstraint( each , childNam , maintainOffset = True)

	print('DONE')





# ... constraint parent suffix name to bind suffix name

def constraintListJnt( namJntList = [] , child = 'ikJnt', parent = 'bJnt' ):
	namLst = []
	for each in namJntList:
		fitstNam = check_name_style(each)[0]
		namLst.append( fitstNam )

	
	for each in namLst:
		parentNam = each + '_' + parent
		childNam = each + '_' + child
		mc.parentConstraint( parentNam , childNam , maintainOffset = True , name = parentNam + '_psCon')
		mc.scaleConstraint( parentNam , childNam , maintainOffset = True , name = parentNam + '_scCon')

		print ('%s object has been create.' %each)