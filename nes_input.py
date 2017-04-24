#enumeration to hold Hex values of the input keys
from enum import Enum

class NESInput(Enum):
    UP = 0x11
    LEFT = 0x1E
    DOWN = 0x1F
    RIGHT = 0x20
    SELECT = 0x22
    START = 0x23
    B = 0x25
    A = 0x26
