#!/usr/bin/python

import rospy

from comms import Communication_ROS
# from a_star import PathPlanner
# from class_model import Model_robot

# Init of program
if __name__ == '__main__':

    rospy.init_node('nav_node', anonymous=True)

    rospy.loginfo("Node init")

    Communication_ROS()

    # PathPlanner()

    rospy.spin()