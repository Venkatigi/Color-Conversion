import cv2
l_image=cv2.imread('wall.jpg')
hsv_image=cv2.cvtColor(l_image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv_image)
cv2.imshow('H',h)
cv2.imshow('S',s)
cv2.imshow('V',v)
merge=cv2.merge((h,s,v))
cv2.imshow('MERGE',merge)
cv2.waitKey(0)
cv2.destroyAllWindows()