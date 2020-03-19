class Snake:
    def __init__(self, startpos, startdir, board):
        self.position = [startpos]
        self.direction = startdir
        self.board = board
    def move(self):
        del self.position[-1]
        oldhead = self.position[0]
        movement = self.__direction(self.direction)
        xneu = oldhead[0] + movement[0]
        yneu = oldhead[1] + movement[1]
        head = (xneu, yneu)
        if self.__collision(head):
            self.position.insert(0, head)
            return False
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

    def __eat(self, foodpos):
        return False
