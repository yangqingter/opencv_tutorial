import cv2
import numpy as np

img=np.zeros((300,300,3),dtype='uint8')
cv2.line(img,(10,10),(10,50),(255,0,0),2)
cv2.rectangle(img,(100,50),(200,150),(0,255,0),2)
cv2.circle(img,(150,150),50,(0,0,255),1)
cv2.putText(img,'Hello, world',(50, 50),0, 1, (255, 255, 255), 2, 1)

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()