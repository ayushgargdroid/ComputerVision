import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    print(frame.shape)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(frame,100,200)

    f = np.fft.fft2(frame)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    rows,cols = frame.shape
    crows,ccols = rows/2, cols/2
    fshift[crows-30:crows+30,ccols-30:ccols+30] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    print img_back

    plt.imshow(frame)
    cv2.imshow('fafag',canny)
    cv2.imshow('afaf',img_back)
    plt.imshow(magnitude_spectrum)
    plt.imshow(img_back,cmap='gray')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()