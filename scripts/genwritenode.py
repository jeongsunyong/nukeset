#coding:utf8
import nuke

def checkError():
	nodes = nuke.selectedNodes()
	if len(nodes) == 0:
		nuke.message("please select node.")
		return 0;
	else:
		return 1;


def genWriteNodes():
	nodes = nuke.selectedNodes()
	for e in nodes: 
		tail = e
		w = nuke.nodes.Write()
		w.setInput(0,tail)


def main():
	result = checkError()
	if result==1:
		genWriteNodes()
