# 파이선 내장 라이브러리에 존재하는 sys 모듈 import
# *는 모듈을 전부 가져온다는 의미
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# QMainWindow클래스를 상속받은 MyWindow 클래스 선언
# 부모 클래스를 의미하는 super메서드, 그 클래스의 속성을 불러오는 __init__초기화 메서드 사용
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 타이틀 변경
        self.setWindowTitle("파이찰칵 GUI")
        self.setGeometry(300,300,400,400)
        self.setWindowIcon(QIcon("web.png"))

# 필수 객체 생성
# QApplication은 QtWidgets 모듈 안에 존재하는 함수 중 하나, 무조건 써야하는 클래스
# sys.argv는 현재 소스코드 파일에 대한 경로를 담고 있는 리스트를 클래스의 생성자로 전달(arguments vector)
app = QApplication(sys.argv)

# Qwidget()은 실제로 화면에 보여지는 윈도우를 생성하는 클래스
# window라는 이름으로 객체를 생성한 후 show 메서드로 창을 띄워줌
# Qwidget()은 그냥 창의 껍데기만 만드는 것
window = MyWindow()
window.show()

# 닫기 버튼 누를 때까지 실행하는 코드
app.exec_()



#main
# 파이선 내장 라이브러리에 존재하는 sys 모듈 import
# *는 모듈을 전부 가져온다는 의미
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic   # ui 파일을 사용하기 위한 모듈 import

#UI파일 연결 코드
UI_class = uic.loadUiType("Camera.ui")[0]

# QMainWindow클래스를 상속받은 MyWindow 클래스 선언
# 부모 클래스를 의미하는 super메서드, 그 클래스의 속성을 불러오는 __init__초기화 메서드 사용


class MyWindow(QMainWindow, UI_class):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        # 윈도우 타이틀 변경
       # self.setWindowTitle("파이찰칵 GUI")
        # self.setGeometry(300,300,400,400)
        # self.setWindowIcon(QIcon("web.png"))

if __name__== "__main__":
    app = app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

# class Ui_Form(self):
#     def setupUi(self, Form):
#         Form.resize(330,442)
#         Form.setAttribute(QtCore.Qt.Wa_TranslucentBackground)
# 필수 객체 생성
# QApplication은 QtWidgets 모듈 안에 존재하는 함수 중 하나, 무조건 써야하는 클래스
# sys.argv는 현재 소스코드 파일에 대한 경로를 담고 있는 리스트를 클래스의 생성자로 전달(arguments vector)
#app = QApplication(sys.argv)

# Qwidget()은 실제로 화면에 보여지는 윈도우를 생성하는 클래스
# window라는 이름으로 객체를 생성한 후 show 메서드로 창을 띄워줌
# Qwidget()은 그냥 창의 껍데기만 만드는 것
# window = MyWindow()
# window.show()

# 닫기 버튼 누를 때까지 실행하는 코드
# app.exec_()