import time
import os
import picamera
from sense_hat import SenseHat

y = (0, 255, 255)
b = (0,   0,   0)

smile = [
b,b,b,b,b,b,b,b,
b,b,y,y,y,y,b,b,
b,y,b,y,y,b,y,b,
b,y,y,y,y,y,y,b,
b,y,b,y,y,b,y,b,
b,y,b,b,b,b,y,b,
b,b,y,y,y,y,b,b,
b,b,b,b,b,b,b,b
]

try:
    os.mkdir("/tmp/capture")
except:
    pass
FILE_PATH_TEMPLATE = "/tmp/capture/img{04d}"


sense = SenseHat()
cam = picamera.PiCamera()
time.sleep(2)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 1 or y > 1 or z > 1:
        sense.set_pixels(smile)
        cam.capture(FILE_PATH_TEMPLATE.format(i))
        time.sleep(0.15)
    else:
        sense.clear()
