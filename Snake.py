class Snake:
    def __init__(self, startpos, startdir):
        self.position = [startpos]
        self.direction = startdir
    def move(self):
        del self.position[-1]
        self.position.insert(0, Head)
    def __collision(self, colpos):
        return False
    def __eat(self,foodpos):
        return False

