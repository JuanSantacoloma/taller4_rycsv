import numpy as np
import cv2 

img = cv2.imread('map.pgm',0)
    ret,img = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
    
    h, w = img.shape[:2]

    alto_mapa = h/14.0 # metros
    ancho_mapa = w/15.0 # metros

    img = cv2.flip(img, 0)

    rows, cols = np.where(img==0)

    rows = rows/alto_mapa - 9.2
    cols = cols/ancho_mapa - 7.8

    oy = rows.tolist()
    ox = cols.tolist()

# img = cv2.imread('map.pgm',0)
# ret,img = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
# # ret,img = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# # kernel = np.ones((3,3),np.uint8)
# # img = cv2.dilate(img,kernel,iterations = 1)
# cv2.imwrite('map.png', img)

# # print(shape(img))

# rows, cols = np.where(img==0)

# rows = rows.tolist()
# cols = cols.tolist()


            
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()