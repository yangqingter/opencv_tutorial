import cv2
import numpy as np

img=np.zeros((300,300,3),dtype='uint8')
cv2.line(img,(10,10),(10,50),(255,0,0),2)


cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()