#coding:utf8
import os
import nuke

def main():
	#nuke.message("$USER : %s \n$NUKE_PATH : %s \n$NUKE_FONT_PATH : %s \n$OCIO : %s" % (os.environ['USER'], os.environ['NUKE_PATH'], os.environ['NUKE_FONT_PATH'], os.environ['OCIO']))

#스앵님코드 
	result = []
	envs = ["USER","OCIO","NUKE_PATH","NUKE_FONT_PATH"]
	for e in envs:
		results.append("$%s : %s" % (e,os.environ[e]))
	nuke.message("\n".join(results))
