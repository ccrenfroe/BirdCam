# The purpose of this script is to handle moving the files around the Images directory. It will determine what images go where.
import os
import sys
import shutil

PICTURES_IN = 'Images/PicturesIn/'
BIRDS_ROOT = 'Images/Birds/'

def new_image(image):
    """Places the new image in the 'PicturesIn' directory"""
    return

def move_image(image, destination):
    """
    Moves an image to a new folder
    
    This should be called after an image has been processed, and therefore has been identified.
    The destination will be the directory of the bird as identified by 'inference.py'.
    If the directory does not exist, a new one will be made.
    """
    return