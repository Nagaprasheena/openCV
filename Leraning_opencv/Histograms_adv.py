import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

pic = cv.imread('Photos/boston.webp')
img = cv.resize(pic,(750,500),cv.INTER_AREA)
cv.imshow('Boston',img)
'''#GrayScale Histogram
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('Masked Image',mask)
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()'''
#Color Histogram
blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),150,255,-1)
color_mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Masked Colored Image',color_mask)
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(color_hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)