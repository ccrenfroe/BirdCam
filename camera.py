# Simple program to test the picamera library with the Arducam.


# Imports
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()
