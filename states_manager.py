from constants import *
import sys, pygame, groups_manager


class States_manager:
    def __init__(self, clock, surface):
        self.running = True
        self.states = ["start", "running", "paused", "dead"]
        self.state = self.states[1]

        self.groups_manager = groups_manager.Groups_manager()
        # self.events = pygame.event.get()






    def draw(self, surface):
        surface.fill((100, 100, 100))#background

        if self.state == "start":
            surface.fill((100, 100, 255))#background

        elif self.state == "running":
            pass
            self.groups_manager.get_drawing_group().draw(surface)


        elif self.state == "paused":
            # surface.fill((255, 100, 100))#background
            pass

        elif self.state == "dead":
            surface.fill((50, 50, 50))#background



        pygame.display.flip()


    def update(self, surface):
        if self.state == "start":
            pass

        elif self.state == "running":
            self.groups_manager.update()



        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass




    def events(self, events):

        self.groups_manager.events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                #used to kill outside loop


                if event.key == pygame.K_p:
                    if self.state == "paused":
                        self.state = "running"
                    else:
                        self.state = "paused"

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    if self.state == "start":
                        self.state = "running"
