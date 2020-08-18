import pygame
import random
from pygame import *

class Item():

    def __init__(self,s_w,s_h,w,h):
        self.s_w=s_w
        self.s_h=s_h
        self.x=random.randint(s_w,s_w+200)
        self.y=random.randint(0,s_h-h)
        self.w=w
        self.h=h

    