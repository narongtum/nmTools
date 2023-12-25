'''

from function.rigging.util import misc
reload(misc)


Can do
1. Make controller thicker

'''

# Reload module
from function.framework.reloadWrapper import reloadWrapper as reload


from function.rigging.util import generic_maya_dict as mnd
reload(mnd)


from function.pipeline import logger 

# logger.Mayalogger.MayaLogger.info('asdasdasd')







# set logging for debug mode
# import logging
# logger = logging.getLogger('debug_text')
# logger.setLevel(logging.DEBUG)
# logging.disable(logging.CRITICAL)


import maya.cmds as mc
import pymel.core as pm
import maya.OpenMaya as om
import re




MAYA_VERSION = mc.about(v=True)	
from function.rigging.util import generic_maya_dict as ext
reload(ext)


# from function.rigging.util import generic_maya_dict as mnd
# reload(mnd)

if MAYA_VERSION == '2022':
	import importlib
	# logger.MayaLogger.info('This is maybe maya 2022.')
	importlib.reload( ext )
	importlib.reload(logger)

elif MAYA_VERSION == '2018':
	# logger.MayaLogger.info('This is maybe maya 2018.')
	reload( ext )
	reload(logger)
else:
	# logger.MayaLogger.info('This is maybe maya 2018.')
	reload( ext )
	reload(logger)



# reload(ext)

# reload for maya 2022
# import importlib
# importlib.reload( ext )


# # # # # # # # # # # # # # # #
# ...  List hierarchy from selected in autodesk maya using python
# # # # # # # # # # # # # # # #

import maya.cmds as mc
import re

from function.rigging.util import generic_maya_dict as mnd

reload(mnd)


def setRotateOrder(rotateOrder='yzx'):
	# Get the parent selected objects only I will take care the rest
	selected = mc.ls(sl=True)

	# Loop through each selected object and list its children
	for obj in selected:
		children = mc.listRelatives(obj, allDescendents=True)

	# Define the regex pattern for *_ctrl
	pattern = r'^.*_ctrl$'

	ctrl_list = []

	for each in children:
		# Basic matching
		if re.search(pattern, each):
			print(f"String '{each}' ends with '_ctrl'")
			ctrl_list.append(each)

	# # # # # # # # # # # # # # # #
	# ... Select and set rotate order
	# # # # # # # # # # # # # # # #


	rot_dict = mnd.rotOrder_dict
	index = rot_dict[order]

	for each in ctrl_list:
		try:
			mc.setAttr('{}.rotateOrder'.format(each), index)
			print('Change rotate order to {0} complete.'.format(order))
		except:
			print(each)
			continue



def ctrlWidth(Width = 5):
	for each in mnd.controller_thicker_list:
		_makeCurveWidth(name = each , Width = Width)





def _makeCurveWidth(name = '', Width = 5):
	print(name)
	if mc.objExists(name):
		try:
			shapeCtrl = shapeName(name)
			mc.setAttr('{}.lineWidth'.format(shapeCtrl), Width)
			print('{} has expand curve width.'.format(name))
		except:
			pass
	else:
		print('{} not found.'.format(name))
			
			






#####################################################
#       multiple copyweight     
#####################################################

from function.rigging.skin import copySkinWeight as skw
reload(skw)

'''
from function.rigging.util import misc
reload(misc)
misc.mulWeight()
'''

# select source first
# then select destination 

def mulWeight():
	selection = mc.ls(sl=True)
	destination = selection[1:]
	source = selection[-1]
	#print 'source is %s, destination is %s' %selection,destination
	
	for each in destination:
		mc.select(source ,r=True)
		mc.select(each ,add=True)
		print ('%s has copied' %each)
		skw.copyWeight()








# renamd all locator in scene
# PROCEED WITH CUATION
def renameAllLocator(suffix='_tempLoc'):
	loc_list = mc.ls(type = 'locator')
	transformList = mc.listRelatives( loc_list, parent=True, fullPath = True )
	mc.select(transformList,r=True)
	reSuf(assetGrp = suffix)









def getShape(node,intermediate=False):
	"""
	[Ref] get from Chad Vernom at skin exporter tutorial
	get the shape from nodeType
	@param[in] name of transform or shape nodeType
	@paran[in] intermediate True to get the intermediate shape, False to get the visible shape.
	@return the name of the desired shape node
	"""
	if mc.nodeType(node) == 'transform':
		shapes = mc.listRelatives(node, shapes=True, path=True)
		if not shapes:
			shapes = []

		for shape in shapes:
			isIntermediate = mc.getAttr('%s.intermediateObject' %shape)
			# sometime there are left over intermediate shape that not used not
			# check the connections to make sure we get the one that is used
			# it not the shape we looking for
			if intermediate and isIntermediate and mc.listConnections(shape, source=False):
				return shape
			elif not intermediate and not isIntermediate:
				return shape

		if shapes:
			return shapes[0]

	elif cm.nodeType(node) in ['mesh' , 'nurbsCurve', 'nurvsSurface']:
		return node
	return None










	

	



# alway use so I move to core already
def makeHeader(funcName):
	print ('\n')
	print ('# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n')
	print ('\t\t\t\t\t%s\n' %funcName)
	print ('# # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n')


def _identifies( name ):
	''' ask what is node type return string '''
	isNode = mc.nodeType( name )
	if isNode == 'transform':
		# if transform node chek shapeNode 
		shape = shapeName( name )
		print (shape)
		isNode = mc.nodeType( shape )
	return isNode



def findLastName(name):
	lastname = name.split('_')[1]
	if lastname:
		return lastname
	else:
		return None


def findRawName(name):
	parts = name.split('_')
	rawName = '_'.join(parts[:-1])
	return rawName



def rawName(name): #... not good leave it behide
	lastname = name.split('_')
	if len(lastname) == 2:
		return lastname[0], lastname[1]
	else:
		return lastname

def findSide( selection ):
	side = ''
	if '_' in selection:
		spText = selection.split('_')[0]
		if spText.endswith('LFT'):
			side = 'LFT'
		elif spText.endswith('RGT'):
			side = 'RGT'
		else:
			side = ''

		print ('This is %s' %side)
		return side
	else:
		mc.warning('There are no underscore.')
		return False

# not work I dunno why
def removeSide(name):
	if findSide(name):
		side = findSide(name)
		index = name.index(side)
		return (name[:index])
	else:
		print('There is no side to splite.')
		return False



def _findExtension(name):
	''' adding maya lastname string '''

	nodeDict = ext.NODE_dict
	nodeType = str(_identifies(name))

	print ('nodeType is %s' %nodeType)
	print (type(nodeType).__name__)

	node_exp = []
	if nodeType == 'None':
		

		for each in nodeDict:

			if each['longName'] == 'group':
				node_exp = each['shortName']
				break
			else:
				node_exp = 'unknown'
				continue


	elif nodeType:
	# for naming null group route
		for each in nodeDict:
			# for rest of node naming route
			if each['longName'] == nodeType:
				node_exp = each['shortName']

				# if found break the loop
				break
			else:
				node_exp = 'unknown'
				continue
	 

	
	# print ('This is shortName	:' +  node_exp)
	return node_exp



def autoSuffix( name ):
	# check if string or list or unicdoe
	if type(name).__name__ == 'unicode' or type(name).__name__ == 'str':
		# if string make it to list
		namList = [ name ]
	elif type(name).__name__ == 'list':
		namList = name

	print (namList)


	for each in namList:
		# convert unicode to ascii
		each = each.encode('ascii')

		if MAYA_VERSION == '2022' or MAYA_VERSION == '2023':
			each = each.decode('utf-8')
		
		lastname = _findExtension(each)
		print ('this is suffix name: %s' %lastname)

		# if object already last name
		if each.endswith( lastname ):
			print ('This is already last name it will skip.\n')
			continue
		else:
			newNam = mc.rename( each  , each +'_'+ lastname )
			print ('%s object has been rename' %newNam)
		

def selAutoSuffix():
	''' just select and run '''
	selection = mc.ls(sl=True)
	if selection:
		autoSuffix( selection )
	else:
		mc.warning('Please select something.')

	'''
	totalObj = len(selection)
	for index , each in enumerate(selection):
		mc.rename(each ,assetGrp + selection[index] )
	print '%s object has been rename' %totalObj'''


	'''
	for each in nodeDict:
		if each["longName"] == nodeType:

			node_exp = each["shortName"]
		else:
			node_exp = 'something'
			print 'This is longname :  ' + each["longName"]




	print node_exp
	return node_exp'''
	
		

















# from jh_ribbon
# used keyword arg because it aceppt arg of addAttr
def addAttribute(objects = [] , longName = '' , niceName = '' , lock = False, **kwargs ):
	for obj in objects:
		# For each attribure if have many attr such as twist,roll
		for each in range(0, len(longName)):
			# if nicename was defined
			attrNice = '' if not niceName else niceName[each]

			#if the attribute does not exists
			if not mc.attributeQuery(longName[each], node = obj , exists = True ):
				mc.addAttr( obj, longName = longName[each], niceName = attrNice  ,**kwargs)
				# if lock was set to true
				mc.setAttr( obj+'.'+longName[each] , lock = 1) if lock else mc.setAttr(obj+'.'+longName[each] , lock = 0 )





# Hide arnold node Must select curve first
def hideArnoldNode( attr = ['rcurve' ,' cwdth' , 'srate' , 'ai_curve_shaderr' ,'ai_curve_shaderg' , 'ai_curve_shaderb' ]  , ctrlName = None):
	if ctrlName == None:
		logger.MayaLogger.info('This is selection curve.')
		ctrlName = mc.ls(sl = True)
		shape = shapeName( ctrlName )
		for each in attr:
			mc.setAttr( shape + '.' + each , keyable = False ,  channelBox = False )

	elif ctrlName:
		logger.MayaLogger.info('This is using specify name curve.')
		shape = shapeName( ctrlName )
		for each in attr:
			mc.setAttr( shape + '.' + each , keyable = False ,  channelBox = False )




# Return shapeName 
def shapeName(ctrl):
	try:
		ctrlShape = mc.listRelatives( ctrl , s = True )[ 0 ]
		return ctrlShape
	except:
		pass

		

# Find if selet object are reference or not
def isRef(name=''):
	
	if ':' in name:
		return True
	else:
		return False

# Convert selection to vertex
def creJntAtVertex():
	mc.select( mc.polyListComponentConversion( tv = True) )
	cluster = mc.cluster( relative = True, envelope = 1.0 )
	mc.select( clear = True )
	joint = mc.joint( scaleCompensate = False )
	snapPointConst(cluster[1], joint)
	mc.delete(cluster)


# Removing selected reference from the scene
def removeSelectedReference() :

	sels = mc.ls( sl=True )
	
	for sel in sels :
		
		if mc.objExists( sel ) and mc.referenceQuery( sel , isNodeReferenced=True ) :
			
			refNode = mc.referenceQuery( sel , referenceNode=True )
			fileName = mc.referenceQuery( refNode , filename=True )
			mc.file( fileName , rr=True )


def findNameSpace():
	nameSpace = pm.selected()[0].namespace()
	return nameSpace







def lockAndHide ( node, lock = True, hide = True, visibility = False):
	'''
	Lock and Hide the attribute of node.
	
	Param :
	node = DAG node
	lock = Boolean
	hide = Boolean
	visibility = Boolean
	'''
	if not visibility :
		for attr in node.listAttr(keyable=True) :
			if not "visibility" in str(attr) :
				if lock :
					attr.lock()
				if hide :
					attr.setKeyable(False)
	else :
		for attr in node.listAttr(keyable=True) :
			if lock :
				attr.lock()
			if hide :
				attr.setKeyable(False)
				
def unlockAndUnhide (nodeList=[]):
	'''
	Unlock and Unhide the classic keyable attribute of the selected nodes.
	
	Param :
	nodeList
	'''
	for node in nodeList :
		for attribute in ['tx','ty','tz','rx','ry','rz','sx','sy','sz','visibility'] :
			node.attr(attribute).unlock()
			node.attr(attribute).setKeyable(True)
				
def listWorldChildren ():
	'''
	Return the transform node at the root of the hierarchy.
	
	Return :
	worldChildrenList = List
	'''
	worldChildrenList = list()
	for elem in pm.ls(assemblies=True) :
		if pm.nodeType(elem) == 'transform' :
			worldChildrenList.append(elem)
	return worldChildrenList


def getTimelineFrameRange():
	'''
	Return the timeline frame range of the scene
	
	Return :
	startFrame = int
	endFrame = int
	'''
	startFrame = pm.playbackOptions (q=True,minTime =True)
	endFrame = pm.playbackOptions (q=True,maxTime =True)
	return startFrame,endFrame

def listNotUniqueName ( batch = False ):
	'''
	Return a list of the nodes that don't have a unique name
	'''
	notUniqueNameList = list()
	for node in pm.ls() :
		if '|' in str(node) :
			notUniqueNameList.append(node)
			
	if len(notUniqueNameList) == 0 :
		logger.MayaLogger.info('All Nodes name OK')
	else :
		for node in notUniqueNameList :
			print (node)
	return notUniqueNameList

def deleteUnknownNode ():
	'''
	Delete unknown Nodes.
	'''
	for unknownNode in pm.ls(type='unknown') :
		try :
			deletedNodeName = str(unknownNode)
			pm.delete(unknownNode)
			logger.MayaLogger.info('Delete :', deletedNodeName)
		except :
			try:
				pm.lockNode(l=False)
				deletedNodeName = str(unknownNode)
				pm.delete(unknownNode)
				logger.MayaLogger.info('Delete :', deletedNodeName)
			except:
				traceback.print_exc()
			else:
				pass
		
def getTopGNodeList ():
	'''
	Return the gAsset Node and the gShotNode at the top of the hierarchy
	'''
	topGNodeList = list()
	for node in pm.ls(assemblies=True):
		if node.nodeType() == 'gAsset' or node.nodeType() == 'gShot' :
			topGNodeList.append(node)
	return topGNodeList
		

def getMayaWindow():
	#Get the maya main window as a QMainWindow instance
	ptr = mui.MQtUtil.mainWindow()
	return sip.wrapinstance(long(ptr), QtCore.QObject)


def selectCharAllControl ( nameSpace = False , addToSelection = False ) :
	pm.select( cl = True )
	
	# Select all the controler of a character.
	if not nameSpace:
		try:
			pm.select('*_ctrl')
		except:
			pass
	else:
		try :
			pm.select('%s:*_ctrl'%nameSpace)
		except :
			pass

	if addToSelection:	
		try :
			pm.select('%s:*_ctrl'%nameSpace, tgl = True)
		except :
			pass





	'''
	if not addToSelection :
		
		try :
			pm.select('%s:*ctrl'%nameSpace)
		except :
			pass
	else :
		try :
			pm.select('%s:*CD'%nameSpace, tgl = True)
		except :
			pass'''
	

		




# separate LFT and RGT
# input from splitName



# split name with underscore return to list
# Return: list of splite objectname
def splitName( name = '' ):

	newName = []
	newName = name.split('_')
	return newName



# count the specify node default is joint
# Return: list of the joints in the fk chain)
def countNode(Nodetype = "joint"):
	
	allJnt = mc.ls(type = Nodetype)
	i = 0
	for each in allJnt:
		i = i + 1
	print ("\n#####")
	print ("Number of all Joint is: %s" %i)

	bindJnt = mc.ls('*_bind_jnt')
	num = 0
	for bind in bindJnt:
		num = num + 1

	print ("Number of bind Joint is: %s" %num)



#####################################################
#      delete  constraint  snapParentCon snapScaleCon                      
#####################################################
# parent  and child
def snapParentConst( parent , child ):
	mc.delete(	mc.parentConstraint( parent ,child ,maintainOffset = False) )
def snapScaleConst( parent , child ):
	mc.delete(	mc.scaleConstraint( parent ,child ,maintainOffset = False)	)
def snapPointConst( parent , child ):
	mc.delete(	mc.pointConstraint( parent ,child ,maintainOffset = False)	)
def orientConst( parent , child ):
	mc.delete(	mc.pointConstraint( parent ,child ,maintainOffset = False)	)






#####################################################
#      remain  constraint  snapParentCon snapScaleCon                      
#####################################################
def snapParentConstrMo( source,target ):
	mc.parentConstraint( source ,target , maintainOffset = True) 






#####################################################
#      remain  constraint  snapParentCon snapScaleCon                      
#####################################################
def snapParentConstr( source, target , **kwargs ):
	mc.parentConstraint( source ,target  ) 
def snapScaleConstr( source, target , **kwargs ):
	mc.scaleConstraint( source ,target )	
def snapPointConstr( source, target , **kwargs  ):
	mc.pointConstraint( source ,target )	
def orientConstr( source, target , **kwargs  ):
	mc.pointConstraint( source ,target )	






###############################                      
#        snapTools            #
###############################


# obselet this use  maya matchTransform function insted
'''
def pointCon():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]
	pct = mc.pointConstraint(src,tgt, mo = False)
	mc.delete(pct)
'''
def pointCon():
	sel = mc.ls(sl = True)
	src = sel[0]
	tgt = sel[1]
	mc.matchTransform( tgt , src, position = True, rotation = False, scale = False )






# obselet this use  maya matchTransform function insted
'''
def orientCon():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]
	pct = mc.orientConstraint(src,tgt, mo = False)
	mc.delete(pct)
'''
def orientCon():
	sel = mc.ls(sl = True)
	src = sel[0]
	tgt = sel[1]
	mc.matchTransform( tgt , src, position = False, rotation = True, scale = False )







# obselet this use  maya matchTransform function insted
'''
def parentCon():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]
	pct = mc.parentConstraint(src,tgt, mo = False)
	mc.delete(pct)
'''

# snap prosition in include scale
def parentCon():
	sel = mc.ls(sl = True)
	src = sel[0]
	tgt = sel[1]
	mc.matchTransform( tgt , src, position = True, rotation = True, scale = False )




def scaleCon():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]
	mc.delete(mc.parentConstraint(src,tgt, mo = False))
	mc.delete(mc.scaleConstraint(src,tgt, mo = False))

# snap for key frame object	
def snapMat():
	sel = mc.ls(sl=True)
	src = sel[0]
	tgt = sel[1]

	srcMatrix = mc.xform( src, query=True, worldSpace=True, matrix=True )
	mc.xform( tgt, worldSpace=True, matrix = srcMatrix )





def snapMatArg( source , target ):
	srcMatrix = mc.xform( source, query = True , worldSpace = True , matrix = True )
	mc.xform( target, worldSpace = True, matrix = srcMatrix )



#####################################################
#       snapParentCon snapScaleCon     delete contsraint                     
#####################################################
def selected():
	selected = mc.ls(sl=True)
	source = selected[0]
	destination = selected[1]
	return source,destination



#####################################################
#      remain  constraint  snapParentCon snapScaleCon  with no mo                    
#####################################################
def snapParentCon(source,target):
	mc.delete(  mc.parentConstraint( source ,target , maintainOffset = False))
	mc.delete(  mc.scaleConstraint( source ,target , maintainOffset = False))

def snapScaleCon(source ,target):
	mc.delete(  mc.scaleConstraint( source ,target , maintainOffset = False))

def snapPointCon(source ,target):
	mc.delete(  mc.pointConstraint( source ,target , maintainOffset = False))  




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




#... constraint parent suffix name to bind suffix name
def constraintListJnt( namJntList = [] , child = 'ikJnt', parent = 'bJnt' ):
	namLst = []
	for each in namJntList:
		fitstNam = splitName( each )[0]
		namLst.append( fitstNam )

	
	for each in namLst:
		parentNam = each + '_' + parent
		childNam = each + '_' + child
		mc.parentConstraint( parentNam , childNam , maintainOffset = True , name = parentNam + '_psCon')
		mc.scaleConstraint( parentNam , childNam , maintainOffset = True , name = parentNam + '_scCon')

		print ('%s object has been create.' %each)





# ========== # 
# edit text add prefix and suffix
# ========== # 
def searchReplace( searchText='', replaceText='' ):
	nameLst = []
	obj = pm.selected()
	for item in obj:
		item.rename(item.name().replace(searchText, replaceText))
		nameLst.append(item.name())
	return nameLst

	'''

	selection = mc.ls(sl=True) # list selcection
	if len(selection) > 0: # check if only one selection
		for each in selection:  # iteration in each selection
			newName = each.replace(searchText, replaceText) # used string method 'replace' and assign to newName
			mc.rename(each, newName) # rename in each old name to new name
	'''

def reSuf(assetGrp=None):
	''' add suffix '''
	selection = mc.ls(selection = True)
	if selection:
		totalObj = len(selection)
		for index , each in enumerate(selection):
			mc.rename(each , selection[index] + assetGrp )
		print ('%s object has been rename' %totalObj)
	else:
		mc.error('Please select something first!.')	

def rePre(assetGrp=None):
	selection = mc.ls(selection = True)
	if selection:
	
		totalObj = len(selection)
		for index , each in enumerate(selection):
			mc.rename(each ,assetGrp + selection[index] )
		print ('%s object has been rename' %totalObj)
	else:
		mc.error('Please select something first!.')


def reNumber(*args):
	selection = mc.ls(selection = True)
	#newName = mc.textField('tfRename',q=True,tx=True)
	#num = mc.intField('ifNumber',q=True,v=True)
	#padding = mc.intField('ifPadding',q=True,v=True)

	for index , each in enumerate(selection):
		mc.rename(each , newName + str(num).zfill(int(padding)) )
		num = num+1



def reName(newName,num,padding):
	selection = mc.ls(selection = True)

	for index , each in enumerate(selection):
		mc.rename(each , newName + str(num).zfill(int(padding)) )
		num = num+1


def printSomething(someOne=''):
	return someOne












###############################                      
#                             #
#   multiple constraint          #
#                             #
############################### 

# select  child
# select  parent
def mpCon():
	''' multiple child with one parent '''
	const = mc.ls(sl=True)
	i=1
	lenConst = len(const)
	for each in const:
		if len(const) != i:
			mc.parentConstraint( const[0], const[i], mo=True, w=1.0)
			mc.scaleConstraint( const[0], const[i], mo=True, w=1.0)
			i=i+1

'''
					   
#   ########################                                        
#   replaceTexture texture file         
#  ##########################                                        
   
def replaceTexure():
# tools for autoplace texture by insert manual texture path
	texturePath = raw_input('place your new texture path :') + '\\'
	fileNode = mc.ls(type='file') # list type 'file' in scene
	for f in fileNode: # loop for every fileNode
		mc.select(f,r=True)
		fullPaht = mc.getAttr('.fileTextureName')
		print fullPaht
		textureName = fullPaht.split('/')[-1]
		print textureName
		projectNewName = texturePath + textureName 
		mc.setAttr('.fileTextureName' , projectNewName, type='string')
'''	







def getDagPath(node=None):
	sel = om.MSelectionList()
	sel.add(node)
	dagPath = om.MDagPath()
	sel.getDagPath(0, dagPath)
	return dagPath

def getLocalOffset(parent, child):
	
	parentWorldMatrix = getDagPath(parent).inclusiveMatrix()
	childWorldMatrix = getDagPath(child).inclusiveMatrix()
	# child World Matrix * invert parent World Matrix = child local matrix
	# return child local matrix
	return childWorldMatrix * parentWorldMatrix.inverse()
   

def rotateOffset(tgt, dmpMtx, mulMtx):
	# TODO: Check euler to quad is enable
	if not mc.pluginInfo('quatNodes', query=True, loaded=True):
		mc.loadPlugin("quatNodes", qt=False)



	# Create name 
	eulQua = tgt + '_eulQua'
	quaInv = tgt + '_quaInv'
	quaPro = tgt + '_quaPro'
	quaEul = tgt + '_quaEul'
	# Add compose matrix
	quaCom = tgt + '_compose'

	# Create More Node
	mc.createNode( 'eulerToQuat', n = eulQua )
	mc.createNode( 'quatInvert', n = quaInv )
	mc.createNode( 'quatProd', n = quaPro )
	mc.createNode( 'quatToEuler', n = quaEul )

	mc.createNode( 'composeMatrix', n = quaCom )# Add compose matrix for get offset orientation


	# Rotate Part
	# Add condition for another type except joint
	logger.MayaLogger.info(tgt)
	if mc.nodeType(tgt) == 'joint':
		logger.MayaLogger.info("This is maybe joint.")
		mc.connectAttr( tgt + '.jointOrient', eulQua + '.inputRotate' )
	elif mc.nodeType(tgt) == 'transform':
		logger.MayaLogger.info("This is maybe mesh or group.")

		# Update more arttr for case joint(freezed) is parent grp is child
		mc.connectAttr('{0}.rotate'.format(tgt) ,'{0}.inputRotate'.format(quaCom), f = True) # Add rotation value from driven
		mc.disconnectAttr('{0}.rotate'.format(tgt) ,'{0}.inputRotate'.format(quaCom)) # No need to keep thr connection the value already add to channel 
		mc.connectAttr('{0}.outputMatrix'.format(quaCom), '{0}.matrixIn[0]'.format(mulMtx)) # Connect rotation space to the MulMtx

		mc.connectAttr( tgt + '.rotate', eulQua + '.inputRotate' )


	else:
		logger.MayaLogger.info("This is maybe something I don't know.")
		mc.connectAttr( tgt + '.rotate', eulQua + '.inputRotate' )

	mc.connectAttr( eulQua + '.outputQuat', quaInv + '.inputQuat' )
	mc.connectAttr( dmpMtx + '.outputQuat', quaPro + '.input1Quat' )

	# get Inverse Quat from Child Rotate Order
	mc.connectAttr( quaInv + '.outputQuat', quaPro + '.input2Quat' )
	mc.connectAttr( quaPro + '.outputQuat', quaEul + '.inputQuat' )

	# get Rotate Order for quaEul
	rotOrder = mc.getAttr( tgt + '.rotateOrder' )
	mc.setAttr( quaEul + '.inputRotateOrder', rotOrder)
	
	allChanel = ['X','Y','Z','W']
	for chanel in allChanel:
		quaVar = mc.getAttr( quaInv + '.outputQuat.outputQuat' + chanel )
		mc.setAttr( quaPro + '.input2Quat.input2Quat' + chanel )

	# Clear Node
	mc.delete( eulQua )

	# Final Connect
	mc.connectAttr( quaEul + '.outputRotate', tgt + '.rotate')

	return quaEul




				


def parentMatrix( src, tgt, mo = True, translate = True, rotate = True, scale = True):

	# This is Outdate the latest is in function.rigging.constraint
	# Add Another version at rigging.constraint
	# TODO : connectAttr -force head_gmbCtrl.rotateOrder head_bJnt_quaEul.inputRotateOrder;  connect rotate order

	"""Alternate of constraint using matrix insted

	Args:
		src: source.
		tgt: target.
		mo: maintain offset.
		t: translate.
		r: rotate.
		s: scale.

	Returns:
		None

	"""



	logger.MayaLogger.info('Start of %s module' %__name__)

	# Create Name
	print (tgt)
	print (type(tgt))
	print (src)
	print (type(src))

	mulMtx = '{0}_mulMtx'.format(tgt)
	dmpMtx = '{0}_dmpMtx'.format(tgt)

	# FUNC
	# got call maya API for get object 
	localOffset =  getLocalOffset( src, tgt )

	offMat = [localOffset(i,j) for i in range(4) for j in range(4)]
	
	# Create
	mc.createNode( 'multMatrix', n = mulMtx )
	mc.createNode( 'decomposeMatrix', n = dmpMtx )
	#  Set and Connect
	if mo == True:
		mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')

	print(type(src))
	mc.connectAttr( '{0}.worldMatrix[0]'.format(src) , '{0}.matrixIn[1]'.format(mulMtx) )
	
	#  Find out Origin Parent
	if mc.pickWalk( tgt , d = 'up')[0] == tgt:
		logger.MayaLogger.info("I'm World Already")
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[2]' )

	# Fist Connect
	mc.setAttr( mulMtx + '.matrixIn[0]', offMat , type = 'matrix')
	
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	if rotate == True:
		quaEul_name = rotateOffset(tgt, dmpMtx, mulMtx)
		# Connnect rotate order for prevent cause error
		mc.connectAttr('{0}.rotateOrder'.format(src), '{0}.inputRotateOrder'.format(quaEul_name))
	# Final Connect
	if translate == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if scale == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale')


	mc.select(tgt, r=True)


	print (' # # # # # # # # #  Matrix parent complete # # # # # # # # # # # #  \n')


def del_sel_matrix(selected = []):
	#... Get short name
	mulMtx = mnd.get_short_name('multMatrix')
	quat = mnd.get_short_name('quatToEuler')
	deComp = mnd.get_short_name('decomposeMatrix')

	for each in selected:
		list_sel = mc.listConnections(each, destination=True)

		for each in list_sel:
			try:
				# .. because after delete it will can't find the rest
				# if each.endswith('_dmpMtx'):
					# logger.MayaLogger.info('Delete %s' %each)
					# mc.delete(each)
				if each.endswith(mulMtx):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)
				if each.endswith(quat):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)
				if each.endswith(deComp):
					logger.MayaLogger.info('Delete %s' %each)
					mc.delete(each)

			except:
				print('There are no matrix node to delete.')
	print('Delete Done...')


def delMatrixConst(selected):
	name = rawName(selected)
	mc.delete('{0}_bJnt_mulMtx'.format(name[0]))
	print (' # # # # # # # # #  Delete matrix parent complete # # # # # # # # # # # #  \n')






# misc.parentSufficMatrix( child = 'bJnt' , parent = 'pxyJnt' , mo = True, w = 1, t = True, r = True, s = True )
def parentSufficMatrix( child = '' , parent = '' , mo = True, w = 1, t = True, r = True, s = True):
	logger.MayaLogger.info('Start of %s module' %__name__)
	# constraint use prefix suffix only #
	naming = '*_' + parent
	proxyList = mc.ls( naming )

	for each in proxyList:
		spEach = each.split('_')
		childNam = spEach[0] + '_' + child
		parentMatrix( each , childNam, mo = mo, translate = t, rotate = r, scale = s)
		print ('parent %s >>> %s' %(each , childNam))

	print ('\t\t\t### constraint matrix complete ###')

# parent multi martix
def parentMulMatrix( src, tgt, mo = True, t = True, r = True, s = True):
	''' parent constraint one source but multiple target matrix'''
	
	# Name
	mulMtx = tgt + '_mulMtx'
	dmpMtx = tgt + '_dmpMtx'
	wtMtx = tgt + '_wtMtx'

	# Create
	mc.createNode( 'multMatrix', n = mulMtx )
	mc.createNode( 'decomposeMatrix', n = dmpMtx )
	mc.createNode( 'wtAddMatrix', n = wtMtx )

	# For many parent
	for p in range(len(src)):
		parent = src[p]
		#parentName = parent.split('_')[0]
		offsetMtx = tgt + '_' + parent + 'Offset_mulMtx'

		# Create
		mc.createNode( 'multMatrix', n = offsetMtx )

		# preFUNC
		localOffset =  getLocalOffset( parent, tgt )
		offMat = [localOffset(i,j) for i in range(4) for j in range(4)]

		#  Set and Connect
		if mo == True:

			mc.setAttr( offsetMtx + '.matrixIn[0]', offMat , type = 'matrix')

		mc.connectAttr( parent + '.worldMatrix[0]', offsetMtx + '.matrixIn[1]' )
		mc.connectAttr( offsetMtx + '.matrixSum', wtMtx + '.wtMatrix[%d].matrixIn'%(p))
		if p == 0:
			mc.setAttr( wtMtx + '.wtMatrix[%d].weightIn'%(p), 1)


	# Main wt connect
	mc.connectAttr( wtMtx + '.matrixSum',  mulMtx + '.matrixIn[0]' )

	# Find out Origin Parent
	if mc.pickWalk( tgt , d = 'up')[0] == tgt:
		print ("I'm World Already")
	elif mc.pickWalk( tgt, d = 'up')[0] != tgt:
		world = mc.pickWalk( tgt, d = 'up')[0]
		mc.connectAttr( world + '.worldInverseMatrix[0]', mulMtx + '.matrixIn[1]' )

	# Final Connect
	mc.connectAttr( mulMtx + '.matrixSum', dmpMtx + '.inputMatrix' )
	# 
	if r == True:
		rotateOffset(tgt, dmpMtx, mulMtx)
	if t == True:
		mc.connectAttr( dmpMtx + '.outputTranslate', tgt + '.translate')
	if s == True:
		mc.connectAttr( dmpMtx + '.outputScale', tgt + '.scale') 
	
	return wtMtx


# ex: parentThis()
def parentThis( mo = True, t = True, r = True, s = True):
	''' select source and targer '''
	sel = mc.ls(sl=1)
	if len(sel) > 2:
		child = sel[-1]        
		del sel[-1]
		parentMulMatrix( src = sel , tgt = child,  mo = mo, t = t, r = r, s = s)
		print (sel)
	elif len(sel) == 2:
		print (sel)
		parentMatrix( sel[0] , sel[-1],  mo = mo, t = t, r = r, s = s)





