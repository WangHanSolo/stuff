'''
Author: Han Wang
Date: August 29 2021

This module will detect faces, extract face embeddings, then recognize the faces
We will use facenet from https://github.com/timesler/facenet-pytorch
'''

import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1
import pickle


# check for gpu
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

# set up facenet to detect faces in frame
mtcnn = MTCNN(image_size = (480,640), margin=0, keep_all=True, device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval()

# set up face embeddings
data = pickle.loads(open('../data/face_enc', "rb").read())

# To capture video from webcam. 
cam = cv2.VideoCapture(0)

while True:
    feed, img = cam.read()
    faces, _ = mtcnn.detect(img)
    if faces is not None:
        for face in faces:
            face = face.astype(int)
            cv2.rectangle(img, (face[0],face[1]), (face[2],face[3]), (255,0,0), 2)

    cv2.imshow("window",img)
    #imshow only works in conjunction with waitKey
    if cv2.waitKey(1) == 27:
        break



