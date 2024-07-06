'''#Images
import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)
def rescaleframe(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shep[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=INTER_AREA)

cv.waitKey(0)'''


'''#Videos
def changeRes(width,height):#only applicable for live vedios
    vid.set(3,width)
    vid.set(4,height)
import cv2 as cv
vid = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame = vid.read()
    frame_resized=rescaleframe(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video_resized',frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
vid.release()
cv.destroyAllWindows()'''
