class Snake:
    def __init__(self, startpos, startdir, board, length):
        self.position = [startpos]
        self.direction = startdir
        self.board = board
        self.length = length
    def move(self):
        oldhead = self.position[0]
        movement = self.__direction(self.direction)
        xneu = oldhead[0] + movement[0]
        yneu = oldhead[1] + movement[1]
        head = (xneu, yneu)
        if not self.board.eat(head) and len(self.position) >= self.length:
            del self.position[-1]
        if self.__collision(head):
            self.position.insert(0, head)
            return False
        self.position.insert(0, head)
        self.length = self.length + 1
        return True
    def __direction(self, dirnum):
        if dirnum == 0:
            return (-1, 0)
        if dirnum == 1:
            return (0, 1)
        if dirnum == 2:
            return (1, 0)
        if dirnum == 3:
            return (0, -1)
    def __collision(self, pos):
        return self.__selfcoll(pos) or self.board.collide(pos)
    def __selfcoll(self, pos):
        return pos in self.position
    def set_direction(self, dirnum):
        self.direction = dirnum