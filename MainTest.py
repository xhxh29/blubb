import pygame
from Board import Board
from Board import BoardState
from Snake import Snake
from pygame import Rect
from pygame import Color
from pygame import time

FOOD_COLOR = Color(255, 0, 0)
EMPTY_COLOR = Color(0, 0, 0)
OBSTACLE_COLOR = Color(100, 100, 100)
SNAKE_COLOR = Color(0, 255, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


def main():
    board = Board(10, 10)
    snake = Snake((5, 5), 0, board)
    board.snake = snake
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    frame = 0
    clock = time.Clock()
    while running:
        clock.tick(60)
        handle_keys(board)
        frame = frame + 1
        screen.fill(EMPTY_COLOR)
        draw(board, screen)
        if frame % 15 == 0:
            if not snake.move():
                running = False
        pygame.display.update()


def handle_keys(board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.snake.set_direction(0)
            if event.key == pygame.K_DOWN:
                board.snake.set_direction(1)
            if event.key == pygame.K_RIGHT:
                board.snake.set_direction(2)
            if event.key == pygame.K_UP:
                board.snake.set_direction(3)

def draw(board, screen):
    boxwidth = float(SCREEN_WIDTH) / float(board.width)
    boxheight = float(SCREEN_HEIGHT) / float(board.height)
    for i in range(board.width):
        for j in range(board.height):
            if board.board[i][j] == BoardState.OBSTACLE:
                pygame.draw.rect(screen, OBSTACLE_COLOR, Rect(
                    i*boxwidth, j*boxheight, boxwidth, boxheight))
            if board.board[i][j] == BoardState.FOOD:
                pygame.draw.rect(screen, FOOD_COLOR, Rect(
                    i*boxwidth, j*boxheight, boxwidth, boxheight))
    for pos in board.snake.position:
        pygame.draw.rect(screen, SNAKE_COLOR, Rect(
            pos[0]*boxwidth, pos[1]*boxheight, boxwidth, boxheight))


main()
