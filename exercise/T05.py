import cv2

img = cv2.imread('../plane.jpg')
im1=cv2.GaussianBlur(img,(3,3),1)
im2=cv2.medianBlur(img,3)

cv2.imshow("img",img)
cv2.imshow('im1',im1)
cv2.imshow('im2',im2)

cv2.waitKey()
cv2.destroyAllWindows()