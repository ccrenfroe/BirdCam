# Simple program to take picture with arducam

# Imports
from picamera import PiCamera

camera = PiCamera()
test_image = camera.capture("test.png")
