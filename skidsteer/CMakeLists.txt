cmake_minimum_required(VERSION 3.0.2)
project(skidsteer)

find_package(catkin REQUIRED COMPONENTS
    rospy
    velodyne_simulator
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

