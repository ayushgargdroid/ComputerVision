import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frameC = frame.copy()
    frameCC = frame.copy()
    cv2.imshow('Orignal', frame)

    canny = cv2.Canny(frame, 100, 200)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,4)
    cv2.imshow('Thresholded', gray)
    cv2.imshow('Canny',canny)

    _,contours,hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,contours,-1,(255,0,0),1)
    cv2.imshow('Contour1', frame)

    _, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frameC,contours,-1,(0,255,0),1)
    cv2.imshow('Contour2',frameC)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()