import pygame , sys
import time 
import random
from pygame.locals import *

def main():
    print("Love")
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
                self.checkEvent()
                width , height = font.size(char)
                textsurface = font.render(char, True, color)
                screen.blit(textsurface,(posx + i,self.posy))
                if not pygame.mixer.get_busy() and key:                    
                    typing.play(2)
    
                pygame.display.flip()
                if key:
                    time.sleep((random.randint(2,6)/70))
                
                i = i+int(width)
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
        a = self.display_keyboard(str(string),myfont,5,color,screen,True,False)
        if a == False:
            self.display_keyboard(str(string),myfont,5,color,screen,True,False)


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
    def command(self,string):
        string = string.upper()
        #print(string)
        a = string.split()
        #print(a)
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
            return ("'"+str(string)+"' is not a known command.....")


class mainRoom(Room):
    description = "This is the main room"

class otherRoom(Room):
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


#main()