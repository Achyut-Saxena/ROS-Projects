#!/usr/bin/env python3

"""
Script to perform local navigation
"""
import rospy

from listeners import LaserListener, GPSListener, GazeboGetModelState
from controller import Controller

if __name__ == "__main__":

    rospy.init_node("p")
    #  Laser = LaserListener(topic_path="/laser/scan")
    #  g = GPSListener('/fix')
    m = GazeboGetModelState(
        "/gazebo/get_model_state", "aws_robomaker_warehouse_Bucket_01_020")

    while not rospy.is_shutdown():

        m.get()

        rospy.sleep(0.01)
