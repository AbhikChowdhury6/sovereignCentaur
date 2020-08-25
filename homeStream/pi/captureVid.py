import cv2
import sys
import imutils
import time
import numpy as np

sensorName = "camera"

#save format
#utctimestapwithms-sensorname
cam = cv2.VideoCapture(0)

#capture frame at 1080p
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

downsizeW = 128
downsizeH = 128

thresh = 20


while True:
    #first frame will be the refrence one and saved
    ret, startFrame = cam.read()
    #save frame
    cv2.imwrite("/home/pi/data/" + str(time.time()) + "-" + sensorName +".jpg", startFrame)
    smallStartFrame = imutils.resize(startFrame, height=downsizeH, width=downsizeW)
    graySmallStartFrame = cv2.cvtColor(smallStartFrame, cv2.COLOR_BGR2GRAY)
    print("startFrame####################################")
    #diff and threshold will be calculated for each subsequent frame and saved
    for i in range(50):
        lastTime = time.time()
        ret, frame = cam.read()
        smallFrame = imutils.resize(frame, height=downsizeH, width=downsizeW)
        graySmallFrame = cv2.cvtColor(smallFrame, cv2.COLOR_BGR2GRAY)
        delta = cv2.absdiff(graySmallStartFrame, graySmallFrame)
        maxDelta = np.max(delta)
        print(maxDelta)
        if maxDelta > thresh:
            cv2.imwrite("/home/pi/data/" + str(time.time()) + "-" + sensorName +".jpg", frame)
        print(time.time()-lastTime)