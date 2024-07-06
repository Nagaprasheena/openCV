import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.webp')
resized = cv.resize(img,(750,500),cv.INTER_AREA)
cv.imshow('Boston',resized)
blank = np.zeros(resized.shape[:2],dtype='uint8')
b,g,r = cv.split(resized)
'''cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)'''
Blue = cv.merge([b,blank,blank])
Green = cv.merge([blank,g,blank])
Red = cv.merge([blank,blank,r])
cv.imshow('Printed Blue',Blue)
cv.imshow('Printed Green',Green)
cv.imshow('Printed Red',Red)
merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)
cv.waitKey(0)