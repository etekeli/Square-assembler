from game.model.Grid import Grid
from game.model.Player.AIFirst import AIFirst
from game.model.Player.Player import Player
import threading

from game.model.models.GameModel import GameModel
from game.network.Agent import *


class SoloModel(GameModel):
    def __init__(self, controller):
        super().__init__(controller)
        self.grid = Grid()
        self.player = Player("localPlayer")
        self.player2 = None
        self.controller = controller

    def newGame(self, size):
        self._newGame(size)

    def play(self, i, j):
        """
        Joue le coup en fonction du mode de jeu
        Return la grille après coup
        """
        if self.grid.destroyable(i, j):
            self.player.addScore(self.grid.destroy(i, j))
            self.grid.gravity()
            self.controller.showAll()
        return self.grid
