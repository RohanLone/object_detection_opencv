import numpy as np
import cv2 as cv

def nothing(x):
    pass   

cap = cv.VideoCapture(0)

# Create a window
cv.namedWindow('Trackbar')

# create trackbars for color change
cv.createTrackbar("L - H", "Trackbar",0,179,nothing)
cv.createTrackbar("L - S", "Trackbar",0,255,nothing)
cv.createTrackbar("L - V", "Trackbar",0,255,nothing)
cv.createTrackbar("U - H", "Trackbar",179,179,nothing)
cv.createTrackbar("U - S", "Trackbar",255,255,nothing)
cv.createTrackbar("U - V", "Trackbar",255 ,255,nothing)

while True:
    
    # Capture frame-by-frame
    _,frame = cap.read()
    
    #operations on the frame come here
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    # get current positions of trackbars
    l_h = cv.getTrackbarPos("L - H", "Trackbar")
    l_s = cv.getTrackbarPos("L - S", "Trackbar")
    l_v = cv.getTrackbarPos("L - V", "Trackbar")
    u_h = cv.getTrackbarPos("U - H", "Trackbar")
    u_s = cv.getTrackbarPos("U - S", "Trackbar")
    u_v = cv.getTrackbarPos("U - V", "Trackbar")
    
    #range for mask window
    min_range = np.array([l_h,l_s,l_v])
    max_range = np.array([u_h,u_s,u_v])
    
    # a mask is the same size as our frame, but has only two pixel
    # values, 0 and 255 -- pixels with a value of 0 (background) are
    # ignored in the original frame while mask pixels with a value of
    # 255 (foreground) are allowed to be kept
    
    mask =  cv.inRange(hsv,min_range,max_range)
    
    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    
    key = cv.waitKey(1)
    if key == 27:
        break    

cap.release()
cv.destroyAllWindows()