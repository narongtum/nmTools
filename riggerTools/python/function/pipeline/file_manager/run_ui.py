from PySide2 import QtWidgets
import importlib
from function.pipeline.file_manager import fileManagerCore

if __name__ == "__main__":
    try:
        importlib.reload(fileManagerCore)

        app = QtWidgets.QApplication.instance()
        if not app:
            app = QtWidgets.QApplication([])

        fileBrowser = fileManagerCore.FileManager()
        fileBrowser.show()
        print("Starting event loop...")
        app.exec_()

    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()
        sys.exit(-1)
