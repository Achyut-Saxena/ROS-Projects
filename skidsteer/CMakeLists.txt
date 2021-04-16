cmake_minimum_required(VERSION 3.0.2)

project(skidsteer)

add_compile_options(-std=c++17)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    geometry_msgs
    sensor_msgs
)

set(dependencies
    roscpp
    rospy
    geometry_msgs
    sensor_msgs
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})
include_directories(include)

add_library(skidsteer_core src/skidsteer.cpp)
target_link_libraries(skidsteer_core ${catkin_LIBRARIES})
# add_dependencies(skidsteer_core ${dependencies})

add_executable(skidsteer src/main.cpp)
target_link_libraries(skidsteer skidsteer_core ${catkin_LIBRARIES})
add_dependencies(skidsteer skidsteer_core)

