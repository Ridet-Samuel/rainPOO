from TP2.bille import Bille
from TP2.creep import Creep
from TP2.player import Player
from p5 import core

player= None
bille= None
creep= []

def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    global player, creep
    player=Player()

    for i in range(0,1000):
        creep.append(Creep())

    print("Setup END---------")

def run():
    print("run")

    player.afficher(core)
    if core.getMouseLeftClick() is not None :
        player.deplacer(core.getMouseLeftClick())

    for c in creep:
        c.afficher(core)

if __name__ == '__main__' :
    core.main(setup,run)
