'''
Author: Han Wang
Date: 8/25/2021

Creates dataset of faces from webcam. Only 1 person can be in frame, cleaning is required after collection
'''

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

output_size = (160,160)

i = 0
pic_num = 0
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for face in faces:
        i+=1
        crop_im = img[face[1]:face[1] + face[3], face[0]:face[0] + face[2]]
        if i % 5 == 0:
            resized = cv2.resize(crop_im, output_size))
            cv2.imwrite("han/han" + str(pic_num) + ".jpg",  resized)
            pic_num+=1