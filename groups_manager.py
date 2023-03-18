from constants import *
import sys, pygame, k9, cars


class Groups_manager:
    def __init__(self):
        pass
        self.player_group = pygame.sprite.GroupSingle()
        self.cars_group = pygame.sprite.Group()
        self.make_cars()
        self.player = k9.K9(COLS // 2, ROWS - 1)
        self.player_group.add(self.player)

        self.drawable_objects = pygame.sprite.Group()




    def update(self):

        # self.collideable_objects.empty()
        # self.collideable_objects.add(self.crates_group, self.border_group)
        self.player_group.update()
        self.cars_group.update()
        # self.bombs_group.update(self)
        # self.crates_group.update()
        # self.border_group.update()
        # self.floor_tiles_group.update()
        # self.enemy_group.update(self)




    def get_drawing_group(self):
        self.drawable_objects.empty()
        self.drawable_objects.add(
            self.player_group,
            self.cars_group
        )
        return self.drawable_objects



    def events(self, events):
        self.player.events(events)


    def make_cars(self):
        for i in range(5):
            for j in range(4):
                if i % 2 != 0:
                    self.cars_group.add(cars.Cars(j * BLOCK_SIZE, 12 - i, 1, 0))

                else:
                    # print(j * -(GAME_WIDTH // 8))
                    self.cars_group.add(cars.Cars(j * BLOCK_SIZE , 12 - i, 1, 1))

    # def get_group(self, search):
    #     return self.main_group[search]

    # def get_main_group(self):
    #     return self.main_group



    # def update_main_group(self):
    #     return {
    #         "player_group" : self.player_group,
    #         "bombs_group" : self.bombs_group,
    #         "crates_group" : self.crates_group,
    #         "border_group" : self.border_group,
    #         "floor_tiles_group" : self.floor_tiles_group,
    #         "collideable_objects" : self.collideable_objects,
    #         "enemy_group" : self.enemy_group
    #     }
