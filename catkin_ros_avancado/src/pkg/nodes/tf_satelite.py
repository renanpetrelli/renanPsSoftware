#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs.msg

class Satelite:

    def __init__(self):
     rospy.init_node('satelite_node', anonymous = True)
     self.rate = rospy.Rate(10)
     self.listener = tf2_ros.TransformListener()

    def posicaoSatelite(self):
        while not rospy.is_shutdown():
         nomeSatelite = rospy.get_param('/satelite/nome')
         nomePlaneta = rospy.get_param('/planeta/nome')
        (trans,rot) = self.listener.lookupTransform(nomePlaneta, nomeSatelite, rospy.Time(0))


if __name__ == '__main__':
    try:
        s = Satelite()
        s.posicaoSatelite()
    except rospy.ROSInterruptException:
        pass    