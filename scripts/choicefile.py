#coding:utf8
import nuke
from PySide2.QtWidgets import *
import glob
import re
import os

class ChoiceFile(QWidget):
        files = glob.glob("/project/circle/in/" + "/**/*")
        def __init__(self):
                super(ChoiceFile,self).__init__()

                self.ok = QPushButton("OK")
                self.cancel = QPushButton("Cancel")
                self.fl = QComboBox()
                self.fl.addItems(self.files)

                self.ok.clicked.connect(self.bt_ok)
                self.cancel.clicked.connect(self.close)
                self.fl.currentIndexChanged.connect(self.indexChanged)
                
                layout=QGridLayout()
                layout.addWidget(QLabel("file"),0,0)
                layout.addWidget(self.fl,0,1)
                layout.addWidget(self.cancel,1,0)
                layout.addWidget(self.ok,1,1)
                
                self.setLayout(layout)
                
        def indexChanged(self):
                self.reformatSize=self.fl.currentText()
                
        def bt_ok(self):
                path = self.fl.currentText()
                f = re.findall('/project/circle/in/\w+/(\S[^/]+)',path)
                ext = os.path.splitext(os.listdir(path)[0])[1]
                read = nuke.nodes.Read(file="%s.######%s" % (path,ext))
                read["1001"].setValue(start)
                read["1001"].setValue(end)
                self.close()


def main():

        global customApp
        try:
                customApo.close()
        except:
                pass
        customApp = ChoiceFile()
        try:
                customApp.show()
        except:
                pass
