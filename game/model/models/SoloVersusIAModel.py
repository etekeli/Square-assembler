from game.model.Grid import Grid
from game.model.Player.AIFirst import AIFirst
from game.model.Player.Player import Player
import threading

from game.model.models.GameModel import GameModel


class SoloVersusIAModel(GameModel):
    def __init__(self, controller):
        super().__init__(controller)
        self.grid = Grid()
        self.player = Player("localPlayer")
        self.player2 = None
        self.AI = AIFirst()
        self.controller = controller

    def newGame(self, level):
        self._newGame(level)
        self.AI.reset()
        self.player2 = self.AI
        self.player.turn = True
        self.player.initColors(level)
        self.AI.initColors(level)
        self.__startAI__()

    # Joue le coup en fonction du mode de jeu
    def play(self, i, j):
        """
        Return la grille après coup
        """
        color = self.grid.get(i, j)
        if self.grid.destroyable(i, j) and self.player.ownsColor(color):
            self.player.addScore(self.grid.destroy(i, j))
            self.grid.gravity()
            self.player.turn = False
            self.AI.removeColor(color)
            self.controller.showAll()
            self.controller.checkGameOver()

    # Lance l'AI
    def __startAI__(self):
        self.thread = threading.Timer(3.0, self.__startAI__)
        self.thread.start()
        self.__AIsPlay__()

    # Joue le coup de l'AI en mode versus AI
    def __AIsPlay__(self):
        if not self.player.turn or self.player.cantDestroyAnything(self.grid):
            decision = self.AI.getDecision(self.grid)
            if decision is not None:
                color = self.grid.get(decision[0], decision[1])
                self.AI.addScore(self.grid.destroy(decision[0], decision[1]))
                self.grid.gravity()
                self.player.removeColor(color)
                self.controller.showAll()
            self.player.turn = True

    def stop(self):
        self.thread.cancel()
        self.thread.cancel()
