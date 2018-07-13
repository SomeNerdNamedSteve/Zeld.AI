import time
import numpy as np
import mss
import cv2
from time import sleep
from key_input import press, release, push
from nes_input import NESInput

controller = NESInput()



def main():
    sleep(3)
    print("Playing the game now!")
    prev = time.time()
    
    button_states = [
        [],
        [],
        []
    ]

    while(True):

        # Data prep for the Neural Network
        image = get_image()
        
        #stop pressing buttons
        button_states = set_button_presses(button_states, False)

        # Start of actual AI
        movement = np.random.choice(len(controller.movement_space)),
        ab = np.random.choice(len(controller.ab_space))
        start_select = np.random.choice(len(controller.start_select_space))
        # End of AI

        button_states = set_button_presses(button_states, True, mvmt=movement, ab=ab, st_sel=start_select)

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

    return pixels

def set_button_presses(btn_states, flag, mvmt=None, ab=None, st_sel=None):

    for btn_state in btn_states:
        if flag:
            btn_state = [
                controller.movement_space[mvmt],
                controller.ab_space[ab],
                controller.start_select_space[st_sel]
            ]
        else:
            if len(btn_state) > 0:
                for btn in btn_state:
                    release(btn)
                btn_state = []
    
    return btn_states


    # for button_state in button_states:
    #     
    #         for button in button_state:
    #             release(button)

    #         button_state = []

if __name__ == '__main__':
    main()