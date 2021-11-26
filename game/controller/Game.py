from time import sleep

from game.controller.HostController import HostController
from game.controller.RemoteController import RemoteController
from game.controller.SoloController import SoloController
from game.controller.SoloVersusIAController import GameSoloVersusAI
from game.view.Dialog import Dialog, NewGameVersusAIDialog
from game.view.Game.GameView import GameView
from game.view.Multiplayer.MultiDialog import MultiDialog


class Game:
    def __init__(self):
        self.controller = None
        self.view = GameView(self)
        self.view.show()

    def newGameDialog(self):
        lvl = Dialog(self.view).show()
        if lvl is not None:
            if self.controller is not None:
                self.controller.supprimer()
                self.controller = None
            self.controller = SoloController(self.view)
            self.controller.newSoloGame(lvl)

    def newGameVersusAIDialog(self):
        lvl = NewGameVersusAIDialog(self.view).show()
        if lvl is not None:
            if self.controller is not None:
                self.controller.supprimer()
                self.controller = None
            sleep(0.2)
            self.controller = GameSoloVersusAI(self.view)
            self.controller.newGame(lvl)

    def newMultiGameDialog(self):
        dialog = MultiDialog(self.view)
        isServer = dialog.show()
        if isServer is not None:
            if self.controller is not None:
                self.controller.supprimer()
                self.controller = None
            sleep(0.2)
            self.controller = (HostController(self.view) if isServer else RemoteController(self.view))
            self.controller.newGame(dialog)
