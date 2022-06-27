# >>>>>   Untimate Playblast Button   <<<<<
# 	Date: 18.June.2021
# 	Author: UI, main function		:	THEDODE 
#			convert function 		: 	noman
#
# - fix can't convert file path with whitespace folder
# - fix can't browse specific file 
# - add watermark
# - add HUD
# - add sound option
# - add logging 
version = 1.18



import maya.cmds as mc
import os
import subprocess
from shutil import copyfile
import time
import datetime



from function.pipeline import fileTools as fileTools 
reload(fileTools)

from function.pipeline import data_dict as data
reload(data)

import socket
localMachine = socket.gethostname()

from function.pipeline import logger 
reload(logger)




# load dictionary
artist = data.ARTIST_dict

QT_PATH = r'C:\\Program Files (x86)\\QuickTime\\QuickTimePlayer.exe'
# FFMPEG = r'D:\\True_Axion\\Tools\\riggerTools\\python\\axionTools\\pipeline\\playBlast\\framework\\ffmpeg-20181016-b2adc31-win64-static\\bin\\ffmpeg.exe'
FFMPEG = r'D:\\sysTools\\nmTools\\riggerTools\\python\\function\\pipeline\\playBlast\\framework\\ffmpeg-20181016-b2adc31-win64-static\\bin\\ffmpeg.exe'
INPUT_PATH = r'D:\\FFOutput\\playBlastTemp.avi'
WATERMARK_PATH = r'D:\\sysTools\\nmTools\\riggerTools\\image\\cam_watermark.png'

					

class PlayblastLogger(logger.MayaLogger):
	LOGGER_NAME = "Playblast"


class function:
	'''
	add HUD findUser here
	'''
	def findUser( self ):
		for each in artist:
			if each["machineName"] == localMachine:
				artistName = each["name"]
				break
			else:
				artistName = 'Unknow'

		return artistName

	
	def currentDate( self ):
		'''
		find time date in desire format
		'''
		
		date = datetime.datetime.now()
		date = date.strftime("%d.%b.%y  %H:%M")

		#mc.date()#f='DD.MM.YY')
		return str(date)


	def showHUD( self,*args ):

		# delete some original HUD
		mc.headsUpDisplay(removePosition=[5,0])
		mc.headsUpDisplay(removePosition=[5,1])
		mc.headsUpDisplay(removePosition=[6,0])
		mc.headsUpDisplay(removePosition=[8,0])
		mc.headsUpDisplay(removePosition=[9,1])
		mc.headsUpDisplay(removePosition=[9,0])

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
		selUser = 'Artist:  ' + selUser
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
		if mc.headsUpDisplay( 'HUDfileName',ex=True):
			mc.headsUpDisplay( 'HUDfileName',remove = True)
			
		if mc.headsUpDisplay( 'HUDres',ex=True):
			mc.headsUpDisplay( 'HUDres',remove = True)
			
		if mc.headsUpDisplay( 'HUDuser',ex=True):
			mc.headsUpDisplay( 'HUDuser',remove = True)
			
		if mc.headsUpDisplay( 'HUDframe',ex=True):
			mc.headsUpDisplay( 'HUDframe',remove = True)

		# reset color
		mc.displayColor( resetToFactory = True )


	def timeLine(self,*args):
		# TimeLine Query 
		startTime = mc.playbackOptions( min = True,q = True )
		endTime = mc.playbackOptions( max = True,q = True )
		mc.textField('startTexFld', edit = True, tx = startTime)
		mc.textField('endTexFld',edit = True, tx = endTime)
		return [ startTime , endTime ]



	def setTimeLine(self,*args):
		# Set The Query Time
		getStartTime = mc.textField('startTexFld', tx = True, q = True)
		getEndTime = mc.textField('endTexFld', tx = True, q = True)
		mc.playbackOptions(min = getStartTime,max = getEndTime)
		
	def keyTime(self,*args):
		# Hips.tx Query
		minKey = mc.keyframe('cog_ctrl.tx',index=(0,0),query=True)
		maxKey =  mc.keyframe('cog_ctrl.tx',iv = True,query=True)
		startTime = minKey[0]
		endTime = startTime + (len(maxKey)-1)
		mc.textField('startTexFld', edit = True, tx = startTime)
		mc.textField('endTexFld',edit = True, tx = endTime)    
		return [ startTime , endTime ]
	
	# SNAP FRAME TO CAM    
	def setCamera(self , *args):
		selCam = mc.listCameras( p = True )
		sel = mc.ls(sl=1)
		imagePath = 'D:/sysTools/nmTools/riggerTools/image/border.png'

		if 'camera1' in selCam:
			cam = 'camera1'
			camShape = 'cameraShape1'
			mc.imagePlane(n = 'frameOutline', c = cam, fn = imagePath ,showInAllViews=0)
			mc.setAttr ( "frameOutlineShape2.depth" ,.5)
			#mc.delete('frameOutline1')
		elif sel > 0:
			cam = sel[0]
			camShape = cam + 'Shape'
			mc.imagePlane(n = 'frameOutline', c = cam, fn = imagePath ,showInAllViews=0)
			mc.setAttr ( "frameOutlineShape2.depth" ,.5)
		elif sel == 0:
			PlayblastLogger.error('There is no Camera')

	
	# PLAYBLAST
	def playBlast( self , *args ):


		# shift to here
		# prevent quicktime merge output by delete raw file after finish convert
		if os.path.exists( INPUT_PATH ):
			PlayblastLogger.info(INPUT_PATH)
			os.remove(	INPUT_PATH	)
		else:
			PlayblastLogger.error('The file does not exist.')
			pass



		# IF have must write overide ask
		overwrite = 1
		# Query RESOLUTION OPTION
		if mc.optionMenu("selRes", q = 1, v = 1) == '1080':
			res = (1920,1080)
			
		elif mc.optionMenu("selRes", q = 1, v = 1) == '720':
			res = (1280,720)
			
		# Query PATH
		prePart ='D:/FFOutput'
		path = mc.textField( 'pathField', tx = True, q = True)	
		
		# Query FileName  
		name = mc.textField( 'nameField', tx = True, q = True)

		global FORMAT

		# Query FileType OPTION
		if mc.optionMenu("selFormat", q = 1, v = 1) == 'mov':
			FORMAT = 'mov'
			
		elif mc.optionMenu("selFormat", q = 1, v = 1) == 'mp4':	
			FORMAT = 'mp4'

		# THE PLAYBLAST FUNCTION
		

		# INPUT_PATH = prePart + '/' + name + '.' + fileType
		# INPUT_PATH = os.path.normpath( INPUT_PATH )
		

		PlayblastLogger.info('INPUT_PATH: %s' %INPUT_PATH)

		indexIn = INPUT_PATH.index('.')
		cleanIn = ( INPUT_PATH[:indexIn] )
		# output file is tempolary to ffOutput
		OUTPUT_PATH = cleanIn + '_preview' + '.' + FORMAT 



		MOVETO_PATH = os.path.join(path , name + '_preview' + '.' + FORMAT )
		MOVETO_PATH = os.path.normpath( MOVETO_PATH )

		fileTools.checkExistFolder( filename = MOVETO_PATH )
		

		PlayblastLogger.info('FORMAT is :%s' %FORMAT)
		PlayblastLogger.info('MOVETO_PATH is :%s' %MOVETO_PATH)


		if mc.checkBox("soundBox", value = True , q = True):
			ableSound = True
			PlayblastLogger.info('I have sound.')
		elif mc.checkBox("soundBox", value = False , q = True):
			ableSound = False
			PlayblastLogger.info("I don't have sound.")

		# disable for now
		ableSound = False
		# playblast raw file
		mc.playblast( filename = INPUT_PATH, format = 'avi', sequenceTime = 0, clearCache = 1, viewer = 0, showOrnaments = 1, widthHeight = res, fp = 4, percent = 100, quality = 100, fo = overwrite, useTraxSounds = ableSound )

		# ffmpeg code
		#cmd ='%s -i %s -f mp4 -vcodec libx264 -preset fast -profile:v main -acodec aac %s -hide_banner' %( FFMPEG , INPUT_PATH , OUTPUT_PATH)
		# -y = Overwrite output files without asking.
		# -i = input file
		ffmpegCmd = '%s -y -i %s ' %( FFMPEG  , INPUT_PATH )

		'''
		overlay = option allows to specify where the top left of the image will appear on the video. 
		So adjust those number based on the resolution of your watermark and of your video.
		
		[short version]
		overlay = (W-w)/2:(H-h)/2

		[long version]
		overlay = ( main_w-overlay_w )/2:( main_h-overlay_h )/2

		'''

		ffmpegCmd += '-max_muxing_queue_size 9999 ' # Solve Too many packets buffered for output stream 0:1
		# if checkbox of watermark is check
		if mc.checkBox("watermarkBox", value = True , q = True):
			ffmpegCmd += '-i %s -filter_complex "overlay = ( main_w-overlay_w )/2:( main_h-overlay_h )/2" '  %WATERMARK_PATH

		ffmpegCmd += '-vcodec libx264 -vprofile baseline -crf 22 -bf 0 -pix_fmt yuv420p -f mov %s' %OUTPUT_PATH
		

		PlayblastLogger.info('ffmpeg is :'+ ffmpegCmd)
		
		try:
			subprocess.call( ffmpegCmd )
			# subprocess.call( 'timeout 30' )
			# time.sleep(1.5)
		except Exception as e:
			raise e
		
		









		# Open quicktime when finish convert
		if os.path.exists( OUTPUT_PATH ):

			if os.path.exists( QT_PATH ):
				copyfile( OUTPUT_PATH , MOVETO_PATH )
				subprocess.Popen(	[QT_PATH , MOVETO_PATH]	)
				# remove avi raw file
				os.remove(	OUTPUT_PATH	)
			else:
				# if quicktime is not exists open using whatever player
				os.startfile(MOVETO_PATH)
				PlayblastLogger.info('Open media file.')

		else:
			PlayblastLogger.error('\nThere are no media file to preview.')



		#return prePart, path, name, filePath


	def openContainFile( self , *args ):
		FOLDER_PATH = mc.textField( 'pathField', tx = True, q = True)
		PlayblastLogger.info(FOLDER_PATH)

		# folder = fileTools.currentBackFolder()
		# folder += r'preview\\'
		if os.path.exists( FOLDER_PATH ):
			fileTools.openContainerFile( path = FOLDER_PATH )
		else:
			PlayblastLogger.info('The file does not exist.')

		
class Ui:
	def __init__(self):
		self.function = function()
	
	def createGUI(self,*args):

		

		# Find folder and important dir
		# partFileName = mc.file( q = True , sn = True )
		scene_anim = fileTools.Scene()
		scene_anim.get_scene_name()
		partFileName = scene_anim.sceneNameFullPath

		splitfileName = partFileName.split('/')
		preName = splitfileName[ len(splitfileName)-1 ]

		# find maya extention
		MayaExt = preName.split('.')[-1]
		
		# name = preName.split( MayaExt )[0]
		name = scene_anim.sceneNameShort_noExt
		
		# PART FINDER
		path = partFileName.split('/'+name)[0]
		# add preview folder
		path += r'\\preview\\'
		# normalize path
		path = os.path.normpath( path )
		
		
		# Make a new window
		if mc.window('pbWin', exists = True):
			mc.deleteUI('pbWin')
	
		dWin = mc.window('pbWin', title=" Playblast %s" %version , iconName ='PB', widthHeight=(300, 200), s = 1, mm = 0, mxb = 0, mw = False )
		
		mc.frameLayout( label='Playblast Options',collapsable=False, mw=5, mh=5 )
		mc.columnLayout( adjustableColumn=True )
		
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 150),(2, 150)])
		
		mc.text( label='Start :', h = 20)
		mc.text( label='End :', h = 20 )
		mc.textField('startTexFld', tx = '' , h = 30)
		mc.textField('endTexFld', tx = '', h = 30 )
		
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )
		
		mc.button( label='GetTime' , command = self.function.timeLine,h=30)
		mc.button( label='SetTime' , command = self.function.setTimeLine,h=30)
		
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )

		# drop down
		mc.optionMenu( 'selRes' ,label='Resolution', w=50, h=30 )
		mc.menuItem(label='1080')
		mc.menuItem(label='720')
		
		mc.optionMenu( 'selFormat' , label=' Format', changeCommand ='print "Format Change"',w=50, h=30 )
		mc.menuItem( label = 'mp4' )
		mc.menuItem( label = 'mov' )
		mc.setParent("..")
				
		# check box
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=3, columnWidth=[(1, 110),(2, 110),(3, 75)])
		
		mc.text( label='', h = 8 )
		mc.checkBox("soundBox", l='sound', value = 1 )
		mc.checkBox("watermarkBox", l='watermark', value = 0 )
		mc.setParent("..")
		
		# FOR HUD Button
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=5, columnWidth=[(1, 5),(2, 140),(3,10),(4,140),(5,1)])
		mc.text( label='' )
		mc.button( label = 'Show HUD', command = self.function.showHUD ,h = 30)
		mc.text( label='' )
		mc.button( label = 'Delete HUD', command = self.function.deleteHUD , h = 30)
		mc.text( label='' )

		#mc.checkBox("fileNameBox", l='name', value = True )
		#mc.checkBox("userBox", l='user', value = True )
		#mc.checkBox("frameBox", l='frameCount', value = True )
		#mc.checkBox("resBox", l='res', value = True )
		
		#Create Space
		mc.text( label='', h = 8 )
		mc.text( label='', h = 8 )
		
		mc.setParent("..")
		
		# BOTTON FOR CLICK
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 50),(2, 250)])
		
		mc.text( label='Path :', h = 25 )
		mc.textField( 'pathField' , fi = path )   
		mc.text( label='Name :', h = 25 )
		mc.textField( 'nameField', fi = name )     
		
		mc.text( label='', h = 8 )
		mc.setParent("..")
		mc.columnLayout( adjustableColumn=True )
		mc.rowColumnLayout( numberOfColumns=1, columnWidth=[(1, 300),(2, 150)])

		# CONNECT FRAME
		mc.button( label = 'Connect Frame', command = self.function.setCamera ,w = 250, h = 30)
		mc.text( label ='', h = 8 )

		# FOR PLAYBLAST
		mc.button( label = 'Playblast', command = self.function.playBlast ,w=300, h=50 )
		mc.text( label ='', h = 8 )

		# FOR BROWSE
		mc.button( label = 'Open folder', command = self.function.openContainFile ,w = 250, h = 30)

		
		mc.showWindow( dWin )
	
'''
# Manual run
run = Ui()
run.createGUI()

'''