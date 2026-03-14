import importlib
import sys
import os

# Blender check
try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

# Global variable to prevent garbage collection
_blender_file_manager_window = None

# Qt Abstraction
try:
    from PySide2 import QtWidgets, QtCore
except ImportError:
    try:
        from PySide6 import QtWidgets, QtCore
    except ImportError:
        try:
            from PyQt5 import QtWidgets, QtCore
        except ImportError:
            # If no Qt found, the NameError will occur later, but at least we tried all major ones
            pass

from function.pipeline.file_manager import fileManagerCore_blender

def get_open_windows_by_name(target_name):
    app = QtWidgets.QApplication.instance()
    result = []
    if app:
        for widget in app.topLevelWidgets():
            if widget.objectName() == target_name:
                result.append(widget)
    return result

def run_file_manager():
    try:
        importlib.reload(fileManagerCore_blender)
        
        app = QtWidgets.QApplication.instance()
        if not app:
            app = QtWidgets.QApplication(sys.argv if not IN_BLENDER else [])

        open_windows = get_open_windows_by_name("FileManager")
        if open_windows:
            win = open_windows[0]
            if win.isMinimized():
                win.showNormal()
            win.raise_()
            win.activateWindow()
            return True
        else:
            global _blender_file_manager_window
            _blender_file_manager_window = fileManagerCore_blender.FileManagerBlender()
            _blender_file_manager_window.setObjectName("FileManager")
            _blender_file_manager_window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
            _blender_file_manager_window.show()
            return _blender_file_manager_window

    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_file_manager()
