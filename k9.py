from constants import *
import pygame, main_entity

class K9(main_entity.Main_entity):

    """
        # TODO:

    """
    def __init__(self, x, y):
        self.color = (0, 255, 0)
        super().__init__(x, y, 1)





    def update(self):
        self.image.fill(self.color)
        # self.move()
        # self.animate()


    def events(self, events):
        for event in events:
            if event.type == pygame.KEYUP:

                if event.scancode == 80:#Left
                    self.rect.x = self.rect.x - BLOCK_SIZE

                if event.scancode == 79:#Right
                    self.rect.x = self.rect.x + BLOCK_SIZE

                if event.scancode == 82:#UP
                    self.rect.y = self.rect.y - BLOCK_SIZE

                if event.scancode == 81:#UP
                    self.rect.y = self.rect.y + BLOCK_SIZE
                    # updates the bomb group when you set a bomb
    # def get_image_from_sprite_sheet(self, row, col):
    #     # print(f"self:{self} row:{row} col:{col} self.y_sprite_sheet_index:{self.y_sprite_sheet_index}")
    #     if row < 0 or row > self.spritesheet.get_width():
    #         raise ValueError("row is either below 0 or larger than spritesheet")
    #     if col < 0 or col > self.spritesheet.get_height():
    #         raise ValueError("col is either below 0 or larger than spritesheet")
    #
    #     image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
    #     image.blit(self.spritesheet, (0, 0), (row, col, BLOCK_SIZE, BLOCK_SIZE))
    #     #image.set_colorkey()
    #     return image



    # def animate(self):
    #     self.frame += self.animation_speed
    #
    #     if self.frame > self.max_frame:
    #         self.frame = 0
    #
    #     self.image = self.get_image_from_sprite_sheet(round(self.frame) * BLOCK_SIZE, self.y_sprite_sheet_index * BLOCK_SIZE)
    #

    def get_coords(self):
        return self.coords
