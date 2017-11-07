import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',cv2.IMREAD_COLOR)
temp = img.flatten()
print(temp)
print(img.shape)
temp = np.reshape(temp,(342,548,3))
print(temp)

canny = cv2.Canny(img,100,255)

plt.subplot(2,2,1)
plt.title('Orignal')
plt.imshow(img,cmap = 'gray')
plt.subplot(2,2,2)
plt.title('Canny')
plt.imshow(canny,cmap = 'gray')
plt.subplot(2,2,3)
plt.title('Temp')
plt.imshow(temp,cmap='gray')

plt.show()