import numpy as np
import cv2

img= cv2.imread('../opencv_logo.jpg')
G=img[:,:,0]
B=img[:,:,1]
R=img[:,:,2]

Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

im = np.hstack((G,B,R,Gray))
cv2.imshow('im',im)

cv2.waitKey()
cv2.destroyAllWindows()