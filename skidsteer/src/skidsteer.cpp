#include "skidsteer/skidsteer.h"

laser::laser(ros::NodeHandle &nh)
{

    this->nh_ = nh;
    
    this->sub_ = this->nh_.subscribe("/scan", 1000, &laser::lscb_, this);       

}




