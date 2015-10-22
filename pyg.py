import pygame
import os
from time import sleep
import sys

def waitMotion():

    wait = 0
    while wait == 0:
        pygame.event.get()
        if pygame.mouse.get_pos()[0] - xloc > 60:
            wait = 1
    return

pygame.init()
size = width, height = 1200, 900
screen = pygame.display.set_mode(size)
imagestore = []
pic1 = pygame.image.load(os.path.join('data','test1.bmp')).convert_alpha()
pic2 = pygame.image.load(os.path.join('data','test2.bmp')).convert_alpha()
pic3 = pygame.image.load(os.path.join('data','test3.bmp')).convert_alpha()
pic4 = pygame.image.load(os.path.join('data','test4.bmp')).convert_alpha()
pic5 = pygame.image.load(os.path.join('data','test5.bmp')).convert_alpha()
pic6 = pygame.image.load(os.path.join('data','test6.bmp')).convert_alpha()
pic7 = pygame.image.load(os.path.join('data','test7.bmp')).convert_alpha()
pic1rect = pic1.get_rect()
pic2rect = pic2.get_rect()
pic3rect = pic3.get_rect()
pic4rect = pic4.get_rect()
pic5rect = pic5.get_rect()
pic6rect = pic6.get_rect()
pic7rect = pic7.get_rect()
imagestore.append(pic1rect)
imagestore.append(pic2rect)
imagestore.append(pic3rect)
imagestore.append(pic4rect)
imagestore.append(pic5rect)
imagestore.append(pic6rect)
imagestore.append(pic7rect)
speed = [0, 0]
black = 0, 0, 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    screen.blit(pic1, pic1rect)
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
        if xloc - pygame.mouse.get_pos()[0] <  -70 and xloc - pygame.mouse.get_pos()[0] >  -70*2:
            screen.blit(pic2, pic2rect)
            pygame.display.flip()       
        pygame.event.get()
        sleep(0.01)
        if xloc - pygame.mouse.get_pos()[0] <  -70*2 and xloc - pygame.mouse.get_pos()[0] >  -70*3:
            screen.blit(pic3, pic3rect)
            pygame.display.flip()       
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]
        if xloc - pygame.mouse.get_pos()[0] <  -70*3 and xloc - pygame.mouse.get_pos()[0] >  -70*4:
            screen.blit(pic4, pic4rect)
            pygame.display.flip()       
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]
        if xloc - pygame.mouse.get_pos()[0] <  -70*4 and xloc - pygame.mouse.get_pos()[0] >  -70*5:
            screen.blit(pic5, pic5rect)
            pygame.display.flip()
        pygame.event.get()
        sleep(0.01)
        print xloc - pygame.mouse.get_pos()[0]
        if xloc - pygame.mouse.get_pos()[0] <  -70*5:
            screen.blit(pic6, pic6rect)
            pygame.display.flip()