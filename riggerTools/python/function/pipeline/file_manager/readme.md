Blender FileManager Walkthrough
I have implemented a dedicated version of the FileManager for Blender. This tool allows you to manage your Blender project files using the same folder structure and SVN integration as the Maya version.

New Files Created
fileManagerCore_blender.py
: The core logic for Blender.
run_ui_blender.py
: The launcher script for Blender.
Key Features
Same Project Structure: Uses the same 
Asset
, Version, Commit, and data.json logic.
Blender Native Operations:
Open: Opens .blend files with a dirty check.
Save/Publish: Saves to Version or Commit folders using bpy.ops.wm.save_as_mainfile.
Link (Reference): Links collections from external .blend files into the current scene.
SVN Integration: Full support for TortoiseSVN commands (Add, Commit, etc.) via the existing project logic.
Clean UI: Stripped of Maya-specific rigging tools to keep the interface focused on file management.
How to use in Blender
Open Blender.
Open the Scripting tab.
Paste and run the following code:
python
import sys
import os
# Add the path to your tools directory
tools_path = r'd:\sysTools\nmTools_github\riggerTools\python'
if tools_path not in sys.path:
    sys.path.append(tools_path)
from function.pipeline.file_manager import run_ui_blender
run_ui_blender.run_file_manager()
The File Manager window will appear, and you can start managing your Blender assets.
NOTE

Ensure you have PySide2 or PyQt5 installed in your Blender's Python environment.