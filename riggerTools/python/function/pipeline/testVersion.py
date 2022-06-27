from pathlib import Path
import os
import sys
import shutil 
# when drop what will happen
FILEPATH = r"D:\True_Axion\Project_Shelldon\Animation\Spine\Tower\Crabby_01_a\Crabby_01_a.spine"

dirName = os.path.dirname(FILEPATH)
fileName = os.path.basename(FILEPATH)


extension = os.path.splitext(fileName)[1]
extLen = len(extension)

versionDir = dirName + '\\version'



if os.path.exists(versionDir):
	print ('This folder has exists.')





allFile = os.listdir(versionDir)
spName = fileName.split('hero'+extension)[0]
workLst = []
num = 0 

for each in allFile:
	if each[-extLen:] == extension:
		# 'there is already this extension in version folder'

		if spName in each:
			# 'there is already this job in version folder'
			# 'find latest version'
			workLst.append(each)
			num = num + 1
			print (each)

		else:
			continue


	else:
		print (each)


 
if workLst:
	print ('there is already this job in version folder')
	latestFile = workLst[-1]
	# extract 
	workNam = latestFile.split(extension)[0][:-4]

	if num <= 9:
		digit = 3
	elif num > 9:
		 digit = 2

	version = num + 1
	strNum = str(version)
	replaceVer = strNum.zfill(digit)

	latestFile = workNam + 'v' + replaceVer + extension


else:
	print ('there is no job in version folder')
	latestFile = spName + 'v001' + extension
	


	 
print (versionDir + '\\' + latestFile)

# shutil.copy( FILEPATH , versionDir + '\\' + latestFile )



print ('Saving file version %s' %(latestFile))
print ( "# # # # # Convert Complete # # # # # ")