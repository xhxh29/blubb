import pygame
import operator
from Board import Board
from Board import BoardState
from Snake import Snake
from Snake import direction
from pygame import Rect
from pygame import Color
from pygame import time
from pygame import display


FOOD_COLOR = Color(255, 0, 0)
EMPTY_COLOR = Color(0, 0, 0)
OBSTACLE_COLOR = Color(100, 100, 100)
SNAKE_COLOR = Color(0, 255, 0)
SNAKE_EYE_COLOR = Color (0, 0, 0)
ENTRY_PORTAL_COLOR = Color(0, 0, 255)
EXIT_PORTAL_COLOR = Color(0, 0, 127)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


def main():
    pygame.init()
    displayinfo = pygame.display.Info()
    sizedisplay = int(min((displayinfo.current_w, displayinfo.current_h)) * 4/5)
    global SCREEN_HEIGHT
    global SCREEN_WIDTH
    SCREEN_HEIGHT = sizedisplay
    SCREEN_WIDTH = sizedisplay
    screen = pygame.display.set_mode((sizedisplay, sizedisplay))
    difficulty = 1
    running = True
    board = None
    while running:
        frame = 0
        if not board is None:
            board = init_level(difficulty, board.snake.length, board.snake.direction)
        else:
            board = init_level(difficulty, 1, 2)
        clock = time.Clock()
        while running:
            clock.tick(60)
            handle_keys(board)
            frame = frame + 1
            screen.fill(EMPTY_COLOR)
            draw(board, screen)
            if frame % board.snake.speed == 0:
                if not board.snake.move():
                    running = False
                if board.levelwon():
                    break
            pygame.display.update()
        difficulty += 1


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


def init_level(difficulty, snake_length, snake_dir):
    board = Board(difficulty*10, difficulty*10)
    entry_portal_pos = board.find_leftmost_entry_portal()
    start_pos = tuple(map(operator.add, entry_portal_pos, direction(snake_dir)))
    snake = Snake(start_pos , snake_dir, board, snake_length)
    board.snake = snake
    snake.speed = max((120./float(difficulty), 1))
    return board

def rect_from_points(p1, p2):
    minx = min((p1[0], p2[0]))
    miny = min((p1[1], p2[1]))
    maxx = max((p1[0], p2[0]))
    maxy = max((p1[1], p2[1]))
    return Rect(minx, miny, maxx-minx, maxy-miny)


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
            if board.board[i][j] == BoardState.ENTRY_PORTAL:
                pygame.draw.rect(screen, ENTRY_PORTAL_COLOR, Rect(
                    i*boxwidth, j*boxheight, boxwidth, boxheight))
            if board.board[i][j] == BoardState.EXIT_PORTAL:
                pygame.draw.rect(screen, EXIT_PORTAL_COLOR, Rect(
                    i*boxwidth, j*boxheight, boxwidth, boxheight))
    for pos in board.snake.position:
        pygame.draw.rect(screen, SNAKE_COLOR, Rect(
            pos[0]*boxwidth, pos[1]*boxheight, boxwidth, boxheight))

    pos = board.snake.position[0]
    lefteyep1 = head_to_world(board.snake, (-0.3, -0.3), boxwidth, boxheight)
    lefteyep2 = head_to_world(board.snake, (-0.0, -0.1), boxwidth, boxheight)
    righteyep1 = head_to_world(board.snake, (-0.3, 0.3), boxwidth, boxheight)
    righteyep2 = head_to_world(board.snake, (-0.0, 0.1), boxwidth, boxheight)
    pygame.draw.ellipse(screen, SNAKE_EYE_COLOR, rect_from_points(righteyep1, righteyep2))
    pygame.draw.ellipse(screen, SNAKE_EYE_COLOR, rect_from_points(lefteyep1, lefteyep2))
def head_to_world(snake, uv, boxwidth, boxheight):
    grid = (boxwidth, boxheight)
    headpos = add(multi(grid, snake.position[0]), (boxwidth * 0.5, boxheight * 0.5))
    uvkoord = add(multfloat(direction(snake.direction %4), uv[0]), multfloat(direction((snake.direction + 1)%4), uv[1]))
    uvkoord = multi(uvkoord, grid)
    return add(headpos, uvkoord)
def add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])
def multi(vec1, vec2):
    return(vec1[0] * vec2[0], vec1[1] * vec2[1])
def multfloat(vec1, komma):
    return(vec1[0] * komma, vec1[1] * komma)


main()
