import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    color_input = np.uint8([[[255,0,0 ]]])#this is for yellow
    hsv_color = cv2.cvtColor(color_input,cv2.COLOR_BGR2HSV)
    #print(hsv_color)
    #range of color[ normally taken as -/+10]
    hsv_color_lower=np.uint8([[[hsv_color[0][0][0]-10,hsv_color[0][0][1]+101,hsv_color[0][0][2]+101]]])
    hsv_color_upper=np.uint8([[[hsv_color[0][0][0]+10,hsv_color[0][0][1],hsv_color[0][0][2]]]])

    # Threshold the HSV image to get only color given
    mask=cv2.inRange(hsv,hsv_color_lower,hsv_color_upper)


    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('Color_mask',mask)
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
