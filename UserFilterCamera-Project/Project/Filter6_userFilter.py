import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from Out import Out  # 나가기 창 임포트
from Advice import Advice  # 도움말 창 임포트
from AfterStart import *
from FilterScreen import *
from RealCamera import overlay_transparent, Filter6
import numpy as np
import cv2
import numpy as np
import cv2
from PIL import Image
import os

BLUE, GREEN, RED, BLACK, WHITE = (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)
DRAW_BG = {'color': BLACK, 'val': 0}
DRAW_FG = {'color': WHITE, 'val': 1}

rect = (0, 0, 1, 1)
drawing = False
rectangle = False
rect_over = False
rect_or_mask = 100
value = DRAW_FG
thickness = 3

###################################################################################3
form_FilterRyan = uic.loadUiType("FilterScreen_new.ui")[0]


class FilterRyan(QDialog, QWidget, form_FilterRyan):
    def __init__(self):
        super(FilterRyan, self).__init__()
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
       # self.btn_different.clicked.connect(self.GoToAgain)

    def GoToGallery(self):  # 폴더 열기 구현
        global filename
        filename = QFileDialog.getOpenFileName(self, "File Load",
                                               'C:/Users/dkan9/PycharmProjects/camera_project/Gallery',
                                               'JPG File(*.jpg)')

        img = cv2.imread(filename[0])
        cv2.imwrite("nemo.jpg", img)

        # filename2 =  QFileDialog.getSaveFileName(self, "File Save",'C:/Users/dkan9/PycharmProjects/camera_project/Gallery','JPG File(*.jpg)')

        def onMouse(event, x, y, flags, param):

            global ix, iy, img, img2, drawing, value, mask, rectangle
            global rect, rect_or_mask, rect_over

            if event == cv2.EVENT_RBUTTONDOWN:
                rectangle = True
                ix, iy = x, y

            elif event == cv2.EVENT_MOUSEMOVE:
                if rectangle:
                    img = img2.copy()
                    cv2.rectangle(img, (ix, iy), (x, y), RED, 2)
                    rect = (min(ix, x), min(iy, y), abs(ix - x), abs(iy - y))
                    rect_or_mask = 0

            elif event == cv2.EVENT_RBUTTONUP:
                rectangle = False
                rect_over = True

                cv2.rectangle(img, (ix, iy), (x, y), RED, 2)
                rect = (min(ix, x), min(iy, y), abs(ix - x), abs(iy - y))
                rect_or_mask = 0
                print('n:적용하기')

            if event == cv2.EVENT_LBUTTONDOWN:
                if not rect_over:
                    print('마우스 왼쪽 버튼을 누른채로 전격이 되는 부분을 선택하세요 ')
                else:
                    drawing = True
                    cv2.circle(img, (x, y), thickness, value['color'], -1)
                    cv2.circle(mask, (x, y), thickness, value['val'], -1)
            elif event == cv2.EVENT_MOUSEMOVE:
                if drawing:
                    cv2.circle(img, (x, y), thickness, value['color'], -1)
                    cv2.circle(mask, (x, y), thickness, value['val'], -1)
            elif event == cv2.EVENT_LBUTTONUP:
                if drawing:
                    drawing = False
                    cv2.circle(img, (x, y), thickness, value['color'], -1)
                    cv2.circle(mask, (x, y), thickness, value['val'], -1)
            return

        def grabcut():
            global ix, iy, img, img2, drawing, value, mask, rectangle
            global rect, rect_or_mask, rect_over

            img = cv2.imread('nemo.jpg')
            img2 = img.copy()

            mask = np.zeros(img.shape[:2], dtype=np.uint8)
            output = np.zeros(img.shape, np.uint8)

            cv2.namedWindow('Input')
            cv2.namedWindow('Output')
            cv2.setMouseCallback('Input', onMouse, param=(img, img2))

            print('오른쪽 마우스 버튼을 누르고 영역을 지정한 후 n을 누르세요')

            while True:
                cv2.imshow('Output', output)
                cv2.imshow('Input', img)

                k = cv2.waitKey(1) & 0xFF

                if k == 27:
                    break
                if k == ord('0'):
                    print('왼쪽 마우스로 제거할 부분을 표시한 후 n을 누르세요')
                elif k == ord('1'):
                    print('왼쪽 마우스로 복원할 부분을 표시한 후 n을 누르세요')
                elif k == ord('r'):
                    print('리셋합니다')
                    rect = (0, 0, 1, 1)
                    drawing = False
                    rectangle = False
                    rect_or_mask = 100
                    rect_over = False
                    value = DRAW_FG
                    img = img2.copy()
                    mask = np.zeros(img.shape[:2], dtype=np.uint8)
                    output = np.zeros(img.shape, np.uint8)
                    print('0:제거배경선택 1:복원전경선택 n:적용하기 r: 리셋')
                elif k == ord('n'):
                    bgdModel = np.zeros((1, 65), np.float64)
                    fgdModel = np.zeros((1, 65), np.float64)

                    if rect_or_mask == 0:
                        cv2.grabCut(img2, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
                    if rect_or_mask == 1:
                        cv2.grabCut(img2, mask, rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_MASK)
                    print('0:제거배경선택 1:복원전경선택 n:적용하기 r: 리셋')
                elif k == ord(chr(32)):

                    cv2.imwrite('self camera test.png', output)
                    print('saved_image')
                    img_ = Image.open('self camera test.png')
                    rgba = img_.convert("RGBA")
                    datas = rgba.getdata()

                    newData = []
                    for item in datas:
                        if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
                            # storing a transparent value when we find a black colour
                            newData.append((255, 255, 255, 0))
                        else:
                            newData.append(item)  # other colours remain unchanged

                    rgba.putdata(newData)
                    rgba.save("Transparent_cpp.png", "PNG")
                    cv2.destroyAllWindows()

                mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')
                output = cv2.bitwise_and(img2, img2, mask=mask2)

            key = cv2.waitKey(1)  # 다음 프레임을 위해서 빠르게 1ms 간격으로 전환

        grabcut()

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(filename[0])
        self.label_2.setPixmap(self.qPixmapFileVar)
        self.close()

    def GoToClick(self):  # 카메라 화면으로 넘어가도록
        Filter6()
        self.loadImageFromFile()

    # def GoToAgain(self):
    #     self.close()
    #     # self.aas = AS()
    #     # self.aas.exec()
    #     # self.show()

    # 파이큐티에 사진 띄우는 함수
    def loadImageFromFile(self):
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("self camera ryan.jpg")
        self.label_2.setPixmap(self.qPixmapFileVar)

