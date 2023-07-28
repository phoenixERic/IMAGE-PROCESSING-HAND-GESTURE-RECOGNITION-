import cv2
import numpy as np

def nothing (x):
    pass
def createTrackbar():
    cv2.namedWindow("thresholding")
    cv2.createTrackbar("T","thresholding",0,255,nothing)


img= cv2.imread("images/hand.jpg")
cv2.imshow("original image",img)
img_graycolor=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image",img_graycolor)

createTrackbar()
while True:
    T=cv2.getTrackbarPos("T","thresholding")
    print(T)
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower=np.array([0,0,0])
    upper=np.array([100,150,200])
    thresh_img=cv2.inRange(img,lower,upper)

    cv2.imshow("threshimage",thresh_img)
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
    cv2.waitKey(0)
cv2.destroyAllWindows()