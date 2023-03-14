import pygame
import random
import winsound
import math

pygame.init()#initializes Pygame
pygame.display.set_caption("Simon!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

def collision(xpos, ypos):
    #print("inside funciton")
    if math.sqrt((xpos - 400)**2 + (ypos - 400)**2)>200 or math.sqrt((xpos - 400)**2 + (ypos - 400)**2)<100:
        #print("outside of ring")
        return -1
    elif xpos < 400 and ypos < 400:
        #print("over red button")
        pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
        pygame.display.flip()
        winsound.Beep(400, 500)
        return 0
    elif xpos < 400 and ypos > 400:
        #print("over blue button")
        pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), pi, (3*pi/2), 100)
        pygame.display.flip()
        winsound.Beep(640, 500)
        return 1
    elif xpos > 400 and ypos < 400:
        #print("over green")
        pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), 0, (pi/2), 100)
        pygame.display.flip()
        winsound.Beep(840, 500)
        return 2
    elif xpos > 400 and ypos > 400:
        #print("over yellow")
        pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
        pygame.display.flip()
        winsound.Beep(1040, 500)
        return 3
    else:
        print("inside of ring!")




#game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers in a TUPLE
Hasclicked = []
playerPattern = []
turn = False
pattern = [] #this holds the random pattern
pi = 3.1415
ded = False

#draw everything first so things don't appear one at a time
pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), pi, (3*pi/2), 100)
pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), 0, (pi/2), 100)
#more colors go here!   
pygame.display.flip()


#gameloop###################################################
while True:
    
    
    event = pygame.event.wait()#event queue 

    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        Hasclicked = True
        print("clicked")

    if event.type == pygame.MOUSEBUTTONUP:
        Hasclicked = False

    if event.type == pygame.MOUSEMOTION:
        #print("moving mouse!")
        mousePos = event.pos
        collision(mousePos[0], mousePos[1])
        
    #player turn=---------------------------------------------
    print("starting player turn")
    if turn == True:
        if len(playerPattern) <len(pattern):
            if hasClicked == True:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked = False
                
    else:
        turn = False
        # pygame.time.wait(800)
                
    
    
        
    #update section---------------------------------------------
    if turn == False:
        print("Starting machine turn")
        pattern.append(random.randrange(0, 2)) #push a new value into the pattern list
        
        #brighten colors and play beep for each number in the pattern
        for i in range(len(pattern)): 
            if pattern[i]==0: #RED
                pygame.draw.arc(screen, (255, 0,0), (200,200,400,400), pi/2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)
                
            elif pattern[i]==1:#BLUE
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)

            elif pattern[i]==1:#YELLOW
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
                pygame.display.flip()
                winsound.Beep(840, 500)
                
            elif pattern[i]==1:#GREEN
                pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), 0, (pi/2), 100)
                pygame.display.flip()
                winsound.Beep(1040, 500)
                
            #redraw board after every beep
            pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
            pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), pi, (3*pi/2), 100)
            pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
            pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), 0, (pi/2), 100)
            pygame.display.flip()
            pygame.time.wait(200) #slows the game down a bit
            turn = True
            playerPattern.clear()
    
    
    playerPattern.append(collision(mousePos[0], mousePos[1]))
    print(playerPattern)        
            
    turn = False       
    #render section---------------------------------------------
    
    
    #game board
    pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), pi, (3*pi/2), 100)
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), 0, (pi/2), 100)
    #more colors go here!
   
    pygame.display.flip()
    #pygame.time.wait(800)
    

#end game loop##############################################

pygame.quit
