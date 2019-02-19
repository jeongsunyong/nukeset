#coding:utf8
import nuke
import os
import re
import sys


#def checkError():
#	nodes = nuke.selectedNodes()
#	if len(nodes) != 1:
#		nuke.message("please select one node.")
#	else:
#		r = re.findall('(\w+[^\d])',nodes[0].name())
#		if (r[0] == "Read" 
#		or r[0] == "Write"
#				) :
#			return 1
#		nuke.message("No Read node.")
#	return 0

brws = "nautilus"
def checkError():
	nodes = nuke.selectedNodes()
	if len(nodes) != 1:
		nuke.message("please select one node.")
	else:
		path = nodes[0].knob('file').getValue()
		if path != "":
			return 1
		nuke.message("No path to read.")
	return 0
def browser():
	if sys.platform == "wind32":
		brws = "start"
	elif sys.platform == "darwin":
		brws = "open"

def fileOpen():
	node = nuke.selectedNode()
	path = node["file"].value()
	os.system("%s %s" % (brws, os.path.dirname(path)))

def main():
	result = checkError()
	if result==1:
		browser()
		fileOpen()
	
# 1.노드 1개선택 아니거나 Read노드아닌경우 에러판단
# 2.경로 윈도우/맥/리눅스 체크
# 3.파일오픈
