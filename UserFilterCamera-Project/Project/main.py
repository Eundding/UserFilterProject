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

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("newnew_pyClick.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button_Start) # 시작하기
        self.btn_2.clicked.connect(self.button_Advice) # 도움말
        self.btn_3.clicked.connect(self.button_Out)  # 나가기
        #self.takenPicture() #찍은 사진 업로드
        self.loadImageFromFile()

    # btn_1이 눌리면 작동할 함수
    def button_Start(self):
        self.close()
        self.aas = AS()
        self.aas.exec()
        self.show()

    def button_Advice(self):
        self.close()
        self.advice = Advice()
        self.advice.exec()
        self.show()

    def button_Out(self):
        self.out = Out()
        self.out.exec()
        self.show()

    def loadImageFromFile(self):
    # QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("firstscreen_re.png")
        self.label.setPixmap(self.qPixmapFileVar)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
