import random

import pygame
from pygame.math import Vector2


class Drop:

    def __init__(self,largeur):
        self.gravity=random.randint(5,20)
        self.size=random.randint(1,100)
        self.r=random.randint(0,255)
        self.v=random.randint(0,255)
        self.b=random.randint(0,255)
        self.position=Vector2(random.randint(0,1500),0)

    def tomber(self,taillefenetre):
        self.position[1]=self.position[1]+self.gravity
        if self.position.y>taillefenetre:
            self.raz()

    def raz(self):
        self.position[1]=0

    def afficher(self,core):
        pygame.draw.line(core.screen, (self.r, self.v, self.b), (self.position.x, self.position.y), (self.position.x, self.position.y + self.size), 1)

