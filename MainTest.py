import pygame
from Board import Board
from Snake import Snake
from pygame import Rect
from pygame import Color
def main():
    board = Board(20, 20, Snake((10,10),0))
    pygame.init()
    screen = pygame.display.set_mode((1000,1000))
    running = True
    while running:
        pygame.draw.rect(screen, Color(255, 0 ,0),Rect(0,0,100,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()