#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs.msg
from  tf.transformations import quaternion_from_euler

class Planeta:

    def __init__(self):
     rospy.init_node('planeta_node', anonymous = True)
     self.rate = rospy.Rate(10)
     self.broadcaster = tf2_ros.TransformBroadcaster()
     self.listener = tf2_ros.TransformListener()

    def posicaoSatelite(self):
        while not rospy.is_shutdown():
         nomeSatelite = rospy.get_param('/satelite/nome')
         nomePlaneta = rospy.get_param('/planeta/nome')
         (trans,rot) = self.listener.lookupTransform('estrela_tf', nomePlaneta, rospy.Time(0))
         tf2Stamp = geometry_msgs.msg.TransformStamped()
         tf2Stamp.header.stamp = rospy.Time.now()
         tf2Stamp.header.frame_id = nomePlaneta
         tf2Stamp.child_frame_id = nomeSatelite
         tf2Stamp.transform.rotation = (0.5, 0.5, 0.0)
         self.tf2Broadcast.sendTransform(tf2Stamp)


if __name__ == '__main__':
    try:
        p = Planeta()
        p.posicaoSatelite()
    except rospy.ROSInterruptException:
        pass    
