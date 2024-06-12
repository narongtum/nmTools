from function.framework.reloadWrapper import reloadWrapper as reload

from function.rigging.readWriteCtrlSizeData import writeCtrlData as wcd
reload(wcd)

from function.pipeline import fileTools
reload(fileTools)

from function.rigging.util import misc as misc
reload(misc)

import maya.cmds as mc

#sys.path.append(r'D:\noman')
# DECLARE GLOBAL VARIABLE

try:
	SHAPE_LIBRARY_PATH = wcd.validCtrlData()
except:
	print('There are no valid data.')


# saving data
def savingData():
	fileTools.checkExistFolder(SHAPE_LIBRARY_PATH)
	allCtrl = mc.ls('*_ctrl')
	if allCtrl:
		allShapeName = []
		ext = ".json"	
		
		print ('\nWriting CtrlData...')
		for each in allCtrl:
			shapeName = wcd.validateCurve(each)
			if shapeName != ''  :
				crvShapeData = wcd.getShape(each) 
				shape = shapeName[0]
				allShapeName.append(shape)
				
				path = SHAPE_LIBRARY_PATH + shape + ext
				
				# save data 
				wcd.saveData(path , data = crvShapeData)
				print ('%s' %each)
			else:
				print('There are no dict data Pass...')

		# print ('\n# # # # Save CtrlData Done # # # #')
		misc.makeHeader('Save CtrlData Done')
		print ('File has been saving at: %s' %SHAPE_LIBRARY_PATH)
	else:
		print ("You must put suffix '*_ctrl' to controller")
   


def loadingData():
	allCtrl = mc.ls('*_ctrl')
	for each in allCtrl:
		shapeName = wcd.validateCurve(each)
		shape = shapeName[0]
		try:
			data = wcd.loadFromLib(shape)
			# replace the controller data
			mc.curve(data["name"],r=True,p=data["points"], k=data["knots"], d=data["degree"], per=bool(data["form"]))
		except:
			print( "The file " + shape + " doesn't exist" )
			continue
	print ('#### load CtrlData Done ####')

'''     
# check if have folder or not
wcd.checkExistFolder(SHAPE_LIBRARY_PATH)
SavingData()        
loadingData()
'''





  