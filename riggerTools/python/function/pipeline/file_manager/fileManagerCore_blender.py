# Qt Abstraction to support PySide2 or PySide6
try:
    from PySide2 import QtWidgets, QtGui, QtCore
    from PySide2.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMenu, QInputDialog, QMessageBox, QAction
    from PySide2.QtCore import Qt, QSize, QDir, QSortFilterProxyModel
    from PySide2.QtGui import QIcon, QPixmap
except ImportError:
    try:
        from PySide6 import QtWidgets, QtGui, QtCore
        from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMenu, QInputDialog, QMessageBox
        from PySide6.QtGui import QAction, QIcon, QPixmap
        from PySide6.QtCore import Qt, QSize, QDir, QSortFilterProxyModel
        # Handle Some PySide6 differences if needed
    except ImportError:
        # Fallback if neither is installed
        pass

import json
import os
import subprocess
import sys
import re
import fnmatch
import logging

import bpy

# UI Shim to make fileManagerMainUI (PySide2) compatible with PySide6
if 'PySide6' in sys.modules:
    import PySide6.QtWidgets as QtWidgets
    import PySide6.QtGui as QtGui
    import PySide6.QtCore as QtCore
    # Add PySide2 module to sys.modules pointing to PySide6 to fool the generated UI
    sys.modules['PySide2'] = sys.modules['PySide6']
    sys.modules['PySide2.QtWidgets'] = sys.modules['PySide6.QtWidgets']
    sys.modules['PySide2.QtGui'] = sys.modules['PySide6.QtGui']
    sys.modules['PySide2.QtCore'] = sys.modules['PySide6.QtCore']

# UI Import
try:
    from function.pipeline.file_manager.file_manager_ui import fileManagerMainUI
except ImportError:
    # If standard import fails, try to find it relative to current script
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)
    from function.pipeline.file_manager.file_manager_ui import fileManagerMainUI

# Logger setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("FileManagerBlender")

# --- Config and Constants ---
user_home = os.path.expanduser("~")
config_directory = os.path.join(user_home, 'Documents', 'maya', 'scripts') # Reusing existing config location
config_file = 'fileManager_config.py'
file_path = os.path.join(config_directory, config_file)

CORE_VERSION = '0.9.6-blender'
THUMBNAIL_NAME = 'thumb.png'
PADDING = 4

if os.path.exists(file_path):
    if config_directory not in sys.path:
        sys.path.append(config_directory)
    try:
        import fileManager_config as config
        DRIVES = config.DRIVES
        PROJECT_NAME = config.PROJECT_NAME
        DICTIONARY_TEMPLATE = config.DICTIONARY_TEMPLATE
        BASE_FOLDER = config.BASE_FOLDER
        ASSET_TOP_FOLDER = config.ASSET_TOP_FOLDER
        SCENE_TOP_FOLDER = config.SCENE_TOP_FOLDER
        DEPT_NAME = config.DEPT_NAME
        DEPT_EMPTY = config.DEPT_EMPTY
        JOB_TEMPLATE = config.JOB_TEMPLATE
        EXCLUDE_VIEW_ITEM = config.EXCLUDE_VIEW_ITEM
        STATIC_FOLDER = config.STATIC_FOLDER
        DEFAULT_PROJECT = config.DEFAULT_PROJECT
        USE_VARIATION = config.USE_VARIATION
        SVN_BIN_PATH = config.SVN_BIN_PATH
        HIDE_FORMAT = config.HIDE_FORMAT
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        # Default Fallbacks
        DRIVES = ["D:\\", "E:\\"]
        PROJECT_NAME = ['P_sample','P_Regulus']
        BASE_FOLDER = "svn_true"
        ASSET_TOP_FOLDER = "Content"
        SCENE_TOP_FOLDER = "Sequence"
        DEFAULT_PROJECT = 'P_Regulus'
        SVN_BIN_PATH = r"C:\Program Files\TortoiseSVN\bin"
else:
    # Default Fallbacks
    DRIVES = ["D:\\", "E:\\"]
    PROJECT_NAME = ['P_sample','P_Regulus']
    DICTIONARY_TEMPLATE = {"base_path":"","entitie_type":"","entitie_name":"","full_entity_name":"","comment":"","department_name":"","add_path_SVN":""}
    BASE_FOLDER = "svn_true"
    ASSET_TOP_FOLDER = "Content"
    SCENE_TOP_FOLDER = "Sequence"
    DEPT_NAME = ['Model', 'Rig', 'Anim']
    DEPT_EMPTY = ['Commit','Texture', 'ConceptArt','FBX']
    JOB_TEMPLATE = ['Version', 'Data', 'Output', 'Commit', 'FBX']
    EXCLUDE_VIEW_ITEM = ['data.json', THUMBNAIL_NAME, 'Commit']
    STATIC_FOLDER = [ASSET_TOP_FOLDER, 'Version', 'Commit']
    DEFAULT_PROJECT = 'P_Regulus'
    USE_VARIATION = ('P_Regulus')
    SVN_BIN_PATH = r"C:\Program Files\TortoiseSVN\bin"
    HIDE_FORMAT = ['*.pyc', '*.o']

BLENDER_EXT = 'blend'

class SvnBlender:
    def execute_cmd(self, cmd_type, file_path, close_on_end, add_fixed_folder=False, logmsg=''):
        file_path = os.path.normpath(file_path)
        if add_fixed_folder == False:
            command_line = r'cd "{0}" && TortoiseProc.exe /command:{1} /path:"{2}" /logmsg:"{4}" /closeonend:{3}'.format(SVN_BIN_PATH, cmd_type, file_path, close_on_end, logmsg )
        else:
            command_line = r'cd "{0}" && TortoiseProc.exe /command:{1} /path:"{2}" /closeonend:{3} --depth=files /nodlg'.format(SVN_BIN_PATH, cmd_type, file_path, close_on_end)
        subprocess.run(command_line, shell=True)

class FileManagerBlender(fileManagerMainUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(FileManagerBlender, self).__init__()
        self.setupUi(self)
        self.path = None
        
        # Asset Model setup
        self.asset_fs_model = QtWidgets.QFileSystemModel(self)
        self.asset_proxy = QtCore.QSortFilterProxyModel(self)
        self.asset_proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.asset_proxy.setFilterKeyColumn(0)
        if hasattr(self.asset_proxy, "setRecursiveFilteringEnabled"):
            self.asset_proxy.setRecursiveFilteringEnabled(True)

        self.setObjectName("FileManager")
        self.setWindowTitle(f"Blender File Manager {CORE_VERSION}")
        self.svn_tool = SvnBlender()

        self.populate_drives()
        self.populate_project()
        self.drive_comboBox.setCurrentText(DRIVES[0])
        self.project_comboBox.setCurrentText(DEFAULT_PROJECT)

        self.setupMenuBar()
        self.entite_TAB.setCurrentIndex(0)  
        self.drive_comboBox.currentIndexChanged.connect(self.update_project_comboBox)
        self.populate_ASSET_treeView()
        self.project_comboBox.currentIndexChanged.connect(self.populate_ASSET_treeView)	

        # Detection of current file
        current_scene = bpy.data.filepath
        if current_scene:
            current_scene = os.path.normpath(current_scene)
            path_elements = current_scene.split(os.path.sep)
            # Try to match project
            for proj in PROJECT_NAME:
                if proj in path_elements:
                    self.project_comboBox.setCurrentText(proj)
                    break
            current_drive = os.path.splitdrive(current_scene)[0] + os.sep
            if current_drive in DRIVES:
                self.drive_comboBox.setCurrentText(current_drive)

        self.asset_dir_TREEVIEW.clicked.connect(self.on_treeview_clicked)
        self.asset_department_listWidget.itemClicked.connect(self.on_department_clicked)
        self.populate_SCENE_treeView()
        self.dir_scene_TREEVIEW.clicked.connect(self.on_treeview_SCENE_clicked)
        self.asset_global_listWidget.itemClicked.connect(self.on_glogal_commit_clicked)

        # Context Menus
        self.asset_department_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.asset_department_listWidget.customContextMenuRequested.connect(self.show_job_context_menu)
        self.asset_version_view_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.asset_version_view_listWidget.customContextMenuRequested.connect(self.show_step_context)
        self.asset_global_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.asset_global_listWidget.customContextMenuRequested.connect(self.handle_right_click_global_widget)
        self.asset_local_view_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.asset_local_view_listWidget.customContextMenuRequested.connect(self.handle_right_click_local_widget)
        self.asset_dir_TREEVIEW.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.asset_dir_TREEVIEW.customContextMenuRequested.connect(self.show_context_menu)

        # Double Clicks
        self.asset_version_view_listWidget.itemDoubleClicked.connect(self.handle_double_click)
        self.asset_local_view_listWidget.itemDoubleClicked.connect(self.handle_double_click_local_widget)
        self.asset_global_listWidget.itemDoubleClicked.connect(self.handle_double_click_global_widget)

        # Buttons
        self.asset_localCommit_BTN.clicked.connect(self.push_btn_local_publish)
        self.asset_commit_BTN.clicked.connect(self.push_btn_global_publish)

        self.check_exists_blender()

    def setupMenuBar(self):
        file_menu = self.menuFile
        create_thumbnail_action = QAction("Create Thumbnail", self)
        create_thumbnail_action.triggered.connect(self.create_thumbnail)
        file_menu.addAction(create_thumbnail_action)

        link_ref_action = QAction("Link Selected Collection", self)
        link_ref_action.triggered.connect(self.linkSelectedReference)
        file_menu.addAction(link_ref_action)

    def linkSelectedReference(self):
        item = self.asset_global_listWidget.currentItem()
        if not item:
            QMessageBox.warning(self, "No Selection", "Please select a file.")
            return
        filepath = self.get_deep_path_global_commit()
        if not os.path.exists(filepath): return

        # Blender Link Logic
        try:
            with bpy.data.libraries.load(filepath, link=True) as (data_from, data_to):
                data_to.collections = data_from.collections
            for coll in data_to.collections:
                if coll:
                    bpy.context.scene.collection.children.link(coll)
            logger.info(f"Linked collections from {filepath}")
        except Exception as e:
            QMessageBox.critical(self, "Link Failed", str(e))

    def handle_double_click(self, item):
        file_path = self.get_deep_path()
        if bpy.data.is_dirty:
            reply = QMessageBox.question(self, 'Save Changes', 'Unsaved changes. Save first?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                bpy.ops.wm.save_mainfile()
            elif reply == QMessageBox.Cancel:
                return
        bpy.ops.wm.open_mainfile(filepath=file_path)
        self.check_exists_blender()

    def create_thumbnail(self):
        filepath = bpy.data.filepath
        if not filepath:
            QMessageBox.warning(self, "Warning", "Save file first!")
            return
        
        # Determine save directory (simplified logic from Maya version)
        save_dir = os.path.dirname(filepath)
        save_path = os.path.join(save_dir, THUMBNAIL_NAME)
        
        # Blender Render Thumbnail
        bpy.context.scene.render.filepath = save_path
        bpy.ops.render.opengl(write_still=True)
        logger.info(f"Thumbnail created at {save_path}")

    def push_btn_global_publish(self):
        original_filepath = bpy.data.filepath
        asset_path = self._get_full_path()
        dept_item = self.asset_department_listWidget.currentItem()
        if not dept_item: return
        department = dept_item.text()
        
        global_folder = os.path.normpath(os.path.join(asset_path, STATIC_FOLDER[2]))
        asset_name = os.path.basename(asset_path)
        publish_name = f"{asset_name}_{department}.{BLENDER_EXT}"
        save_full_path = os.path.join(global_folder, publish_name)

        reply = QMessageBox.question(self, 'Confirm Publish', f'Publish to Global Commit?\n{publish_name}', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            bpy.ops.wm.save_as_mainfile(filepath=save_full_path)
            if original_filepath:
                bpy.ops.wm.open_mainfile(filepath=original_filepath)
            self.load_global_commit(global_folder)

    def push_btn_local_publish(self):
        original_filepath = bpy.data.filepath
        if not original_filepath: return
        
        asset_path = self._get_full_path()
        dept_item = self.asset_department_listWidget.currentItem()
        if not dept_item: return
        department = dept_item.text()
        
        local_folder = os.path.normpath(os.path.join(asset_path, department, STATIC_FOLDER[2]))
        file_name = os.path.basename(original_filepath)
        save_full_path = os.path.join(local_folder, file_name)

        reply = QMessageBox.question(self, 'Confirm Publish', f'Publish to Local Commit?\n{file_name}', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            bpy.ops.wm.save_as_mainfile(filepath=save_full_path)
            bpy.ops.wm.open_mainfile(filepath=original_filepath)
            self.load_local_commit(local_folder)

    # --- Help Methods Ported from Maya version ---
    def populate_drives(self):
        self.drive_comboBox.clear()
        self.drive_comboBox.addItems(DRIVES)

    def populate_project(self):
        self.project_comboBox.clear()
        self.project_comboBox.addItems(PROJECT_NAME)

    def update_project_comboBox(self):
        selected_drive = self.drive_comboBox.currentText()
        selected_project = self.project_comboBox.currentText()
        self.path = os.path.join(selected_drive, BASE_FOLDER, selected_project, ASSET_TOP_FOLDER)

    def populate_ASSET_treeView(self):
        self.path = os.path.join(self.drive_comboBox.currentText(), BASE_FOLDER, self.project_comboBox.currentText(), ASSET_TOP_FOLDER)
        if not os.path.exists(self.path): return
        self.asset_fs_model.setRootPath(self.path)
        self.asset_proxy.setSourceModel(self.asset_fs_model)
        self.asset_dir_TREEVIEW.setModel(self.asset_proxy)
        self.asset_dir_TREEVIEW.setRootIndex(self.asset_proxy.mapFromSource(self.asset_fs_model.index(self.path)))
        for i in range(1, 4): self.asset_dir_TREEVIEW.setColumnHidden(i, True)

    def populate_SCENE_treeView(self):
        path = os.path.join(self.drive_comboBox.currentText(), BASE_FOLDER, self.project_comboBox.currentText(), SCENE_TOP_FOLDER)
        if not os.path.exists(path): return
        self.scene_fs_model = QtWidgets.QFileSystemModel(self)
        self.scene_fs_model.setRootPath(path)
        self.dir_scene_TREEVIEW.setModel(self.scene_fs_model)
        self.dir_scene_TREEVIEW.setRootIndex(self.scene_fs_model.index(path))

    def on_treeview_clicked(self, index):
        self.asset_local_view_listWidget.clear()
        self.asset_global_listWidget.clear()
        self.asset_department_listWidget.clear()
        self.asset_version_view_listWidget.clear()
        src_index = self._asset_proxy_to_source(index)
        file_path = self.asset_fs_model.filePath(src_index)
        if os.path.isdir(file_path):
            self.load_asset_departments(file_path)
            global_commit_folder = os.path.join(file_path, STATIC_FOLDER[2])
            if os.path.exists(global_commit_folder):
                self.load_global_commit(global_commit_folder)

    def load_asset_departments(self, folder_path):
        self.asset_department_listWidget.clear()
        items = [n for n in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, n)) and n not in EXCLUDE_VIEW_ITEM]
        self.asset_department_listWidget.addItems(sorted(items))

    def on_department_clicked(self, item):
        asset_path = self._get_full_path()
        dept_text = item.text()
        version_folder = os.path.join(asset_path, dept_text, 'Version')
        self.show_version_entite(version_folder)
        local_commit_folder = os.path.join(asset_path, dept_text, STATIC_FOLDER[2])
        if os.path.exists(local_commit_folder):
            self.load_local_commit(local_commit_folder)

    def show_version_entite(self, folder):
        self.asset_version_view_listWidget.clear()
        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if not any(fnmatch.fnmatch(f, p) for p in HIDE_FORMAT)]
            self.asset_version_view_listWidget.addItems(files)

    def load_global_commit(self, folder):
        self.asset_global_listWidget.clear()
        if os.path.exists(folder):
            self.asset_global_listWidget.addItems(os.listdir(folder))

    def load_local_commit(self, folder):
        self.asset_local_view_listWidget.clear()
        if os.path.exists(folder):
            self.asset_local_view_listWidget.addItems(os.listdir(folder))

    def _get_full_path(self):
        index = self.asset_dir_TREEVIEW.currentIndex()
        src_index = self._asset_proxy_to_source(index)
        return os.path.normpath(self.asset_fs_model.filePath(src_index))

    def _asset_proxy_to_source(self, index):
        model = self.asset_dir_TREEVIEW.model()
        return model.mapToSource(index) if isinstance(model, QSortFilterProxyModel) else index

    def get_deep_path(self):
        asset_path = self._get_full_path()
        dept = self.asset_department_listWidget.currentItem().text()
        file_name = self.asset_version_view_listWidget.currentItem().text()
        return os.path.normpath(os.path.join(asset_path, dept, STATIC_FOLDER[1], file_name))

    def get_deep_path_global_commit(self):
        asset_path = self._get_full_path()
        item = self.asset_global_listWidget.currentItem()
        if not item: return ""
        return os.path.normpath(os.path.join(asset_path, STATIC_FOLDER[2], item.text()))

    def check_exists_blender(self):
        # Implementation of scene synchronization for Blender
        pass

    # Stub implementations for context menus and missing signals
    def on_treeview_SCENE_clicked(self, index): pass
    def on_glogal_commit_clicked(self): pass
    def show_job_context_menu(self, pos): pass
    def show_step_context(self, pos): pass
    def handle_right_click_global_widget(self, pos): pass
    def handle_right_click_local_widget(self, pos): pass
    def show_context_menu(self, pos): pass
    def handle_double_click_local_widget(self, item): pass
    def handle_double_click_global_widget(self, item): pass

def run():
    # In Blender, we might need to handle the event loop differently 
    # but for a floating window, standard QApplication works if an event loop exists.
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])
    
    global win
    win = FileManagerBlender()
    win.show()
    return win

if __name__ == "__main__":
    run()
