import cv2
from PIL import Image
import numpy as np
import time 

from util import get_limits
from util import detect


yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
   
    
   

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #print(frame.shape)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    
    #detect(mask)############
    count = np.sum(np.nonzero(mask))
  
    #print("count =",count)
    #*if count == 0:
    #  print("Not Red")
    #else:
       # print("Red")
    #    points = cv2.findNonZero(mask)
    #    avg = np.mean(points, axis=0)
    #    print(avg)
    
    


    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    
    (h, w) = hsvImage.shape[:2]
    
    (cX, cY) = (w // 2, h // 2)
    
    left = hsvImage[0:479, 0:280]
    cv2.imshow("Left", left)
    right = hsvImage[0:479, 360:639]
    cv2.imshow("Right", right)
    middle = hsvImage[0:479, 281:359]
    cv2.imshow("middle", middle)
    
    
    height, width, channels = left.shape
    hsvL = cv2.cvtColor(left, cv2.COLOR_BGR2HSV_FULL)
    maskL = cv2.inRange(hsvL, lowerLimit, upperLimit)
    ones = cv2.countNonZero(maskL)
    percent_color = (ones/(height*width)) * 100
    print("left")
    print("Non Zeros Pixels:{:d} and Area Percentage:{:.2f}".format(ones,percent_color))
    cv2.imshow("mask left", maskL)
    #area percentahe 5 left##########################################################################################333
    
    height, width, channels = right.shape
    hsvR = cv2.cvtColor(right, cv2.COLOR_BGR2HSV_FULL)
    maskR = cv2.inRange(hsvR, lowerLimit, upperLimit)
    ones = cv2.countNonZero(maskR)
    percent_color = (ones/(height*width)) * 100
    print("right")
    print( "Non Zeros Pixels:{:d} and Area Percentage:{:.2f}".format(ones,percent_color))
    cv2.imshow("mask right", maskR)
    ##### above 2.5
    height, width, channels = middle.shape
    hsvm = cv2.cvtColor(middle, cv2.COLOR_BGR2HSV_FULL)
    maskm = cv2.inRange(middle, lowerLimit, upperLimit)
    ones = cv2.countNonZero(maskm)
    percent_color = (ones/(height*width)) * 100
    print("middle")
    print(" Non Zeros Pixels:{:d} and Area Percentage:{:.2f}".format(ones,percent_color))
    cv2.imshow("mask middle", maskm)
    #above 10
    
  
    
   
    

cap.release()

cv2.destroyAllWindows()
