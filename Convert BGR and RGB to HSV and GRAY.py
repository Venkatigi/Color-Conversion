import cv2
wall_image=cv2.imread('wall.jpg')
cv2.imshow('car',wall_image)
#BGR2HSV
hsv_image=cv2.cvtColor(wall_image,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv_image)
#RGB2HSV
hsv_image1=cv2.cvtColor(wall_image,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv_image1)
#BGR2GRAY
gray_image=cv2.cvtColor(wall_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray_image)
#RGB2GRAY
gray_image1=cv2.cvtColor(wall_image,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()