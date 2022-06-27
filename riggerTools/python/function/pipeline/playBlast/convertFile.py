import os
import subprocess

#"D:\\True_Axion\\Tools\\riggerTools\\python\\axionTools\\pipeline\\playBlast\\ffmpeg-20181016-b2adc31-win64-static\\bin\\ffmpeg.exe"
# FFMPEG convert fie V 0.2
# FFMPEG instance path
#FFMPEG = r'C:\\ffmpeg-20140629-git-8657612-win64-static\\bin\\ffmpeg.exe'

FFMPEG = r'D:\\True_Axion\\Tools\\riggerTools\\python\\axionTools\\pipeline\\playBlast\\framework\\ffmpeg-20181016-b2adc31-win64-static\\bin\\ffmpeg.exe'

logic = []

logic = raw_input("press y to continue or press anykey to exit:\n")

while logic == ('y'):

	INPUT_PATH = raw_input("Please type path file : \n")

	# find index of EXT
	indexIn = INPUT_PATH.index('.')
	# clean name contain for name only etc. noman.mov cleanIn is noman
	cleanIn = (INPUT_PATH[:indexIn])

	print (cleanIn)

	OUTPUT_PATH = cleanIn + '_small.mp4'


	#outRawPath= INPUT_PATH[:-4]
	#print(outRawPath)

	#OUTPUT_PATH = outRawPath + '_small.mov'

	#cmd ='%s -y -i %s -vcodec libx264 -vprofile baseline -crf 22 -bf 0 -pix_fmt yuv420p -f mov %s' %( FFMPEG , INPUT_PATH , OUTPUT_PATH)
	# cmd ='%s -i %s -f mp4 -vcodec libx264 -preset fast -profile:v main -acodec aac %s ' %( FFMPEG , INPUT_PATH , OUTPUT_PATH)
	ffFormat = '-acodec aac' , '-pix_fmt yuv420p'

	print '\nUsing %s format.' %ffFormat[1]
	cmd ='%s -i %s -f mp4 -vcodec libx264 -preset fast -profile:v main %s %s ' %( FFMPEG , INPUT_PATH, ffFormat[1] , OUTPUT_PATH)
	print cmd
	subprocess.call(cmd)

	print('\nconverted path file is ' +str(OUTPUT_PATH))
	logic = raw_input("\npress y to continue or press anykey to exit:\n")

else:
	print("end progress")


#ffmpeg -i example.mov -f mp4 -vcodec libx264 -preset fast -profile:v main -acodec aac example.mp4 -hide_banner
#%s -i %s -f mp4 -vcodec libx264 -preset fast -profile:v main -acodec aac %s -hide_banner
