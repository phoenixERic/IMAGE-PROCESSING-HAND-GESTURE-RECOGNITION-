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
    lower = np.array([0,60, 224])
    upper = np.array([179, 255, 255])
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
def centroid(contour):
    if len(contour) == 0: # if the array is empty return (-1,-1) 
        return (-1,-1)
    M=cv2.moments(contour) # gives a dictionary of all moment values calculated
    try:
        x = int(M['m10']/M['m00'])  # Centroid is given by the relations, 𝐶𝑥 =𝑀10/𝑀00 and 𝐶𝑦 =𝑀01/𝑀00
        y = int(M['m01']/M['m00'])
    except ZeroDivisionError:
        return (-1,-1) 
    return (x,y)
def threshold(mask):
    _, thresh = cv2.threshold(
        mask, 127, 255, cv2.THRESH_BINARY
    )  # if pixel intensity <= 127 then set it as 0 and pixel intensity > 127 set it as 255
    return thresh

#################################################################################
########## Driver Code ##########################################################
#################################################################################

vid = cv2.VideoCapture(0)
create_trackbars()
prev_x,prev_y,cur_x,cur_y = -1,-1,-1,-1
frame_num = 4
last_timestamp=0
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
    max_cntr = max_contour(contours)  # finding maximum contour of the thresholded area
    (centroid_x,centroid_y) = centroid(max_cntr)
    if(centroid_x,centroid_y)!=(-1,-1):
        frame = cv2.circle(frame , (centroid_x,centroid_y) , 
                           5 , (255,255,0) , -1)
        # print(centroid_x,centroid_y)
        hand_detected = cv2.contourArea(max_cntr)>=14000
        #print(cv2.contourArea(max_cntr)) 
        if hand_detected:
            if prev_x == -1:
                prev_x, prev_y = centroid_x, centroid_y
                frame_num = 4
                # print(prev_x,prev_y)
            if frame_num == 0:
                cur_time = time.time()
                time_elapsed = cur_time - last_timestamp
                hand_motion = detect_motion(prev_x, prev_y, 
                        centroid_x, centroid_y, time_elapsed)
                print(hand_motion)
                performAction(hand_motion)
                prev_x, prev_y = centroid_x, centroid_y
                last_timestamp = time.time()

                # Re-initializing the frame counter
                if hand_motion != NO_MOTION:
                    frame_num = 4
                else:
                    frame_num = 6
            else:
                frame_num -= 1
        else:
            prev_x, prev_y = -1, -1
            frame_num = 4
        
            
        
        
    cv2.imshow('video', frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(10)

    if key == ord('q'):
        
        break

vid.release()

cv2.destroyAllWindows()