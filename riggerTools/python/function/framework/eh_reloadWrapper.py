# -*- coding: utf-8 -*-
# ...
# ... DESCRIPTION: Enhanced, efficient module reloader
# ...

import sys

# --- 1. Check the version and find the correct reload function (only need to do this once) ---
# ... (We use sys.version_info[0] to check the Python version.)

if sys.version_info[0] == 3:
	# ... Python 3 (Maya 2014-2022+)
	if sys.version_info[1] >= 4:
		# ... Python 3.4+ (Maya 2017+)
		from importlib import reload as _internal_reload
		# print("ReloadWrapper: Using importlib.reload (Python 3.4+)")
	else:
		# ... Python 3.0 - 3.3 (Maya 2014-2016)
		from imp import reload as _internal_reload
		print("ReloadWrapper: Using imp.reload (Python 3.0-3.3)")
else:
	# ... Python 2 (Maya 2013-2020)
	# ... 'reload'  built-in 
	_internal_reload = reload
	print("ReloadWrapper: Using built-in reload (Python 2.7)")


def reloadWrapper(module_to_reload):
	"""
	# ... Wrap the correct reload function (found in Step 1)
	# ... to ensure it works the same across all versions
	"""
	try:
		_internal_reload(module_to_reload)
		# print(f"Reloaded: {module_to_reload.__name__}")
	except Exception as e:
		print(f"Error reloading module {module_to_reload.__name__}: {e}")

def reloadAll(modList = []):
	"""
	# ... Reloads a list of modules using the efficient wrapper.
	"""
	for mod in modList:
		reloadWrapper(mod)

