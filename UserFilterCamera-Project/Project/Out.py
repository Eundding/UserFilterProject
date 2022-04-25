import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

form_Out = uic.loadUiType("나가기.ui")[0]
class Out(QDialog,QWidget,form_Out):
    def __init__(self):
        super(Out,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.No_button.clicked.connect(self.home)
        self.Yes_button.clicked.connect(self.RealOut)

    def home(self):
        self.close()

    def RealOut(self):
        self.app.exec_()
