import cv2
import numpy as np
img_path ="./images/sherlock_kid.png"
img=cv2.imread(img_path)
# img=np.zeros([400,760,3])
#cv2.imshow("image",img)
#cv2.waitKey(0)
#img.fill(255)
# cv2.imshow("image",img)
# cv2.waitKey(0)
img_shape=img.shape
img_white=np.full(img_shape,255,dtype=np.uint8)
#cv2.imshow("image",img_white)
#cv2.waitKey(0)

# img_negative=np.subtract(img_white,img)

# cv2.imshow("image",img_negative)
# cv2.waitKey(0)
#img+red(0,0,50)
