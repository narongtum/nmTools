import maya.cmds as mc
from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.util import misc
reload(misc)

from functools import partial
'''
Descr:      This script will place evenly spaced joints along the selected curve. 
'''


fiboCheck = True



def run():
	ui = buildUI()
	ui.show()





class buildUI(object):

	def __init__(self):
		self.winName = 'jntAlong_CurveUI'
		self.winTitle = 'Set up a joint along selected curve'
		print ('Initiation building %s UI' %self.winTitle)

		 

		


	def show(self):

		if mc.window( self.winName, exists = True ):
			mc.deleteUI( self.winName)

		

	#===# UI Part==========================================================================================================================#
		myWindow = mc.window( self.winName , title = self.winTitle, w = 200, h = 150, mnb = True, maximizeButton = True, sizeable = True)
		mc.columnLayout(adjustableColumn=True)
		rowColumnLayout = mc.rowColumnLayout(nc = 2, cw = [(1, 100) , (2, 100)] )
	#=============================================================================================================================#   
		mc.text(label = "Prefix:", align = "left")
		mc.textField( "prefix" )	

		mc.text(label = "Name:", align = "left")
		mc.textField( "name" ,text='joint')

		mc.text(label = "Suffix:", align = "left")
		mc.textField( "suffix" ,text='_bJnt')	

		mc.text(label = "Joint amount:", align = "left")
		# jointAmountIF = mc.intField( value = 3 , minValue = 2 )
		mc.intField('jointAmount', minValue=3, value=10)
		# jointAmount = cmds.intSliderGrp( "jointAmount", f = True, cat = [1, 'left', 0], minValue = 1,  fmn = 2, fmx = 200, v = 2 )


		mc.button(label = "Create" , w = 75 , command = self.createJntAlongCurve )

		# split with fibonacci number
		mc.checkBox( 'fiboBox', label = "Fibonacci" ,value = False)

		# direction splite
		mc.checkBox( 'directBox', label = "Reverse" ,value = False)

		# mc.button(l = "Cancle" , w = 75 , command = print'%s' %self.winTitle )
		mc.showWindow()

	#-----------------------------------------------------------------------------------------------------------------------------#

	def _core_along_curve( self, prefix , name , suffix , jointAmount , curveSelected ):
		rootJnt = ''
		previousJnt = ''

		if not mc.checkBox( 'fiboBox' ,value = True ,q=True ):
			print ('You choose to devide same length')



			jnt_grp=[]
			# use constance length
			for i in range( 0, jointAmount ):
				mc.select( cl=True )
				newJnt = mc.joint(  name = '{0}{1}{2:02d}{3}'.format( prefix , name ,i+1, suffix )  )
				print ('This is joint name >>> {0}{1}{2:02d}{3}'.format( prefix , name ,i+1, suffix ))
				motionPath = mc.pathAnimation(newJnt, c = curveSelected, fractionMode = True )
				# delete key
				mc.cutKey( motionPath + ".u", time = () )
			
				
				mc.setAttr( motionPath + ".u", i * ( 1.0/(jointAmount-1) ) )
				mc.delete(newJnt + ".tx", icn = True)
				mc.delete(newJnt + ".ty", icn = True)
				mc.delete(newJnt + ".tz", icn = True)
				
				mc.delete(motionPath)

				# for parent
				if i == 0:
					previousJnt = newJnt
					rootJnt = newJnt

					continue

				mc.parent(newJnt , previousJnt)
				previousJnt = newJnt


				# set orientation
				mc.joint(rootJnt, e=True, oj= 'yzx', sao = 'yup' , ch = True, zso = True)

				jnt_grp.append(newJnt)

			#... set orient of last joint
			lastJnt = jnt_grp[-1]
			mc.setAttr(f'{lastJnt}.jointOrientX', 0)
			mc.setAttr(f'{lastJnt}.jointOrientY', 0)
			mc.setAttr(f'{lastJnt}.jointOrientZ', 0)






		else:
			#... if use Fibonacci length
			#... make jointAmount delete the previous last



			# limit for 30 number
			fibo = ( 1,2,3,5,8,13,21,34,55,89,144,233,
					377,610,987,1597,2584,4181,6765,10946,
					17711,28657,46368,75025,121393,
					196418,317811,514229 )

			length_value = (0,0.267,0.496,0.634,0.746,0.822,0.887,0.948,1.00)

			if jointAmount >= len(fibo):
				mc.error("Terminate Limit for 30 number.")
											
				
			length = 1.0
			jointAmount = jointAmount - 1
			spNum = []

			# sum number in list method 1
			spNum = fibo[:jointAmount]
			print (sum(spNum))
			total = 0
			sumVal = []

			# sum number in list method 2
			for ele in range(0, len(spNum)): 
				total = total + spNum[ele]

			previousJnt = ''  
			rootJnt = ''

			for i in range(0, jointAmount):
				mc.select( cl=True )   
				value = float(fibo[i])/float(total)
				roundVal = round(value , 3)
				sumVal.append(roundVal)
				# sumVal = sumVal[::-1]
			
			# ask direction slice from Top to End or End to top
			if mc.checkBox( 'directBox' ,value = True ,q=True ) == True:
				direct = False
			else:
				direct = True

			print ('direct is %s' %direct)
			sumVal = sorted( sumVal, reverse = direct )
			print ('sum of value is ' + str(sum(sumVal)))

			# insert 0 for make it match with input
			sumVal.insert(0,0)


			print ('********')												
			print (sumVal)
			print ('*********\n')	

			previousVal = 0

			#... loop through value
			for i in range(0,len(sumVal)):

				#... check if the previous last number
				# previous_last = len(sumVal)-1
				print ('This is number %s' %i)
				# print ('This is number %s' %previous_last)



				mc.select( cl=True )


				newJnt = mc.joint(  name = '{0}{1}{2:02d}{3}'.format( prefix , name ,i+1, suffix )  )

				if i == 0:
					previousJnt = newJnt
					rootJnt = newJnt


				motionPath = mc.pathAnimation( newJnt, c = curveSelected, fractionMode = True )
				mc.cutKey( motionPath + ".u", time = () )

				print (sumVal[i])

				previousVal += sumVal[i]

				if i == 0:
					previousJnt = newJnt
					rootJnt = newJnt
					mc.setAttr( motionPath + ".u", sumVal[i] )


					
				else:

					if previousVal > 1.00:
						mc.setAttr( motionPath + ".u", 1.00 )
					else:
						mc.setAttr( motionPath + ".u", previousVal )




				if i > 0:
					mc.parent( newJnt , previousJnt)
					previousJnt = newJnt 					
					
				mc.joint(rootJnt, e=True, oj= 'yzx', sao = 'yup' , ch = True, zso = True)	

				#... Delete connection
				# mc.delete(newJnt + ".tx", icn = True)
				# mc.delete(newJnt + ".ty", icn = True)
				# mc.delete(newJnt + ".tz", icn = True)
				# mc.delete(motionPath)

				mc.select( cl=True )


















			



	# Function
	def createJntAlongCurve( self,jointAmount ):

		curveSelected = mc.ls( sl = True )[0]
		# Check is Edge or Curve

		isNode = misc._identifies( curveSelected )

		#Gather information
		prefix = mc.textField( "prefix", q=True , tx=True )

		name = mc.textField( "name", 	q=True , tx=True )

		suffix = mc.textField( "suffix", q=True , tx=True )


		jointAmountNum = mc.intField( "jointAmount", query=True , value=True )


	
		# if textField is empty us name of curve instead
		if name == '':
			print ('textField is empty us name of curve instead.')
			name = mc.ls(sl=True)[0]

		if isNode == 'nurbsCurve':
			self._core_along_curve( prefix , name , suffix , jointAmountNum ,curveSelected)
		elif isNode == 'mesh':
	
			try:
				curveEdge = mc.polyToCurve()[0]
				self._core_along_curve( prefix , name , suffix , jointAmountNum ,curveEdge)
				mc.delete(curveEdge)
			except:
				mc.error('Please using edge select.')
				
		else:
			mc.warning('Please create curve or select edge.')
			return False


	# def _findFiboLength( self, jointAmount ):



# run()