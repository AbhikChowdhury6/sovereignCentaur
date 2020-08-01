import cv2
import sys
import imutils
import time

sensorName = "camera"

#save format
#utctimestapwithms-sensorname

thresh = 1000

cam = cv2.VideoCapture(0)

#capture frame at 1080p
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


while True:
    #first frame will be the refrence one and saved
    startFrame = cam.read()
    #save frame
    cv2.imwrite("/home/pi/data/" + str(time.time()) + "-" + sensorName +".jpg", startFrame)
    smallStartFrame = imutils.resize(startFrame, height=64, width=128)
    graySmallStartFrame = cv2.cvtColor(smallStartFrame, cv2.COLOR_BGR2GRAY)

    #diff and threshold will be calculated for each subsequent frame and saved
    for i in range(1000):
        lastTime = time.time()
        frame = cam.read()
        smallFrame = imutils.resize(frame, height=64, width=128)
        graySmallFrame = cv2.cvtColor(smallFrame, cv2.COLOR_BGR2GRAY)
        totalDelta = sum(cv2.absdiff(graySmallStartFrame, graySmallFrame))
        print(totalDelta)
        if totalDelta > thresh:
            cv2.imwrite("/home/pi/data/" + str(time.time()) + "-" + sensorName +".jpg", frame)
        print(time.time()-lastTime)