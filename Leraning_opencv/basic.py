import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
#1)Converting image into grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#2)Blurring
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
#3)Edge Cascading
canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)
#4)Dilating
dilate = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dialted',dilate)
#5)Eroding(Opposite to dilating)
erode = cv.erode(dilate,(3,3),iterations=5)
cv.imshow('Eroded',erode)
#6)Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)
#7)Cropping
cropped = img[0:200,300:500]
cv.imshow('Cropped',cropped)

cv.waitKey(0)