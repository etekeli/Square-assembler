from tkinter import *
import sys


class GameStateView(Canvas):
    """Canvas contenant la barre d'état (scores, temps...)"""

    def __init__(self, root):
        sys.setrecursionlimit(10000)
        super().__init__()
        self.pack(side=RIGHT, expand=True)
        self.configure(bg='aquamarine')
        self.root = root
        self.scoreText1 = None
        self.scoreText2 = None
        self.player1 = None
        self.player2 = None
        self.score1 = ""
        self.score2 = "enemy score"
        self.timer1 = ""
        self.timer2 = ""
        self.timerText1 = None
        self.timerText2 = None
        self.stateText = None

    # self.top = Canvas(self, bg='green').grid()
    # self.bottom = Canvas(self, bg='red').grid()

    # Affiche le canevas
    def show(self, model):
        self.state = model.getStateString
        self.player1 = model.player
        self.score1 = f'Votre score :\n {str(model.us.score)}'
        if model.player2 is not None:
            self.score2 = "Score de l'adversaire :\n " + str(model.enemy.score)
            self.player2 = model.enemy
        self.writeScore()

    def writeScore(self):
        """Dessine le score"""
        x = int(self.winfo_width() / 2)

        y = int(2 * self.winfo_height() / 10)
        if self.scoreText1 is not None:
            self.delete(self.scoreText1)
        self.scoreText1 = self.create_text(x, y, fill="black", font="Times 11 bold", text=self.score1)

        yTimer1 = int(3 * self.winfo_height() / 10)
        if self.timerText1 is not None:
            self.delete(self.timerText1)
        self.timerText1 = self.create_text(x, yTimer1, fill="black", font="Times 11 bold", text=self.timer1)

        y2 = int(5 * self.winfo_height() / 10)
        if self.player2 is not None:
            if self.scoreText2 is not None:
                self.delete(self.scoreText2)
            self.scoreText2 = self.create_text(x, y2, fill="black", font="Times 11 bold", text=self.score2)

        yTimer2 = int(6 * self.winfo_height() / 10)
        if self.timerText2 is not None:
            self.delete(self.timerText2)
        self.timerText2 = self.create_text(x, yTimer2, fill="black", font="Times 11 bold", text=self.timer2)

        yState = int(8 * self.winfo_height() / 10)
        if self.player2 is not None:
            if self.stateText is not None:
                self.delete(self.stateText)
            self.stateText = self.create_text(x, yState, fill="black", font="Times 11 bold", text=self.state)

    # Redessine le score quand la fenêtre
    # est redimensionnée
    def on_resize(self):
        self.writeScore()
