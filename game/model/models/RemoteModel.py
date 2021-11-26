from game.model.models.GameModel import GameModel
from game.network.Agent import *


class RemoteModel(GameModel):
    def __init__(self, controller):
        super().__init__(controller)
        self.HostTurn = True
        self.controller = controller

    # Joue le coup en fonction du mode de jeu
    def play(self, i, j):
        """ Return la grille après coup """
        color = self.grid.get(i, j)
        if self.grid.destroyable(i, j) and not self.HostTurn and self.player2.ownsColor(color):
            self.player2.addScore(self.grid.destroy(i, j))
            self.grid.gravity()
            self.player.removeColor(color)
            self.nextTurn()
            self.controller.notify({'state': REMOTE_MOVE, 'i': i, 'j': j})
            self.controller.showAll()
        return self.grid

    def enemyPlay(self, i, j):
        color = self.grid.get(i, j)
        #if self.grid.destroyable(i, j) and self.HostTurn and self.player.ownsColor(color):
        self.player.addScore(self.grid.destroy(i, j))
        self.player2.removeColor(color)
        self.grid.gravity()
        self.nextTurn()
        self.controller.showAll()
        return self.grid

    def toArray(self):
        arr = super().toArray()
        arr['hostTurn'] = self.HostTurn
        return arr

    def load(self, msg):
        super().load(msg)
        self.HostTurn = msg['hostTurn']

    def nextTurn(self):
        if self.HostTurn:
            if not self.player2.cantDestroyAnything(self.grid):
                self.HostTurn = not self.HostTurn
        else:
            if not self.player.cantDestroyAnything(self.grid):
                self.HostTurn = not self.HostTurn

    @property
    def us(self):
        return self.player2

    @property
    def enemy(self):
        return self.player

    @property
    def getStateString(self):
        return 'Votre adversaire est en train de jouer' if self.HostTurn else 'A vous de jouer'
