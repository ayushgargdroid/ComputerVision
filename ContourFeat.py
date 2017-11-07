import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('contourFeat.png',0)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

t = thresh.copy()
_, contours, hierarchy = cv2.findContours(t,1,2)

epsilon = 0.1*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)

print len(contours)
plt.subplot(2,2,1)
plt.title('Orignal')
plt.imshow(img,cmap='gray')

plt.subplot(2,2,2)
plt.title('Thresh')
plt.imshow(thresh,cmap='gray')
plt.show()


t = img.copy()
epsilon = 0.01*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
cv2.drawContours(t,approx,0,(255,0,0),2)
cv2.imshow('Contours2',t)
cv2.waitKey(0)