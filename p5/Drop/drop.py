from random import random

import pygame
from pygame.math import Vector2

import core


class Drop:

    def __init__(self,largeur):
        self.gravity=random.ramdint(5,20)
        self.size=2
        self.r=random.ramdint(0,255)
        self.v=random.ramdint(0,255)
        self.b=random.ramdint(0,255)
        self.position=Vector2(largeur,0)

    def tomber(self,taillefenetre):
        self.position[1]=self.position[1]+self.gravity
        if self.position.y>taillefenetre:
            self.raz()

    def raz(self):
        self.position[1]=0

    def afficher(self):
        pygame.draw.line(core.screen, (self.r, self.v, self.b), (self.position.x, self.position.y), (self.position.x, self.position.y + self.size), 1)

