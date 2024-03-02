#!/usr/bin/env python

import rospy
from rosgraph_msgs.msg import Clock
from std_msgs.msg import Int32

def clock_callback(msg):
    rospy.loginfo("Simulation started")
    start_publishing_counter()

def start_publishing_counter():
    pub_counter = rospy.Publisher('/sim_time', Int32, queue_size=10)
    rate = rospy.Rate(1000)  

    counter = 0
    while not rospy.is_shutdown():
        pub_counter.publish(counter)
        counter += 1
        rate.sleep()

def clock_subscriber():
    rospy.init_node('clock_subscriber', anonymous=True)
    sub_clock = rospy.Subscriber('/clock', Clock, clock_callback)
    rospy.spin() 

if __name__ == '__main__':
    try:
        clock_subscriber()
    except rospy.ROSInterruptException:
        pass
