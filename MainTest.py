import pygame
from Board import Board
from Board import BoardState
from Snake import Snake
from pygame import Rect
from pygame import Color

FOOD_COLOR = Color(255,0,0)
EMPTY_COLOR = Color(0,0,0)
OBSTACLE_COLOR = Color(100,100,100)
SNAKE_COLOR = Color(0,255,0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
def main():
    board = Board(50, 50)
    snake = Snake((10,10),0,board)
    board.snake = snake
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    running = True
    frame = 0
    while running:
        frame = frame + 1
        draw(board, screen)
        if frame % 30 == 0:
            if not snake.move():
                running = False
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
def draw(board, screen):
    boxwidth = float(SCREEN_WIDTH) / float(board.width)
    boxheight = float(SCREEN_HEIGHT) / float(board.height)
    for i in range(board.width):
        for j in range(board.height):
            if board.board[i][j] == BoardState.EMPTY:
                pygame.draw.rect(screen, EMPTY_COLOR, Rect(i*boxwidth, j*boxheight, boxwidth, boxheight))
            if board.board[i][j] == BoardState.OBSTACLE:
                pygame.draw.rect(screen, OBSTACLE_COLOR, Rect(i*boxwidth, j*boxheight, boxwidth, boxheight))
            if board.board[i][j] == BoardState.FOOD:
                pygame.draw.rect(screen, FOOD_COLOR, Rect(i*boxwidth, j*boxheight, boxwidth, boxheight))
    for pos in board.snake.position:
        pygame.draw.rect(screen, SNAKE_COLOR, Rect(pos[0]*boxwidth, pos[1]*boxheight, boxwidth, boxheight))
            

main()