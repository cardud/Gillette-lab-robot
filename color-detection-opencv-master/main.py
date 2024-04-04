import cv2
from PIL import Image
import numpy as np
import time 

from util import get_limits#detect


yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    
    #detect(mask)############
    count = np.sum(np.nonzero(mask))
  
    #print("count =",count)
    if count == 0:
        print("Not Red")
    else:
       # print("Red")
        points = cv2.findNonZero(mask)
        avg = np.mean(points, axis=0)
        print(avg)
    (h, w) = hsvImage.shape[:2]
        
    (cX, cY) = (w // 2, h // 2)
# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
    right = hsvImage[h, 5:cX]
    left = hsvImage[h, 100:cX]
    cv2.imshow("right", right)
    #cv2.imshow("middle", m)
    cv2.imshow("left", left)
    (b, g, r) = hsvImage[0, 0]
    print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
    


    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
