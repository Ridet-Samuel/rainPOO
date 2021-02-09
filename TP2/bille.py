from pygame.math import Vector2, Vector3


class Bille(object) :

    def __init__(self):
        self.vitesse=1000
        self.taille=6
        self.position=Vector2()
        self.direction=Vector2()
        self.couleur=Vector3()

    def suivre(self):
        pass

    def manger(self):
        pass

    def mourir(self):
        pass

    def afficher(self):
        pass
pass


