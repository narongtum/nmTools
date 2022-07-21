from axionTools.rigging import kneeLock as kl
reload(kl)

from axionTools.rigging.util import misc as misc
reload(misc)

from axionTools.pipeline import fileTools as fileTools 
reload(fileTools)



def runLock(nameUPR,namePov,nameLWR,stretchNode,upperJnt,lowerJnt):
	nameUPR = kl.createDistance( nameUPR , namePov )
	nameLWR = kl.createDistance( namePov , nameLWR )


	node = kl.createBlendColor( 
										name 		= nameUPR[0] 			, 
										uprDistance = nameUPR[2]			, 
										lwrDistance = nameLWR[2] 			,
										uprNam 		= nameUPR[4]			,
										side 		=  nameUPR[5]              
									)


	namLock = kl.doAddAttr( nameUPR[6] , nameLWR[4])

	kl.distJnt( 
					stretchNode		= 		stretchNode 			, 
					upperJnt		= 		upperJnt				, 
					lowerJnt 		= 		lowerJnt	 			, 
					blendName		=		node[0]      	   		,
					namLock         =     	namLock           		,
					povName         =     	nameUPR[6]
				)



	kl.arrangeGrp(
					nameGrp		=	nameUPR[3]	,    
					side		=	nameUPR[5]	,
					distanceName=	nameUPR[2]	,
					uprLoc		=	nameUPR[7]	,
					lwrLoc		=	nameUPR[8]	
					
	)


	kl.arrangeGrp(
					nameGrp		=	nameLWR[3]	,    
					side		=	nameLWR[5]	,
					distanceName=	nameLWR[2]	,
					uprLoc		=	nameLWR[7]	,
					lwrLoc		=	nameLWR[8]	
					
	)

'''
from axionTools.rigging import kneeLockCmds as run

run.runLock(			nameUPR = 'shoulderLFT_null_grp',
						namePov = 'armLFT_pov_ctrl',
						nameLWR = 'handLFT_IK_ctrl',
						stretchNode = 'armStretchLFT_pma',
						upperJnt = 'lowerArmLFT_IK_jnt',
						lowerJnt = 'handLFT_IK_jnt')
'''