import random

import pygame
from pygame.math import Vector2, Vector3


class Creep(object) :

    def __init__(self):
        self.taille=3
        self.position=Vector2(random.randint(0,400),random.randint(0,400))
        self.couleur=Vector3(255,0,0)

    def mourir(self):
        pass

    def afficher(self,core):
        pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)),(int(self.position.x), int(self.position.y)), self.taille)
