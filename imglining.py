import cv2
import numpy as np

def nothing (x):
    pass
def createTrackbar():
    cv2.namedWindow("thresholding")
    cv2.createTrackbar("H_min","thresholding",0,255,nothing)
    cv2.createTrackbar("H_max","thresholding",0,255,nothing)
    cv2.createTrackbar("S_min","thresholding",0,255,nothing)
    cv2.createTrackbar("S_max","thresholding",0,255,nothing)
    cv2.createTrackbar("V_min","thresholding",0,255,nothing)
    cv2.createTrackbar("V_max","thresholding",0,255,nothing)
    
img= cv2.imread("images/colors.jpeg")
cv2.imshow("original image",img)
img_graycolor=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image",img_graycolor)

createTrackbar()
while True:
    H_min=cv2.getTrackbarPos("H_min","thresholding")
    H_max=cv2.getTrackbarPos("H_max","thresholding")
    V_min=cv2.getTrackbarPos("V_min","thresholding")
    V_max=cv2.getTrackbarPos("V_max","thresholding")
    S_min=cv2.getTrackbarPos("S_min","thresholding")
    S_max=cv2.getTrackbarPos("S_max","thresholding")
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower=np.array([H_min,S_min,V_min])
    upper=np.array([H_max,S_max,V_max])
    thresh_img=cv2.inRange(img,lower,upper)

    cv2.imshow("threshimage",thresh_img)
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()