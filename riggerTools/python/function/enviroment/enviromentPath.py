# For store all path


'''
from function.enviroment import enviromentPath as env
reload(env)

nodeDict = mnd.NODE_dict

PROJECT_NAME = env.PROJECT_NAME
'''

PROJECT_NAME = 'nmMenu_git'

REPO_PATH = r'D:/sysTools/nmTools_github/riggerTools'

SHAPE_LIBRARY_PATH = '{0}/python/function/rigging/ctrlSizeLibrary/'.format(REPO_PATH)

PLUGINS_PATH = '{0}/python/function/plugin/2018'.format(REPO_PATH)

ICON_PATH = '{0}/image'.format(REPO_PATH)

REFERENCE_PATH = '{0}/python/function/rigging/autoRig/reference/'.format(REPO_PATH)


ENVIROMENT_PATH = [
						{	'repoPath': 			r'D:/sysTools/nmTools/riggerTools'		},
						{	'pluginsPath': 			r'D:/sysTools/nmTools/riggerTools/python/function/plugin/2018'		},
						{	'iconPath': 			r'D:/sysTools/nmTools/riggerTools/image'		},
						{	'shapeLibraryPath': 	r'D:/sysTools/nmTools/riggerTools/python/function/rigging/ctrlSizeLibrary/'		},

				]