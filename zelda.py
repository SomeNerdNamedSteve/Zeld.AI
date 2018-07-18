import time
import numpy as np
import mss
import cv2
import random
from time import sleep
from key_input import press, release, push
from nes_input import NESInput
from keras.models import Sequential
from keras.layers import Dense, Flatten
from collections import deque

controller = NESInput()

model = Sequential()

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
            button_state = []


        # Start of actual AI

        button_set = np.random.choice(len(controller.action_space))

        # End of AI

        #start_pressing_buttons
        button_state = controller.action_space[button_set]
        set_button_state(button_state, True)

        # get the framerate
        now = time.time()
        diff = now - prev
        # print(1/diff)
        prev = now

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

# function grabs screen and return a 1-d array of screen
def capture_screen():
    with mss.mss() as sct:
        display = {
            'top': 74,
            'left': 2,
            'width': 240,
            'height': 240
        }

        img = cv2.cvtColor(np.array(sct.grab(display), dtype = np.uint8), cv2.COLOR_RGBA2RGB)
        print(img.shape)
        # large = cv2.resize(img, (0,0), fx=4.5, fy=4.5)
        # cv2.imshow('Seeing Replay', large)
        # grey_img = tf.image.rgb_to_grayscale(img, name=None)
        # print(grey_img)

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
