#!/usr/bin/env python3

"""
Script to perform local navigation
"""
from math import atan2, pi
import time

import rospy
from sensor_msgs.msg import LaserScan
from weights import *
from geometry_msgs.msg import Twist, Vector3
import numpy as np


class LaserListener:
    """
    Class to subscribe to laser
    """

    def __init__(self, topic_path):
        self.sub = rospy.Subscriber(
            name=topic_path, data_class=LaserScan, callback=self.callback, queue_size=10)
        self.sin = get_sin_weights()
        self.cos = get_cos_weights()

        self.final_dir = [0, 0]
        self.ranges = []

    def callback(self, msg):
        """
        Call back function for the laser
        """
        self.ranges = msg.ranges
        #  print(self.ranges)

    def move_dir(self):
        """
        Returns direction to move in
        """
        #  print(self.ranges)
        self.dir = []

        if self.ranges != self.dir:
            for i in range(len(self.ranges)):
                if self.ranges[i] == math.inf:
                    self.dir.append([LASER_MAX_RANGE *
                                     self.cos[i], LASER_MAX_RANGE * self.sin[i]])
                else:
                    self.dir.append([self.ranges[i] *
                                     self.cos[i], self.ranges[i] * self.sin[i]])

            self.final_dir = np.sum(self.dir, axis=0)
            # TODO: NORMALISE THE SUM

        else:
            self.final_dir = [0, 0]

        return self.final_dir


class Controller:
    """
    Class to controll the motion of the robot
    """

    def __init__(self, scaling_factor):
        self.msg = Twist()
        self.scaling_factor = scaling_factor

        self.prev_velocity = 0
        self.desired_velocity = 0
        self.prev_angle = 0
        self.desired_angle = 0

        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    def move(self, final_dir):
        """
        Composes velocity message
        """
        final_dir = [i * self.scaling_factor for i in final_dir]

        #  print(final_dir)
        self.desired_velocity = final_dir[1]
        self.desired_angle = (
            (atan2(final_dir[1], final_dir[0]) * 180)/pi) - 90

        self.desired_velocity = (
            3 * self.prev_velocity + self.desired_velocity)/4
        self.desired_angle = (3 * self.prev_angle/5 + self.desired_angle)/4

        self.prev_velocity = self.desired_velocity
        self.prev_angle = self.desired_angle

        self.publish()

    def publish(self):
        """
        Publishes the self.msg
        """
        self.msg.linear.x = self.desired_velocity
        self.msg.angular.z = self.desired_angle

        self.pub.publish(self.msg)


if __name__ == "__main__":

    LASER_MAX_RANGE = 30
    MAX_DISTANCE = 10
    TIME_DIFFERECNE = 0.5

    current_distance = 0

    rospy.init_node("p")
    Laser = LaserListener(topic_path="/laser/scan")

    C = Controller(scaling_factor=0.0001)

    while not rospy.is_shutdown():

        final_dir = Laser.move_dir()
        #  print(final_dir)
        C.move(final_dir)

        rospy.sleep(0.01)

