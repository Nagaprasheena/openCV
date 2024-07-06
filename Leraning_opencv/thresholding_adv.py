import cv2 as cv

pic = cv.imread('Photos/cat.jpg')
img = cv.resize(pic,(650,450),cv.INTER_CUBIC)
cv.imshow('Cat',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Simple Thresholding
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholded',thresh)
threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse',thresh_inv)
#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Threshold',adaptive_thresh)
adaptive_thresh1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Threshold1',adaptive_thresh1)
cv.waitKey(0)