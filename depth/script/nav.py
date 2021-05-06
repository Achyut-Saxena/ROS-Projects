#!/usr/bin/env python3

"""
Script to perform local navigation
"""
import rospy

from listeners import *
from controller import Controller

if __name__ == "__main__":

    rospy.init_node("p")
    Laser = LaserListener(topic_path="/laser/scan")
    g = GPSListener('/fix')
    i = ImuListener("/imu")

    Con = Controller(1)

    while not rospy.is_shutdown():

        Con.move()
        rospy.sleep(0.01)
