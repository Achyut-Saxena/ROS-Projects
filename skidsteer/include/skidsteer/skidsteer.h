#ifndef SKIDSTEER_H
#define SKIDSTEER_H

#include "ros/console.h"
#include "ros/node_handle.h"
#include "ros/ros.h"
#include "geometry_msgs/TwistStamped.h"
#include "ros/subscriber.h"
#include "sensor_msgs/LaserScan.h"
#include <memory>
#include "realtime_tools/realtime_publisher.h"
#include "nav_msgs/Odometry.h"

class laser
{

    // This Class is for Laser Based Obstacle Avoidance system.

    public: 
        laser(ros::NodeHandle &nh);
        void guide_();
        void lscb_(const sensor_msgs::LaserScan::ConstPtr &msg);
       
    private:
        ros::Subscriber sub_;

    protected:
        ros::NodeHandle nh_;
        std::shared_ptr<realtime_tools::RealtimePublisher<geometry_msgs::TwistStamped>> vel_pub_;
        std::shared_ptr<sensor_msgs::LaserScan> ls_;
};

class imu
{

    // This Class is for publishing IMU based Odometry.

    public:
        imu(ros::NodeHandle &nh_);
        void odom_();

    private:
        ros::Subscriber sub_;

    protected:
        ros::NodeHandle nh_;
        std::shared_ptr<realtime_tools::RealtimePublisher<nav_msgs::Odometry>> odom_pub_;
};


#endif
