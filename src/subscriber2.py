#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class change():
    def __init__(self):
        rospy.init_node('changer', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        rospy.Subscriber('velocity_change', Twist, self.update_value)
        rospy.spin()

    def update_value(self, data):

        data.linear.x = 1.0
        data.angular.z = 0.1
        self.pub.publish(data)

if __name__ == '__main__':
    change = change()
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        rate.sleep()


            