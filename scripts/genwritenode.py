#coding:utf8
import nuke
from PySide2.QtWidgets import *

class MakeWrite(QWidget):
	formats = ["2048x1152","1920x1080","2048x872"]
	exts = [".exr",".dpx",".tga",".mov"]
	
	def __init__(self):
		super(MakeWrite,self).__init__()
		#option
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")
		
		self.ext = QComboBox()
		self.ext.addItems(self.exts)

		self.fm = QComboBox()
		self.fm.addItems(self.formats)

		self.reformat = QCheckBox("&reformat", self)
		self.reformat.setChecked(True)

		self.slate = QCheckBox("&slate", self)
		self.slate.setChecked(True)

		
		#event
		self.ok.clicked.connect(self.bt_ok)
		self.fm.currentIndexChanged.connect(self.indexChanged)
		self.cancel.clicked.connect(self.close)
		

		#set layout
		layout = QGridLayout()
		layout.addWidget(self.reformat, 0, 0)
		layout.addWidget(self.fm,0,1)
		layout.addWidget(QLabel("master Ext"),1,0)
		layout.addWidget(self.ext,1,1)
		layout.addWidget(self.slate,2,0)
		layout.addWidget(self.cancel,3,0)
		layout.addWidget(self.ok,3,1)

		self.setLayout(layout)

	def indexChanged(self):
		self.reformatSize = self.fm.currentText()

	def bt_ok(self):
		print self.fm.currentText()
		print self.ext.currentText()
		print self.reformat.isChecked()
		print self.slate.isChecked()
		ext = self.ext.currentText()
		self.close()

def checkError():
	nodes = nuke.selectedNodes()
	if len(nodes) == 0:
		nuke.message("please select node.")
		return 0;
	else:
		return 1;

def genNodes():
	nuke.message("%s" % (ext))
	nodes = nuke.selectedNodes()
	for e in nodes: 
		tail = e

		w = nuke.nodes.Write()
		r = nuke.nodes.Reformat()
		s = nuke.nodes.slate()
		m = nuke.nodes.AddTimeCode()

		w["file_type"].setValue("exr")
		w["create_directories"].setValue(True)
		w["file"].setValue("/test/test.####%s" % (ext))
		r["type"].setValue("to box")
		r["box_width"].setValue(2048)
		r["box_height"].setValue(968)
		r["box_fixed"].setValue(True)
		m["startcode"].setValue("01:00:00:00")
		m["useFrame"].setValue(True)
		m["frame"].setValue(1001)

		r.setInput(0,tail)
		m.setInput(0,r)
		s.setInput(0,m)
		w.setInput(0,s)


def main():

	result = checkError()
	if result != 1:
		return
	global customApp

	try:
		customApp.close()
	except:
		pass
	customApp = MakeWrite()
	try:
		customApp.show()
		nuke.message("%s" % (ext))
		genNodes()
	except:
		pass

#r=nuke.nodes.Reformat() 값을 넣어서 하면 하나씩만됨
#체크한거 값을 받아서 변수를 넣으려는데 전역변수로 해도 적용이 안되고 genNodes클래스만들어도안되서 생각해보기
#그냥 값 대입하면 되긴 되는데 체크한걸 받아와서 다른 함수에서 그 값을 쓰는 방법 생각해보기
