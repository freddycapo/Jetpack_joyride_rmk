import pygame
from pygame import *

from Player import Player

pygame.init()

width=1000
heigth=600
win=pygame.display.set_mode((width,heigth))
clock = pygame.time.Clock()
bg = pygame.image.load("src/images/background.png")

p=Player(100,300,75,75)

def UpdateScreen():
    win.blit(pygame.transform.scale(bg,(width,heigth)),(0,0))
    p.show(win)
    pygame.display.update()

run=True
while run:
    clock.tick(50)

    p.move(heigth)

    UpdateScreen()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()