import pygame
import random

from Item import Item

class Rocket(Item):

    def __init__(self,s_w,s_h,w,h):
        super().__init__(s_w,s_h,w,h)
        self.vel=8
        self.image=pygame.image.load("src\images\Rocket.png")

    def move(self):
        if self.x>= -self.w:
            self.x-=self.vel
        else:
            self.x=random.randint(self.s_w+200,self.s_w+1000)
            self.y=random.randint(0,self.s_h-self.h)
    
    def show(self,window):
        window.blit(pygame.transform.scale(self.image,(self.w,self.h)),(self.x,self.y))
        