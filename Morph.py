import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png')
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1)
opening = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(opening)
plt.show()