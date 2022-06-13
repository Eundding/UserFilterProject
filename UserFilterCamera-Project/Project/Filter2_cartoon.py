import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Out import Out #나가기 창 임포트
from Advice import Advice # 도움말 창 임포트
from AfterStart import *
from FilterScreen import *
from RealCamera import *
import cv2
import time
from Filter2_cartoon import *
from Filter6_userFilter import *
from Filter3_Coin_1 import *
from Filter4_Coin_2 import *
from Filter5_neon import *



###################################################################################3
form_CartoonFilter = uic.loadUiType("FilterScreen_other.ui")[0]
class CartoonFilter(QDialog,QWidget,form_CartoonFilter):
    def __init__(self):
        super(CartoonFilter,self).__init__()
        self.initUI()
        self.show()
        # basic setting
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("FilterScreen_new.png")
        self.label.setPixmap(self.qPixmapFileVar)
    def initUI(self):
        self.setupUi(self)
        self.btn_Click.clicked.connect(self.GoToClick)
        #self.btn_different.clicked.connect(self.GoToAgain)

    def GoToClick(self): #카메라 화면으로 넘어가도록
        Filter2()
        self.loadImageFromFile()

    # def GoToAgain(self):
    #     self.close()
    #     self.aas = AS()
    #     self.aas.exec()
    #     self.show()

    # 파이큐티에 사진 띄우는 함수
    def loadImageFromFile(self):
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("C:\\Users\\dkan9\\PycharmProjects\\camera_project\\Gallery\\self camera cartoon.jpg")
        self.label_2.setPixmap(self.qPixmapFileVar)
        self.label_2.setAlignment(Qt.AlignVCenter)
        self.label_2.setAlignment(Qt.AlignHCenter)