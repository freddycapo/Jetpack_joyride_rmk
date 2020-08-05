import pygame
from pygame import *

from Player import Player

pygame.init()

width=1000
heigth=600
win=pygame.display.set_mode((width,heigth))
clock = pygame.time.Clock()

p=Player(100,300,75,75)

run=True
while run:
    clock.tick(50)

    p.move(heigth)
    p.show(win)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()