import cv2
import time
import numpy as np
from time import sleep
from PIL import ImageGrab
from key_input import press, release, push
from nes_input import NESInput

bouding_box = (114, 156, 625, 605)
controller = NESInput()

def main():
    sleep(3)
    print("Playing the game now!")
    while(True):
        #capture screen (captured at top left hand corner of main display)
        screencap = np.array(ImageGrab.grab(bbox=bouding_box))
        print(screencap)
        # cv2.imshow('window', cv2.cvtColor(np.array(screencap), cv2.COLOR_BGR2RGB))
        # If q is pressed, quit the game
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

# def test_screen():
#     screencap = np.array(ImageGrab.grab(bbox=bouding_box))
#     cv2.imwrite('window.png', cv2.cvtColor(np.array(screencap), cv2.COLOR_BGR2RGB))

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
    get_to_game()
    # main()
    # test_screen()