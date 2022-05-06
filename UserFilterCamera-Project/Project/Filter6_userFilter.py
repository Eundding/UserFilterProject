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


###################################################################################3
form_FilterRyan = uic.loadUiType("FilterScreen.ui")[0]
class FilterRyan(QDialog,QWidget,form_FilterRyan):
    def __init__(self):
        super(FilterRyan,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.btn_Gallery.clicked.connect(self.GoToGallery)
        self.btn_Click.clicked.connect(self.GoToClick)
        self.btn_different.clicked.connect(self.GoToAgain)


    def GoToGallery(self): #폴더 열기 구현
        self.close()

    def GoToClick(self): #카메라 화면으로 넘어가도록
        ryan()
        self.loadImageFromFile()

    def GoToAgain(self):
        self.close()
        # self.aas = AS()
        # self.aas.exec()
        # self.show()


    # 파이큐티에 사진 띄우는 함수
    def loadImageFromFile(self):
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("self camera ryan.jpg")
        self.label_2.setPixmap(self.qPixmapFileVar)



