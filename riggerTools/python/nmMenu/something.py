# MAIN Menu
import sys
import os.path


# find variable enviroment
path = os.path.dirname(os.path.abspath(__file__))
print('this is path: {0}'.format(path))
abs_path = os.path.normpath(path)
PROJECT_PATH = abs_path.replace(r'\python\nmMenu','')
print('this is PROJECT_PATH: {0}'.format(PROJECT_PATH))

# add path
PLUGINS_PATH = PROJECT_PATH + "\\python\\function\\plugin\\2018\\"

# load plugins
#mc.loadPlugin( PLUGINS_PATH + "AnimSchoolPicker.mll", quiet = True)

# naming
PROJECT_NAME = 'nmMenu'

iconPath = PROJECT_PATH + r'\\image'
