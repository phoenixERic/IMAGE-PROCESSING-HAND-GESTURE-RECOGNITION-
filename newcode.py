import cv2
import numpy as np
import time
import pyautogui

def empty(a):
    pass

def create_trackbars():
    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 640, 300)
    cv2.createTrackbar('HueMin', 'Trackbars', 0, 179, empty)
    cv2.createTrackbar('HueMax', 'Trackbars', 179, 179, empty)
    cv2.createTrackbar('SatMin', 'Trackbars', 0, 255, empty)
    cv2.createTrackbar('SatMax', 'Trackbars', 255, 255, empty)
    cv2.createTrackbar('ValMin', 'Trackbars', 0, 255, empty)
    cv2.createTrackbar('ValMax', 'Trackbars', 255, 255, empty)

def create_mask(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos('HueMin', 'Trackbars')
    hue_max = cv2.getTrackbarPos('HueMax', 'Trackbars')
    sat_min = cv2.getTrackbarPos('SatMin', 'Trackbars')
    sat_max = cv2.getTrackbarPos('SatMax', 'Trackbars')
    val_min = cv2.getTrackbarPos('ValMin', 'Trackbars')
    val_max = cv2.getTrackbarPos('ValMax', 'Trackbars')
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    return mask

def find_contours(thresh):
    contours, heirarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)  #give list of all essential boundary points
    return contours

def max_contour(contours):
    if len(contours) == 0:
        return []
    max_cntr = max(contours, key=lambda x: cv2.contourArea(x))
    epsilon = 0.005 * cv2.arcLength(
        max_cntr, True
    )  # maximum distance from contour to approximated contour. It is an accuracy parameter
    max_cntr = cv2.approxPolyDP(max_cntr, epsilon, True)
    return max_cntr
def threshold(mask):
    _, thresh = cv2.threshold(
        mask, 127, 255, cv2.THRESH_BINARY
    )  # if pixel intensity <= 127 then set it as 0 and pixel intensity > 127 set it as 255
    return thresh
    def centroid(cnt):
        if(len(cnt)==0):
            return(-1,-1)
            M=cv2.moments(cnt)
            try:
                x=int(M['m10']/M['m00'])
                y=int(M['m10']/M['m00'])
            except ZeroDivisionError:
                return(-1,-1)
            return(x,y)


#################################################################################
########## Driver Code ##########################################################
#################################################################################

vid = cv2.VideoCapture(0)
create_trackbars()

while True:
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)  # resolving mirror image issues

    # Cropping the frame so that only right-half frame will detect hand motion
    height, width = frame.shape[:2]

        # Let's get the starting pixel coordiantes (top left of frame)
    start_row, start_col = int(0), int(width * .5)
    # Let's get the ending pixel coordinates (bottom right of frame)
    end_row, end_col = int(height), int(width)

    frame = frame[
        start_row:end_row, start_col:
        end_col]  # only considering frame row from start_row to end_row and col from start_col to end_col, so that main focus is on our hands

    frame = cv2.GaussianBlur(frame, (5, 5), 0)  # to remove noise from frame

    mask = create_mask(frame)
    threshImg = threshold(mask)
    contours = find_contours(mask)
    frame = cv2.drawContours(frame, contours, -1, (255, 0, 0),
                             2)  # drawing all contours
    max_cntr = max_contour(
        contours)  # finding maximum contour of the thresholded area

    cv2.imshow('video', frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break
    

vid.release()

cv2.destroyAllWindows()
#0,179,60,255,224,255