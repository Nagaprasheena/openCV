import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/boston.webp')
cv.imshow('Boston',img)
#BGR to GrayScale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
#BGR to LAB or l*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)
#Image plot
plt.imshow(img)
plt.show()
#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(rgb)
plt.show()
#HSV to RGB
hsv_rgb = cv.cvtColor(hsv,cv.COLOR_HSV2RGB)
cv.imshow('HSV_RGB',hsv_rgb)
#LAB to RGB
lab_rgb = cv.cvtColor(lab,cv.COLOR_LAB2RGB)
cv.imshow('LAB_RGB',lab_rgb)
cv.waitKey(0)