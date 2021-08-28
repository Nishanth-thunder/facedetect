import cv2
import numpy as np
img=cv2.imread('p.jpeg')
imgjo=np.hstack((img,img))
cv2.imshow("hori",imgjo)
cv2.waitKey(0)