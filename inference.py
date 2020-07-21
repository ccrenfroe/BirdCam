import argparse
import numpy as np
from numpy import asarray

# import tflite_runtime.interpreter as tflite //Why was this here?
import tensorflow as tf

#For image preprocessing
import os
import sys
from PIL import Image

def process_image(image_path):
    image = Image.open(image_path)
    new_image = image.resize((224,224))
    np_image = asarray(new_image)
    np_image = np_image.astype('uint8')
    return [np_image]

# Load interpreter
interpreter = tf.lite.Interpreter(model_path="aiy_vision_classifier_birds_V1_2.tflite")
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

# Inputting the image
image = process_image('Images/PicturesIn/painted-bunting_adult-male.jpg')
interpreter.set_tensor(input_details[0]['index'], image)

# run the inference
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])

# Output
print("the output is {}".format(output_data))


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#             'i',
#             '--image',
#             help='image to be classified')
