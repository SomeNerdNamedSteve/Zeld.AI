import time
import mss
import cv2
import random
import keras.backend as K
import tensorflow as tf
import numpy as np
from time import sleep
from key_input import press, release, push
from nes_input import NESInput
from actor_critic import ActorCritic
from collections import deque


controller = NESInput()
ac_model = ActorCritic()

def main(screen):

    session = tf.Session()
    K.set_session(session)

    curr_state = capture_screen(screen)

    button_state = []
    countdown(5)

    print("Now Playing")
    prev = time.time()

    # actual testing loop
    while(True):
        button_reset(button_state)

        # Start of actual AI

        button_set = np.random.choice(len(controller.action_space))

        # End of AI

        #start_pressing_buttons
        button_state = controller.action_space[button_set]
        set_button_state(button_state, True)

        # Get new state
        new_state = capture_screen(screen)

        # get the framerate
        now = time.time()
        diff = now - prev
        # print(1/diff)
        prev = now

        # Get Data for next part of loop
        curr_state = new_state

        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break

# function grabs screen and return a 1-d array of screen
def capture_screen(display):
    with mss.mss() as sct:
        img = cv2.cvtColor(np.array(sct.grab(display), dtype = np.uint8), cv2.COLOR_RGBA2RGB)
        # large = cv2.resize(img, (0,0), fx=4.5, fy=4.5)
        # cv2.imshow('Seeing Replay', large)
        # grey_img = tf.image.rgb_to_grayscale(img, name=None)
        # print(grey_img)

    return img

def set_button_state(btns, flag):
    for btn in btns:
        if flag:
            press(btn)
        else:
            release(btn)

def countdown(seconds):
    while seconds != 0:
        print(seconds)
        sleep(1)
        seconds -= 1

def button_reset(s):
    #stop pressing buttons
    if s != []:
        set_button_state(s, False)
        s = []

if __name__ == '__main__':
    screen = {
        'top': 74,
        'left': 2,
        'width': 240,
        'height': 240
    }
    main(screen)
    test_image()
