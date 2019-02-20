#coding:utf8

import os
from PySide2.QtWidgets import *

class CheckEnv(QWidget):
	layout = QVBoxLayout()
	def __init__(self):
		super(CheckEnv, self).__init__()
		self.setLayout(self.layout)
		self.setEnv()

	def setEnv(self):
		envs = ["USER","OCIO","NUKE_PATH","NUKE_FONT_PATH"]
		for e in envs:
			self.layout.addWidget(QLabel("$%s : %s" % (e, os.environ.get(e,""))))

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = CheckEnv()
	try:
		customApp.show()
	except:
		pass





#import os
#import nuke

#def main():
	#nuke.message("$USER : %s \n$NUKE_PATH : %s \n$NUKE_FONT_PATH : %s \n$OCIO : %s" % (os.environ['USER'], os.environ['NUKE_PATH'], os.environ['NUKE_FONT_PATH'], os.environ['OCIO']))

#스앵님코드 
#	result = []
#	envs = ["USER","OCIO","NUKE_PATH","NUKE_FONT_PATH"]
#	for e in envs:
#		results.append("$%s : %s" % (e,os.environ[e]))
#	nuke.message("\n".join(results))
