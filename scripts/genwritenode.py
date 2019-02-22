#coding:utf8
import nuke
from PySide2.QtWidgets import *

class MakeWrite(QWidget):
	formats = ["2048x1152","1920x1080","2048x872"]
	exts = [".exr",".dpx",".tga",".mov"]
	inputexts=""
	inputwidth=0
	inputhieght=0
	order=[]
	
	def __init__(self):
		super(MakeWrite,self).__init__()
		#option
			#OK/cancel button
		self.ok = QPushButton("OK") #ok선언
		self.cancel = QPushButton("Cancel") #cancel선언
			#ext op
		self.ext = QComboBox() #ext선언
		self.ext.addItems(self.exts) # ext에 확장자명 옵션들 추가
			#reformat size op
		self.fm = QComboBox() #format선언(size)
		self.fm.addItems(self.formats) # fm에 사이즈명 옵션들 추가
			#reformat gen op
		self.reformat = QCheckBox("&reformat", self) # reformat 체크박스
		self.reformat.setChecked(True) #default checked
			#slate gen op
		self.slate = QCheckBox("&slate", self) #slate 체크박스
		self.slate.setChecked(True) #default checked

		
		#event
		self.ok.clicked.connect(self.bt_ok) #ok를 클릭하면 bt_ok호출
		self.fm.currentIndexChanged.connect(self.indexChanged) #현재 선택된 아이템 변경시 indexchanged호출
		self.cancel.clicked.connect(self.close) #cancel을 클릭하면 close
		

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
		self.reformatSize = self.fm.currentText() #현재 선택된 문자열 저장

	def bt_ok(self):
		#print self.fm.currentText()
		#print self.ext.currentText()
		#print self.reformat.isChecked()
		#print self.slate.isChecked()
		inputext = self.ext.currentText().replace(".","")
		inputwidth=(self.fm.currentText().split('x'))[0]
		inputheight=(self.fm.currentText().split('x'))[1]
#		if self.reformat.isChecked()
#			
#		if self.slate.isChecked()
#			
#		genWrite()
#		self.close()

	def checkError():
		nodes = nuke.selectedNodes()
		if len(nodes) == 0:
			nuke.message("please select node.")
			return 0;
		else:
			return 1;

	def genWrite(node):
		w = nuke.node.Write()
		w["file_type"].setValue(inputext)
		w["create_directories"].setValue(True)
		w["file"].setValue("/test/test.####%s" % (inputext))
#		w.setInput(0,#다음순서)
#	def genSlate(node):
		s = nuke.node.slate()
#		s.setInput(0,#다음순서)
	def genTimecode(node):
		m = nuke.node.AddTimeCode()
		m["startcode"].setValue("01:00:00:00")
		m["usrFrame"].setValue(True)
		m["frame"].setValue[1001]
#		m.setInput(0,#다음순서)
	def genReformat():
		r = nuke.node.Reformat()
		r["box_width"].setValue(inputwidth)
	#	r["box_height"].setValue(#inputheight)
		r["box_fixed"].setValue(True)
		r["type"].setValue("to box")	
#		r.setInput(0,#다음순서)

	def genNodes():
		nodes = nuke.selectedNodes()
		
		for e in nodes: 
			tail = e


	

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
	except:
		pass

#r=nuke.nodes.Reformat() 값을 넣어서 하면 하나씩만됨
#체크한거 값을 받아서 변수를 넣으려는데 전역변수로 해도 적용이 안되고 genNodes클래스만들어도안되서 생각해보기
#그냥 값 대입하면 되긴 되는데 체크한걸 받아와서 다른 함수에서 그 값을 쓰는 방법 생각해보기
