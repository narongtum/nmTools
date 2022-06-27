import maya.cmds as mc
import pymel.core as pm
'''

from function.asset import assetTools as ast
reload(ast)

'''













def replaceTex():
# tools for autoplace texture by insert manual texture path
	
	texturePath = raw_input('place your new texture path:')
	fileNode = mc.ls(type='file') # list type 'file' in scene
	for f in fileNode: # loop for every fileNode
		mc.select(f,r=True)
		fullPaht = mc.getAttr('.fileTextureName')
		print fullPaht
		textureName = fullPaht.split('/')[-1]
		print textureName
		projectNewName = texturePath + '\\' + textureName 
		mc.setAttr('.fileTextureName' , projectNewName, type='string')



#####################################################
#       import and remove namespace              
#####################################################
def impRem():
	allrefs = pm.getReferences(recursive = True )
	for ref in allrefs:
		try:
			allrefs[ref].importContents( removeNamespace = True )
		except RuntimeError:
			pass
	print '\nImport and clear namespace ...'




# ========== # 
# shading
# ========== # 


def transferShade():
	sel = mc.ls( sl = True )
	mc.hyperShade( smn = True )
	refMat = mc.ls(sl=True)[0]

	for each in sel:
		if not each == sel[0]:

			mc.select( sel , r = True )
			mc.hyperShade( assign = refMat )
	mc.select(sel , r = True)