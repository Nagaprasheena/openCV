import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
#Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
    #-x ->left
    #-y ->up
    #x ->right
    #y ->down
translated = translate(img,100,-50)
cv.imshow('Translated',translated)
#Rotation
def rotate(img,angle,rotPoint):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)
    #-ve rotAngle ->clockwise
    #+ve rotAngle ->anticlockwise
rotated = rotate(img,-45,None)
cv.imshow('Rotated',rotated)
#Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
    #For enlarging=cv.INTER_LINEAR or cv.INTER_CUBIC
    #For dimnishing=cv.INTER_AREA
cv.imshow('Resized',resized)
#Flipping
flip = cv.flip(img,0)
    #For Flipping along x-axis ->Flipcode=0
    #For Flipping along y-axis ->Flipcode=1
    #For Flipping along both x-axis and y-axis->Flipcode=-1
cv.imshow('Flipped',flip)
#Cropping
cropped = img[100:200,300:500]
cv.imshow('Cropped',cropped)
cv.waitKey(0)