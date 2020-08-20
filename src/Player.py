import pygame
from pygame import *

class Player():

    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.propulsion=1
        self.gravity=1
        self.image=pygame.image.load("src\images\Player.png")

    def move(self,Sh):
        keys=pygame.key.get_pressed()
        if not keys[K_SPACE] and self.y<=Sh-self.h:
            self.propulsion=1
            if self.gravity<8:
                self.gravity+=0.5
            self.y+=self.gravity
        elif keys[K_SPACE] and self.y>=0:
            self.gravity=1
            if self.propulsion<10:
                self.propulsion+=0.5
            self.y-=self.propulsion

    def show(self,win):
        win.blit(pygame.transform.scale(self.image,(self.w,self.h)),(self.x,self.y))