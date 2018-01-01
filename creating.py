import urllib
import cv2
import numpy as np
import time
import imutils as im
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
    x = img.shape[0]
    y = img.shape[1]
    # (ex, ey) = (int(x / 4), int(y / 4))
    (ex, ey) = (x/2,y)
    (sx, sy) = (0, 0)
    # cv2.rectangle(img, (sx, sy), (ex, ey), (0, 0, 255), 1)
    handImage = img[sy:ey, sx:ex]
    # put the image on screen
    cv2.imshow('IPWebcam',img)


    #To give the processor some less stress
    time.sleep(0.01)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        cv2.imwrite("sumit_feet_bottom/bottom%d.jpg" % (count), img)
        print count

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break