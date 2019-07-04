from websocket import create_connection
import json
import time

ip = "192.168.43.90"
ws = create_connection("ws://"+ ip +"/ws")

#schema
    #type
        #
obj = {}



ws.send(json.dumps(obj))
time.sleep(.1)


print("Receiving...")
while True:
    print("waiting")
    result =  ws.recv()
    print("Received '%s'" % result)


class hapserver:
    def __init__(self,ip = "192.168.43.90"):
        self.ws = create_connection("ws://"+ ip +"/ws")

    def send(self,hapFrames):
        #loop through hap frames and send them
        for f in hapFrames:
            print(json.dumps(f))
            self.ws.send(json.dumps(f))
            time.sleep(.1)
        print("Sent")

        

class hapFrames:
    def __init__(self):
        self.frames = []
        #ms and frame

    def addBWFrame(self, ms, lit, size):
        #make an array of size filled with zeroes
        #loop through the lit array and set
        frame = {}
        r = [0]*size
        g = [0]*size
        b = [0]*size

        for l in lit:
            r[l]=255
            g[l]=255
            b[l]=255
        
        frame['ms'] = ms
        frame['red'] = r
        frame['blue'] = b
        frame['green'] = g
        self.frames.append(frame)
        print ("added")
        print(frame)

