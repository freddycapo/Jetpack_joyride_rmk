import pygame
import random
from pygame import *

from Item import Item

class Coin(Item):

    def __init__(self,s_w,s_h,w,h):
        super().__init__(s_w,s_h,w,h)
        self.vel=6
        self.image=pygame.image.load("src\images\Coin.png")

    def move(self):
        if self.x>= -self.w:
            self.x-=self.vel
        else:
            self.x=random.randint(self.s_w,self.s_w+300)
            self.y=random.randint(0,self.s_h-self.h)
    
    def show(self,window):
        window.blit(pygame.transform.scale(self.image,(self.w,self.h)),(self.x,self.y))

