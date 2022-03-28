import cv2
left=cv2.imread("/home/h/PSMNet/test_img/left/11.png",cv2.IMREAD_COLOR)
right=cv2.imread("/home/h/PSMNet/test_img/right/11.png",cv2.IMREAD_COLOR)
#1241*376
left=cv2.resize(left, dsize=(1241, 376),interpolation=cv2.INTER_AREA)
right=cv2.resize(right, dsize=(1241, 376),interpolation=cv2.INTER_AREA)

cv2.imwrite("/home/h/PSMNet/test_img/left/11.png",left)
cv2.imwrite("/home/h/PSMNet/test_img/right/11.png",right)