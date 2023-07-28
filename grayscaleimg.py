import cv2
img_path ="./images/gray_scale.png"
img=cv2.imread(img_path)
img_graycolor=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh_img=cv2.threshold(img_graycolor,50,255,cv2.THRESH_BINARY)
#cv2.imshow("th img",thresh_img)
cv2.waitKey(0)
#reading of pixel dimensions
(h,w)=img_graycolor.shape
for num in range(0,h):
    for num2 in range(0,w):
        if img_graycolor[num][num2]>70 :
            
             img_graycolor[num,num2]=255
        else:
            img_graycolor[num,num2]=0
cv2.imshow("image",img_graycolor)
cv2.waitKey(0)

