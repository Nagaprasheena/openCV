import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#Paint it with certain color
blank[:] = 255,0,0
cv.imshow('Filled Blank',blank)
blank[200:300,300:400] = 0,0,255
cv.imshow('Coloured Blank',blank)
#Draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('Rectangle',blank)
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)#(or thickness=cv.FILLED)
cv.imshow('Rectangle_1',blank)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)#(or thickness=cv.FILLED)
cv.imshow('Rectangle_2',blank)
#Draw a circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)#((250,250) or (blank.shape[1]//2,blank.shape[0]//2) since blank.shape[0]=blank.shape[1]=500)
cv.imshow('Circle',blank)
#Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=1)
cv.imshow('Line',blank)
#Write Text
cv.putText(blank,"Hello",(200,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)