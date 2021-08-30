'''
Author: Han Wang
Date: 8/25/2021

Does facial recognition on video feed
'''
import face_recognition
import imutils #imutils includes opencv functions
import pickle
import time
import cv2
import os
import sys


# Load the cascade
face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cam = cv2.VideoCapture(0)

output_size = (160,160)

i = 0
pic_num = 0
while True:
    feed, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=[30,30])
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("window",img)
    #imshow only works in conjunction with waitKey
    if cv2.waitKey(1) == 27:
        break

