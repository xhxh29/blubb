import random
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[BoardState.EMPTY for x in range(width)] for y in range(height)]
        self.totalfood = 0
        self.__gen_board(30)
        self.found_portal = False
        
    def collide(self, position):
        if self.board[position[0]][position[1]] == BoardState.OBSTACLE:
            return True
        if self.board[position[0]][position[1]] == BoardState.EXIT_PORTAL:
            if self.totalfood == 0:
                self.found_portal = True
                return False
            return True
        return False


        return False
    def eat(self, position):
        if self.board[position[0]][position[1]] == BoardState.FOOD:
            self.board[position[0]][position[1]] = BoardState.EMPTY
            self.totalfood = self.totalfood - 1
            return True
        return False
    def __gen_board(self, density):
        i = 0
        down = True
        while i < self.width:
            i += random.randrange(3, 6)
            if i >= self.width:
                break
            length = random.randrange(0, self.height-2)
            if down:
                for j in range(length):
                    self.board[i][j] = BoardState.OBSTACLE
            else:
                for j in range(length):
                    self.board[i][self.height - 1 - j] = BoardState.OBSTACLE
            down = not down

        for i in range(self.width):
            for j in range(self.height):
                if i == 0 or j == 0 or i == self.width -1 or j == self.height -1:
                    self.board[i][j] = BoardState.OBSTACLE
                    if i == self.width - 1:
                        self.board[i][j] = BoardState.EXIT_PORTAL
                    if j == int(self.height / 2) and i == 0:
                        self.board[i][j] = BoardState.ENTRY_PORTAL
                    continue
                if random.randrange(density) == 0 and self.board[i][j] == BoardState.EMPTY:
                    self.board[i][j] = BoardState.FOOD
                    self.totalfood = self.totalfood + 1
    def levelwon(self):
        return self.found_portal

    def find_leftmost_entry_portal(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == BoardState.ENTRY_PORTAL:
                    return (i, j)


from enum import Enum
class BoardState(Enum):
    EMPTY = 0
    OBSTACLE = 1
    FOOD = 2
    ENTRY_PORTAL = 3
    EXIT_PORTAL = 4
