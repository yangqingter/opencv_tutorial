import numpy as np
import cv2

img = cv2.imread('../opencv_logo.jpg')
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()