import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret1,frame1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)

ret2,frame2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

a = cv2.GaussianBlur(img,(5,5),0)
ret3,frame3 = cv2.threshold(a,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.subplot(2,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('img')
plt.subplot(2,2,2)
plt.imshow(frame1,cmap = 'gray')
plt.title('frame1')
plt.subplot(2,2,3)
plt.hist(frame3.ravel(),256)
plt.title('frame2')
plt.subplot(2,2,4)
plt.imshow(frame3,cmap = 'gray')
plt.title('frame3')

plt.show()