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


###################################################################################3
form_neonFilter = uic.loadUiType("FilterScreen_new.ui")[0]

class neonFilter(QDialog,QWidget,form_neonFilter):
    def __init__(self):
        super(neonFilter,self).__init__()
        self.initUI()
        self.show()
        # basic setting
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("FilterScreen_new.png")
        self.label.setPixmap(self.qPixmapFileVar)

    def initUI(self):
        self.setupUi(self)
        self.btn_Gallery.clicked.connect(self.GoToGallery)
        self.btn_Click.clicked.connect(self.GoToClick)
        self.btn_different.clicked.connect(self.GoToAgain)


    def GoToGallery(self): #폴더 열기 구현
        global filename
        #filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        filename = QFileDialog.getOpenFileName(self, "File Load",
                                               'C:/Users/dkan9/PycharmProjects/camera_project/Gallery', 'PNG File(*.png);; JPG File(*.jpg)')
        print(filename[0]) # 파일 경로 포함
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(filename[0])
        self.label_2.setPixmap(self.qPixmapFileVar)


    def GoToClick(self): #카메라 화면으로 넘어가도록
        Filter5()
        self.loadImageFromFile()

    def GoToAgain(self):
        self.close()

    # 파이큐티에 사진 띄우는 함수
    def loadImageFromFile(self):
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("self camera neon.jpg")
        self.label_2.setPixmap(self.qPixmapFileVar)



