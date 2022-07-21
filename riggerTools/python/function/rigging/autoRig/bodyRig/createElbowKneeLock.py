from function.rigging.autoRig.bodyRig import midLockModule
reload( midLockModule )

charName = ''
elem = ''

newnameUPR, newnameLWR, uprDistance, newnameUPR, newnameLWR  ,newnameLWR ,endP ,uprLoc ,lwrLoc = midLockModule.createDistance( charName , elem , startP = 'upperArmFkLFT_ctrl' , endP = 'elbowLFT_ctrl' )