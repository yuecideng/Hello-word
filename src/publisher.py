#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist 

def talker():
    pub = rospy.Publisher('velocity_change', Twist, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = Twist()
    msg.linear.x = 0.5
    msg.angular.z = 0.1

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#/turtle1/cmd_vel