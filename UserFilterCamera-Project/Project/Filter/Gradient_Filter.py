import cv2
import sys
import time
import numpy as np

def gradient_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w // 2, h // 2))
    dx = cv2.Sobel(img, cv2.CV_32F, 1, 0)  # float 형태의 미분값을 저장
    dy = cv2.Sobel(img, cv2.CV_32F, 0, 1)

    mag = cv2.magnitude(dx, dy)  # 그래디언트 크기
    mag = np.clip(mag, 0, 255).astype(np.uint8)  # 255보다 커질 수 있으므로 saturate 연산



    return mag


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
        cv2.imwrite('self camera test.jpg', frame)
        print('saved_image')

    if key == ord('q'):  # esc 누르면 종료
        break

cap.release()