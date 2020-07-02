import pygame , sys
import time 
import random
from pygame.locals import *

def main():
    print("Horror")
    scrn = screen()
    scrn.run()

class Events:
    
    posy = 0
    def display_keyboard(self,sentence,font,posx, color,screen,key,output):
        i = 0
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.mixer.init()
        typing = pygame.mixer.Sound("Sounds\Keyboard.wav")
        if int(self.posy) >= 690:
            time.sleep(1.5)
            screen.fill((0,0,0))
            self.posy = 0
            return False
        for char in sentence:
            run = True
            while run:
                self.checkEvent()
                width , height = font.size(char)
                textsurface = font.render(char, True, color)
                if(int(posx)+int(i)+int(width)) < 950:
                    screen.blit(textsurface,(posx + i,self.posy))
                    if not pygame.mixer.get_busy() and key:                    
                        typing.play(2)

                    pygame.display.flip()
                    if key:
                        time.sleep((random.randint(2,6)/70))
                    
                    i = i+int(width)
                    run = False
                else:  
                    self.checkEvent()
                    width , height = font.size("-")
                    textsurface = font.render("-", True, color)                    
                    screen.blit(textsurface,(posx + i,self.posy))
                    if not pygame.mixer.get_busy() and key:                    
                        typing.play(2)

                    pygame.display.flip()
                    if key:
                        time.sleep((random.randint(2,6)/70))
                    
                    i = i+int(width)                  
                    self.posy += 25
                    posx = 0 - int(i) + 5

        if key or output:
            self.posy += 25
        
        return

    def getInput(self,screen):
        run = True
        name = ""
        posx = 5
        myfont = pygame.font.SysFont('Georgia', 24)
        while run: 
         for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name += evt.unicode
                        self.display_keyboard(evt.unicode,myfont,posx,(255,255,255),screen,False, False)
                        width , height = myfont.size(evt.unicode)
                        posx += width
                    
                    elif evt.key == K_BACKSPACE:

                        if len(name) != 0:
                            last_char, height = myfont.size(name[-1])                        
                            name = name[:-1]
                        
                    
                            
                        # screen.blit(screen,(posx-last_char,self.posy),(640,512,last_char-2,self.posy))
                            pygame.draw.rect(screen, (0,0,0), pygame.Rect(posx-last_char, self.posy, last_char, 25))
                            pygame.display.update()
                            if posx > 5:
                                posx -= last_char

                        else:
                            posx = 5

                    elif evt.key == K_SPACE:
                            
                            name += " "
                            posx += 6

                    elif evt.key == K_RETURN:
                        self.posy += 25
                        # print(name)
                        return name
                elif  evt.type == QUIT:
                    pygame.quit()

        return

    def println(self,string,screen):
        myfont = pygame.font.SysFont('Georgia', 24)       
        color = (255,255,255)
        a = self.display_keyboard(str(string),myfont,5,color,screen,False,True)
        if a == False:
            self.display_keyboard(str(string),myfont,5,color,screen,False,True)


    def checkEvent(self):
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
 
class Room:
    north = None
    south = None
    east = None
    west = None
    description = ""

    def setNorth(self,room):
        self.north = room
        room.south = self
    def setSouth(self,room):
        self.south = room
        room.north = self
    def setEast(self,room):
        self.east = room
        room.west = self
    def setWest(self,room):
        self.west = room
        room.east = self
    # def newCommands(self,string):
    #     pass    
    def command(self,string):
        string = string.upper()
        #print(string)
        a = string.split()
        #print(a)
        #self.newCommands(string)
        if a[0] == "GO" or a[0] == "TRAVERSE" or a[0] == "WALK":
            if a[1] == "NORTH":
                return self.north
            elif a[1] == "SOUTH":
                return self.south
            elif a[1] == "EAST":
                return self.east
            elif a[1] == "WEST":
                return self.west
        elif a[0] == "LOOK" or a[0] == "CHECK":
            if a[1] == "AROUND":
                return self.description
        else:
            return None
        


class bedRoom(Room):
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





class livingRoom(Room):
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

class closet(Room):
    description = "You are in the closet. The room is filled with various clothes and hangers."

class kitchen(Room):
    description = "You are in your kitchen containing various appliances and drawers"

class garden(Room):
    description = "You are in the back garden. You haven't taken care of the greenery in a while with only a few plants remaining"

class bathroom(Room):
    description = "You are in your bathroom. There is a small shower, sink and toilet. Simple stuff"

class porch(Room):
    description = "You exit your house. The mailbox seems to be recently used. A newspaper is resting on your stairs and your car remains where you left it the day before."

class road(Room):
    description = "You are in the road"

class carRoad(Room):
    description = "You are in the road. There is a crashed car on the side of the road."

class forRoad(Room):
    description = "The road here seems to blend in with the forest around it"

class forest(Room):
    description = "You are in the Forest"

class forestTree(Room):
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
        # MR.setNorth(livingRoom())
        # MR.setSouth(closet())
        # MR.north.setWest(kitchen())
        # MR.north.setEast(porch())
        # MR.north.west.setWest(garden())
        # MR.north.west.setSouth(bathroom())
        
        evnt = Events()
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
                else:
                    evnt.println(("'"+str(a)+"' is not a known command....."),screen)


main()