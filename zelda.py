import cv2
import numpy as np
from time import sleep
from PIL import ImageGrab
from key_input import PressKey, ReleaseKey
from nes_input import NESInput

def main():
    print("Playing the game now!")
    while(True):
        #capture screen (captured at top left hand corner of main display)
        screencap = np.array(ImageGrab.grab(bbox=(0,55 ,1000,945)))
        cv2.imshow('window', cv2.cvtColor(np.array(screencap), cv2.COLOR_BGR2RGB))
        # If q is pressed, quit the game
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
