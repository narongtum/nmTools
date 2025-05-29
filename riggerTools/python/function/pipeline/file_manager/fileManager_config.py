#... Put this file to ...\Documents\maya\scripts
#... Path file for file manager

DRIVES = [      "D:\\",
				"E:\\"      ]

PROJECT_NAME = ['P_RP','P_Regulus','P_jobby']

DICTIONARY_TEMPLATE = {     

							"base_path":""              ,
							"entitie_type":""           ,
							"entitie_name":""           ,
							"full_entity_name":""       ,
							"comment":""                ,
							"department_name":""        ,
							"add_path_SVN":""

							}

BASE_FOLDER = "svn_true"
ASSET_TOP_FOLDER = "Content"
SCENE_TOP_FOLDER = "Sequence"

THUMBNAIL_NAME      =   'thumb.png'
# DEPT_NAME         =   ['Model', 'Rig']
DEPT_NAME           =   ['Model', 'Rig', 'Anim']
# DEPT_EMPTY        =   ['ConceptArt', 'ConceptArt', 'Texture', 'VFX', 'Anim']
DEPT_EMPTY          =   ['Commit','Texture', 'ConceptArt','FBX']
JOB_TEMPLATE        =   ['Version', 'Data', 'Output', 'Commit', 'FBX']
EXCLUDE_VIEW_ITEM   =   ['data.json', THUMBNAIL_NAME, 'Commit']
STATIC_FOLDER       =   [ASSET_TOP_FOLDER, 'Version', 'Commit']
DEFAULT_PROJECT     =   'P_Regulus'
PADDING             =   4
MAYA_EXT            =   'ma'
USE_VARIATION       =   ('P_Regulus')
SVN_BIN_PATH        = r"C:\Program Files\TortoiseSVN\bin"
HIDE_FORMAT = ['*.pyc', '*.o','*.png','.mayaSwatches']



GROUP_NAMES = ('Model_grp', 'Export_grp')

PROJECT_DETAIL = {
	"P_LEGO": {
		"typeNum": "1",
		"FILE_01_NAMING_REPLACE": "Rig",
		"FILE_01_NAMING_WITH": "Gameplay_Model",
		"FILE_02_NAMING_REPLACE": "Rig",
		"FILE_02_NAMING_WITH": "Character_Model"
	},
	"P_Regulus": {
		"typeNum": "2",
		"FILE_01_NAMING_REPLACE": "Rig",
		"FILE_01_NAMING_WITH": "Gameplay_Model",
		"FILE_02_NAMING_REPLACE": "Rig",
		"FILE_02_NAMING_WITH": "Character_Model"
	},
	"P_RP": {
		"typeNum": "1",
		"FILE_01_NAMING_REPLACE": "Rig",
		"FILE_01_NAMING_WITH": "SK",
	}

}

