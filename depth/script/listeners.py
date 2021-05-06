#!/usr/bin/env python3

"""
All listener classes used are defined here
"""

from math import inf, cos, pi, radians
import rospy
from sensor_msgs.msg import LaserScan, NavSatFix, Imu
from gazebo_msgs.srv import GetModelState
from geometry_msgs.msg import Quaternion
from weights import get_cos_weights, get_sin_weights
import numpy as np
from math import atan2

"""
def get_dist(current, target):
    Returns distance from current to target
    current = np.array(current)
    target = np.array(target)

    dist = np.linalg.norm(current - target)
    return dist * 1e5


def yaw_from_quat(quat):
    returns yaw from quat object
    x = quat.x
    y = quat.y
    z = quat.z
    w = quat.w

    yaw = atan2(2*(w*z + x*y), (1-(2*(y*y + z*z))))
    return yaw


class ImuListener:
    Class to return imu data

    def __init__(self, topic_path):

        self.sub = rospy.Subscriber(
            name=topic_path, data_class=Imu, callback=self.callback, queue_size=10)

        self.orientation = Quaternion()
        self.yaw = 0

        #  print("\n\nImu initialised\n\n")

    def callback(self, msg):
        Call back function for the laser
        self.orientation = msg.orientation

    def get_angle(self):
        self.yaw = yaw_from_quat(self.orientation)
        #  print(self.yaw)
        return self.yaw
"""
class GPSListener:
    """
    Class to subscribe to GPS
    """

    def __init__(self, topic_path):
        self.sub = rospy.Subscriber(
            name=topic_path, data_class=NavSatFix, callback=self.callback, queue_size=10)

    def callback(self, msg):
        """
        Call back function for the laser
        """
        self.lat = msg.latitude
        self.long = msg.longitude
        #print(self.lat,self.long)
    def get(self):
        return([self.lat, self.long])

"""
class LaserListener:
    Class to subscribe to laser

    def __init__(self, topic_path):
        self.sub = rospy.Subscriber(
            name=topic_path, data_class=LaserScan, callback=self.callback, queue_size=10)
        self.sin = get_sin_weights()
        self.cos = get_cos_weights()

        self.final_dir = [0, 0]
        self.ranges = []
        self.dir = []

        self.laser_max_range = laser_max_range

    def callback(self, msg):
        Call back function for the laser
        self.ranges = msg.ranges

    def move_dir(self):
        Returns direction to move in
        self.dir = []

        if self.ranges != self.dir:
            for i in range(len(self.ranges)):
                #  print(self.ranges)
                if self.ranges[i] == inf:
                    self.dir.append([self.laser_max_range *
                                     self.cos[i], self.laser_max_range * self.sin[i]])
                else:
                    self.dir.append([self.ranges[i] *
                                     self.cos[i], self.ranges[i] * self.sin[i]])

            self.final_dir = np.sum(self.dir, axis=0)
           # TODO: NORMALISE THE SUM

"""
