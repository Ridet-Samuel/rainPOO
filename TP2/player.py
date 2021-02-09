import pygame
from pygame.math import Vector2, Vector3


class Player(object) :

    def __init__(self):
        self.taille=35
        self.vitesse=1000
        self.forme= "rond"
        self.position=Vector2(200,200)
        self.direction=Vector2()
        self.couleur=Vector3(255,255,0)

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self,position):
        self.position.x=position[0]
        self.position.y=position[1]

    def afficher(self,core):
        if self.forme == "rond" :
            pygame.draw.circle(core.screen,(int(self.couleur.x),int(self.couleur.y),int(self.couleur.z)), (int(self.position.x),int(self.position.y)),self.taille)
