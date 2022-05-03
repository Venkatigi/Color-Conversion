import cv2
lam_image=cv2.imread('wall.jpg')
cv2.imshow('original image',lam_image)
#RGB2YCrCb
ycrcb_image=cv2.cvtColor(lam_image,cv2.COLOR_RGB2YCrCb)
cv2.imshow('RGB 2 YCrCb',ycrcb_image)
#BGR2YCrCb
ycrcb_image1=cv2.cvtColor(lam_image,cv2.COLOR_BGR2YCrCb)
cv2.imshow('BGR 2 YCrCb',ycrcb_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()