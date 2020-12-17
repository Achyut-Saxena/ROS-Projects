#!/usr/bin/env python
import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

class spawn_model:
	def __init__(self, name="model_name", xml="path/to/model",
				 robot_namespace="/", reference_frame="world", 
				 x=0, y=0, z=0, qx=0, qy=0, qz=0, qw=1):

		self.name = name
		self.xml = xml
		self.robot_namespace = robot_namespace
		self.reference_frame = reference_frame

		self.pose = Pose()
		self.pose.position.x = x
		self.pose.position.y = y
		self.pose.position.z = z
		self.pose.orientation.x = qx
		self.pose.orientation.y = qy
		self.pose.orientation.z = qz
		self.pose.orientation.w = qw
    	
	def spawn(self):
		with open(self.xml, 'r') as f:
			xml = f.read()

		s = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel
							  )(self.name, xml, self.robot_namespace, self.pose, self.reference_frame)
			
		return "Done"

class spawnable:
    def __init__(self, d):
        self.obj = str(list(d.keys())[0])
        print(str(d)+'\n\n'+self.obj)
        self.name = d[self.obj]['name']
        [self.x, self.y, self.z] = d[self.obj]['xyz'].split(' ')
        [self.qx, self.qy, self.qz, self.qw] \
            = d[self.obj]['qxqyqzqw'].split(' ')

        self.x = float(self.x)
        self.y = float(self.y)
        self.z = float(self.z)
        self.qx = float(self.qx)
        self.qy = float(self.qy)
        self.qz = float(self.qz)
        self.qw = float(self.qw)
