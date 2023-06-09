from constants import *
import pygame

class Main_entity(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y, width):
        super().__init__()
        self.width = BLOCK_SIZE * width
        self.height = BLOCK_SIZE
        self.color = (255, 255, 255)
        # self.spritesheet = pygame.image.load(SPRITESHEET).convert()
        # self.y_sprite_sheet_index = y_sprite_sheet_index

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        # self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x * BLOCK_SIZE, y * BLOCK_SIZE)

        # self.frame = 0
        # self.max_frame = (self.spritesheet.get_width() // BLOCK_SIZE) - 1
        # self.animation_speed = TICK_RATE / self.max_frame / 100

        self.coords = pygame.math.Vector2(self.rect.x, self.rect.y)



    def update(self):
        pass
        # self.animate()

    def events(events):
        pass


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
