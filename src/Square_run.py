#!/usr/bin/env python
# license removed for brevity
import rospy

from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg_s = Twist()
    msg_t = Twist()
   
    while not rospy.is_shutdown():
        time_current = rospy.get_time()
        while (rospy.get_time() - time_current) < 5.0:
            msg_s.linear.x = 0.5
            pub.publish(msg_s)
        time_current = rospy.get_time()
        
        while (rospy.get_time() - time_current) < 1.0:
            msg_t.angular.z = 1.57
            pub.publish(msg_t)

        rate.sleep()
   
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
