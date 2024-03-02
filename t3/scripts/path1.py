#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64, Int32

def gas_pedal_publisher():
    rospy.init_node('gas_pedal_publisher', anonymous=True)
    pub_gas_pedal = rospy.Publisher('/cmd_vel', Float64, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    def int32_callback(msg):
        if msg.data > 19280:
            gas_pedal_value = 0.0  # Stop the car
        else:
            gas_pedal_value = 1  # Continue with gas pedal value 0.1
        pub_gas_pedal.publish(gas_pedal_value)

    sub_int32 = rospy.Subscriber('/sim_time', Int32, int32_callback)

    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        gas_pedal_publisher()
    except rospy.ROSInterruptException:
        pass
