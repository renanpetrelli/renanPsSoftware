#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

def calculaModulo(x,y,z):
    somaQuadrados = x**2 + y**2 + z**2
    return math.sqrt(somaQuadrados)



class Listener():
    def __init__(self):
        rospy.init_node('listenerVelocidades', anonymous=True)
        rospy.Subscriber('velocidade', Twist, self.modulo)
        self.pubModuloVelocidadeLinear = rospy.Publisher('velocidadeLinear', Float32, queue_size=10)
        self.pubModuloVelocidadeAngular = rospy.Publisher('velocidadeAngular', Float32, queue_size=10)

    def modulo(self, msg):
     xlinear, ylinear, zlinear = msg.linear.x, msg.linear.y, msg.linear.z
     moduloVelocidadeLinear = Float32()
     moduloVelocidadeLinear.data = calculaModulo(xlinear, ylinear, zlinear)
     self.pubModuloVelocidadeLinear.publish(moduloVelocidadeLinear)

     xAngular, yAngular, zAngular = msg.angular.x, msg.angular.y, msg.angular.z
     moduloVelocidadeAngular = Float32()
     moduloVelocidadeAngular.data = calculaModulo(xAngular, yAngular, zAngular)
     self.pubModuloVelocidadeAngular.publish(moduloVelocidadeAngular)

if __name__ == '__main__':
    l = Listener()
    rospy.spin()