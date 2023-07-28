import cv2
img_path ="./images/sherlock_kid.png"
img=cv2.imread(img_path)
print(img)

print(img.shape)
img_HSV=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("image",img_HSV)
#cv2.waitKey(0)
#cv2.imwrite("./images/sherlock_kid_hsv.png",img_HSV)
print(img_HSV.shape)
img_resized=cv2.resize(img,(300,700))
#cv2.imshow("image",img_resized)
#cv2.waitKey(0)
img_cropped=img_HSV[50:300,400:700]
cv2.imshow("image",img_cropped)
cv2.waitKey(0)
cv2.imshow("./images/sherlock_kid_cropped.png",img_cropped)
