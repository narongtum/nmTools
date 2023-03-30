from function.framework.reloadWrapper import reloadWrapper as reload
from function.rigging.tools import proc as pc 
reload(pc)

import maya.cmds as mc

def cleanup():
	# clear Open VIS _ctrl
	pc.clearVis( '_ctrl', hide = False )
	pc.clearVis( '_flc', hide = True )
	pc.clearVis( '_loc', hide = True )
	_deleteTemplate()

	print ('''\n
	
			
		\t\t\t\t 	   :/     /;               _ 							
		\t\t\t\t 	  ;  /___/  ;             ; ;                  														                        
		\t\t\t\t 	 ,:-"'   `"-:.            / ;       //_/ /  /                                                          
		\t\t\t\t_   /,---.   ,---./   _     _; /        ( o   o )                        
		\t\t\t\t_:>((  |  ) (  |  ))<:_ ,-""_,"         =(  =  )=                         
		\t\t\t\t	/`````   `````/""""",-""			-  -  -
		\t\t\t\t	 '-.._ v _..-'      )                                               
		\t\t\t\t	   / ___   ____,..  \
		\t\t\t\t	  / /   | |   | ( /. \
		\t\t\t\t     / /    | |    | |  / /   	                         								
		\t\t\t\t	 `"     `"     `"    `"
		\t\t\t\t Rig 		Complete  		 Meow
		''')



def _deleteTemplate():
	if mc.objExists('template_ctrl'):
		mc.delete('template_ctrl')
		print ('Delete template joint...')
	else:
		mc.warning('There are no template joint please check.')
