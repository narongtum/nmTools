import sys
import os
from PySide2 import QtWidgets, QtCore, QtGui

# Add the root directory of riggerTools to sys.path if needed
current_dir = os.path.dirname(os.path.abspath(__file__))
pipeline_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
if pipeline_dir not in sys.path:
    sys.path.append(pipeline_dir)

from function.pipeline.file_manager import fileManagerCore_standalone

def run_file_manager():
    try:
        app = QtWidgets.QApplication.instance()
        if not app:
            app = QtWidgets.QApplication(sys.argv)
            
        # Apply Dark Theme
        app.setStyle("Fusion")
        dark_palette = QtGui.QPalette()
        dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
        dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
        dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(dark_palette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

        file_browser = fileManagerCore_standalone.FileManager()
        file_browser.setObjectName("FileManagerStandalone")
        file_browser.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        file_browser.show()
        
        # Only execute app if it's the standalone instance
        if not QtWidgets.QApplication.instance().parent():
            sys.exit(app.exec_())

    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()
        sys.exit(-1)

if __name__ == '__main__':
    run_file_manager()
