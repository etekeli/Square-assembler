from game.network.HostAgent import HostAgent
from game.network.SearchAgent import SearchAgent
from game.view.Dialog import *


class MultiDialog(Dialog):
	niveaux = {"Grille 10x10": 10, "Grille 20x20": 20}

	def __init__(self, parent):
		super().__init__(parent)
		parent.waitingDialog = self
		self.isServer = None
		self.resizable(False, False)

	def createButtons(self):
		"""Création des boutons pour la connexion et l'hébergement"""
		self.buttonWindow = Frame(self)
		Button(self.buttonWindow, text="Héberger", command=lambda: self.waiting(True)).pack(pady=5)
		Button(self.buttonWindow, text="Se connecter", command=lambda: self.waiting(False)).pack(pady=5)
		self.buttonWindow.pack()

	def waiting(self, isServer):
		"""Passage sur la fenêtre d'attente"""
		self.isServer = isServer
		self.buttonWindow.destroy()
		Label(self, text="En attente d'adversaire...").pack()

	def show(self):
		"""Lance l'affichage de la fenêtre"""
		self.deiconify()
		self.grab_set()
		self.buttonWindow.wait_window()
		return self.isServer
