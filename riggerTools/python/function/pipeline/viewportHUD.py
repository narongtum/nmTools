'''
show / hide HUD 
merge with playblast tools
'''


from function.pipeline import data
reload(data)

import socket
localMachine = socket.gethostname()

import maya.cmds as mc
import time
import datetime


'''
#manual run
from function.pipeline import viewportHUD 
reload(viewportHUD)


function = viewportHUD.mayaHUD()


function.runShowHUD()
function.deleteHUD()


'''


artist = data.ARTIST_dict

class mayaHUD(object):
	def __init__(self):
		pass

	'''
	add HUD findUser here
	'''
	def findUser( self ):
		for each in artist:
			if each["machineName"] == localMachine:
				artistName = each["name"]
			else:
				pass
		if artistName:
			return artistName
		else:
			return None

	def currentDate( self ):
		'''
		find time date in desire format
		'''
		
		date = datetime.datetime.now()
		date = date.strftime("%d.%b.%y  %H:%M")
		d2 = date 
		#mc.date()#f='DD.MM.YY')
		callDate = str(d2)#"Date: "+ 
		return callDate


	def runShowHUD( self,*args ):

		# delete some original HUD
		mc.headsUpDisplay(	removePosition	=	[5,0]	)
		mc.headsUpDisplay(	removePosition	=	[5,1]	)
		mc.headsUpDisplay(	removePosition	=	[6,0]	)
		mc.headsUpDisplay(	removePosition	=	[8,0]	)
		mc.headsUpDisplay(	removePosition	=	[9,1]	)
		mc.headsUpDisplay(	removePosition	=	[9,0]	)

		#Find Max Frame
		maxTimeA = mc.playbackOptions(q=True, max=True)
		minTimeA = mc.playbackOptions(q=True, min=True)
		maxFrame = ( maxTimeA - minTimeA + 1 )

		callFrame = mc.currentTime( q=True)
		countFrame = '(%d)' %(maxFrame)

		#FindFileName For Shot Name
		partFileName = mc.file( q=1,sn=1)
		splitfileName = partFileName.split('/')
		preName = splitfileName[len(splitfileName)-1]
		name = preName.split('.ma')[0]	

		# Name for Display HUD
		selUser = self.findUser()
		selUser = 'Artist: ' + selUser
		fileName = name
		selRes = 'Resolution : 4K '


		HUDfileName = mc.headsUpDisplay( 'HUDfileName', section=5, block=0, blockAlignment='left', dataWidth=50, dataFontSize = 'large', labelFontSize = 'large', l = fileName, blockSize = 'small', allowOverlap=True)
		HUDframe = mc.headsUpDisplay('HUDframe', section=6, block=0, blockAlignment='left', dataWidth = 40, labelFontSize = 'large', dataFontSize = 'large',allowOverlap = True, pre = 'currentFrame',l=countFrame)
		HUDres = mc.headsUpDisplay('HUDres', section=8, block=0, blockAlignment='right', dataWidth = 1, labelFontSize = 'large', dataFontSize='large',allowOverlap=True, event='idle', command = self.currentDate)
		HUDuser = mc.headsUpDisplay( 'HUDuser',section=9, block=0, blockAlignment='right', dataWidth=50, dataFontSize = 'large', labelFontSize = 'large', l = selUser, blockSize = 'small', allowOverlap=True)

		# SetTextColor
		mc.displayColor('headsUpDisplayLabels',17,dormant=True)
		mc.displayColor('headsUpDisplayValues',17,dormant=True)


	def deleteHUD( self,*args ):
		mc.displayColor( resetToFactory = True )

		if mc.headsUpDisplay( 'HUDfileName',ex = True):
			mc.headsUpDisplay( 'HUDfileName',remove = True)
			
		if mc.headsUpDisplay( 'HUDres',ex = True):
			mc.headsUpDisplay( 'HUDres',remove = True)
			
		if mc.headsUpDisplay( 'HUDuser',ex = True):
			mc.headsUpDisplay( 'HUDuser',remove = True)
			
		if mc.headsUpDisplay( 'HUDframe',ex = True):
			mc.headsUpDisplay( 'HUDframe',remove = True)

		

