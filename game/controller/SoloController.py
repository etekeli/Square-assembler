from game.controller.GameController import GameController
from game.model.models.SoloModel import SoloModel
from game.view.Game.GameCanvas import GameCanvas


class SoloController(GameController):
    def __init__(self, view):
        super().__init__(view, SoloModel(self))

    def newSoloGame(self, level):
        self.model.newGame(level)
        self.showAll()

    def supprimer(self):
        pass
