# this script records videos when there is a person in frame

#!/usr/bin/env python3

import cv2


cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret,frame = cam.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8,minSize = [30,30])

        if len(faces) > 0:
            pass
        else:
            pass
        cv2.imshow("window",frame)
        #imshow only works in conjunction with waitKey
        if cv2.waitKey(1) == 27:
            break
    else:
        print("no feed")

##!/usr/bin/env python
#
#import cv2 
#
#cap = cv2.VideoCapture(0)
#
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
#writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
#
#while True:
#    ret,frame = cap.read()
#    writer.write(frame)
#    
#cap.release()
#writer.release()
