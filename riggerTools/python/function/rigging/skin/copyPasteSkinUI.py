'''
from function.rigging.skin import copyPasteSkinUI as cpu
reload(cpu)
'''

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc
import maya.mel as mel



class BuildUI:
	"""
	Class to build a simple UI for copying and pasting skin weights in Maya.
	"""
	
	# Constants for UI dimensions
	WINDOW_WIDTH = 200
	WINDOW_HEIGHT = 100

	def __init__(self):
		self.width = self.WINDOW_WIDTH
		self.height = self.WINDOW_HEIGHT
		self.ui = 'skinData'
		self.winID = f'{self.ui}Win'

	def show(self):
		"""
		Show the UI window. If the window already exists, delete it before creating a new one.
		"""
		print(self.winID)

		if mc.window(self.winID, exists=True):
			print('It already exists. Deleting it.')
			mc.deleteUI(self.winID)

		mc.window(self.winID, title=self.ui, widthHeight=(self.width, self.height), sizeable=False)
		mc.rowColumnLayout(numberOfColumns=2)
		mc.button(h=self.height, w=self.width*0.5, label="Copy Skinweight", command=self.click_copySkin, ann="Export mesh general data")
		mc.button(h=self.height, w=self.width*0.5, label="Paste Skinweight", command=self.click_pasteSkinJ, ann="Import joint into selected mesh (Just add no skin data.)")
		mc.showWindow()

	def click_copySkin(self, *args):
		"""
		Execute the MEL command to copy skin weights.
		"""
		try:
			mel.eval('artAttrSkinWeightCopy')
			print('Executed artAttrSkinWeightCopy')
		except Exception as e:
			print(f'Error executing artAttrSkinWeightCopy: {e}')

	def click_pasteSkinJ(self, *args):
		"""
		Execute the MEL command to paste skin weights.
		"""
		try:
			mel.eval('artAttrSkinWeightPaste')
			print('Executed artAttrSkinWeightPaste')
		except Exception as e:
			print(f'Error executing artAttrSkinWeightPaste: {e}')

# Example usage
# ui = BuildUI()
# ui.show()
