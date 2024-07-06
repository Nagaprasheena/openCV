import cv2 as cv
import numpy as np

pic = cv.imread('Photos/boston.webp')
img = cv.resize(pic,(650,450),cv.INTER_AREA)
cv.imshow('Boston',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Edges',lap)
#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)
#Comapring laplacian and sobel with canny
canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)