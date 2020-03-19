class Board:
    def __init__(self, width, height, snake):
        self.width = width
        self.height = height
        self.snake = snake
    def collide(self, position):
        return False
    def eat(self, position):
        return False
