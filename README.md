# nmTools 🛠️
### A Comprehensive Rigging & Animation Toolset for Autodesk Maya

![Maya Version](https://img.shields.io/badge/Maya-2018--2023+-blue.svg)
![Language](https://img.shields.io/badge/Language-Python%20%2F%20MEL-yellow.svg)

**nmTools** is a curated collection of professional scripts designed to streamline the rigging and animation pipeline in Autodesk Maya. Developed to handle complex rigging tasks and daily animation workflows, it integrates both custom tools and respected open-source utilities into a unified interface.

---

## 🌟 Key Features

### 📂 Pipeline & File Management
*   **Custom File Manager**: Efficiently manage project scenes and versions.
*   **Asset Utilities**: Batch publish files, auto-thumbnail generation, and outliner organization.
*   **Texture Management**: Tools for path correction and texture search/replace.

### 🎭 Animation Tools
*   **Studio Library Integration**: Quick access to pose and animation libraries.
*   **Picker Support**: Integrated support for **DreamWall Picker** and **AnimSchool Picker**.
*   **Workflow Enhancers**: ZvParentMaster, Tweener, and Onion Skin Renderer.
*   **Technical Tools**: Snap IK/FK, Playblast Tool, and Controller Mirroring.

### 🦴 Rigging Toolset
*   **Skeleton & Joints**: Create joints at vertices, orient joints with Comet tools, and generate joints along curves.
*   **Skinning Suite**:
    *   **SkinWrangler** & **DoraWeight** integration.
    *   Custom weight import/export and smoothing tools.
    *   Recursive weight copying and rounding.
*   **Controller Generation**: Auto-create master groups, zero groups, and custom controller shapes.
*   **Blendshapes**: Advanced symmetrical and asymmetrical blendshape tools.
*   **AutoRig Templates**: Basic Biped and Quadruped joint templates to jumpstart your rigs.

---

## 📸 Previews

| File Manager | Renamer Tool |
| :---: | :---: |
| ![File Manager](riggerTools/image/sample/sample_file_manager.png) | ![Renamer](riggerTools/image/sample/sample_renamer.png) |

---

## 🚀 Installation

### 1. Repository Setup
Clone or download this repository to your preferred tools directory (e.g., `D:/sysTools/nmTools_github`).

### 2. Configure Maya
To initialize **nmTools** on startup, add the following to your `userSetup.py`:

```python
import sys
import maya.utils
import importlib

# Add the python path (Change this to your actual path)
sys.path.append('D:/sysTools/nmTools_github/riggerTools/python')

# Import and run the menu (choose the version corresponding to your Maya)
from nmMenu import nmMenu2023 
importlib.reload(nmMenu2023)
maya.utils.executeDeferred('nmMenu2023.runMenu()')
```

### 3. Requirements
*   **Autodesk Maya 2018 - 2023+**
*   **PyMEL**: Ensure PyMEL is installed with your Maya distribution.

---

## 🛠️ Usage
Once installed, a new menu **"nmMenu"** will appear in your Maya main menu bar. From there, you can access all the rigging, animation, and pipeline utilities categorized by department.

---

## 📝 How to Import Modules

To use internal modules (such as those in the `function` package) in your own scripts or other software (Maya, Blender, etc.), you must add the repository's python path to `sys.path`.

### Python Import Setup

```python
import sys
import os

# 1. Define the path to riggerTools/python
# (Change this to your actual installation path)
tools_path = r'd:\sysTools\nmTools_github\riggerTools\python'

if tools_path not in sys.path:
    sys.path.append(tools_path)

# 2. Example: Importing from the 'function' module
from function.pipeline.file_manager import fileManagerCore_standalone
# or
from function.rigging.autoRig.base import core
```

---

## 🤝 Credits
This toolset includes and integrates several amazing community tools:
*   [Studio Library](https://www.studiolibrary.com/)
*   [SkinWrangler](https://github.com/chrisevans3d/skinWrangler)
*   [ZvParentMaster](http://www.creativecrash.com/maya/script/zv-parent-master)
*   Comet Scripts by Michael Comet
*   DoraSkinWeight by Hiroki Itoh




# If file name prefix is 'eh_' is mean ai generate file


---
*Developed with ❤️ by Narongtum*
