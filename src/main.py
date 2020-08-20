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

start_pos_player=(100,300)
player_width=player_heigth=80

p=Player(start_pos_player[0],start_pos_player[1],player_width,player_heigth)

n_coins=5
n_rockets=3
coins=[]
rockets=[]

coin_width=coin_heigth=35
coin_dist=300

for coin in range(0,n_coins):
    coins.append(Coin(width,heigth,coin_width,coin_heigth))

rocket_width=rocket_heigth=75
rocket_dist=1000

for rocket in range(0,n_rockets):
    rockets.append(Rocket(width,heigth,rocket_width,rocket_heigth))

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
        coin.move(coin_dist)

    for rocket in rockets:
        rocket.move(rocket_dist)

    UpdateScreen()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()