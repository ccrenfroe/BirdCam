# Imports
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time

# Global
vs = cv2.VideoCapture(0)
#vs = VideoStream(src=0).start()
time.sleep(2)
firstFrame = None
# CONSTANT
MIN_AREA = 500

while True:
    frame = vs.read()
    if frame[0] is False: # If read returned False, there was no frame to grab.
        print("Error getting frame")
        exit()
    else: # Gets the image
        frame = frame[1]
   
    #Resize to make the image less intensive to process
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to gray to make the image easier to run through Gaussian blur.
    gray = cv2.GaussianBlur(gray, (21, 21), 0) # Smooths out the pixels to get rid of any high variation between pixel intensities in a given region (x, x)
    if firstFrame is None:
        firstFrame = gray
        continue
    
    # Compute Abs diffrence between current frame and first frame.
    frameDelta = cv2.absdiff(firstFrame,gray) # Simple subtraction of pixel intensities
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1] # Thresholding the frameDelta. Only showing changes greater than x pixels, given by 2nd parameter argument.

    thresh = cv2.dilate(thresh, None, iterations=2)
    contours = cv2.findContours(thresh.copy(), cv2. RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    
    # Loop over the contours.
    # If the current contour is too small, ignore it
    for c in contours:
        if cv2.contourArea(c) < MIN_AREA:
            continue
        # Else a bounding box is drawn around it
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Showing frames
    cv2.imshow("First",firstFrame)
    cv2.imshow("Normal",frame)
    cv2.imshow("Thresh",thresh)
    cv2.imshow("Frame Delta", frameDelta)

vs.release()
cv2.destroyAllWindows()
