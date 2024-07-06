import cv2 as cv
import numpy as np

pic = cv.imread('Photos/boston.webp')
img = cv.resize(pic,(750,500),cv.INTER_AREA)
cv.imshow('Boston',img)
blank = np.zeros(img.shape[:2],dtype='uint8')
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)
cv.waitKey(0)