import numpy as np
import cv2

a = cv2.imread("input.jpg", cv2.IMREAD_UNCHANGED)
b = cv2.imread("input.jpg", cv2.IMREAD_UNCHANGED)

a = a.astype(float)/255
b = b.astype(float)/255

d=1-(1-a)*(1-b)
out=(d*255).astype(np.uint8) 

cv2.imshow("water", out)
cv2.waitKey(0)
