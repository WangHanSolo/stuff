#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


pub = rospy.Publisher('/people/image',Image)

def callback(data):
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(data)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    




def listener():
    rospy.init_node('people')
    rospy.Subscriber("/right_camera/image_raw", Image, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()