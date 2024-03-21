from function.framework.reloadWrapper import reloadWrapper as reload


'''
from function.rigging.readWriteCtrlSizeData import flipController as fip
reload(fip)
'''
import maya.cmds as mc
from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)






def run():
	ui = buildUI()
	ui.show()



class buildUI():
	def __init__(self):
		print ('initiation building UI')
		self.widt = 750
		self.ui = 'TAI shapeTools'
		self.win = '%sWin' % self.ui

	def show(self):

		if mc.window(self.win, exists=True):
			mc.deleteUI(self.win)
		  
		mc.window( self.win, width = self.widt , widthHeight=(200, 110) )
		mc.columnLayout( adjustableColumn = True )
		mc.button( label = 'Copy ControllerShape ' , command = self.copyCtrlShape , ann = "Select source and destination.")
		mc.button( label = 'Flip ControllerX'   	,	command = self.flipCtrlShapeX , ann = "click object and click the button")
		mc.button( label = 'Flip ControllerY'   	,	command = self.flipCtrlShapeY , ann = "click object and click the button")
		mc.button( label = 'Flip ControllerZ'   	,	command = self.flipCtrlShapeZ , ann = "click object and click the button")


		mc.showWindow()





	def flipCtrlShapeX( self , sel , axis = [ 1, -1, -1 ] ):
		sel = mc.ls(sl=True)
		print ('flip axis is %s' %axis)
		shapes = wcd.getShape(sel[0])	
		newShapes = []

		for i, each in enumerate(shapes["points"]):
			shapes["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
		newShapes.append(shapes)

		mc.curve( sel , replace = True,p=newShapes[0]["points"], k=newShapes[0]["knots"], d=newShapes[0]["degree"], per=bool(newShapes[0]["form"]) )




	# flip controller

	def flipCtrlShapeY( self , sel , axis = [-1, -1, 1] ):
		sel = mc.ls(sl=True)
		print ('flip axis is %s' %axis)
		shapes = wcd.getShape(sel[0])	
		newShapes = []


		for i, each in enumerate(shapes["points"]):
			shapes["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
		newShapes.append(shapes)
		# this is mean
		# for each number of joint [i] 1,2,3,4,5,..... number of point
		# for each is value ( -0.12 3.93, 12.53 )
		# that mean make this multiply with -1
		# and append that to new shape

		# specifiy the shape that u went to make
		# wcd.setShape(sel[0], newShapes)

		mc.curve( sel , replace = True,p=newShapes[0]["points"], k=newShapes[0]["knots"], d=newShapes[0]["degree"], per=bool(newShapes[0]["form"]) )


	

	def flipCtrlShapeZ( self , sel , axis = [ -1, 1, -1 ] ):
		sel = mc.ls(sl=True)
		print ('flip axis is %s' %axis)
		shapes = wcd.getShape(sel[0])	
		newShapes = []


		for i, each in enumerate(shapes["points"]):
			shapes["points"][i] = [each[0] * axis[0], each[1] * axis[1], each[2] * axis[2]]
		newShapes.append(shapes)

		# wcd.setShape(sel[0], newShapes)

		# try to use cleaner metod
		mc.curve( sel , replace = True,p=newShapes[0]["points"], k=newShapes[0]["knots"], d=newShapes[0]["degree"], per=bool(newShapes[0]["form"]) )



	# copy controller
	def copyCtrlShape(self,sel = None):
		sel = mc.ls(sl=True)
		print ('##### copyCtrlShape #####')
		try:
			data = wcd.getShape(sel[0])	
			mc.curve( sel[1], replace = True,p=data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]) )
		except:
			print ('Error occured: Maybe you should delete curve history.')




#run()







