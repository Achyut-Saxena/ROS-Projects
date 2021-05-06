#!/usr/bin/env python3
"""
Controller class for the robot
"""


from math import atan2, pi
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import NavSatFix
from listeners import *

from time import sleep
import random


class Controller:
    """
    Class to controll the motion of the robot
    """
    def __init__(self):
       self.goal = NavSatFix()
       self.goal.latitude = 49.900889625060174
       self.goal.longitude = 8.898545755445237
       self.goal.altitude = -2.6991185756052882
       self.listeners = GPSListener("/fix")
       self.klp=10
       self.kap=10
       self.pub = Publisher()

    def control_signal(self):
       print("Hello")
       coord = self.listeners.get()
       lat_e = coord[0]-self.goal.latitude
       long_e = coord[1]-self.goal.longitude
       print(lat_e,long_e)
       msg = Twist()
       msg.linear.x = lat_e*self.klp
       msg.angular.z = long_e*self.kap
       self.pub.msg = msg
       self.pub.message_publish()

class Publisher:
    """
    Constantly latches to the robot and publishes a message
    """
    def __init__(self):
        self.pub=rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.msg = Twist()
        self.msg.linear.x = 0
        self.msg.angular.z = 0

    def message_publish(self):
        self.pub.publish(self.msg)

if __name__ == '__main__':
    rospy.init_node("Control")
    c = Controller()
    rate = rospy.Rate(10)
    print(rospy.is_shutdown())
    while not rospy.is_shutdown():
        print("0")
        print("1")
        c.control_signal()
        print("2")
        rate.sleep()
        print("3")
    
