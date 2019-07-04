#prototype thalmic nuclei for Body worn IMU data
import sys
from websocket import create_connection
import json
import time

#ip = "192.168.43.90"
ip = sys.argv[1]
ws = create_connection("ws://"+ ip +"/ws")

name = sys.argv[2]
print(name + " Connected!!!")
#schema
#save timestamp and each data point seperately
#
#
#


BNOf = open(name + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(int(round(time.time() * 1000))) + ".csv", "a+")

while True:
#    print("waiting")
    result =  ws.recv()
#    print(result)
    BNOf.write(result)
#    print(time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime()) + "." + str(int(round(time.time() * 1000))))
#    print(len(result.split("\n")))
    #got a packet
    #parse Packet
    #append to relevant files
    #sendo to other processes
    #wait again

