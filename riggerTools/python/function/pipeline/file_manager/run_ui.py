from PySide2 import QtWidgets
import importlib
from function.pipeline.file_manager import fileManagerCore
import sys

def run_file_manager():
    try:
        importlib.reload(fileManagerCore)

        app = QtWidgets.QApplication.instance()
        if not app:
            app = QtWidgets.QApplication([])

        # storing it as an attribute of the app object which 
        # ensures it remains in scope as long as the application is running.
        app.fileBrowser = fileManagerCore.FileManager()
        app.fileBrowser.show()
        print("Starting event loop...")
        app.exec_()

    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()
        sys.exit(-1)

if __name__ == "__main__":
    run_file_manager()
