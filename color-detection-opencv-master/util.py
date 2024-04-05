import numpy as np
import cv2


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

def detect(window,LL,UL,name):
    height, width, channels = window.shape
    hsv = cv2.cvtColor(window, cv2.COLOR_BGR2HSV_FULL)
    name = cv2.inRange(hsv, LL, UL)
    ones = cv2.countNonZero(mask)
    percent_color = (ones/(height*width)) * 100
    print("Non Zeros Pixels:{:d} and Area Percentage:{:.2f}".format(ones,percent_color))
    cv2.imshow("mask", name)

