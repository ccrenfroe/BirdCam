import birdcam.inference as inferencer
import birdcam.camera as camera

def main():
    image = "Images/PicturesIn/blue_Jay.jpg"
    inferencer.classify_bird(image)

    camera.capture()

if __name__ == "__main__":
    main()

# Thinking this will be for the future. 1  main script to run everything from.

# import argparse
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#             'i',
#             '--image',
#             help='image to be classified')
