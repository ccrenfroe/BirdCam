# BirdCam

Bird detector and classifier implemented using a Raspberry Pi and Tensorflow Lite.

## Things to think about

The camera will be set up to observe the bird feeder. What should be done to prevent false positives when the sway of the bird feeder indicates change?

Squirrels like to mess with the bird feeder alot also. Should Tensorflow train on squirrels as well?

Changes in time of day could also casue false positives.

How to detect change betweena  brown bird and brown background?

## Dataset

https://www.tensorflow.org/datasets/catalog/caltech_birds2011  - First Candidate.

## Hardware

* Raspberry Pi 4B 4gb [Link](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* Arducam Autofocus Pi camera [Link](https://www.amazon.com/gp/product/B07SN8GYGD/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

## Dependencies

## API's

[Picamera](picamera.readthedocs.io)
[Raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md)
[Raspivid](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md)

## Plan

1. Basics
  1. Connect Pi and computer using ssh.
  2. Create script for Pi to stream video
  3. Create script on computer to do steps 1 and 2.

2. Motion Detection
  4. Create script to take a picture when a certain amount of change is detected in the video stream.
  5. Test for false positives such as the sway of the bird feeder.

3. Machine Learning
  6. Train Tensorflow lite with the birds dataset.
  7. Test Tensorflow with pictures of birds. If it can be tested with pictures of birds from the camera, even better.
  8. Optionally add squirrels?
  
4. Organize Data
  9. Setup directory structure and automate where the pictures taken go to.
  10. Seperate folder for each bird type

## Potential future work

* Setup WebApp for the whole thing to run through.
* Connect the images taken to a SQL database.
* Send the images taken to AWS
