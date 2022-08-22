#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs.msg
from tf.transformations

class Estrela:

    def __init__(self):
     rospy.init_node('estrela_node', anonymous = True)
     self.rate = rospy.Rate(10)
     self.tf2Broadcast = tf2_ros.TransformBroadcaster()

    
    def posicaoPlaneta(self):
      while not rospy.is_shutdown():
       nomePlaneta = rospy.get_param('/planeta/nome')
       tf2Stamp = geometry_msgs.msg.TransformStamped()
       tf2Stamp.header.stamp = rospy.Time.now()
       tf2Stamp.header.frame_id = 'estrela_tf'
       tf2Stamp.child_frame_id = nomePlaneta
       tf2Stamp.transform.rotation = (0.5, 0.5, 0.0)
       self.tf2Broadcast.sendTransform(tf2Stamp)

if __name__ == '__main__':
    try:
        e = Estrela()
        e.posicaoPlaneta()
    except rospy.ROSInterruptException:
        pass    