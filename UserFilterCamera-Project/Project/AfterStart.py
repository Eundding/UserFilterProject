import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic
from FilterScreen import *

form_AS = uic.loadUiType("AfterStart.ui")[0]
class AS(QDialog,QWidget,form_AS):
    def __init__(self):
        super(AS,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.btn_Filter1.clicked.connect(self.F1)
        self.btn_Filter2.clicked.connect(self.F1)
        self.btn_Filter3.clicked.connect(self.F1)



    def F1(self):
        self.close()
        self.fs = FS()
        self.fs.exec()
        self.show()


