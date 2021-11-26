from tkinter import *
from .GameOverView import GameOverView
from game.view.Game.GridView import GridView
import sys


# Canvas contenant la grille
class GameCanvas(Canvas):
    def __init__(self, root):
        self.gameOverView = None
        sys.setrecursionlimit(10000)
        super().__init__(root, highlightthickness=0, borderwidth=0, relief=FLAT, highlightbackground="black")
        self.pack(side=LEFT, expand=True)
        self.configure(bg='snow')
        self.controller = None
        self.grid = None
        self.gridView = None

    # Affiche le canevas et la grille passée en paramètre
    def showGrid(self, grid):
        self.grid = grid
        self.gridView = GridView(self, self.grid, self.controller)
        self.gridView.show()

    # Affiche l'écran de fin
    def showGameOver(self):
        self.gameOverView = GameOverView(self)

    # Recalcule la taille des cases
    # quand le fenêtre est redimensionnée
    def on_resize(self):
        if not self.grid is None:
            self.gridView.on_resize()
        if self.gameOverView is not None:
            self.gameOverView.on_resize()
