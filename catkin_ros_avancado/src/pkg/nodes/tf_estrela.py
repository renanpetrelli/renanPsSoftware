#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs.msg
import math 

class Estrela:

    def __init__(self):
     rospy.init_node('estrela_node', anonymous = True)
     self.rate = rospy.Rate(10)
     self.tf2Broadcast = tf2_ros.TransformBroadcaster()

    
    def posicaoPlaneta(self):
      while not rospy.is_shutdown():
       x = rospy.Time.now().to_sec()
       nomePlaneta = rospy.get_param('/planeta/nome')
       raioPlaneta = rospy.get_param('/planeta/raio')
       tf2Stamp = geometry_msgs.msg.TransformStamped()
       tf2Stamp.header.stamp = rospy.Time.now()
       tf2Stamp.header.frame_id = 'estrela'
       tf2Stamp.child_frame_id = nomePlaneta

       tf2Stamp.transform.translation.x = raioPlaneta * math.sin(x)
       tf2Stamp.transform.translation.y = raioPlaneta * math.cos(x)
       tf2Stamp.transform.translation.z = 0.0

       tf2Stamp.transform.rotation.x = 0.0
       tf2Stamp.transform.rotation.y = 0.0
       tf2Stamp.transform.rotation.z = 0.0
       tf2Stamp.transform.rotation.x = 1.0

       self.tf2Broadcast.sendTransform(tf2Stamp)
       self.rate.sleep()

if __name__ == '__main__':
    try:
        e = Estrela()
        e.posicaoPlaneta()
    except rospy.ROSInterruptException:
        pass    