cmake_minimum_required(VERSION 3.0.2)
project(lidskid)
find_package(catkin REQUIRED COMPONENTS
    urdf    
)

include_directories(
    ${catkin_INCLUDE_DIRS}
)

