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

def main(screen):

    curr_state = capture_screen(screen)
    observation_space_shape = curr_state.shape

    # Config for the AI to run
    controller = NESInput() # Get Controller and control setup
    session = tf.Session() # Create a tensorflow session
    K.set_session(session) # Set session for Keras
    ac_model = ActorCritic(session, controller.action_space, observation_space_shape) # ActorCritic class initializer

    button_state = []
    print("We are good to go! Playing Now")
    countdown(10)

    print("Now Playing")
    prev = time.time()

    # RL Loop
    while(True):
        button_reset(button_state)

        # Start of AI

        button_set = np.random.choice(len(controller.action_space))

        # End of AI

        #start pressing buttons for the AI
        button_state = controller.action_space[button_set]
        set_button_state(button_state, True)

        # Get new state
        new_state = capture_screen(screen)

        # get the framerate
        now = time.time()
        diff = now - prev
        # print(1/diff)
        prev = now

        # Update curr_state with the new_state
        curr_state = new_state

# function grabs screen and return a 1-d array of screen
def capture_screen(display):
    with mss.mss() as sct:
        return cv2.cvtColor(np.array(sct.grab(display),
                            dtype = np.uint8),
                            cv2.COLOR_RGBA2RGB)

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
    if s != []:
        set_button_state(s, False)
        s = []

def test_image(screen):
    display = capture_screen(screen)
    print(type(display))
    cv2.imwrite('test.png', display)

if __name__ == '__main__':
    screen = {
        'top': 74,
        'left': 2,
        'width': 240,
        'height': 240
    }
    main(screen)
    # test_image(screen)
