import time
import numpy as np
import mss
import cv2
import tensorflow as tf
from time import sleep
from key_input import press, release, push
from nes_input import NESInput

controller = NESInput()



def main():
    sleep(3)
    print("Playing the game now!")
    prev = time.time()
    button_state = []

    while(True):

        # Data prep for the Neural Network
        image = capture_screen()
        
        #stop pressing buttons
        if button_state != []:
            set_button_state(button_state, False)
            btn_state = []

        
        # Start of actual AI

        button_set = np.random.choice(controller.action_space)

        # End of AI

        #start_pressing_buttons
        button_state = controller.action_space[button_set]
        set_button_state(button_state, False)

        # get the framerate
        now = time.time()
        diff = now - prev
        # print(1/diff)
        prev = now

# function grabs screen and return a 1-d array of screen
def capture_screen():
    with mss.mss() as sct:
        display = {
            'top': 74,
            'left': 2,
            'width': 240,
            'height': 240
        }

        img = np.array(sct.grab(display))

    pixels = img.flatten()

    return pixels

def set_button_state(btns, flag):
    for btn in btns:
        if flag:
            press(btn)
        else:
            release(btn)

if __name__ == '__main__':
    main()