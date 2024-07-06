import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.webp')
resized = cv.resize(img,(750,500),cv.INTER_AREA)
cv.imshow('Boston',resized)
#Averaging
average = cv.blur(resized,(5,5))
cv.imshow('Average Blur',average)
#Gaussian blur
gauss = cv.GaussianBlur(resized,(5,5),0)
cv.imshow('Gaussian blur',gauss)
#Median blur
median = cv.medianBlur(resized,5)
cv.imshow('Median blur',median)
#Bilateral blur
bilateral = cv.bilateralFilter(resized,150,35,35)
cv.imshow('Bilateral blur',bilateral)
cv.waitKey(0)