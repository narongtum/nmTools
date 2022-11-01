# from function.framework.reloadWrapper import reloadWrapper as reload





'''
import importlib
maya_version = mc.about( version=True )
# --- reload ---
def python2():
	if int( maya_version ) < 2021:
		return True
	return False

def load( code ):
	if python2():
		reload( code )
	else:
		importlib.reload( code )

def reloadAll( modList = [] ):
	for mod in modList:
		load( mod )
'''

#exc
# import core
# core.load( bababa )

#or

#exc
# import core
# core.reloadAll( [ core, rigtool, rigtool2 ] )


def reloadFunction():
	try:
		reload  # Python 2.7
		print('This might be python 2.7')
	except NameError:
		try:
			from importlib import reload  # Python 3.4+
			print('Python 3.4+')
		except ImportError:
			from imp import reload  # Python 3.0 - 3.3
			print('Python 3.0 - 3.3')




# Reload module
def reloadWrapper(function):
	try:
		reload(function)
		# print('This might be Python 2.7')
	except NameError:
		try:
			from importlib import reload  # Python 3.4+
			reload(function)
			# print('This might be Python 3.4+')
		except ImportError:
			from imp import reload  # Python 3.0 - 3.3
			reload(function)
			# print('This might be Python 3.0 - 3.3')