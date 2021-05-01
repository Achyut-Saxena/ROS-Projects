#!/usr/bin/env python3

"""
Script to perform local navigation
"""

import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu


def callback(msg):
    """
    returns msg.data
    """
    print(msg)


rospy.init_node("p")
print("hi")

#  rospy.wait_for_service("imu")
#  print("imu working")

while not rospy.is_shutdown():
    print("rospy is up")
    rospy.Subscriber(
        name="laser/scan", data_class=LaserScan, callback=callback, queue_size=10)
    print("laser scan")

    rospy.Subscriber(
        name="imu", data_class=Imu, callback=callback, queue_size=10)
    print("imu")

    rospy.spin()

