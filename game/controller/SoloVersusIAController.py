from game.controller.GameController import GameController
from game.model.models.SoloVersusIAModel import SoloVersusIAModel


class GameSoloVersusAI(GameController):
    def __init__(self, view):
        super().__init__(view, SoloVersusIAModel(self))

    def newGame(self, level):
        self.model.newGame(level)
        self.showAll()

    def supprimer(self):
        pass
