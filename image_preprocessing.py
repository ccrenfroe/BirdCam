# This script will handle all of the preprocessing of images I need to do before I can feed it into the Birds model for image classification.

#Imports
import sys
from PIL import Image
from numpy import asarray

def process_image(image_path):
    min = sys.maxsize
    max = -sys.maxsize


    image = Image.open(image_path)
    new_image = image.resize((224,224))    
    np_image = asarray(new_image)

    if min > np_image.min():
        min = np_image.min()
    if max < np_image.max():
        max = np_image.max()    

    np_image = np_image.astype('float32')
    np_image -= min
    np_image /= (max - min)
    # print(np_image)
    img = Image.fromarray(np_image, 'RGB')
    img.show()

    return img

def main():
    image = "Images/TestImages/mourningdove.jpg"
    new_image = process_image(image)

    return

if __name__ == "__main__":
    main()