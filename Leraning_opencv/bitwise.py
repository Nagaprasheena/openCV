import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)
#Bitwise AND ->Intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND',bitwise_and)
#Bitwise OR ->Union regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_or)
#Bitwise XOR ->Non Intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_xor)
#Bitwise NOT
rectangle_not = cv.bitwise_not(rectangle)
cv.imshow('Recatngle NOT',rectangle_not)
circle_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT',circle_not)
cv.waitKey(0)