'''
Author: Han Wang
Date:   8/31/2021

This node publishes the faces in each frame. 
The face detecting part is referenced from https://github.com/timesler/facenet-pytorch
'''
#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image

from face_detection.msg import Face
from face_detection.msg import Faces
import cv2
from cv_bridge import CvBridge

import torch
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(image_size=(1280,720), margin=0, keep_all=True, device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval()

bridge = CvBridge()

pub = rospy.Publisher('/face_detection/Faces', Faces)

def callback(data):
    img = bridge.imgmsg_to_cv2(data)
    faces, confidences = mtcnn.detect(img)
    facelist_rosmsg = Faces()
    # for some reason, it crashes if its None.
    if faces is not None:
        for face, confidence in zip(faces, confidences):
            face = face.astype(int)
            cv2.rectangle(img, (face[0],face[1]), (face[2],face[3]), (255,0,0),2)
            face_rosmsg = Face()
            face_rosmsg.x = face[0]
            face_rosmsg.y = face[1]
            face_rosmsg.w = face[2] - face[0]
            face_rosmsg.h = face[3] - face[1]
            # convert numpy float32 to native python type
            face_rosmsg.confidence =  confidence.item()
            facelist_rosmsg.face_list.append(face_rosmsg)
#    img_msg = bridge.cv2_to_imgmsg(img, encoding='rgb8')
    pub.publish(facelist_rosmsg)
    
def listener():
    rospy.init_node('face_detection_node.py')
    rospy.Subscriber("/usb_cam/image_raw", Image, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()