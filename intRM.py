import pygame , sys
import time 
import random
from pygame.locals import *
import AMap, FMap, HMap, LMap
import helpers

def main():
    
    scrn = screen()
    scrn.run()

class screen:
    pygame.init()
    screen = pygame.display.set_mode((980, 720))
    clock = pygame.time.Clock()
    horror = 0
    fantasy = 0
    action = 0
    love = 0

    def run(self):
        
        myfont = pygame.font.SysFont('Georgia', 24)
       
        color = (255,255,255)
        evnt = helpers.IntEvents()
        done = False
        while not done:
                evnt.checkEvent()
                evnt.display_keyboard("Hello, My name is Dr.Martin Cross, and you are?",myfont,5,color,self.screen,True,False)
                corr = "No"
                while corr.upper() == "NO":
                    invalid = True                  
                    name = evnt.getInput(self.screen)
                    while invalid == True:
                        evnt.display_keyboard(str(name)+" is your name? Is this correct? (Yes/No)",myfont,5,color,self.screen,True,False)
                        corr = evnt.getInput(self.screen)
                        corr = corr.upper()
                        print(corr)
                        if corr == "YES":
                            evnt.display_keyboard("Great "+str(name)+" let's progress further",myfont,5,color,self.screen,True,False)
                            invalid = False
                        elif corr == "NO":
                            evnt.display_keyboard("OK, so what IS your name?",myfont,5,color,self.screen,True,False)
                            invalid = False
                        else:
                            evnt.display_keyboard("Stop trying to play smart with me lets get to business",myfont,5,color,self.screen,True,False)
                            invalid = True

                a = evnt.display_keyboard("So tell me, why are you here?",myfont,5,color,self.screen,True,False)
                b = evnt.display_keyboard("Scared - I am scared of the future to come",myfont,5,color,self.screen,False,True)
                c = evnt.display_keyboard("Fictional - I am disjointed from the real world",myfont,5,color,self.screen,False,True)
                d = evnt.display_keyboard("Angry - I feel angry, I haven't felt calm in ages",myfont,5,color,self.screen,False,True)
                e = evnt.display_keyboard("Numb - I have lost all love for the world around me",myfont,5,color,self.screen,False,True)
                if a == False or b == False or c == False or d == False or e == False:
                    evnt.display_keyboard("So tell me, why are you here?",myfont,5,color,self.screen,True,False)
                    evnt.display_keyboard("Scared - I am scared of the future to come",myfont,5,color,self.screen,False,True)
                    evnt.display_keyboard("Fictional - I am disjointed from the real world",myfont,5,color,self.screen,False,True)
                    evnt.display_keyboard("Angry - I feel angry, I haven't felt calm in ages",myfont,5,color,self.screen,False,True)
                    evnt.display_keyboard("Numb - I have lost all love for the world around me",myfont,5,color,self.screen,False,True)

                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "SCARED":
                        a = evnt.display_keyboard("I see, fear is a very strong emotion in one's life",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("I see, fear is a very strong emotion in one's life",myfont,5,color,self.screen,True,False)
                        self.horror += 1
                        run = False
                    elif str(prob) == "FICTIONAL":
                        a = evnt.display_keyboard("I see, we will deal with your fictional mind",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("I see, we will deal with your fictional mind",myfont,5,color,self.screen,True,False)
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "ANGRY":
                        a = evnt.display_keyboard("I see, anger can be easily controlled",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("I see, anger can be easily controlled",myfont,5,color,self.screen,True,False)
                        self.action += 1
                        run = False
                    elif str(prob) == "NUMB":
                        a = evnt.display_keyboard("Love is a very complex detail in one's life. We will find the love in your heart once again",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Love is a very complex detail in one's life. We will find the love in your heart once again",myfont,5,color,self.screen,True,False)
                        self.love += 1
                        run = False
                    else:
                        a = evnt.display_keyboard("I don't think you understood me, try again.",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("I don't think you understood me, try again.",myfont,5,color,self.screen,True,False)
                        
                a = evnt.display_keyboard("OK "+str(name)+" what is your favourite primary colour?",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("OK "+str(name)+" what is your favourite primary colour?",myfont,5,color,self.screen,True,False)
                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "RED":
                        a = evnt.display_keyboard("You DO have that fire in your eyes! Red suits you",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("You DO have that fire in your eyes! Red suits you",myfont,5,color,self.screen,True,False)
                        self.action += 1
                        self.horror +=1
                        run = False
                    elif str(prob) == "BLUE":
                        a = evnt.display_keyboard("I see, quite a cold colour now isn't it?",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("I see, quite a cold colour now isn't it?",myfont,5,color,self.screen,True,False)
                        self.horror += 1
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "YELLOW":
                        a = evnt.display_keyboard("Ahh, yellow is a rather happy colour in my humble opinion.",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Ahh, yellow is a rather happy colour in my humble opinion.",myfont,5,color,self.screen,True,False)
                        self.love += 1
                        self.fantasy += 1
                        run = False
                    else:
                        a = evnt.display_keyboard(str(prob)+ "is not a primary colour.",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard(str(prob)+ "is not a primary colour.",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("Next question, do you think you are strong or weak?",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("Next question, do you think you are strong or weak?",myfont,5,color,self.screen,True,False)
                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "STRONG":
                        a = evnt.display_keyboard("Interesting... you dont look so strong to me! HAHA",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Interesting... you dont look so strong to me! HAHA",myfont,5,color,self.screen,True,False)
                        self.action += 1
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "WEAK":
                        a = evnt.display_keyboard("Interesting... you are weak but strong at heart!",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Interesting... you are weak but strong at heart!",myfont,5,color,self.screen,True,False)
                        self.horror += 1
                        self.love += 1
                        run = False
                    else:
                        a = evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("Ok so, if a fight were to break out near you and your friend/relative were in it would you:",myfont,5,color,self.screen,True,False)
                b = evnt.display_keyboard("a) Intervene or b) Run?",myfont,5,color,self.screen,True,False)
                if a == False or b == False:
                    evnt.display_keyboard("Ok so, if a fight were to break out near you and your friend/relative were in it would you:",myfont,5,color,self.screen,True,False)
                    evnt.display_keyboard("a) Intervene or b) Run?",myfont,5,color,self.screen,True,False)
                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "INTERVENE" or str(prob) == "A":
                        a = evnt.display_keyboard("Ok, you are brave ready to help whether it would hurt you or not.",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Ok, you are brave ready to help whether it would hurt you or not.",myfont,5,color,self.screen,True,False)
                        self.action += 1
                        self.love += 1
                        run = False
                    elif str(prob) == "RUN" or str(prob) == "B":
                        a = evnt.display_keyboard("Ok, you are selfish. Unable to help others in need.",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Ok, you are selfish. Unable to help others in need.",myfont,5,color,self.screen,True,False)
                        self.horror += 1
                        self.fantasy +=1
                        run = False
                    else:
                        a = evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("Next up, what do you want to be remembered for when you die?",myfont,5,color,self.screen,True,False)
                b = evnt.display_keyboard("a) As a kind-hearted person that always cared for others.",myfont,5,color,self.screen,False,True)
                c = evnt.display_keyboard("b) As the strongest person alive! I want to be feared by many!",myfont,5,color,self.screen,False,True)
                d = evnt.display_keyboard("c) As a creative person that gave pleasure to others.",myfont,5,color,self.screen,False,True)
                e = evnt.display_keyboard("d) I don't care about what others think about me.",myfont,5,color,self.screen,False, True)
                if a == False or b== False or c == False or d == False or e == False:
                    evnt.display_keyboard("Next up, what do you want to be remembered for when you die?",myfont,5,color,self.screen,False, True)
                    evnt.display_keyboard("a) As a kind-hearted person that always cared for others.",myfont,5,color,self.screen,False, True)
                    evnt.display_keyboard("b) As the strongest person alive! I want to be feared by many!",myfont,5,color,self.screen,False, True)
                    evnt.display_keyboard("c) As a creative person that gave pleasure to others.",myfont,5,color,self.screen,False, True)
                    evnt.display_keyboard("d) I don't care about what others think about me.",myfont,5,color,self.screen,False, True)
                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "A":
                        self.love += 1
                        run = False
                    elif str(prob) == "B":
                        self.action += 1
                        run = False
                    elif str(prob) == "C":
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "D":
                        self.horror += 1
                        run = False
                    else:
                        a = evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("Hmm... Interesting",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("Hmm... Interesting",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("Do you enjoy Summer or Winter ?",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("Do you enjoy Summer or Winter ?",myfont,5,color,self.screen,True,False)

                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "SUMMER":
                        a = evnt.display_keyboard("Ahh the heat it's my personal favourite too!",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Ahh the heat it's my personal favourite too!",myfont,5,color,self.screen,True,False)
                        self.action += 1
                        self.love += 1
                        run = False
                    elif str(prob) == "WINTER":
                        a = evnt.display_keyboard("Ahh staying at home drinking some hot chocolate, I also enjoy the winter time.",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Ahh staying at home drinking some hot chocolate, I also enjoy the winter time.",myfont,5,color,self.screen,True,False)
                        self.horror += 1
                        self.fantasy +=1
                        run = False
                    else:
                        a = evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("Stop testing me! Go again",myfont,5,color,self.screen,True,False)


                a = evnt.display_keyboard("What is your star sign?",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("What is your star sign?",myfont,5,color,self.screen,True,False)

                run = True
                while run:
                    prob = evnt.getInput(self.screen)
                    prob = prob.upper()

                    if str(prob) == "ARIES":
                        self.action += 1
                        run = False
                    elif str(prob) == "TAURUS":
                        self.love += 1
                        run = False
                    elif str(prob) == "GEMINI":
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "CANCER":
                        self.love += 1
                        run = False
                    elif str(prob) == "LEO":
                        self.action += 1
                        run = False
                    elif str(prob) == "VIRGO":
                        self.horror += 1
                        run = False
                    elif str(prob) == "LIBRA":
                        self.love += 1
                        run = False
                    elif str(prob) == "SCORPIO":
                        self.horror += 1
                        run = False
                    elif str(prob) == "SAGITTARIUS":
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "CAPRICORN":
                        self.action += 1
                        run = False
                    elif str(prob) == "AQUARIUS":
                        self.fantasy += 1
                        run = False
                    elif str(prob) == "PISCES":
                        self.horror += 1
                        run = False
                        
                    
                    else:
                        a = evnt.display_keyboard("You might want to rethink your decision... Go again",myfont,5,color,self.screen,True,False)
                        if a == False:
                            evnt.display_keyboard("You might want to rethink your decision... Go again",myfont,5,color,self.screen,True,False)
                    
                
                a = evnt.display_keyboard("Interesting, I don't personally believe in that mumbo jumbo but it might help in my studies.",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("Interesting, I don't personally believe in that mumbo jumbo but it might help in my studies.",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("From what I have gathered I think I have the right medication for you, here take this.",myfont,5,color,self.screen,True,False)
                if a == False:
                    evnt.display_keyboard("From what I have gathered I think I have the right medication for you, here take this.",myfont,5,color,self.screen,True,False)

                a = evnt.display_keyboard("After taking the medication you feel nauseous.... your eyes dim and you fall in a deep sleep",myfont,5,color,self.screen,False,True)
                if a == False:
                    evnt.display_keyboard("After taking the medication you feel nauseous.... your eyes dim and you fall in a deep sleep",myfont,5,color,self.screen,False,True)
                time.sleep(5)
                
                if self.horror >= self.love and self.horror >= self.fantasy and self.horror >=self.action:
                    if self.horror == self.love:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            HMap.main()
                        else:
                            LMap.main()
                    elif self.horror == self.fantasy:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            HMap.main()
                        else:
                            pygame.quit()
                            FMap.main()
                    elif self.horror == self.action:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            HMap.main()
                        else:
                            pygame.quit()
                            AMap.main()
                    else:
                        pygame.quit()
                        HMap.main()
                elif self.love >= self.horror and self.love >= self.fantasy and self.love >=self.action:
                    if self.love == self.horror:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            LMap.main()
                        else:
                            HMap.main()
                    elif self.love == self.fantasy:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            LMap.main()
                        else:
                            pygame.quit()
                            FMap.main()
                    elif self.love == self.action:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            LMap.main()
                        else:
                            pygame.quit()
                            AMap.main()
                    else:
                        pygame.quit()
                        LMap.main()
                elif self.fantasy >= self.horror and self.fantasy >= self.love and self.fantasy >=self.action:
                    if self.fantasy == self.horror:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            FMap.main()
                        else:
                            HMap.main()
                    elif self.fantasy == self.love:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            FMap.main()
                        else:
                            pygame.quit()
                            LMap.main()
                    elif self.fantasy == self.action:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            FMap.main()
                        else:
                            pygame.quit()
                            AMap.main()
                    else:
                        pygame.quit()
                        FMap.main()
                else:
                    if self.action == self.horror:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            AMap.main()
                        else:
                            HMap.main()
                    elif self.action == self.love:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            AMap.main()
                        else:
                            LMap.main()
                    elif self.action == self.fantasy:
                        choice = random.randint(1,2)
                        if choice == 1:
                            pygame.quit()
                            AMap.main()
                        else:
                            pygame.quit()
                            FMap.main()
                    else:
                        pygame.quit()
                        AMap.main()
                
                done == True
               # time.sleep(2)

   

