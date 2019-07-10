import bme280
import smbus2
import sys
import time
import adafruit_bno055
from busio import I2C
from board import SDA, SCL


sensor = adafruit_bno055.BNO055(i2c, 0x28)

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)





while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print(humidity, pressure, ambient_temperature)
    sleep(1)
