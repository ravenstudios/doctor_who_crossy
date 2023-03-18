from constants import *
import pygame
import main_entity
import random

class Cars(main_entity.Main_entity):
    def __init__(self, x, y, length):
        super().__init__(x, y, length)
        self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.speed = 5


    def update(self):
        self.image.fill(self.color)
        if self.rect.right < 0:
            self.rect.x = (COLS + random.randint(1,  5)) * BLOCK_SIZE
            self.color = COLORS[random.randint(0, len(COLORS) - 1)]
        self.rect = self.rect.move(-self.speed, 0)
