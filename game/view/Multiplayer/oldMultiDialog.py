from tkinter import *
from game.view.Dialog import *


class MultiDialog(Dialog):
	niveaux = {"Grille 10x10": 10, "Grille 20x20": 20}

	def __init__(self, parent, controller):
		Dialog.__init__(self, parent, controller)

	def init(self):
		self.protocol("WM_DELETE_WINDOW", self.on_closing)

	# Crée les champs pour entrer les IP
	def createButtons(self):
		b1 = Button(self, text="Héberger", command=self.host).pack(pady=5)
		b2 = Button(self, text="Se connecter", command=self.connect).pack(pady=5)

	def on_closing(self):
		self.grab_release()
		self.controller.stop()
		self.destroy()

	def host(self, event=None):
		self.clear()
		Label(self, text="En attente d'adversaire...").pack()
		self.controller.newGameMulti(self, True)

	def connect(self, event=None):
		self.clear()
		Label(self, text="Connection ...").pack()
		self.controller.newGameMulti(self, False)

