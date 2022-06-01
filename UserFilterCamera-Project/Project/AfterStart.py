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
from Filter2_cartoon import *
from Filter6_userFilter import *
from Filter3_Coin_1 import *
from Filter4_Coin_2 import *
from Filter5_neon import *


form_AS = uic.loadUiType("AfterStart_new.ui")[0]
class AS(QDialog,QWidget,form_AS):
    def __init__(self):
        super(AS,self).__init__()
        self.initUI()
        self.show()
        self.loadImageFromFile()

    def initUI(self):
        self.setupUi(self)
        self.btn_1.clicked.connect(self.original)
        self.btn_2.clicked.connect(self.cartoon)
        self.btn_3.clicked.connect(self.Coin_1)
        self.btn_4.clicked.connect(self.Coin_2)
        self.btn_5.clicked.connect(self.neon)
        self.btn_6.clicked.connect(self.userfilter)

 ########################################################################################
    def original(self): #btn_1
        self.fs = FS()
        self.fs.exec()
        self.show()

    def cartoon(self): #btn_2
        self.f2 = CartoonFilter()
        self.f2.exec()
        self.show()

    def Coin_1(self): #btn_3
        self.f3 = Coin1Filter()
        self.f3.exec()
        self.show()

    def Coin_2(self):
        self.f4 = Coin2Filter()
        self.f4.exec()
        self.show()

    def neon(self):
        self.f5 = neonFilter()
        self.f5.exec()
        self.show()

    def userfilter(self):
        self.FR = FilterRyan()
        self.FR.exec()
        self.show()

    def loadImageFromFile(self):
    # QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("AfterStart_new_re.png")
        self.label.setPixmap(self.qPixmapFileVar)




