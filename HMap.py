import pygame , sys
import time 
import random
from pygame.locals import *
import helpers

def main():
    print("Horror")
    scrn = screen()
    scrn.run()

class bedRoom(helpers.Room):
    description = "You are in your bedroom. There is a computer to your left and a door in front of you. Light through the window brightens the room."
    computer = False
    window_closed = True

    def command(self,string):
        #super().newCommands(string)
        if super().command(string) == None:
            string = string.upper()
            a = string.split()
            if a[0] == "TURN" or a[0] == "SWITCH":
                if a[1] == "ON" or a[1] == "COMPUTER":
                    if a[2] == "COMPUTER" or a[2] == "ON":
                        if self.computer == False:
                            self.computer = True
                            return ("The computer turns on.")
                        else:
                            return("The computer is already switched on.")
                if a[1] == "OFF" or a[1] == "COMPUTER":
                    if a[2] == "COMPUTER" or a[2] == "OFF":
                        if self.computer == True:
                            self.computer = False
                            return ("The computer turns off.")
                        else:
                            return("The computer is already switched off.")
            elif a[0] == "LOOK":
                if a[1] == "AT":
                    if a[2] == "COMPUTER":
                        if self.computer == True:
                            return "You see the recent chat you had with your therapist"
                        else:
                            return "The computer is off"
                    elif a[2] == "WINDOW":
                        if self.window_closed == True:
                            return "The window is closed"
                        else:
                            return "You look outside the window. There are a considerable amount of clouds."
            elif a[0] == "OPEN":
                if a[1] == "WINDOW":
                    if self.window_closed == True:
                        self.window_closed =False
                        return "You open the window"
                    else:
                        return "The window is already open"
            elif a[0] == "CLOSE":
                if a[1] == "WINDOW":
                    if self.window_closed == False:
                        self.window_closed = True
                        return "You close the window"
                    else:
                        return "The window is already closed"
            elif a[0] == "SLEEP" or a[0] == "NAP":
                time.sleep(2)
                return "After a good nap you wake up refreshed ready for a hard day's work"
        else:
            return super().command(string)





class livingRoom(helpers.Room):
    description = "You are now in your living quarters. There is a Television and the main door in front of you."
    tv_off = True

    def command(self,string):
        #super().newCommands(string)
        if super().command(string) == None:
            string = string.upper()
            a = string.split()
            if a[0] == "TURN" or a[0] == "SWITCH":
                if a[1] == "ON" or a[1] == "TELEVISION" or a[1] == "TV":
                    if a[2] == "TELEVISION" or a[2] == "ON" or a[2] == "TV":
                        if self.tv_off == True:
                            self.computer = False
                            return ("The television turns on.")
                        else:
                            return("The television is already switched on.")
                if a[1] == "OFF" or a[1] == "TELEVISION" or a[1] =="TV":
                    if a[2] == "TELEVISION" or a[2] == "OFF" or a[2] == "TV":
                        if self.computer == True:
                            self.computer = False
                            return ("The television turns off.")
                        else:
                            return("The television is already switched off.")
        else:
            return super().command(string)

class closet(helpers.Room):
    description = "You are in the closet. The room is filled with various clothes and hangers."

class kitchen(helpers.Room):
    description = "You are in your kitchen containing various appliances and drawers"

class garden(helpers.Room):
    description = "You are in the back garden. You haven't taken care of the greenery in a while with only a few plants remaining"

class bathroom(helpers.Room):
    description = "You are in your bathroom. There is a small shower, sink and toilet. Simple stuff"

class porch(helpers.Room):
    description = "You exit your house. The mailbox seems to be recently used. A newspaper is resting on your stairs and your car remains where you left it the day before."

class road(helpers.Room):
    description = "You are in the road"

class carRoad(helpers.Room):
    description = "You are in the road. There is a crashed car on the side of the road."

class forRoad(helpers.Room):
    description = "The road here seems to blend in with the forest around it"

class forest(helpers.Room):
    description = "You are in the Forest"

class forestTree(helpers.Room):
    description = "The forest here seems different than the rest. One tree seems to be climbable"


def genMap():
    BedRooom = bedRoom()
    Closet = closet()
    LivingRoom = livingRoom()
    Kitchen = kitchen()
    Bathroom = bathroom()
    Garden = garden()
    Porch = porch()
    Forest = forest()
    ForestTree = forestTree()
    Road = road()
    ForRoad = forRoad()
    CarRoad = carRoad()

    BedRooom.setSouth(Closet)
    BedRooom.setNorth(LivingRoom)
    LivingRoom.setWest(Kitchen)
    LivingRoom.setEast(Porch)
    Kitchen.setSouth(Bathroom)
    Kitchen.setWest(Garden)
    Porch.setEast(Road)
    

    return BedRooom

class screen:
    
    clock = pygame.time.Clock()
    horror = 0
    fantasy = 0
    action = 0
    love = 0

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((980, 720))

        MR = genMap()                
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
                elif isinstance(b,helpers.Room):
                    MR = b
                    evnt.println(MR.description,screen)# pylint: disable=maybe-no-member
                else:
                    evnt.println(("'"+str(a)+"' is not a known command....."),screen)
