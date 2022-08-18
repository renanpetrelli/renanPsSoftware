#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import random

class Talker:
    def __init__(self):
        rospy.init_node('sensor_velocidade', anonymous=True)
        self.pubVelocidade = rospy.Publisher('velocidade', Twist, queue_size=10)
        self.list = list(range(10))
    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            v = Twist()
            v.linear.x = random.choice(self.list) 
            v.linear.y = random.choice(self.list) 
            v.linear.z = random.choice(self.list)

            v.angular.x = random.choice(self.list) 
            v.angular.y = random.choice(self.list) 
            v.angular.z = random.choice(self.list)


            self.pubVelocidade.publish(v)
            rate.sleep()


if __name__ == '__main__':
    try:
        t = Talker()
        t.start()
    except rospy.ROSInterruptException:
        pass    