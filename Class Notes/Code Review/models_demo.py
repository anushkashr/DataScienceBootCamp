import numpy as np 
import cv2 

cap = cv2.VideoCapture('people-detection.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

 

while(1): 
    ret, frame = cap.read()
    cv2.imshow('frame',frame) 
    fgmask = fgbg.apply(frame)
    cv2.imshow('fgmask', fgmask) 
    cv2.imshow('frame',frame ) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break


cap.release() 
cv2.destroyAllWindows()


