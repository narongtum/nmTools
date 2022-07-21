import maya.cmds as mc
import os

class Function:


	def _createTex ( self, name = '' ):

		file = name + '_file'
		mc.shadingNode( 'file', asTexture = True, isColorManaged = True, name = file )
		p2d = mc.shadingNode( 'place2dTexture', asUtility = True )
		
		mc.connectAttr( p2d + '.coverage', file + '.coverage', f = True )
		mc.connectAttr( p2d + '.translateFrame', file + '.translateFrame', f = True )
		mc.connectAttr( p2d + '.rotateFrame', file + '.rotateFrame', f = True )
		mc.connectAttr( p2d + '.mirrorU', file + '.mirrorU', f = True )
		mc.connectAttr( p2d + '.mirrorV', file + '.mirrorV', f = True )
		mc.connectAttr( p2d + '.stagger', file + '.stagger', f = True )
		mc.connectAttr( p2d + '.wrapU', file + '.wrapU', f = True )
		mc.connectAttr( p2d + '.wrapV', file + '.wrapV', f = True )
		mc.connectAttr( p2d + '.repeatUV', file + '.repeatUV', f = True )
		mc.connectAttr( p2d + '.offset', file + '.offset', f = True )
		mc.connectAttr( p2d + '.rotateUV', file + '.rotateUV', f = True )
		mc.connectAttr( p2d + '.noiseUV', file + '.noiseUV', f = True )
		mc.connectAttr( p2d + '.vertexUvOne', file + '.vertexUvOne', f = True )
		mc.connectAttr( p2d + '.vertexUvTwo', file + '.vertexUvTwo', f = True )
		mc.connectAttr( p2d + '.vertexUvThree', file + '.vertexUvThree', f = True )
		mc.connectAttr( p2d + '.vertexCameraOne', file + '.vertexCameraOne', f = True )
		mc.connectAttr( p2d + '.outUV', file + '.uv', f = True )
		mc.connectAttr( p2d + '.outUvFilterSize', file + '.uvFilterSize', f = True )

		return file



	def _createShdWithTexture( self, given_path, model ):
		norm_path = os.path.normpath( given_path)

		shd = model + '_shd'
		mat = model + '_mat'
		#file = model + '_file'

		mc.sets( renderable = True, noSurfaceShader = True, empty = True, name = shd )
		print shd
		mc.shadingNode( 'lambert', asShader = True, name = mat )
		print mat
		mc.connectAttr( mat + '.outColor', shd + '.surfaceShader', f = True )

		# create texture _file
		file = self._createTex( model )
		print file
		mc.connectAttr( file + '.outColor', mat + '.color', f = True )
		# assign shade #
		mc.sets( model, forceElement = shd )
		
		# assign path to _file
		try:
			if os.path.exists( norm_path ):
				print '\n...path found...'
				texture_path = norm_path + '\\' + model + '_Albedo.png'

				if os.path.exists( texture_path ):
					print '...texture found...'
					print texture_path
					mc.setAttr( file + '.fileTextureName',  texture_path, type = "string" )
		except :
			print '\n....Assign Path Texture Fail...'

		mc.select( cl = True )


	def _createShdFromSelected( self, given_path ):
		sel = mc.ls(sl=True)
		for model in sel:
			self._createShdWithTexture( given_path, model )
			print '...assign to %s...' % model

	def createShdCmd( self, *args ):
		pathString = mc.textField('pathField', tx = True, q = True )
		self._createShdFromSelected(  pathString )




class Ui:
	def __init__(self):
		self.Function = Function()

	def createGUI(self, *args):
		# Make a new window
		if mc.window('shdWin', exists = True):
			mc.deleteUI('shdWin')

		dWin = mc.window('shdWin', title="Create Shader From Select", iconName='css', widthHeight=(300, 100), s = True, mm = False, mxb = False, mw = False )
		
		mc.frameLayout( label='select model',collapsable=False, mw=5, mh=5 )
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 50), (2, 230)] )
		mc.text( label='Path :' )
		mc.textField('pathField', tx = '', h = 25 )

		mc.setParent("..")
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 300)])

		mc.text( label='  >>  paste texture path here  <<   ', h = 15)
		mc.text( label='' )
		mc.button( label='Create Shader From Model' ,w=100, h=30, c = self.Function.createShdCmd )
		mc.showWindow( dWin )
		

# Manual run
#run = Ui()
#run.createGUI()
