import random
from random import randint
import sys
import pygame
from pygame import *
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Drawing Line")

screen.fill((0,80,0))
color=100,255,200
width=2
for i in range(1,1001):
        pygame.draw.line(screen,color,(randint(0,800),randint(0,600)),(randint(0,800),randint(0,600)),width)

while True:
        for event in pygame.event.get():
                if event.type in (QUIT,KEYDOWN):
                        sys.exit()

        pygame.display.update()
