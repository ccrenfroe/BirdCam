# The purpose of this script is to identify birds in images fed in. It includes all of the functions necessary to assist in the process of inference on images.
import numpy as np
from numpy import asarray
import csv
import tensorflow as tf
import sys
from PIL import Image

def process_image(image_path):
    """Preprocess the image to be put into the model"""
    image = Image.open(image_path)
    new_image = image.resize((224,224))
    np_image = asarray(new_image)
    np_image = np_image.astype('uint8')
    return [np_image]

def find_label(model_output):
    """Return the label corresponding to the bird based off of the inference results"""
    max_label = 0
    index  = -1
    # Loop through model_output array and find the largest value
    for label in model_output: 
        index += 1
        if max_label < label:
            answer = index
    return answer

def get_bird_name(index):
    """Return birds name according to labelmap"""
    with open('aiy_birds_V1_labelmap.csv') as csvIn:
        labels = list(csv.reader(csvIn)) # Converts the labelmap.csv to a list for easy indexing.
        label = labels[index+2][1] # Plus 2 to ignore the first 2 lines of the CSV, and 1 to go to the 'name' column
    return label

def classify_bird(image_in):
    """
    Returns the bird detected in the image.
    """
    # Load interpreter
    interpreter = tf.lite.Interpreter(model_path="aiy_vision_classifier_birds_V1_2.tflite")
    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.allocate_tensors()

    # Inputting the image
    image = process_image(image_in)
    interpreter.set_tensor(input_details[0]['index'], image)

    # run the inference
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    # Output
    index = find_label(output_data)
    label = get_bird_name(index)
    print(label)
    return label

def main():
    image = ""
    classify_bird(image)

if __name__ == "__main__":
    main()
