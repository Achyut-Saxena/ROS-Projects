#!/usr/bin/env python3

"""
All listener classes used are defined here
"""

from math import inf, cos, pi, radians
import rospy
from sensor_msgs.msg import LaserScan, NavSatFix
from gazebo_msgs.srv import GetModelState
from weights import get_cos_weights, get_sin_weights
import numpy as np


class GazeboGetModelState:
    """
    Class to return pose of any object in the gazebo simmulation
    """

    def __init__(self, service_name, model_name):
        rospy.wait_for_service(service_name)

        self.model_name = model_name
        self.req = rospy.ServiceProxy(service_name, GetModelState)

    def get(self):
        """
        Gets the model state based on the name
        """
        model_state = self.req(self.model_name, "")


class GPSListener:
    """
    Class to subscribe to GPS
    """

    def __init__(self, topic_path):
        self.sub = rospy.Subscriber(
            name=topic_path, data_class=NavSatFix, callback=self.callback, queue_size=10)

        self.lat0 = 49.89999999917954
        self.long0 = 8.899999997026308
        self.R = 6371000

        self.lat = 0
        self.long = 0

        self.scalelat = (1/57.24)
        self.scalelong = (-1/88.73)

        self.x = 0
        self.y = 0

    def callback(self, msg):
        """
        Call back function for the laser
        """
        self.lat = msg.latitude
        self.long = msg.longitude

        self.calculate_projection(self.R)

    def calculate_projection(self, R):
        self.x = R * (self.lat - self.lat0) * self.scalelat
        self.y = R * (self.long - self.long0) * self.scalelong

        #  print([self.x, self.y])


class LaserListener:
    """
    Class to subscribe to laser
    """

    def __init__(self, topic_path, laser_max_range):
        self.sub = rospy.Subscriber(
            name=topic_path, data_class=LaserScan, callback=self.callback, queue_size=10)
        self.sin = get_sin_weights()
        self.cos = get_cos_weights()

        self.final_dir = [0, 0]
        self.ranges = []
        self.dir = []

        self.laser_max_range = laser_max_range

    def callback(self, msg):
        """
        Call back function for the laser
        """
        self.ranges = msg.ranges

    def move_dir(self):
        """
        Returns direction to move in
        """
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
