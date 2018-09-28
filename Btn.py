import pygame
from Const import *


class Btn:
    def __init__(self, x, y, wid, hei):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.coolDown = 0
        self.actif = True
        self.click = False
        self.hightLight = False
        self.press = False

    def getPress(self):
        mpos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.coolDown < 0:
                self.click = True
                self.coolDown = 20
        self.hightLight = False
        self.press = False
        if mpos[0] < self.x + self.wid and mpos[0] > self.x and mpos[1] < self.y + self.hei and mpos[1] > self.y:
            self.hightLight = True
            if self.click:
                self.press = True
        self.click = False

        return [self.hightLight, self.press]


    def ref(self):

        self.coolDown -= 1
