import numpy as np

class NESInput():
    def __init__(self):
        self.up = 0x11
        self.left = 0x1E
        self.down = 0x1F
        self.right = 0x20
        self.select = 0x22
        self.start = 0x23
        self.b = 0x25
        self.a = 0x26

        self.action_space = np.array([
            [],
            [self.up],
            [self.down],
            [self.left],
            [self.right],
            # [self.select],
            [self.start],
            [self.a],
            [self.b],
            [self.a, self.b],
            [self.up, self.a],
            [self.up, self.b],
            [self.down, self.a],
            [self.down, self.b],
            [self.left, self.a],
            [self.left, self.b],
            [self.right, self.a],
            [self.right, self.b],
            [self.up, self.left],
            [self.up, self.right],
            [self.down, self.left],
            [self.down, self.right],
            [self.up, self.left, self.a],
            [self.up, self.right, self.a],
            [self.down, self.left, self.a],
            [self.down, self.right, self.a],
            [self.up, self.left, self.b],
            [self.up, self.right, self.b],
            [self.down, self.left, self.b],
            [self.down, self.right, self.b],
            [self.up, self.left, self.a, self.b],
            [self.up, self.right, self.a, self.b],
            [self.down, self.left, self.a, self.b],
            [self.down, self.right, self.a, self.b]
        ])
