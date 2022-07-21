'''
from function.rigging.skin import copySkinFromRef as cpr
reload (cpr)

cpr.ui()

'''
from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc

from function.rigging import templateUi 
reload(templateUi)



def runUi():
	'''
	User interface for copy skin
	'''

	CopySkinUI()



class CopySkinUI(templateUi.templateUi):
	'''Inherited from MlUi
	morgan lumis
	'''

	def __init__(self):

		super(CopySkinUI, self).__init__('copySkinWeightsUi', 'copySkinWeights', width=400, height=120,info='')

		self.buildWindow()
		self.srcMeshField = self.selectionField(label='Source Mesh',
												annotation='Select source skin.',
												buttonLabel ='Set',
												text='')


		mc.button(label='Copy Skin',command = self.copySkin , annotation='Copy the Source Skin to selection.')

		self.finish()

		
	def copySkin(self,*args):
		# Get the variable
		sourceMesh = mc.textFieldButtonGrp(self.srcMeshField, query=True, text=True)

		if not sourceMesh:
			raise RuntimeError('Input a source mesh into the UI to copy skin from.')



		destinationMesh = mc.ls(sl=True)



		
		# sourceSkin = sourceMesh
		# destinationSkin = destinationMesh

		mc.select( sourceMesh,r=True )
		mc.select( destinationMesh,add=True )
		
		mc.copySkinWeights(
							noMirror=True,
						   surfaceAssociation='closestPoint',
						   influenceAssociation='closestJoint',
						   normalize=True)
		
		mc.select(deselect=True)
		



if __name__ == '__main__':
	ui()