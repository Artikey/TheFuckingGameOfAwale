#!/usr/bin/python3
import pygame
from Player import Player
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("RPGStyledBoard")

p = Player(50, 50, 40, 60, 5, (255, 0, 0))
running = True
while running:
    win.fill((0, 0, 0))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]
        p.x -= p.vel

    if keys[pygame.K_RIGHT]:
        p.x += p.vel
    if keys[pygame.K_UP]:
        p.y -= p.vel
    if keys[pygame.K_DOWN]:
        p.y += p.vel

    p.draw(win)
    pygame.display.update()

pygame.quit()
