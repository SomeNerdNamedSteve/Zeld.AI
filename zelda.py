import time
import numpy as np
import random
import mss
import cv2
from time import sleep
from key_input import press, release, push
from nes_input import NESInput

controller = NESInput()
sys_random = random.SystemRandom()

def main():
    sleep(3)
    print("Playing the game now!")
    prev = time.time()
    
    while(True):

        # Data prep for the Neural Network
        image = get_image()

        
        # Where the real fun is

        # get the framerate
        now = time.time()
        diff = now - prev
        print(1/diff)
        prev = now

# function grabs screen and return a 1-d array of screen
def get_image():
    with mss.mss() as sct:
        display = {
            'top': 74,
            'left': 2,
            'width': 240,
            'height': 240
        }

        img = np.array(sct.grab(display))

    pixels = img.flatten()
    print(img.shape)

    return pixels


if __name__ == '__main__':
    main()