#!/usr/bin/python3
import sys, pygame
from pygame.locals import *
from Board import Board
from Const import *
from RPGBoard import *

pygame.init()
theBoard = Board()
theGame = RPGBoard()
runningFile = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_f:
                if runningFile == 0:
                    runningFile = 1
                else:
                    runningFile = 0
    if runningFile == 0:
        theBoard.ref()
        theBoard.draw()
    elif runningFile == 1:
        theGame.ref()
        theGame.draw()
        
    pygame.display.flip()
