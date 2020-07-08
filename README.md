# BirdCam

## Purpose

Bird detector and classifier implemented using a Raspberry Pi and Tensorflow Lite.

The goal of this project is to implement a Smart BirdCam. The BirdCam should be fully automated, left to watch a bird feeder and take a picture when a bird shows up. The iamge should then be sent to some server, or locally, to then be run through a classifier and then stored into a directory for that birds species. Hopefully, the user can notice trends in what birds are visiting them and get some cool pictures as well.

## Dataset

<s> <https://www.tensorflow.org/datasets/catalog/caltech_birds2011>  - First Candidate. </s>

<https://tfhub.dev/google/lite-model/aiy/vision/classifier/birds_V1/1> - Birds V1.1 ;
Tensorflow mobile bird classification model using the MobileNetV2 architecture  and the iNaturalist dataset.

## Hardware

* Raspberry Pi 4B 4gb [Link](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* Arducam Autofocus Pi camera [Link](https://www.amazon.com/gp/product/B07SN8GYGD/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

I suggest [this](https://www.amazon.com/CanaKit-Raspberry-4GB-Basic-Starter/dp/B07VYC6S56/ref=pd_lpo_147_img_2/146-6394024-8709460?_encoding=UTF8&pd_rd_i=B07VYC6S56&pd_rd_r=5541e070-5353-4f25-a815-786f0e5ca915&pd_rd_w=aQ4LV&pd_rd_wg=yy3j5&pf_rd_p=7b36d496-f366-4631-94d3-61b87b52511b&pf_rd_r=0WTRDN6F9CNVJZZG94YW&psc=1&refRID=0WTRDN6F9CNVJZZG94YW) kit for the pi. Comes with power supply, case for the pi, and hdmi adapter for a computer screen. Could always just get the pi alone and a power supply also and just ssh into the pi.
Also, I recommend the [SanDisk Extreme 32Gb](https://www.amazon.com/gp/product/B06XWMQ81P/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) SDHC Card.

## Dependencies

Most of these should be available through Anaconda, so I would start my installing that.

[PIL](https://www.pythonware.com/products/pil/) - May change to pillow
[numpy](https://numpy.org/)
[imutils](https://pypi.org/project/imutils/)
[cv2](https://docs.opencv.org/2.4/index.html)
[tflite_runtime.interpreter](https://www.tensorflow.org/lite/guide/python#install_just_the_tensorflow_lite_interpreter)

## Docs

### For the Camera

[Picamera](picamera.readthedocs.io)
[Raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md)
[Raspivid](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md)

### For Motion Detection

[OpenCV](https://docs.opencv.org/2.4/index.html)

### For Object Classification

[Tensorflow Lite](https://www.tensorflow.org/lite/api_docs)

## Tasks

Streaming

* Connect Pi and computer using ssh.
* Create script for Pi to stream video
* Create script on computer to do steps 1 and 2.

Motion Detection

* Create script to take a picture when a certain amount of change is detected in the video stream.
* Try and find a balance for the motion detector to not pick up sway of bird feeder and only pick up birds.
* Implement some sort of timer. If some change is detected for more than x amount of time, take a picture.

Machine Learning

* Test Tensorflow with pictures of birds. If it can be tested with pictures of birds from the camera, even better.
* Optionally add squirrels?
  
Organize Data

* Setup directory structure and automate where the pictures taken go to.
* Seperate folder for each bird type

Other

* Create testing script to run the pictures from the TestingImages directory through the image_preprocessing.py script. Use pytest or unittest.
* bash script to download all of the dependencies

### Things to think about

The camera will be set up to observe the bird feeder.
What should be done to prevent false positives when the sway of the bird feeder indicates change?

Squirrels like to mess with the bird feeder alot also. Should Tensorflow train on squirrels as well?

Changes in time of day could also casue false positives.

How to detect change between a brown bird and brown background?

## Potential future work

* Setup WebApp for the whole thing to run through.
* Connect the images taken to a SQL database.
* Send the images taken to AWS

## Useful sources

<https://www.tensorflow.org/lite/guide/get_started#2_convert_the_model_format>
<https://www.tensorflow.org/lite/guide/python>
<https://www.tensorflow.org/lite/models/image_classification/overview>
