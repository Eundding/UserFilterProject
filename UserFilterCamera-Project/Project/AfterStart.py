import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from Out import Out #나가기 창 임포트
from Advice import Advice # 도움말 창 임포트
from AfterStart import *
from FilterScreen import *
from RealCamera import *


form_AS = uic.loadUiType("AfterStart.ui")[0]
class AS(QDialog,QWidget,form_AS):
    def __init__(self):
        super(AS,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.btn_Filter1.clicked.connect(self.F3)
        self.btn_Filter2.clicked.connect(self.F2)
        self.btn_Filter3.clicked.connect(self.F3)

    def F2(self):
        self.close()
        self.fs = FS()
        self.fs.exec()
        self.show()

    def F3(self):
        self.close()
        self.fs = FS()
        self.fs.exec()
        self.show()


    # def F2(self):


