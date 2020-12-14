#!/usr/bin/python

import rospy

from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid

import numpy as np
from   rospy.numpy_msg import numpy_msg
from a_star import PathPlanner
from a_start_AtsushiSakai import AStarPlanner

from prm import prm_planning


# from class_model import Model_robot

class Communication_ROS:

    def __init__(self):

        # Atributos
        self.topicSubs = "/map"

        self.height = 0
        self.width = 0
        self.data = 0
        self.resol = 0.0

        self.sx = -2.0 
        self.sy = 1.0
        self.gx = 4.0
        self.gy = 4.0
        # self.ogrid = rospy.Subscriber(self.topicSubs, OccupancyGrid, callback, queue_size=10)
        rospy.Subscriber("/map", OccupancyGrid, self.callback)
        
    def callback(self,msg):
        
        self.height = msg.info.height
        self.width = msg.info.width
        self.data = msg.data
        self.world = np.zeros((self.width,self.height))
        self.resol = msg.info.resolution
        self.offset_x = msg.info.origin.position.x
        self.offset_y = msg.info.origin.position.y

        for i in range(self.width): 
            for j in range(self.height):
                if self.data[i + j * self.width] == 100:
                    self.world[i][j] = 1
                elif self.data[i + j * self.width] == -1:
                        self.world[i][j] = 0
                else:
                    self.world[i][j] = self.data[i + j * self.width]

        # self.planer = PathPlanner(self.world,False)
        # self.heur = self.planer.a_star(self.test_start, self.test_goal)
        rows, cols = np.where(self.world==1)
        mov_x = self.offset_x/self.resol
        mov_y = self.offset_y/self.resol
        rows = rows + mov_x 
        cols = cols + mov_y 

        self.rx = np.array(rows)/10
        self.ry = np.array(cols)/10
        # print(self.rx)
        rr=0.5
        # print('sx={} ,sy={}, gx={}, gy={}, ox={}, oy={}, rr={}'.format(self.sx, self.sy, self.gx, self.gy, self.rx, self.ry,rr))
        self.roadx ,self.roady = prm_planning(self.sx, self.sy, self.gx, self.gy, self.rx, self.ry, rr)

        self.roadx = self.roadx[::-1]
        self.roady = self.roady[::-1]

        # print(self.roadx)
        # print(self.roady)
        