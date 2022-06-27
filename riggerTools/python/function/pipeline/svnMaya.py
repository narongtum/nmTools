# -*- coding: utf-8 -*-
import os
import re
import logging 
import threading
import tempfile, subprocess, traceback
import maya.cmds as cmds
import pymel.core as pm
import subprocess

from function.pipeline import fileTools
reload(fileTools)

'''
from function.pipeline import svnMaya as svn 
reload(svn)
'''


class General():
	"""
	set log data just for sample study not proper use
	"""
	def __init__(self):
		pass

	def setLog(self, logLevel):
		LOG_LEVELS = {	'debug'		: logging.DEBUG,
						'info'		: logging.INFO,
						'warning'	: logging.WARNING,
						'error'		: logging.ERROR,
						'critical'	: logging.CRITICAL	}

		LOG_LEVEL = LOG_LEVELS.get(logLevel)
		logging.basicConfig(level=LOG_LEVEL)


	def log_dict(self, inputDict):
		if inputDict:
			string = ''
			try:
				string += str(inputDict)
			except:
				logging.warning('Can not convert inputDict to string.')

			for k,v in inputDict.item():
				string += '\t\t'
				string += 'key:'+str(k)+'\t'
				string += 'value:'+str(v)
			logging.debug(string)

	def log_list(self, inputList):
		if inputList:
			string = ''
			if inputList:
				try:
					string += str(inputList)
				except:
					logging.warning("can't convert inputList to string.")

				for i in inputList:
					string += '\t' + str(i)
			logging.debug(string)

		else:
			logging.debug('log_list:input is None')




def svnCommit( commit_path ):
	''' commit follow commit_path '''
	cmd = r'TortoiseProc.exe /command:commit /path:"%s"  /closeonend:0' %commit_path
	subprocess.call(cmd)
	print ('%s has been commited.' %commit_path)
	

			
def commitCurrentPath():
	path = fileTools.currentPath()

	if path!= None:
		svnCommit( path )
	else:
		print ('File not exists Please Check.')
