import sys
import pygame
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Ellipse")

while True:
        for event in pygame.event.get():
                if event.type in (QUIT,KEYDOWN):
                        sys.exit()

        screen.fill((0,255,0))

        color=255,0,255
        position=100,100,400,300
        width=8
        pygame.draw.ellipse(screen,color,position,width)

        pygame.display.update()