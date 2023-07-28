import cv2 
videoreader=cv2.VideoCapture(0)#readin from webcam
while True:
    yes,frame=videoreader.read()
    if not yes:
        break
    cv2.imshow("this is videoo",frame)
    key=cv2.waitKey(10)
    if key==ord('q'):
        break
videoreader.release()
cv2.destroyAllWindows()

