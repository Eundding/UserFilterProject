import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
import threading
import cv2
import numpy as np
import os
import time


def RealCamera():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    _, frame = cap.read()


    while True:
        start_time = time.time()
        _, frame = cap.read()

        cv2.imshow('frame', frame)

        key = cv2.waitKey(33)

        if key == ord(chr(32)):
            current = str(time.time())
            cv2.imwrite('self camera test.jpg', frame)
            print('saved_image')

        elif key == ord('q'):
            print('------------streaming end---------------')
            break
    # Clean up
    #cv2.destroyAllWindows()


