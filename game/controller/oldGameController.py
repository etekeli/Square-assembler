from game.model.models.GameModel import GameModel
from game.model.Player.Player import Player
from game.view.Game.GameView import GameView


class GameController:
    def __init__(self):
        self.waitingDialog = None
        self.model = GameModel(self)
        self.view = GameView(self)
        self.player = Player("J1 - Local")

    def launch(self):
        self.view.show()

    def play(self, i, j):
        self.model.play(i, j)
        self.showAll()
        self.checkGameOver()

    def showAll(self):
        self.view.showGrid(self.model.grid)
        self.view.showGameState(self.model.player, self.model.player2)

    def checkGameOver(self):
        if self.model.GameOver():
            self.gameover = True
            self.view.gameCanvas.showGameOver()
