import cv2

img = cv2.imread('../opencv_logo.jpg')
print(img.shape)
cv2.imshow('im',img[50:200,50:200])

cv2.waitKey()
cv2.destroyAllWindows()