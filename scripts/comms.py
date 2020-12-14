#!/usr/bin/python

import rospy

from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid

import numpy
from   rospy.numpy_msg import numpy_msg

# from class_model import Model_robot

class Communication_ROS:

    def __init__(self):

        # Atributos
        self.topicSubs = "/map"

        self.height = 0.0
        self.width = 0.0
        self.data = 0.0
        
        # self.ogrid = rospy.Subscriber(self.topicSubs, OccupancyGrid, callback, queue_size=10)
        rospy.Subscriber("/map", OccupancyGrid, self.callback)
        # print(OccupancyGrid)
        # self.topicPubFront = "/front_wheel_ctrl/command"
        # self.topicPubLeft  = "/left_wheel_ctrl/command"
        # self.topicPubRight = "/right_wheel_ctrl/command"

        

        # self.flagCmd = False

        # self.modelo = Model_robot()

        # Publicador
        # self.pubVelFront = rospy.Publisher(self.topicPubFront, numpy_msg(Float64), queue_size=10)
        # self.pubVelLeft  = rospy.Publisher(self.topicPubLeft, numpy_msg(Float64), queue_size=10)
        # self.pubVelRight = rospy.Publisher(self.topicPubRight, numpy_msg(Float64), queue_size=10)

        # Subscriptor
        # rospy.Subscriber(self.topicSubs, numpy_msg(Twist), self.cmd_vel_CB, queue_size=10)

    def callback(self,msg):
        
        self.height = msg.info.height
        self.width = msg.info.width
        self.data = msg.data
        
        for i in range(self.width): 
            for j in range(self.height):
              world[i][j] = self.data[i + j * self.width]

        rospy.loginfo(rospy.get_caller_id() + "I heard %s", world)
        return world
            
        