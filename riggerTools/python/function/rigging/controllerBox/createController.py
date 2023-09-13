'''
from function.rigging.controllerBox import createController
reload(createController)
createController.run()

'''

from function.framework.reloadWrapper import reloadWrapper as reload

import maya.cmds as mc
from functools import partial
from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)
# define ctrl LIBRARY path
SHAPE_LIBRARY_PATH = 'D:\\sysTools\\nmTools\\riggerTools\\python\\function\\rigging\\ctrlSizeLibrary\\'




def run() :
	# ControlMaker call back
	ui = ControlMaker()
	ui.showUI()

class ControlMaker( object ) :
	
	def __init__( self ) :
		
		print ('Script for creating controller.\nModify from peckpeckpeckpeckpeck@gmail.com')
		self.ui = 'Controller'
		self.win = '%sWin' % self.ui
	
	def showUI( self ) :
		
		if mc.window( self.win , exists = True ) :
			mc.deleteUI( self.win )
		
		mc.window( self.win , title = 'Controller Tools' , resizeToFitChildren = False )
		
		mc.columnLayout( '%sMainCL'%self.ui , adjustableColumn = False )


		# create controller button
		mc.button( '%sCurveButton'%self.ui , l = 'Right Click to Choose Controller' , w=310 , h=25  , c=partial( self.checkCurve ))
		# create popup
		mc.popupMenu()

		# list of right click
		labels = 	( 
					'arrow' , 'circle' , 'cross' , 
					'cube' , 'double' , 'orient' , 
					'quad' , 'ring' , 'sphere' , 
					'square' , 'stick' ,'placement' , 
					'hat' , 'plus','gear'
					)

		for label in labels :
			mc.menuItem( l =label , command = partial( self.changeButtonLabel , label ) )
		


		# number of columns
		nc = 6
		# width
		wid = 300
		# collumn width
		cw = ( wid / nc )
		mc.rowLayout( numberOfColumns=nc , columnWidth6=(cw,cw,cw,cw,cw,cw) )
		mc.button( width = cw , label = 'Red' , 		bgc = [1, 0, 0] , 	command = partial(self.assignColor,'red')   )
		mc.button( width = cw , label = 'DarkRed' , 	bgc = [0.6, 0.03, 0.03] , 	command = partial(self.assignColor,'darkRed'))
		mc.button( width = cw , label = 'Green' , 		bgc = [0, 1, 0] ,	command = partial(self.assignColor,'green') )
		mc.button( width = cw , label = 'Yellow' , 		bgc = [1, 1, 0] ,	command = partial(self.assignColor,'yellow') )  
		mc.button( width = cw , label = 'Blue' , 		bgc = [0, 0, 1] ,	command = partial(self.assignColor,'blue') ) 	
		mc.button( width = cw , label = 'SoftBlue' , 	bgc = [0, 0, 0.5]  ,	command = partial(self.assignColor,'softBlue') )
		

		
		# another button
		mc.setParent( '..' )
		nc2 = 2
		mc.rowLayout( numberOfColumns = nc2 , columnWidth2=(cw,cw) )
		mc.button( width = cw , label='white' , bgc=[1,1,1], command = partial(self.assignColor,'white')  )
		mc.button( width = cw , label='None' , bgc=[0,0,0.02], command = partial(self.assignColor,'none')  )
		# mc.button( width = cw , label='B' , bgc=[0,0,1]  )
		# mc.button( width = cw , label='Y' , bgc=[1,1,0]   )
		# mc.button( width = cw , label='W' , bgc=[1,1,1]  )
		# mc.button( width = cw , label='W' , bgc=[1,1,1]  )
		

		
		
	



		mc.showWindow( self.win )
		mc.window( self.win , e=True , width = wid + 8 )
		mc.window( self.win , e=True , h=150 )
		

		# -------------
		# function part
		# -------------
	
	def changeButtonLabel( self , label='' , arg=None ) :
		
		mc.button( '%sCurveButton'%self.ui , e=True , l=label )


#  ( 'arrow' , 'circle' , 'cross' , 'double' , 'orient' , 'quad' , 'ring' , 'sphere' , 'square' , 'stick' ,'placement' , 'hat')

	def checkCurve( self , arg=None ) :

		label = mc.button( '%sCurveButton'%self.ui , q=True , l=True )
		
		if label == 'arrow':

			self.createController(shapeName = 'arrow_ctrlShape')

		elif label == 'placement':
			self.createController(shapeName = 'placement_ctrlShape')

		elif label == 'circle':
			self.createController(shapeName = 'circle_ctrlShape')

		elif label == 'cross':
			self.createController(shapeName = 'cross_ctrlShape')

		elif label == 'cube':
			self.createController(shapeName = 'cube_ctrlShape')
				
		elif label == 'double':
			self.createController(shapeName = 'double_ctrlShape')

		elif label == 'orient':
			self.createController(shapeName = 'orient_ctrlShape')

		elif label == 'quad':
			self.createController(shapeName = 'quad_ctrlShape')

		elif label == 'ring':
			self.createController(shapeName = 'ring_ctrlShape')

		elif label == 'sphere':
			self.createController(shapeName = 'plainSphereB_ctrlShape')

		elif label == 'square':
			self.createController(shapeName = 'square_ctrlShape')

		elif label == 'stick':
			self.createController(shapeName = 'stick_ctrlShape')

		elif label == 'hat':
			self.createController(shapeName = 'hat_ctrlShape')

		elif label == 'diamond':

			self.createController(shapeName = 'diamond_ctrlShape')

		elif label == 'plus':
			self.createController(shapeName = 'plus_ctrlShape')

		elif label == 'gear':
			self.createController(shapeName = 'gear_ctrlShape')




	def createController( self , shapeName ):
		self.data = wcd.loadData(path = SHAPE_LIBRARY_PATH + shapeName + '.json')
		self.curveName = mc.curve(  p=self.data["points"], k=self.data["knots"], d=self.data["degree"], per=bool(self.data["form"]))
		
		mc.setAttr( '%s.overrideEnabled'	% self.curveName , 1 )
		mc.setAttr( '%s.overrideColor' 		% self.curveName , self.data['colour'] )




	def assignColor( self , color = '' , arg = None ) :
		
		colorDict = { 	'yellow'		: 17 	, 'red' 			: 13 ,
						'softBlue' 		: 18 	, 'blue' 			: 6 ,
						'white' 		: 16 	, 'brown'			: 11 ,
						'black' 		: 1 	, 'gray' 			: 2 ,
						'softGray'		: 3 	, 'darkRed' 		: 4 ,
						'darkBlue' 		: 5 	, 'darkGreen'		: 7 ,
						'green' 		: 14 	, 'none' 			: 0 	}
					
		colorID = colorDict[ color ]
		selected = mc.ls( sl=True )
		
		for each in selected :
			# find shape node
			shapes = mc.listRelatives( each , shapes = True )
			
			if shapes :
				
				for shape in shapes :
					
					if color == 'none' :
						# set the 'none' color for user click none
						mc.setAttr( '%s.overrideColor'	 	% shape , colorID )
						mc.setAttr( '%s.overrideEnabled' 	% shape , 0 )
					else :
						mc.setAttr( '%s.overrideEnabled'	% shape , 1 )
						mc.setAttr( '%s.overrideColor' 		% shape , colorID )
						
