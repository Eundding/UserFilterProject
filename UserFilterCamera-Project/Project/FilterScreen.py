import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

form_FS = uic.loadUiType("FilterScreen.ui")[0]
class FS(QDialog,QWidget,form_FS):
    def __init__(self):
        super(FS,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.btn_Gallery.clicked.connect(self.GoToGallery)
        self.btn_Click.clicked.connect(self.GoToClick)
        self.btn_different.clicked.connect(self.GoToAgain)


    def GoToGallery(self):
        self.close()

    def GoToClick(self):
        self.close()

    def GoToAgain(self):
        self.close()

