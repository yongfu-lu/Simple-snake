class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = (0, 1)

    def move(self, cell_size):
        self.x += self.dir[0]*cell_size
        self.y += self.dir[1]*cell_size