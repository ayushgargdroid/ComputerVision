import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('ferrari.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
im2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)

plt.subplot(1,2,1)
plt.title('Orignal')
plt.imshow(img,cmap='gray')

cv2.drawContours(img, contours, -1, (0,255,0), 3)

plt.subplot(1,2,2)
plt.title('Contours')
plt.imshow(img,cmap='gray')

plt.show()