import sys, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([640, 480])


while True:
    screen.fill((120, 120, 120))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
