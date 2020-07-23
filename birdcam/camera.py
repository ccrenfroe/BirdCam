# This script is meant to handle all of the functionality of the camera.
# Could possibly extend this to have more functionality, like flipping snapshots if the camera is updside down, changing zoom, etc. If so, this could turn into a camera class.

import os
import time
from picamera import PiCamera

PICTURES_IN = 'Images/PicturesIn/'

timestr = time.strftime("%Y%m%d-%H%M%S")

camera = PiCamera()

camera.capture(PICTURES_IN + timestr + ".jpg")

