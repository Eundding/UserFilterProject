import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

from_Advice = uic.loadUiType("Advice.ui")[0]
class Advice(QDialog,QWidget,from_Advice):
    def __init__(self):
        super(Advice,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.OK_button.clicked.connect(self.home)

    def home(self):
        self.close()
