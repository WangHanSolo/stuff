'''
Author: Han Wang
Date:   8/31/2021

This node publishes the faces in each frame. 
The face detecting part is referenced from https://github.com/timesler/facenet-pytorch
'''
#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import std_msgs.msg

from face_detection.msg import Face
from face_detection.msg import Faces
import cv2
from cv_bridge import CvBridge

import torch
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1



class node:
    def __init__(self) -> None:
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.mtcnn = MTCNN(image_size=(1280,720), margin=0, keep_all=True, device=device)
        self.resnet = InceptionResnetV1(pretrained='vggface2').eval()
        self.bridge = CvBridge()

        self.sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
        self.pub = rospy.Publisher('/face_detection/Faces', Faces)

    def callback(self,data):
        img = self.bridge.imgmsg_to_cv2(data)
        faces, confidences = self.mtcnn.detect(img)
        facelist_rosmsg = Faces()
        # for some reason, it crashes if its None.
        if faces is not None:
            for face, confidence in zip(faces, confidences):
                if confidence > 0.90:
                    face = face.astype(int)
                    face_rosmsg = Face()
                    h = std_msgs.msg.Header()
                    h.stamp = rospy.Time.now()
                    face_rosmsg.x = face[0]
                    face_rosmsg.y = face[1]
                    face_rosmsg.w = face[2] - face[0]
                    face_rosmsg.h = face[3] - face[1]
                    # convert numpy float32 to native python type
                    face_rosmsg.confidence =  confidence.item()
                    face_rosmsg.name = "unknown"
                    print(img.shape)
                    print(face[1],face[3],face[0],face[2])
                    face_rosmsg.img = self.bridge.cv2_to_imgmsg(img[face[1]:face[3], face[0]:face[2]])
                    facelist_rosmsg.face_list.append(face_rosmsg)
        self.pub.publish(facelist_rosmsg)
    
def listener():
    rospy.init_node('face_detection_node.py')
    n = node()
    rospy.spin()


if __name__ == '__main__':
    listener()