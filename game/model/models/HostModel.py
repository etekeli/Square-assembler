from game.model.models.GameModel import GameModel
from game.model.Player.Player import Player
from game.network.Agent import *


class HostModel(GameModel):
    def __init__(self, controller):
        super().__init__(controller)
        self.HostTurn = True

    def newGame(self, level, player2):
        self._newGame(level)
        self.player2 = Player(player2)
        self.player.initColors(level)
        self.player2.initColors(level)

    # Joue le coup en fonction du mode de jeu
    def play(self, i, j):
        """ Return la grille après coup """
        color = self.grid.get(i, j)
        if self.grid.destroyable(i, j) and self.HostTurn and self.player.ownsColor(color):
            self.player.addScore(self.grid.destroy(i, j))
            self.player2.removeColor(color)
            self.grid.gravity()
            self.nextTurn()
            self.controller.notify({'state': HOST_MOVE, 'i': i, 'j': j})
            self.controller.showAll()

    def enemyPlay(self, i, j):
        color = self.grid.get(i, j)
        #if self.grid.destroyable(i, j) and not self.HostTurn and self.player2.ownsColor(color):
        self.player2.addScore(self.grid.destroy(i, j))
        self.player.removeColor(color)
        self.grid.gravity()
        self.nextTurn()
        self.controller.showAll()
        # self.controller.notify({'state': HOST_MOVE, 'i': i, 'j': j})
        return self.grid

    def toArray(self):
        arr = super().toArray()
        arr['hostTurn'] = self.HostTurn
        return arr

    def nextTurn(self):
        if self.HostTurn:
            if not self.player2.cantDestroyAnything(self.grid):
                self.HostTurn = not self.HostTurn
        else:
            if not self.player.cantDestroyAnything(self.grid):
                self.HostTurn = not self.HostTurn

    @property
    def us(self):
        return self.player

    @property
    def enemy(self):
        return self.player2

    @property
    def getStateString(self):
        return 'Votre adversaire est en train de jouer' if not self.HostTurn else 'A vous de jouer'
