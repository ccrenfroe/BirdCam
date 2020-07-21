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
    # min = np_image.min()
    # max = np_image.max()    

    # # normalize to the range 0-1
    # np_image = np_image.astype('float32')
    # np_image -= min
    # np_image /= (max - min)

    return [np_image]

# Load interpreter
interpreter = tf.lite.Interpreter(model_path="aiy_vision_classifier_birds_V1_2.tflite")
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)
print(output_details)

interpreter.allocate_tensors()

# Inputting the image
image = process_image('Images/PicturesIn/mourningdove.jpg')
print(image)
interpreter.set_tensor(input_details[0]['index'], image)

# run the inference
interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])

print("the output is {}".format(output_data))


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#             'i',
#             '--image',
#             help='image to be classified')
