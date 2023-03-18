from constants import *
import pygame
import main_entity
import random

class Cars(main_entity.Main_entity):
    def __init__(self, x, y, length, dir): #0 left 1 right
        super().__init__(x, y, length)
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.speed = 0
        self.dir = dir
        self.origin = x

    def update(self):
        self.image.fill(self.color)


        if self.dir == 0:
            self.rect = self.rect.move(-self.speed, 0)
            if self.rect.right < 0:
                self.rect.x = self.origin
                self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        if self.dir == 1:
            self.rect = self.rect.move(self.speed, 0)
            if self.rect.left > GAME_WIDTH:
                self.rect.x = self.origin
                self.color = COLORS[random.randint(0, len(COLORS) - 1)]
