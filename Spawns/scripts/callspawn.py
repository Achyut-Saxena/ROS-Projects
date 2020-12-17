#!/usr/bin/env python

import rospy
from spawn import spawn_model
from spawn import spawnable

'''
if __name__ == "__main__":
	rospy.init_node('spawn_service')
	rospy.wait_for_service('/gazebo/spawn_urdf_model')

	spawn_model(name="steer_model", 
			xml="/home/achyut2906/catkin_ws/src/skid2/model/steer.xacro").spawn()
'''
import yaml

if __name__ == "__main__":

	files_dict = { 
                   "tree: /home/achyut2906/catkin_ws/src/skid2/model/oak_tree/model.sdf", 
                   "beer: /home/achyut2906/catkin_ws/src/skid2/model/beer/model.sdf", 
                   "school: /home/achyut2906/catkin_ws/src/skid2/model/school/model.sdf", 
                   "sun: /home/achyut2906/catkin_ws/src/skid2/model/sun/model.sdf", 
                   "house_1: /home/achyut2906/catkin_ws/src/skid2/model/house_1/model.sdf", 
                   "house_2: /home/achyut2906/catkin_ws/src/skid2/model/house_2/model.sdf", 
                   "car: /home/achyut2906/catkin_ws/src/skid2/model/prius_hybrid/model.sdf"
    }
with open("/home/achyut2906/catkin_ws/src/skid2/config/model.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

    for d in data:
        obj = spawnable(d)
        a = spawn_model(
            name=obj.name, model_path=files_dict(obj.obj),
            x=obj.x, y=obj.y, z=obj.z, qx=obj.qx, qy=obj.qy, qz=obj.qz, qw=obj.qw
        ).spawn()

        print(a)

