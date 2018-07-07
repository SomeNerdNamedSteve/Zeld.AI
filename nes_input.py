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
        self.action_space = [
            self.up,
            self.down,
            self.left,
            self.right,
            self.start,
            self.select,
            self.a,
            self.b
        ]