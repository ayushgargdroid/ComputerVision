import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    bnw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([20,50,50])
    upper_blue = np.array([50,255,255])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    res = cv2.GaussianBlur(res,(5,5),0)
    kernel = np.ones((5, 5), np.uint8)
    res1 = cv2.morphologyEx(res,cv2.MORPH_OPEN,kernel)
    res2 = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
    _, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cv2.imshow('frame',frame)
    cv2.imshow('HSV mask',mask)
    cv2.imshow('Result', res)
    cv2.imshow('Result1', res1)
    cv2.imshow('Result2', res2)
    cv2.drawContours(frame,contours,-1,(255,0,0),2)
    cv2.imshow('Contours', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()