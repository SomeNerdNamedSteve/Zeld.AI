import cv2
import time
import numpy as np
import random
from time import sleep
from PIL import ImageGrab, Image
from key_input import press, release, push
from nes_input import NESInput

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
        data_input = data_prep_main(screencap)
        
        # Where the real fun is
        step()

        # get the framerate
        # now = time.time()
        # diff = now - prev
        # print(1/diff)
        # prev = now

def test_screen():
    screencap = np.array(ImageGrab.grab(bbox=bouding_box))
    create_image(screencap, 'window.png')
    pixel_averages = data_prep_main(screencap)
    nn_pixel_averages = np.asarray(pixel_averages, dtype=np.uint8)
    create_image(nn_pixel_averages, 'test.png', resize=True)
    

def create_image(np_arr, name, resize=False):
    img = Image.fromarray(np_arr, 'RGB')

    if resize:
        img = img.resize((240, 240), Image.NEAREST)

    img.save(name)

def step():
    # set control for step
    random_action = random.randrange(0, len(controller.action_space))
    control = controller.action_space[random_action]
    push(control)

def data_prep_main(capture):
    averages = get_average_values(capture)
    return np.array(averages)

def get_average_values(np_arr, step=10):
    
    # just to make sure that the screen is square
    if np_arr.shape[0] != np_arr.shape[1]:
        raise Exception('Input array much be a square')

    length = np_arr.shape[0]
    num_squares = length // step
    output_arr = []
    
    for i in range(num_squares):
        row_min = i * 10
        row_max = row_min + 10
        output_row = []
        for j in range(num_squares):
            el_min = j * 10
            el_max = el_min + 10
            grid = np_arr[row_min:row_max, el_min:el_max]
            avg = np.average(grid, axis=(0,1))
            output_row.append(avg)

        output_arr.append(output_row)

    return np.floor(output_arr)

if __name__ == '__main__':
    # main()
    test_screen()