import pygame
from pygame.math import Vector2, Vector3


class Player(object) :

    def __init__(self):
        self.taille=12
        self.vitesse=1000
        self.forme= "rond"
        self.position=Vector2()
        self.direction=Vector2()
        self.couleur=Vector3()

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self):
        pass

    def afficher(self):
        pygame.draw.circle()
