import sys
import os
import time
deviceName = sys.argv[1]
deviceInstance = sys.argv[2]
sensorList = ["camera"]


while True:
    #grab filenames from datafolder
    folderContentslist = os.listdir("/home/pi/data/")

    #parse out time and generate filepath
    #iterate over lists and extract the year, month, day, hour, minute and sensorname
    for fn in folderContentslist:
        arr = fn.split("-")
        
        arr
        0]
    
    while True:
        #based on the sensorname generate commands that group files into sets of 100 send and delete originals
        #send a set of images
        #send a set of other stuff
        #send a set of other stuff

    #wait a bit and repeat
    time.sleep(.5)

