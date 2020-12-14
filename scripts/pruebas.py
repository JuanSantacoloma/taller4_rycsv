        
        
        self.max_x = 423.0
        self.min_x = 149.0
        self.resolution = 0.0500000007451

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)

        range(self.x_width)


    rx = np.array(rx)
    ry = np.array(ry)
    
    np.savetxt('px.csv',rx,delimiter=',')
    np.savetxt('py.csv',ry,delimiter=',')

    
    px = np.loadtxt('/home/camilo/ROS_UN/rycsv_ws/src/rycsv_pkg/scripts/px.csv',delimiter=',')
    py = np.loadtxt('/home/camilo/ROS_UN/rycsv_ws/src/rycsv_pkg/scripts/py.csv',delimiter=',')
    
    
    px = np.flip(px)
    py = np.flip(py)
    
    path_array = np.column_stack((px, py))