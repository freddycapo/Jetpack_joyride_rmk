import pygame
import random

from Item import Item

class Rocket(Item):

    def __init__(self,s_w,s_h,w,h):
        super().__init__(s_w,s_h,w,h)
        self.vel=8
        self.image=pygame.image.load("src\images\Rocket.png")
    
        