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
        if self.board[position[0]][position[1]] == BoardState.PORTAL:
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
        for i in range(self.width):
            for j in range(self.height):
                if j == 0 or i == self.width -1 or j == self.height -1:
                    self.board[i][j] = BoardState.OBSTACLE
                    continue
                if i == 0:
                    self.board[i][j] = BoardState.PORTAL
                    continue
                if random.randrange(density) == 0:
                    self.board[i][j] = BoardState.FOOD
                    self.totalfood = self.totalfood + 1
    def levelwon(self):
        return self.found_portal
                

from enum import Enum
class BoardState(Enum):
    EMPTY = 0
    OBSTACLE = 1
    FOOD = 2
    PORTAL = 3