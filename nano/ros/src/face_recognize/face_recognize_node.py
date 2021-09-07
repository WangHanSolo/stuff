'''
Author: Han Wang
Date:   8/31/2021

This node publishes the faces in each frame. 
'''
#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from face_detection.msg import Face
from face_detection.msg import Faces
from cv_bridge import CvBridge

import face_recognition
import pickle


class node:
    def __init__(self):
        self.image = None
        self.faces = None
        self.bridge = CvBridge()
        self.faces_sub = rospy.Subscriber("/face_detection/Faces", Faces, self.callback)
        self.pub = rospy.Publisher('/face_recognize/face', Image)

        # load the known faces and embeddings saved in file
#        data = pickle.loads(open('face_enc', "rb").read())

    def callback(self,msg):
        self.faces = msg.face_list
        if self.faces is not None:
            for face in self.faces:
                self.image = face.img
                print(face.name)
        
        
        self.pub.publish(self.image)

if __name__ == '__main__':
    rospy.init_node('face_recognize_node.py')
    n = node()
    rospy.spin()

