# The purpose of this script is to handle moving the files around the Images directory. It will determine what images go where.
import os
import sys

PICTURES_IN = 'Images/PicturesIn/'
BIRDS_ROOT = 'Images/Birds/'

# May not be needed
def new_image(image):
    """Places the new image in the 'PicturesIn' directory"""
    os.replace(image,PICTURES_IN + image)
    return

def move_image(image, destination):
    """
    Moves an image to a new folder
    
    This should be called after an image has been processed, and therefore has been identified.
    The destination will be the directory of the bird as identified by 'inference.py'.
    If the directory does not exist, a new one will be made.
    An assumption is made that no files in the specified birds directory is deleted, causing the numbering system to possibly overwrite a file.

    Parameters:
        image (string) : Image file that is being moved
        label (string) : Name of the bird. Will be used to rename the image.
        destination (string) : The label passed in that is the name of the bird. This will be used to rename the image as well as find/create the directory for the bird.
    
    TODO: Extend functionality to create a subdirectory for the current date. 
    """
    directories = os.listdir(BIRDS_ROOT)
    destination = destination.replace(" ","_")

    for directory in directories:
        if directory == destination:
            num = len(os.listdir(BIRDS_ROOT + directory)) + 1 # unique number for the file
            os.replace(image,BIRDS_ROOT + destination + "/" + destination + str(1) + ".jpg")
            return
    else: # the directory doesn't exist
        try: # and make it
            os.mkdir(BIRDS_ROOT + destination)
            os.replace(image,BIRDS_ROOT + destination + "/" + destination + "1.jpg") # Add the image
        except OSError as e:
            print(e)
        return

def main():
    image = "Images/PicturesIn/mourningdove.jpg"
    move_image(image,"testing")
    # new_image("img__12345.jpg")

if __name__ == "__main__":
    main()
