# This script will handle all of the preprocessing of images I need to do before I can feed it into the Birds model for image classification.

#Imports
from PIL import Image
from numpy import asarray

def process_image(image_path):
    image = Image.open(image_path)
    new_image = image.resize((224,224))
    
    pixels = asarray(new_image)

    # confirm pixel range is 0-255
    print('Data Type: %s' % pixels.dtype)
    print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))

    # convert from integers to floats
    pixels = pixels.astype('float32')

    # normalize to the range 0-1
    pixels /= 255.0

    # confirm the normalization
    print('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))
    new_image.save("result.jpg")
    
    return new_image

def main():
    image = "Images/TestImages/test.jpg"
    new_image = process_image(image)

    return

if __name__ == "__main__":
    main()