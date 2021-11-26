
from game.model.Player.Player import Player


class GameController:
    def __init__(self, view, model=None):
        self.waitingDialog = None
        self.network = None
        self.model = model
        self.view = view
        self.view.controller = self
        self.player = Player("J1 - Local")

    def launch(self):
        self.view.show()

    def play(self, i, j):
        self.model.play(i, j)
        self.checkGameOver()

    def showAll(self):
        self.view.showGrid(self.model.grid)
        self.view.showGameState(self.model)

    def forceGameOver(self):
        self.model.forceGameOver = True
        self.gameover = True
        self.view.gameCanvas.showGameOver()

    def checkGameOver(self):
        if self.model.GameOver():
            self.gameover = True
            self.view.gameCanvas.showGameOver()
