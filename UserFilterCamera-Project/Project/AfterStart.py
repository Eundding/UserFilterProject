import sys
import cv2
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from Out import Out #나가기 창 임포트
from Advice import Advice # 도움말 창 임포트
from AfterStart import *
from FilterScreen import *
from RealCamera import *
from Filter1_cartoon import *
from Filter2_gradient import *
from Filter6_userFilter import *

form_AS = uic.loadUiType("AfterStart.ui")[0]
class AS(QDialog,QWidget,form_AS):
    def __init__(self):
        super(AS,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.btn_Filter1.clicked.connect(self.Filter1)
        self.btn_Original.clicked.connect(self.original)
        self.btn_Filter3.clicked.connect(self.Filter2)
        self.btn_Filter6.clicked.connect(self.Filter6)

 ########################################################################################
    def Filter1(self):
        self.f1 = F1()
        self.f1.exec()
        self.show()

    def original(self):
        self.fs = FS()
        self.fs.exec()
        self.show()

    def Filter2(self):
        self.f2 = F2()
        self.f2.exec()
        self.show()

    def Filter6(self):
        self.FR = FilterRyan()
        self.FR.exec()
        self.show()




