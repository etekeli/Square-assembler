import sys
import tkinter

from game.view.Game.GameCanvas import GameCanvas
from game.view.TopMenu import TopMenu
from game.view.Game.GameStateView import GameStateView


class GameView(tkinter.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pack_propagate(False)
        TopMenu(self, self.game)
        self.bind('<Configure>', self.on_resize)
        self.gameCanvas = GameCanvas(self)
        #self.gameCanvas = GameCanvas(self, self.game)
        self.gameState = GameStateView(self)
        self.__controller = None

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, val):
        self.__controller = val
        self.gameCanvas.controller = val

    def show(self):
        self.title("Jeu Python - PILS 2021")
        self.minsize(1000, 750)
        self.geometry("1000x750")
        self.mainloop()

    def showGrid(self, grid):
        self.gameCanvas.delete("all")
        self.gameCanvas.showGrid(grid)

    def showGameState(self, model):
        self.gameState.show(model)

    def reset(self):
        if self.gameCanvas.gameOverView is not None:
            del self.gameCanvas.gameOverView
            self.gameCanvas.gameOverView = None

    # Redimensionne ses fils quand la
    # fenêtre est redimensionnée
    def on_resize(self, event):
        #	---------------
        # |					|	Sc|
        # |	Grile		|	o |
        #	|					|	re|
        #	---------------
        # On veut afficher la grille en carré.
        # La barre d'état de jeu doit être affichée
        # à droite de la grille et doir avoir comme
        # largeur 1 quart de la taille d'un côté de
        # la grille

        smallest_border = min(self.winfo_width(), self.winfo_height())
        game_state_width = int(smallest_border / 4)

        if self.winfo_width() >= smallest_border + game_state_width:
            grid_len = smallest_border
        else:
            grid_len = smallest_border - game_state_width

        if self.gameCanvas is not None:
            self.gameCanvas.config(width=grid_len, height=grid_len)
            self.gameCanvas.on_resize()

        if self.gameState is not None:
            self.gameState.config(width=game_state_width, height=grid_len)
            self.gameState.on_resize()
