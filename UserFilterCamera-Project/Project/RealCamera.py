import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
import threading
import cv2
import numpy as np
import os
import time, dlib


def RealCamera(): # original
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
            cv2.imwrite('self camera original.jpg', frame)
            print('saved_image')

        elif key == ord('q'):
            print('------------streaming end---------------')
            break
    # Clean up
    #cv2.destroyAllWindows()

#########################################################################################
def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w // 2, h // 2))
    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    dst = cv2.bitwise_and(blr, edge)  # and연산
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    return dst


def Filter2(): # cartoon Filter
    cap = cv2.VideoCapture(0)  # 카메라 오픈.
    if not cap.isOpened():
        print('video open failed!')
        sys.exit()

    while True:  # 무한 루프
        ret, frame = cap.read()  # 웹 카메라의 프레임값 불러오기
        if not ret:
            break

        frame = cartoon_filter(frame)  # 프레임에 카툰 필터 적용

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)  # 다음 프레임을 위해서 빠르게 1ms 간격으로 전환

        if key == ord(chr(32)):
            current = str(time.time())
            cv2.imwrite('self camera cartoon.jpg', frame)
            print('saved_image')

        if key == ord('q'):  # esc 누르면 종료
            break

    cap.release()



#########################################################################################


def Coin_x(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w // 2, h // 2))
    dx = cv2.Sobel(img, -1, 1, 0, delta=128)  # delta 값을 지정해주지 않으면 미분이 - 부분은 0
    return dx

def Filter3():
    cap = cv2.VideoCapture(0)  # 카메라 오픈.

    if not cap.isOpened():
        print('video open failed!')
        sys.exit()

    while True:  # 무한 루프
        ret, frame = cap.read()  # 웹 카메라의 프레임값 불러오기

        if not ret:
            break

        frame = Coin_x(frame)  # 프레임에 필터 적용

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)  # 다음 프레임을 위해서 빠르게 1ms 간격으로 전환

        if key == ord(chr(32)):
            current = str(time.time())
            cv2.imwrite('self camera coin1.jpg', frame)
            print('saved_image')

        if key == ord('q'):  # esc 누르면 종료
            break

    #cap.release()
#########################################################################################

def Coin_y(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w // 2, h // 2))
    dy = cv2.Sobel(img, -1, 0, 1, delta=128)  # delta 값을 지정해주지 않으면 미분이 - 부분은 0
    return dy

def Filter4():
    cap = cv2.VideoCapture(0)  # 카메라 오픈.

    if not cap.isOpened():
        print('video open failed!')
        sys.exit()

    while True:  # 무한 루프
        ret, frame = cap.read()  # 웹 카메라의 프레임값 불러오기

        if not ret:
            break

        frame = Coin_y(frame)  # 프레임에 필터 적용

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)  # 다음 프레임을 위해서 빠르게 1ms 간격으로 전환

        if key == ord(chr(32)):
            current = str(time.time())
            cv2.imwrite('self camera coin2.jpg', frame)
            print('saved_image')

        if key == ord('q'):  # esc 누르면 종료
            break

    #cap.release()
############################################################################################

def gradient_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w // 2, h // 2))
    dx = cv2.Sobel(img, cv2.CV_32F, 1, 0)  # float 형태의 미분값을 저장
    dy = cv2.Sobel(img, cv2.CV_32F, 0, 1)

    mag = cv2.magnitude(dx, dy)  # 그래디언트 크기
    mag = np.clip(mag, 0, 255).astype(np.uint8)  # 255보다 커질 수 있으므로 saturate 연산
    return mag

def Filter5():
    cap = cv2.VideoCapture(0)  # 카메라 오픈.

    if not cap.isOpened():
        print('video open failed!')
        sys.exit()

    while True:  # 무한 루프
        ret, frame = cap.read()  # 웹 카메라의 프레임값 불러오기

        if not ret:
            break

        frame = gradient_filter(frame)  # 프레임에 카툰 필터 적용

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)  # 다음 프레임을 위해서 빠르게 1ms 간격으로 전환

        if key == ord(chr(32)):
            current = str(time.time())
            cv2.imwrite('self camera neon.jpg', frame)
            print('saved_image')

        if key == ord('q'):  # esc 누르면 종료
            break

    #cap.release()

############################################################################################

def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
    try :
        bg_img = background_img.copy()
        # convert 3 channels to 4 channels
        if bg_img.shape[2] == 3:
            bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2BGRA)

        if overlay_size is not None:
            img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

        b, g, r, a = cv2.split(img_to_overlay_t)

        mask = cv2.medianBlur(a, 5)

        h, w, _ = img_to_overlay_t.shape
        roi = bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]

        img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
        img2_fg = cv2.bitwise_and(img_to_overlay_t, img_to_overlay_t, mask=mask)

        bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)] = cv2.add(img1_bg, img2_fg)

        # convert 4 channels to 4 channels
        bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGRA2BGR)
        return bg_img
    except Exception : return background_img

def Filter6():
    CAM_ID = 0
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    capture = cv2.VideoCapture(CAM_ID)
    overlay = cv2.imread('ryan_transparent.png', cv2.IMREAD_UNCHANGED)
    #overlay = cv2.imread('금붕어.png', cv2.IMREAD_UNCHANGED)


    capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    while True:
        ret, frame = capture.read()
        ori = frame.copy()

        #detect faces
        faces = detector(frame)

        if len(faces) == 0:
            continue

        face = faces[0]

        dlib_shape = predictor(frame, face)
        shape_2d = np.array([[p.x,p.y]for p in dlib_shape.parts()])

        top_left = np.min(shape_2d, axis=0)
        bottom_right = np.max(shape_2d, axis=0)

        face_size = int(max(bottom_right - top_left) * 1.8)

        center_x, center_y = np.mean(shape_2d, axis=0).astype(int)

        result = overlay_transparent(ori, overlay, center_x, center_y, overlay_size=(face_size, face_size))


        frame = cv2.rectangle(frame, pt1=(face.left(), face.top()), pt2=(face.right(),face.bottom()), color=(255,255,255),
                              thickness=2, lineType=cv2.LINE_AA)

        for s in shape_2d:
            cv2.circle(frame, center=tuple(s), radius=1, color=(255,255,255),thickness=2, lineType=cv2.LINE_AA)

        cv2.circle(frame, center=tuple(top_left),radius=1, color=(255,0,0),thickness=2,lineType=cv2.LINE_AA)
        cv2.circle(frame, center=tuple(bottom_right),radius=1, color=(255,0,0),thickness=2,lineType=cv2.LINE_AA)

        cv2.circle(frame, center=tuple((center_x,center_y)),radius=1, color=(0,0,255),thickness=2,lineType=cv2.LINE_AA)

        cv2.imshow('result', result)

        key = cv2.waitKey(1)

        if key == ord(chr(32)):
            current = str(time.time())
            cv2.imwrite('self camera ryan.jpg', result)
            print('saved_image')

        if key == ord('q'):  # esc 누르면 종료
            break


