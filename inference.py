import argparse
import numpy as np
# import tflite_runtime.interpreter as tflite //Why was this here?
import tensorflow as tf

# Load interpreter
interpreter = tf.lite.Interpreter(model_path="aiy_vision_classifier_birds_V1_2.tflite")
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

print(input_details)
print(output_details)

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#             'i',
#             '--image',
#             help='image to be classified')
