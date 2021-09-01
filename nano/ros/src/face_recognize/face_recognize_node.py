'''
Author: Han Wang
Date:   8/31/2021

This node publishes the faces in each frame. 
'''
#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from face_detection.msg import Face
from face_detection.msg import Faces
from cv_bridge import CvBridge

class node:
    def __init__(self):
        self.image = None
        self.faces = None
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('/face_recognize/image_raw', Image)
        self.faces_sub = rospy.Subscriber("/face_detection/Faces", Faces, self.faces_callback)
        self.image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.image_callback)

    def image_callback(self,msg):
        self.image = self.bridge.imgmsg_to_cv2(msg)
        if self.faces is not None:
            for face in self.faces:
                cv2.rectangle(self.image,(face.x,face.y),(face.x+face.w, face.y+face.h),(255,0,0),2)

        image_msg = self.bridge.cv2_to_imgmsg(self.image, encoding="rgb8")
        self.pub.publish(image_msg)

        return None
    def faces_callback(self,msg):
        self.faces = msg.face_list

if __name__ == '__main__':
    rospy.init_node('face_recognize_node.py')
    n = node()
    rospy.spin()

