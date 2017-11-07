import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()
    if _ == True:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower_pink = np.array([165,50,50])
        upper_pink = np.array([185,255,255])
        mask = cv2.inRange(hsv,lower_pink,upper_pink)

        res = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow('hsv',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('result',res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()
