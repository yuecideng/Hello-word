#!/usr/bin/env python
# license removed for brevity
import rospy

from turtlesim.msg import Color

def talker():
    pub = rospy.Publisher('/turtle1/color_sensor', Color, queue_size=1)
    rospy.init_node('color_change', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = Color()
    msg.r = 255
    msg.g = 0
    msg.b = 0
    while not rospy.is_shutdown():
        #rospy.loginfo()
        pub.publish(msg)
        rate.sleep()
   
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
