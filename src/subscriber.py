#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
 
def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
     data.linear.x = 1.0
     data.angular.z = 0.2
     pub.publish(data)
     

def listener():
    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('velocity_change', Twist, callback)
    
    rospy.spin()


if __name__ == '__main__':
    listener()
     