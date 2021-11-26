from game.view.Dialog import *
from game.view.Multiplayer.oldMultiDialog import MultiDialog


class TopMenu(Menu):
	def __init__(self, root, game):
		super().__init__(root)
		self.game = game
		self.root = root
		self.root.config(menu=self)

		# menu Jeu
		self.menuJeu = Menu(self.root, tearoff=0)
		self.add_cascade(label="Jeu", menu=self.menuJeu)
		self.menuJeu.add_command(label="Nouveau", command=self.game.newGameDialog)
		self.menuJeu.add_separator()
		self.menuJeu.add_command(label="Versus AI", command=self.game.newGameVersusAIDialog)
		self.menuJeu.add_separator()
		self.menuJeu.add_command(label="Multi", command=self.game.newMultiGameDialog)
		self.menuJeu.add_separator()
		self.menuJeu.add_command(label="Quitter", command=self.root.quit)

		# menu A propos
		self.menuAPropos = Menu(self.root, tearoff=0)
		self.add_cascade(label="A propos de...", menu=self.menuAPropos)
		self.menuAPropos.add_command(label="20720010 - 20720002")

