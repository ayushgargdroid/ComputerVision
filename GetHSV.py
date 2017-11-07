import numpy as np
import cv2

r = 0
b = 0
g = 0


def click(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        b, g, r = c[x][y]
        print 'R = ', r, '\nG = ', g, '\nB = ', b, '\n'
    elif event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = c[x][y]
        hsv = np.uint8([[[b, g, r]]])
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2YCR_CB)
        h, s, v = hsv[0][0]
        print 'Y = ', h, '\nCR = ', s, '\nCB = ', v, '\n'


a = cv2.VideoCapture(0)
while True:
    global c, b, g, r
    _, c = a.read()
    cv2.imshow('window', c)
    cv2.setMouseCallback('window', click)
    kill = cv2.waitKey(1) & 0xFF
    if kill == 27:
        break
cv2.destroyAllWindows()
a.release()