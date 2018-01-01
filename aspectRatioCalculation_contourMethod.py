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
            feetImage = gray[d.top():d.bottom(),d.left():d.right()]
            _,thresh = cv2.threshold(feetImage,125,255,cv2.THRESH_BINARY)
            cnts = cv2.findContours(feetImage.copy(), cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            # check for green
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)

                ((x, y), radius) = cv2.minEnclosingCircle(c)

                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                area = cv2.contourArea(c)
                print("area", area)

                # only proceed if the radius meets a minimum size
                if radius > 5:
                    # draw the circle and centroid on the frame,

                    # cv2.circle(frame, (int(x), int(y)), int(radius),
                    #          (0, 255, 255), 2)
                    cv2.circle(output, center, 5, (0, 0, 255), -1)
                    leftmost = tuple(c[c[:, :, 0].argmin()][0])
                    rightmost = tuple(c[c[:, :, 0].argmax()][0])
                    topmost = tuple(c[c[:, :, 1].argmin()][0])
                    bottommost = tuple(c[c[:, :, 1].argmax()][0])
                    # cv2.rectangle(output,(leftmost,topmost),(rightmost,bottommost),(255,0,0))
                    rect1 = cv2.minAreaRect(c)
                    box = cv2.boxPoints(rect1)
                    box = np.int0(box)
                    cv2.drawContours(output, [c], -1, (255, 0, 255), 2)
    cv2.imshow("output", output)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()



