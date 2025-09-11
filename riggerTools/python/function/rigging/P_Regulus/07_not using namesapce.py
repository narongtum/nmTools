from function.rigging.util import misc
reload(misc)
prefix = 'CH026_Firis_01_Rig_'

misc.select_hierarchy(f'{prefix}Export_grp')
misc.searchReplace( searchText = prefix, replaceText='' )


if mc.objExists(f'{prefix}facial_bsh'):
    mc.select(f'{prefix}facial_bsh',r=True)
    misc.searchReplace( searchText = prefix, replaceText='' )
    


skinName_list = mc.ls(type='skinCluster')
for each in skinName_list :
    mc.select(each,r=True)
    misc.searchReplace( searchText = prefix, replaceText='' )
    


startTime = mc.playbackOptions( min = True,q = True )
endTime = mc.playbackOptions( max = True,q = True )

endTimeReal = endTime+1


bake_range = (startTime, endTimeReal)





mc.select('*_bJnt',r=True)
mc.select('*root',add=True)

    

bake_joints = mc.ls(sl=True)
bake_attrs = ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]
mc.playbackOptions(min = startTime,max = endTimeReal)
mc.bakeResults(bake_joints, preserveOutsideKeys=True, simulation=True, t=bake_range, at=bake_attrs)



if mc.objExists(f'Face'):
    mc.select('Face',r=True)
    
mc.bakeResults('facial_bsh', preserveOutsideKeys=True, simulation=True, t=bake_range)    
    


from function.pipeline import fileTools as fileTools 
reload(fileTools)

#path=fileTools.currentFolder().replace('\\', '/')
path=fileTools.findCurrentPath(step = 'current')

fileName=fileTools.getFileName()[0]

exportCommand = 'file -force -options "v=0;" -typ "FBX export" -pr -es '
path = path.replace('\\','/')


exportFBXPath = r'"'+ path + fileName + '.fbx' '"'
exportCommand += exportFBXPath


mc.select('Export_grp',r=True)


mel.eval( exportCommand )

