import random

class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        self.x = random.randrange(0, self.screen_width-self.cell_size, self.cell_size)
        self.y = random.randrange(0, self.screen_height - self.cell_size, self.cell_size)