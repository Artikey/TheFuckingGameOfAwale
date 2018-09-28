import sys, pygame
from pygame.locals import *
from Board import Board
from Const import *

pygame.init()
theBoard = Board()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    theBoard.draw()
    pygame.display.flip()
