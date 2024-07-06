'''#Reading image
import cv2 as cv
img = cv.imread('Photos/boston.webp')
cv.imshow('Boston',img)
cv.waitKey(0)'''


#Reading vedio
import cv2 as cv
vid = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame = vid.read()
    cv.imshow('Dog',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
vid.release()
cv.destroyAllWindows()