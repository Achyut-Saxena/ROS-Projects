#!/usr/bin/env python3
"""
Controller class for the robot
"""


from math import atan2, pi
import rospy
from geometry_msgs.msg import Twist


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
        Composes velocity message (call this)
        """
        goal_x = 0.433449 
        goal_y = 9.631706
        self.current = self.get_gps.get()

        inc_x = goal_x - self.current[0]
        inc_y = goal_y - self.current[1]

        theta = 0
        angle_target = atan2(inc_y, inc_x)
        if abs(angle_target-theta)>0.1:
            self.desired_velocity = 0.0
            self.desired_angle = 0.3

        else:
            self.desired_velocity = 0.5
            self.desired_angle = 0.0

   """     final_dir = [i * self.scaling_factor for i in final_dir]

        if final_dir[1] > 0.05:
            self.desired_velocity = final_dir[1]
            self.desired_angle = (
                (atan2(final_dir[1], final_dir[0]) * 180)/pi) - 90

        else:
            self.desired_velocity = 0
            self.desired_angle = 45

        self.desired_velocity = (
            3 * self.prev_velocity + self.desired_velocity)/4
        self.desired_angle = (3 * self.prev_angle/5 + self.desired_angle)/4

        self.prev_velocity = self.desired_velocity
        self.prev_angle = self.desired_angle
"""
        self.publish()

    def publish(self):
        """
        Publishes the self.msg
        """
        self.msg.linear.x = self.desired_velocity
        self.msg.angular.z = self.desired_angle

        self.pub.publish(self.msg)
