#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def transform_callback(msg):
    rospy.loginfo("Received transform message: %s", msg)

def transform_subscriber():
    rospy.init_node('data', anonymous=True)
    sub_transform = rospy.Subscriber('/odom', Odometry, transform_callback)
    rate = rospy.Rate(0.1)  # Read messages at 1Hz
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        transform_subscriber()
    except rospy.ROSInterruptException:
        pass
