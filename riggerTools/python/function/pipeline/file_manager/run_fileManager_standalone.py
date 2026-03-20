import sys
import os

tools_path = r'd:\sysTools\nmTools_github\riggerTools\python'
if tools_path not in sys.path:
	sys.path.append(tools_path)


from function.pipeline.file_manager import run_ui_standalone
run_ui_standalone.run_file_manager()

