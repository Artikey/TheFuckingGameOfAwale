import pygame
pygame.init()
clock = pygame.time.Clock()
screenWidth,screenHeigth = 800,600
window = pygame.display.set_mode([screenWidth,screenHeigth])
noir=(0,0,0)
blanc=(255,255,255)

def fontSize(taille):
    return pygame.font.Font(None, taille)
