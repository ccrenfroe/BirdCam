# This script will handle all of the preprocessing of images I need to do before I can feed it into the Birds model for image classification.
#Imports
import os
import sys
from PIL import Image
from numpy import asarray

DIRECTORY_IN = 'Images/PicturesIn/' # Folder of images to be processed
DIRECTORY_OUT = 'Images/Processed/' # Folder for images post processing

def process_image(DIRECTORY_IN):
    for filename in os.listdir(DIRECTORY_IN):
        # Used to find the min and max of the image file
        # min = sys.maxsize
        # max = -sys.maxsize
        filepath = DIRECTORY_IN + filename
    
        image = Image.open(filepath)
        new_image = image.resize((224,224))    
        np_image = asarray(new_image)

        # Performing minmax normalization
        # if min > np_image.min():
        min = np_image.min() # Get min
        print(min)
        # if max < np_image.max():
        max = np_image.max() # Get max
        print(max)
        np_image = np_image.astype('float32')
        print('Min: %.3f, Max: %.3f' % (np_image.min(), np_image.max()))
        np_image -= min
        np_image /= (max - min)
        print('Min: %.3f, Max: %.3f' % (np_image.min(), np_image.max()))
        # print(np_image)
        img = Image.fromarray(np_image, 'RGB') # Convert back to an image

        # Save to 'Processed' directory
        filename = filename.split(".")[0] + "_processed.png"
        print(filename)
        img.save(DIRECTORY_OUT + filename)
    return

def main():
    process_image(DIRECTORY_IN)
    return

if __name__ == "__main__":
    main()