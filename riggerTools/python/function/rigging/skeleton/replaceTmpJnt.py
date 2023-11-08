# DO NOT USE MERGE TO JOINT TOOLS



'''
from function.rigging.skeleton import replaceTmpJnt as rtj
reload(rtj)
'''



from function.framework.reloadWrapper import reloadWrapper as reloader

from function.rigging.autoRig.base import core
reloader(core)

from function.rigging.autoRig.base import rigTools
reloader( rigTools )

from function.pipeline import logger 
reloader(logger)

class utilLogger(logger.MayaLogger):
	LOGGER_NAME = "replaceTmpJnt"

def replaceTmpJnt(			nameSpace = '',
							tmpJnt = (	'tail01_tmpJnt' ,
										'tail02_tmpJnt' ,
										'tail03_tmpJnt' ,
										'tail04_tmpJnt'	)		,
							side = ''							,
							extName = 'bJnt'):

	""" Replace template joint with new ext name

	Args:
		nameSpace: name space if have.
		tmpJnt: The first parameter.
		side: side
		extName = name of last name

	Returns:
		List of the new joint

	"""

	# make raw name
	rawName = []
	for each in tmpJnt:
		if side:
			tmp = each.split('_')[0][:-3]
		else:
			tmp = each.split('_')[0]
		rawName.append(tmp)


	bJnts_list = []

	for num in range(0,len(tmpJnt)):
		tmp = core.Dag( tmpJnt[num] )
		bJnt = rigTools.jointAt( tmp )

		bJnt.name = "{0}{1}{2}_{3}".format(nameSpace,rawName[num],side,extName )
		# bJnt.name = nameSpace + rawName[num] + side + '_' + extName

		bJnts_list.append( bJnt.name  )


		if not  num == 0:
			bJnt.parent( bJnts_list[ num -1] )

	utilLogger.info('End of the replaceTmpJnt function.')
	return bJnts_list



