import pygame
from pygame import *

class Player():

    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.propulsion=10
        self.gravity=8

    def move(self,Sh):
        keys=pygame.key.get_pressed()
        if not keys[K_SPACE] and self.y<=Sh-self.h:
            self.y+=self.gravity
        elif keys[K_SPACE] and self.y>=0:
            self.y-=self.propulsion

    def show(self,win):
        pygame.draw.rect(win,(255,255,255),(self.x,self.y,self.w,self.h))
        pygame.display.update()
        win.fill((0,0,0))
                