import sys
import random
from random import randint
import pygame
from pygame import *
pygame.init()

screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Rectangles")
pos_x=300
pos_y=250
vel_x=2
vel_y=1
color=100,100,100            
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))
    
    pos_x +=vel_x
    pos_y +=vel_y
    if pos_x>500 or pos_x<0:
        vel_x=-vel_x
        rand1=randint(0,255)
        rand2=randint(0,255)
        rand3=randint(0,255)
        color=rand1,rand2,rand3
    if pos_y>400 or pos_y<0:
        vel_y=-vel_y
        rand1=randint(0,255)
        rand2=randint(0,255)
        rand3=randint(0,255)
        color=rand1,rand2,rand3
    width=0
    pos=pos_x,pos_y,100,100
    pygame.draw.rect(screen,color,pos,width)

    pygame.display.update()
