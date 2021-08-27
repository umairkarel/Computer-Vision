import cv2
import numpy as np

cam = cv2.VideoCapture(0)
magnifier = 100
zoom = 1
target = [40, 60]


def getBounds(x, y, magnifier):
    magnifier //= 2

    if x-magnifier < 0:
        x = 0
    elif x+magnifier > width:
        x = width-magnifier*2
    else:
        x -= magnifier

    if y-magnifier < 0:
        y = 0
    elif y+magnifier > height:
        y = height-magnifier*2
    else:
        y -= magnifier

    return x,y

def magnify(glass, x,y):

    magnified = cv2.resize(glass, None, fx=zoom, fy=zoom, interpolation= cv2.INTER_LINEAR)
    zoomX, zoomY, _ = magnified.shape
    zoomX //= zoom
    zoomY //= zoom

    return magnified[zoomX:zoomX*2, zoomY:zoomY*2]

while True:
    ret, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))

    target[0] += 2
    target[1] += 1

    x,y = getBounds(*target, magnifier)

    glass = frame[y:y+magnifier, x:x+magnifier]
    glass += 60

    if zoom >= 2:
        frame[y:y+magnifier, x:x+magnifier] = magnify(glass, x,y)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()