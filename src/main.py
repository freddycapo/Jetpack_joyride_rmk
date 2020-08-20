import pygame
from pygame import *

from Player import Player
from Coin import Coin
from Rocket import Rocket

pygame.init()

width=1000
heigth=600
win=pygame.display.set_mode((width,heigth))
clock = pygame.time.Clock()
bg = pygame.image.load("src/images/background.png")

p=Player(100,300,80,80)

n_coins=5
n_rockets=3
coins=[]
rockets=[]

for coin in range(0,n_coins):
    coins.append(Coin(width,heigth,35,35))

for rocket in range(0,n_rockets):
    rockets.append(Rocket(width,heigth,75,75))


def UpdateScreen():
    #win.fill((0,0,0))
    win.blit(pygame.transform.scale(bg,(width,heigth)),(0,0))
    p.show(win)
    for coin in coins:
        coin.show(win)
    for rocket in rockets:
        rocket.show(win)
    pygame.display.update()

run=True
while run:
    clock.tick(60)

    p.move(heigth)

    for coin in coins:
        coin.move(300)

    for rocket in rockets:
        rocket.move(1000)

    UpdateScreen()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()