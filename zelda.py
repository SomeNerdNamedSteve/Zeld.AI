import cv2
import time
import numpy as np
import random
from time import sleep
from PIL import ImageGrab
from key_input import press, release, push
from nes_input import NESInput
from pprint import pprint

bouding_box = (1, 74, 241, 314)
controller = NESInput()
sys_random = random.SystemRandom()

def main():
    sleep(3)
    print("Playing the game now!")
    # prev = time.time()
    while(True):

        # Data prep for the Neural Network
        
        screencap = np.array(ImageGrab.grab(bbox=bouding_box)) # capture screen
        input_array = screencap.flatten() # flatten array
        colored_layers = create_color_layers(input_array, screencap.shape[0], screencap.shape[1])
        
        # Where the real fun is
        step()

        # get the framerate
        # now = time.time()
        # diff = now - prev
        # print(1/diff)
        # prev = now

def step():
    # set control for step
    random_action = random.randrange(0, len(controller.action_space))
    control = controller.action_space[random_action]
    push(control)

def get_average_value(arr):
    pass

def create_color_layers(np_arr, rows, cols):
    red_vals = []
    green_vals = []
    blue_vals = []

    for i, el in np.ndenumerate(np_arr):
        curr_color = i[0] % 3
        if curr_color == 0:
            red_vals.append(el)
        elif curr_color == 1:
            green_vals.append(el)
        elif curr_color == 2:
            blue_vals.append(el)

    red_vals = np.array(red_vals).reshape(rows, cols)
    green_vals = np.array(green_vals).reshape(rows, cols)
    blue_vals = np.array(blue_vals).reshape(rows, cols)

    return np.array([red_vals, green_vals, blue_vals])



def test_screen():
    screencap = np.array(ImageGrab.grab(bbox=bouding_box))
    input_array = screencap.flatten()
    colored_layers = create_color_layers(input_array, screencap.shape[0], screencap.shape[1])
    cv2.imwrite('window.png', cv2.cvtColor(np.array(screencap), cv2.COLOR_BGR2RGB))

def get_to_game():
    sleep(3)
    print('starting game')
    start_to_game_seq = [
        controller.start,
        controller.start,
        controller.right,
        controller.a,
        controller.down,
        controller.right,
        controller.right,
        controller.a,
        controller.right,
        controller.right,
        controller.right,
        controller.right,
        controller.right,
        controller.a,
        controller.select,
        controller.select,
        controller.select,
        controller.start,
        controller.start
    ]
    
    for action in start_to_game_seq:
        push(action)
        sleep(0.5)
        
    


if __name__ == '__main__':
    # get_to_game()
    # main()
    test_screen()