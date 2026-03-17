import os
import re

source = r"d:\sysTools\nmTools_github\riggerTools\python\function\pipeline\file_manager\fileManagerCore.py"
dest = r"d:\sysTools\nmTools_github\riggerTools\python\function\pipeline\file_manager\fileManagerCore_standalone.py"

with open(source, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Remove Maya imports
    if line.strip().startswith('import maya.') or line.strip().startswith('import pymel.'):
        new_lines.append('# ' + line)
        continue
    
    # Remove function module imports that use Maya
    if 'function.rigging' in line or 'function.pipeline.fileTools' in line or 'nsSkinClusterIO' in line:
        new_lines.append('# ' + line)
        continue

    # Mock MAYA_VERSION
    if 'MAYA_VERSION = int(mc.about(v=True))' in line:
        new_lines.append('MAYA_VERSION = 2022\n')
        continue

    # Def getMayaMainWindow
    if 'def getMayaMainWindow():' in line:
        new_lines.append(line)
        new_lines.append('\treturn None\n')
        continue
    if 'main_window_ptr =' in line or 'pointer =' in line or 'wrapInstance(' in line:
        if 'return None' not in ''.join(new_lines[-2:]):
            new_lines.append('# ' + line)
        continue
        
    # Replace mc. and pm. calls with pass or dummy
    if 'mc.' in line or 'pm.' in line or 'om.' in line or 'omui.' in line or 'mel.' in line:
        # replace the statement with a comment
        new_lines.append('# ' + line)
        continue

    if 'fileTools.' in line or 'runWrite.' in line or 'skinIO.' in line or 'jtt.' in line or 'adjust.' in line or 'rsw.' in line:
        new_lines.append('# ' + line)
        continue

    new_lines.append(line)

with open(dest, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Conversion complete.")
