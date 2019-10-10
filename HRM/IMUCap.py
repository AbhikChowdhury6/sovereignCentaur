import sys
import time
import adafruit_bno055
from busio import I2C
from board import SDA, SCL

i2c = I2C(SCL, SDA)

sensor = adafruit_bno055.BNO055(i2c, 0x28)


while True:
    sensor.accelerometer
    sensor.gyroscope
    sensor.magnetometer
    sensor.quaternion
    sensor.linear_acceleration
    time.sleep(1)