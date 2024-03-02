#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64, Time

def gas_pedal_publisher():
    rospy.init_node('gas_pedal_publisher', anonymous=True)
    pub_gas_pedal = rospy.Publisher('/cmd_vel', Float64, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    while not rospy.is_shutdown():
        gas_pedal_value = 0.1
        pub_gas_pedal.publish(gas_pedal_value)
        rate.sleep()

if __name__ == '__main__':
    try:
        gas_pedal_publisher()
    except rospy.ROSInterruptException:
        pass

    
