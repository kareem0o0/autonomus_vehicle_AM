import rospy
from std_msgs.msg import String, Int32, Bool

def my_callback(my_string):
    rospy.loginfo("%s", my_string.data)
    

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/sim_time", Int32, my_callback) #("same topic for puplisher",data type, function you need to excute)
    rospy.spin()


if __name__== '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass