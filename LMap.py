import pygame , sys
import time 
import random
from pygame.locals import *
import helpers

def main():
    print("Love")
    scrn = screen()
    scrn.run()


class mainRoom(helpers.Room):
    description = "This is the main room"

class otherRoom(helpers.Room):
    description = "This is another room"



class screen:
    
    clock = pygame.time.Clock()
    horror = 0
    fantasy = 0
    action = 0
    love = 0

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((980, 720))

        MR = mainRoom()
        
        MR.setNorth(otherRoom())
        
        evnt = helpers.GameEvents()
        done = False
        while not done:
            evnt.checkEvent()
            evnt.println(MR.description,screen)
            run = True
            while run:
                a = evnt.getInput(screen)
                b = MR.command(a)
                if isinstance(b,str):
                    evnt.println(b,screen)
                elif isinstance(b,Room):
                    MR = b
                    evnt.println(MR.description,screen)# pylint: disable=maybe-no-member


