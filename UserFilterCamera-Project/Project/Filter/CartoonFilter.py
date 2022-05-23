# import cv2
# import sys
# import time
#
# def cartoon_filter(img):
#     h, w = img.shape[:2]
#     img2 = cv2.resize(img, (w // 2, h // 2))
#
#     blr = cv2.bilateralFilter(img2, -1, 20, 7)
#     edge = 255 - cv2.Canny(img2, 80, 120)
#     edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
#     dst = cv2.bitwise_and(blr, edge)  # and연산
#     dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
#
#     return dst
#
#
# cap = cv2.VideoCapture(0)  # 카메라 오픈.
#
# if not cap.isOpened():
#     print('video open failed!')
#     sys.exit()
#
# while True:  # 무한 루프
#     ret, frame = cap.read()  # 웹 카메라의 프레임값 불러오기
#
#     if not ret:
#         break
#
#     frame = cartoon_filter(frame)  # 프레임에 카툰 필터 적용
#
#     cv2.imshow('frame', frame)
#     key = cv2.waitKey(1)  # 다음 프레임을 위해서 빠르게 1ms 간격으로 전환
#
#     if key == ord(chr(32)):
#         current = str(time.time())
#         cv2.imwrite('self camera test.jpg', frame)
#         print('saved_image')
#
#     if key == ord('q'):  # esc 누르면 종료
#         break
#
# cap.release()
# cv2.destroyAllWindows()