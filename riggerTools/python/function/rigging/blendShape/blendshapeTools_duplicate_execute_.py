# run function from blendshapeTools
# Duplicate poly and create connect blendshape

from function.rigging.blendShape import blendshapeTools as bshTools
reload(bshTools)

from function.rigging.autoRig.base import core
reload(core)

from function.rigging.autoRig.base import rigTools
reload( rigTools )





# Eyebrow
eyeBrowLFT_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYEBROW_DICT , side = 'LFT')
eyeBrowRGT_dict  = bshTools.createBshToPly( bsh_dict = bshTools.EYEBROW_DICT , side = 'RGT')


# Eyeball
eyelidAll_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELIDALL_DICT , side = 'LFT')
eyelidAll_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELIDALL_DICT , side = 'RGT')


# Eyelid Up LFT
eyelidUpLFT_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELID_UP_DICT , side = 'LFT')
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpLFT_dict ,MembIndex = 0, inbIndex=0 ,weight=0.5) 
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpLFT_dict ,MembIndex = 1, inbIndex=1 ,weight=0.5)
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpLFT_dict ,MembIndex = 4, inbIndex=2 ,weight=0.5) 
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpLFT_dict ,MembIndex = 5, inbIndex=3 ,weight=0.5)
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpLFT_dict ,MembIndex = 6, inbIndex=4 ,weight=0.5) 


# Eyelid Up RGT
eyelidUpRGT_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELID_UP_DICT , side = 'RGT')
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpRGT_dict ,MembIndex = 0, inbIndex=0 ,weight=0.5) 
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpRGT_dict ,MembIndex = 1, inbIndex=1 ,weight=0.5)
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpRGT_dict ,MembIndex = 4, inbIndex=2 ,weight=0.5) 
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpRGT_dict ,MembIndex = 5, inbIndex=3 ,weight=0.5)
bshTools.connectInbetweenForPly( bsh_dict = eyelidUpRGT_dict ,MembIndex = 6, inbIndex=4 ,weight=0.5) 





# Eyelid Lo LFT
eyelidLoLFT_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELID_LO_DICT , side = 'LFT')
bshTools.connectInbetweenForPly( bsh_dict = eyelidLoLFT_dict ,MembIndex = 0, inbIndex=0 ,weight=0.5) 
bshTools.connectInbetweenForPly( bsh_dict = eyelidLoLFT_dict ,MembIndex = 1, inbIndex=1 ,weight=0.5)
# Eyelid Lo LFT
eyelidLoRGT_dict = bshTools.createBshToPly( bsh_dict = bshTools.EYELID_LO_DICT , side = 'RGT')
bshTools.connectInbetweenForPly( bsh_dict = eyelidLoRGT_dict ,MembIndex = 0, inbIndex=0 ,weight=0.5)
bshTools.connectInbetweenForPly( bsh_dict = eyelidLoRGT_dict ,MembIndex = 1, inbIndex=1 ,weight=0.5)






# Mounth mid
mounthMid_dict = bshTools.createBshToPly( bsh_dict = bshTools.LIP_ALL_DICT , side = '')
mounthLFT_dict = bshTools.createBshToPly( bsh_dict = bshTools.LIP_SIDE_DICT , side = 'LFT')
mounthRGT_dict = bshTools.createBshToPly( bsh_dict = bshTools.LIP_SIDE_DICT , side = 'RGT')


# add new

# Nose Mid
noseMid_dict = bshTools.createBshToPly( bsh_dict = NOSEALL_DICT , side = '')
# Nose Side
noseLFT_dict = bshTools.createBshToPly( bsh_dict = NOSESIDE_DICT , side = 'LFT')
noseRGT_dict = bshTools.createBshToPly( bsh_dict = NOSESIDE_DICT , side = 'RGT')

# Cheek
cheekLFT_dict = bshTools.createBshToPly( bsh_dict = CHEEK_DICT , side = 'LFT')
cheekRGT_dict = bshTools.createBshToPly( bsh_dict = CHEEK_DICT , side = 'RGT')

# Face
jaw_dict = bshTools.createBshToPly( bsh_dict = JAW_DICT , side = '')





print '''\n
	# ========================
	# - End of duplicate ply for blendshape -
	# ========================
	'''

