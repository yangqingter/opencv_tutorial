import cv2
import numpy as np

a1=np.arange(0,10,1)
a1.ravel()

img = cv2.imread('../opencv_logo.jpg')
img_g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img_g,100,0.05,5 )

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img, (int(x),int(y)),3,(255,0,255),1)

cv2.imshow('im',img)
cv2.waitKey()
cv2.destroyAllWindows()



