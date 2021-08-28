import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cam = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)

magnifier = 100
zoom = 1
curX,curY = 0,0
offset = 13
glassOpacity = 20

def getBounds(x, y, magnifier):
    magnifier //= 2

    if x-magnifier < 0:
        x = 0
    elif x+magnifier > width:
        x = width-magnifier*2
    else:
        x -= magnifier

    if y-(magnifier*2)-offset < 0:
        y = 0
    else:
        y = y-(magnifier*2)-offset

    return x,y

def magnify(glass, x,y):

    magnified = cv2.resize(glass, None, fx=zoom, fy=zoom, interpolation= cv2.INTER_LINEAR)
    zoomX, zoomY, _ = magnified.shape
    zoomX //= int(zoom)
    zoomY //= int(zoom)

    return magnified[zoomX:zoomX*2, zoomY:zoomY*2]

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    width = int(cam.get(3))
    height = int(cam.get(4))
    img = frame.copy()

    detector.findHands(img)
    lmList, boundingBox =  detector.findPosition(img)

    if lmList:
        curX,curY = lmList[8]
        x,y = getBounds(curX,curY, magnifier)

        frame[y:y+magnifier, x:x+magnifier] += glassOpacity

        zoom,_,_ = detector.findDistance(8,12,img)
        zoom = (zoom//20) + 1

        
        if 2 <= zoom <= 4:
            frame[y:y+magnifier, x:x+magnifier] = magnify(frame[y:y+magnifier, x:x+magnifier], x,y)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()