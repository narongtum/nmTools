import maya.cmds as mc





def tween( percentage, obj = None , attrs = None , selection = True ):
	if not obj and not selection:
		raise ValueError("no object giving")

	# if no obj si specified, get it from the first selection
	if not obj:
		obj = mc.ls( selection = True)[0]

	if not attrs:
		# qury from selection that keyable na
		attrs = mc.listAttr( obj, keyable=True )
	# time at current timeline
	currentTime = mc.currentTime(query = True)

	for attr in attrs:
		print attr
		# Build full name of the attr with tis object
		attrFull = '%s.%s' %(obj,attr)

		# Get the keyframe of the attr on this obj
		keyframes = mc.keyframe(attrFull, query=True)

		# If there are no keyframes, then continue
		if not keyframes:
			continue
		print keyframes


		previousKeyframes = []
		for frame in keyframes:
			if frame < currentTime:
				previousKeyframes.append(frame)

		#using list compherehesion 
		laterKeyframes = [frame for frame in keyframes if frame > currentTime ]

		# both key must be empty
		if not previousKeyframes and not laterKeyframes:
			continue



		if previousKeyframes:
			# get the max value
			previousframe = max(previousKeyframes)

		else:
			previousframe = None

			# Using one line technique

		nextframe = min(laterKeyframes) if laterKeyframes else None

		print previousframe, nextframe
		if not previousframe or not nextframe:
			continue

		previousValue = mc.getAttr( attrFull , time = previousframe )
		nextValue = mc.getAttr( attrFull, time = nextframe )

		print previousValue, nextValue

		difference = nextValue - previousValue
		weightedDiffence = ( difference * percentage ) / 100.0

		currentValue = previousValue + weightedDiffence
		mc.setKeyframe(attrFull, time = currentTime, value = currentValue )

		

class TweenWindow(object):

	windowName = "Tweener_Window"

	def show(self):

		if mc.window(self.windowName, query = True , exists = True):
			mc.deleteUI(self.windowName)
			
		mc.window( self.windowName )
		self.buildUI()
		mc.showWindow()

	def buildUI(self):
		column = mc.columnLayout()
		mc.text( label = 'Use this slide to set the tween amount' )
		row = mc.rowLayout( numberOfColumns = 2 )
		self.slider = mc.floatSlider( min = 0 , max = 100, value = 50 , step = 1 , changeCommand = tween )
		# not use() because not exec just tell python put the function here
		mc.button(label="Reset" , command = self.reset )

		mc.setParent(column)
		mc.button( label = "Close" , command = self.close )

	def reset(self , *args):
		mc.floatSlider( self.slider, edit=True, value = 50 )
		print "Reseting UI"
		print args
		pass

	def close(self , *args):
		mc.deleteUI(self.windowName)
