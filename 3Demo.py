import pygame
import os
from time import sleep
import sys

# rewrite the code to be easily scaled. 

def waitMotion():

    wait = 0
    while wait == 0:
        pygame.event.get()
        if pygame.mouse.get_pos()[0] - xloc > 60:
            wait = 1
    return

pic = []
picrect = []

pygame.init()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
imagestore = []
for i in range(1,12):
    picture = pygame.image.load(os.path.join('demo','clip'+str(i)+'.bmp')).convert_alpha()
    picture = pygame.transform.scale(picture, size)
    pic.append(picture)
    picrect.append(pic[i-1].get_rect())

speed = [0, 0]
black = 0, 0, 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    screen.blit(pic[0], picrect[0])
    pygame.display.flip()
    pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
        pygame.event.get()
        xloc = pygame.mouse.get_pos()[0]
    while pygame.mouse.get_pressed()[0]:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.event.get()
        print xloc - pygame.mouse.get_pos()[0]
        sleep(0.01)
        if xloc - pygame.mouse.get_pos()[0] >  0:
            screen.blit(pic[1], picrect[1])
            pygame.display.flip() 

        pygame.event.get()
        if xloc - pygame.mouse.get_pos()[0] <  -70 and xloc - pygame.mouse.get_pos()[0] >  -70*2:
            screen.blit(pic[2], picrect[2])
            pygame.display.flip()

        pygame.event.get()
        sleep(0.01)
        if xloc - pygame.mouse.get_pos()[0] <  -70*2 and xloc - pygame.mouse.get_pos()[0] >  -70*3:
            screen.blit(pic[3], picrect[3])
            pygame.display.flip() 

        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]
        if xloc - pygame.mouse.get_pos()[0] <  -70*3 and xloc - pygame.mouse.get_pos()[0] >  -70*4:
            screen.blit(pic[4], picrect[4])
            pygame.display.flip()     
    
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]
        if xloc - pygame.mouse.get_pos()[0] <  -70*4 and xloc - pygame.mouse.get_pos()[0] >  -70*5:
            screen.blit(pic[5], picrect[5])
            pygame.display.flip()  
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]

        if xloc - pygame.mouse.get_pos()[0] <  -70*5 and xloc - pygame.mouse.get_pos()[0] >  -70*6:
            screen.blit(pic[6], picrect[6])
            pygame.display.flip()  
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]

        if xloc - pygame.mouse.get_pos()[0] <  -70*6 and xloc - pygame.mouse.get_pos()[0] >  -70*7:
            screen.blit(pic[7], picrect[7])
            pygame.display.flip()  
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]

        if xloc - pygame.mouse.get_pos()[0] <  -70*7 and xloc - pygame.mouse.get_pos()[0] >  -70*8:
            screen.blit(pic[8], picrect[8])
            pygame.display.flip()  
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]

        if xloc - pygame.mouse.get_pos()[0] <  -70*8:
            screen.blit(pic[9], picrect[9])
            pygame.display.flip()       
