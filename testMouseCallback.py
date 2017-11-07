import cv2
import numpy as np

mode = True
drawing  = False
ix = iy = 0
existingRect = []

def createExistingRect():
    global img
    for i in existingRect:
        cv2.rectangle(img,(i[0],i[1]),(i[2],i[3]),(255,0,255),1)

def mouseCallback(event,x,y,flags,param):
    global mode,drawing,ix,iy,img,existingRect
    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        img = np.zeros((512, 512, 3), np.uint8)
        createExistingRect()
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,255),1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),1)
    elif event == cv2.EVENT_LBUTTONUP and drawing == True:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,255),1)
            existingRect = existingRect + [(ix,iy,x,y)]
        else:
            cv2.circle(img,(x,y),5,(0,0,255),1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('Figures')
cv2.setMouseCallback('Figures',mouseCallback)

while(True):
    cv2.imshow('Figures',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break
cv2.destroyAllWindows()

