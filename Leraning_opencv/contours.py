import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
'''blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)'''
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found: ')
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours drawn',blank)
cv.waitKey(0)