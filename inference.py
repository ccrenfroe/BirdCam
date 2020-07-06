import argparse
import numpy as np
import tflite_runtime.interpreter as tflite
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_d
# Load interpreter
interpreter = tflite.Interpreter(model_path="aiy_vision_classifier_birds_V1_2.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)
print(output_details)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
            'i',
            '--image',
            help='image to be classified')

