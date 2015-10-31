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
for i in range(1,33):
    picture = pygame.image.load(os.path.join('scissor','scissor'+str(i)+'.bmp')).convert_alpha()
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
	index = (pygame.mouse.get_pos()[0] / -20)%32
        print index
        pygame.event.get()
        screen.blit(pic[index], picrect[index])
        pygame.display.flip()
        pygame.event.get()
        sleep(0.01)
