#!/usr/bin/python3
import pygame

from Player import Player


class RPGBoard():
    def __init__(self):
        pygame.init()
        
        self.win = pygame.display.set_mode((800,600))
        
        pygame.display.set_caption("RPGStyledBoard")

        self.p = Player(50, 50, 40, 60, 1, (255, 0, 0))
        
    def ref(self):
        self.win.fill((0, 0, 0))
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.p.x -= self.p.vel
            
        if keys[pygame.K_RIGHT]:
            self.p.x += self.p.vel
            
        if keys[pygame.K_UP]:
            self.p.y -= self.p.vel
            
        if keys[pygame.K_DOWN]:
            self.p.y += self.p.vel
    def draw(self):
        self.p.draw(self.win)
        pygame.display.update()

