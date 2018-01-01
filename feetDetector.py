from imutils import face_utils
import imutils
import dlib
import cv2
import numpy as np
import urllib
import time
import imutils as im

detector = dlib.simple_object_detector("feet_01.svm")


# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.43.1:8080/shot.jpg'
count =0
while True:
    count +=1
    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = im.resize(img,500,500,cv2.INTER_AREA)
    gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    output = img.copy()
    rects = detector(gray)
    ## search for feet in the frame---------------
    if len(rects) > 0 :
        for k, d in enumerate(rects):
            cv2.rectangle(output, (d.left(), d.top()), (d.right(), d.bottom()), (0, 255, 255))
    cv2.imshow("output", output)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()



