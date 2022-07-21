# Skin tools
import maya.cmds as mc
import maya.mel as mm
from functools import partial

def run() :
	# SkinTools call back
	ui = SkinTools()
	ui.show()

class SkinTools( object ) :
	
	def __init__( self ) :
		print 'Tools for skinning.\nCreated by peckpeckpeckpeckpeck@gmail.com'
		self.ui = 'pkSkinTools'
		self.win = '%sWin' % self.ui
		self.paintModeRadioButtons = { '%sPaintAddRB'%self.ui : 'Add' ,
										'%sPaintReplaceRB'%self.ui : 'Replace' ,
										'%sPaintSmoothRB'%self.ui : 'Smooth' ,
										'%sPaintScaleRB'%self.ui : 'Scale'
										}
		self.paintUi = 'artAttrSkinContext'
	
	def show( self ) :
		
		if mc.window( self.win , exists=True ) :
			mc.deleteUI( self.win )
		
		mc.window( self.win , t='pkSkinTools' , rtf=True )
		mc.columnLayout( '%sMainCL'%self.ui , adj=True )
		
		mc.button( l='Curves' , c=partial( self.toggleVis , 'nurbsCurves' ) )
		mc.button( l='Surfaces' , c=partial( self.toggleVis , 'nurbsSurfaces' ) )
		mc.button( l='Polygons' , c=partial( self.toggleVis , 'polymeshes' ) )
		mc.button( l='Joints' , c=partial( self.toggleVis , 'joints' ) )
		mc.button( l='Grid' , c=partial( self.toggleVis , 'grid' ) )
		mc.button( l='WireShd' , c=partial( self.toggleVis , 'wos' ) )
		
		mc.separator()
		
		mc.button( l='Paint' , c=partial( self.paintTool ) , h=50 )
		
		mc.separator()
		
		mc.floatField( '%sValueFF'%self.ui , changeCommand=partial( self.paintValueChange ) )
		mc.popupMenu()
		for ix in ( 0 , 0.01 ,0.05 , 0.1 , 0.25 , 0.5 , 0.75 , 0.98 , 1 ) :
			mc.menuItem( l=str( ix ) , c=partial( self.setValueFloatField , ix ) )
		
		# mc.setParent( '..' )
		
		mc.radioCollection( '%sPaintRCL'%self.ui )
		for key in self.paintModeRadioButtons.keys() :
			mc.radioButton( key ,
				label=self.paintModeRadioButtons[ key ] ,
				changeCommand=partial( self.setOperation ) )
		
		mc.radioButton( self.paintModeRadioButtons.keys()[0] , e=True , sl=True )
		
		mc.button( l='Flood' , h=50 , c=partial( self.flood ) )
		
		mc.separator()
		wid = 56
		mc.rowLayout( nc=2 , cw2=[wid,wid] )
		mc.button( l='Hold' , w=wid , c=partial( self.hold , True ) )
		mc.button( l='Unhold' , w=wid , c=partial( self.hold , False ) )
		
		mc.showWindow( self.win )
		mc.window( self.win , e=True , w=120 )
		mc.window( self.win , e=True , h=380 )
	
	def setValueFloatField( self , val=0.0 , arg=None ) :
		# Set value float field's value
		mc.floatField( '%sValueFF'%self.ui , e=True , v=val )
		self.paintValueChange()
	
	def paintValueChange( self , arg=None ) :
		# Float field's change command
		if mc.artAttrSkinPaintCtx( self.paintUi , exists=True ) :
			
			val = mc.floatField( '%sValueFF'%self.ui , q=True , v=True )
			mc.artAttrSkinPaintCtx( self.paintUi , e=True , value=val )
	
	def getJointFromSelectedObjects( self ) :
		# Returns the first joint that was found in selected objects
		sels = mc.ls( sl=True )
		jnt = None
		
		for sel in sels :
			if mc.nodeType( sel ) == 'joint' :
				jnt = sel
		
		return jnt
	
	def hold( self , hold=True , arg=None ) :
		# Hold/Unhold weight influences
		# If object is selected, script will hold/unhold all of object's influences.
		# If joint is selected, script will hold/unhold selected joint.
		sels = mc.ls( sl=True )
		
		for sel in sels :
			
			if mc.nodeType( sel ) == 'joint' :
				
				mc.setAttr( '%s.liw' % sel , hold )
			
			else :
				
				skn = mm.eval( 'findRelatedSkinCluster %s' % sels[0] )
				infs = mc.skinCluster( skn , q=True , inf=True )
				
				for inf in infs :
					
					mc.setAttr( '%s.liw' % inf , hold )
	
	def flood( self , arg=None ) :
		
		jnt = self.getJointFromSelectedObjects()
		
		if jnt :
			# A joint and components are selected
			
			sels = mc.ls( sl=True , fl=True )
			sels.remove( jnt )
			val = mc.floatField( '%sValueFF'%self.ui , q=True , v=True )
			
			for sel in sels :
				# Selected infos
				geo = sel.split( '.' )[0]
				skn = mm.eval( 'findRelatedSkinCluster %s' % geo )
				infs = mc.skinCluster( skn , q=True , inf=True )
				wghtVals = mc.skinPercent( skn , sel , q=True , v=True )
				
				for ix in range( len( infs ) ) :
					
					if infs[ ix ] == jnt :
						
						self.assignWeightToVtx( val=val , vtx = sel , skn=skn , inf=infs[ ix ] , wghtVal=wghtVals[ ix ] )
			
		else :
			# No joint is selected
			mc.artAttrSkinPaintCtx( self.paintUi , e=True , clear=True )
	
	def assignWeightToVtx( self , vtx='' , val=0 , skn='' , inf='' , wghtVal=0.0 ) :
		# Get the current operation.
		# Assign calculated weight value to the input vertex regarding the current operation.
		currState = self.getOperation()
						
		if currState == 'Add' :
			newVal = wghtVal + val
			mc.skinPercent( skn , vtx , transformValue=[ ( inf , newVal ) ] )
		
		elif currState == 'Replace' :
			newVal = val
			mc.skinPercent( skn , vtx , transformValue=[ ( inf , newVal ) ] )
		
		elif currState == 'Scale' :
			newVal = wghtVal * val 
			mc.skinPercent( skn , vtx , transformValue=[ ( inf , newVal ) ] )
		
		elif currState == 'Smooth' :
			mm.eval( 'warning "Smooth operation works only in paint mode";' )
	
	def getOperation( self , arg=None ) :
		# Get current state of paint operation
		key = mc.radioCollection( '%sPaintRCL'%self.ui , q=True , sl=True )
		return self.paintModeRadioButtons[ key ]
	
	def setOperation( self , arg=None ) :
		# Set state of paint operation
		if mc.currentCtx() == 'artAttrSkinContext' :
			
			currState = self.getOperation()
			
			mm.eval( 'artAttrPaintOperation artAttrCtx %s;' % currState )
			mm.eval( 'artUpdateStampProfile solid artAttrCtx;' )
			mm.eval( 'artAttrCtx -e -opacity 1 %s;' % self.paintUi )
		
	def paintTool( self , arg=None ) :
		# Call paint skin weight tool
		mm.eval( 'ArtPaintSkinWeightsToolOptions' )
		
		self.setOperation()
		self.paintValueChange()

	def toggleVis( self , elem='' , arg=None ) :
		# Toggle visibility
		currPanel = mc.getPanel( wf=True )
		
		if elem == 'nurbsCurves' :
			
			currState = mc.modelEditor( currPanel , q=True , nurbsCurves=True )
			mc.modelEditor( currPanel , e=True , nurbsCurves=not( currState ) )
			
		elif elem == 'nurbsSurfaces' :
			
			currState = mc.modelEditor( currPanel , q=True , nurbsSurfaces=True )
			mc.modelEditor( currPanel , e=True , nurbsSurfaces=not( currState ) )
			
		elif elem == 'polymeshes' :
			
			currState = mc.modelEditor( currPanel , q=True , polymeshes=True )
			mc.modelEditor( currPanel , e=True , polymeshes=not( currState ) )
			
		elif elem == 'joints' :
			
			currState = mc.modelEditor( currPanel , q=True , joints=True )
			mc.modelEditor( currPanel , e=True , joints=not( currState ) )
			
		elif elem == 'grid' :
			
			currState = mc.modelEditor( currPanel , q=True , grid=True )
			mc.modelEditor( currPanel , e=True , grid=not( currState ) )
			
		elif elem == 'wos' :
			
			currState = mc.modelEditor( currPanel , q=True , wos=True )
			mc.modelEditor( currPanel , e=True , wos=not( currState ) )
		

run()