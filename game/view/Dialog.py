from tkinter import *


class Dialog(Toplevel):
	niveaux = {"Grille 10x10": 10, "Grille 20x20": 20}

	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.level = IntVar()
		self.createButtons()
		self.center()
		self.init()
		self.protocol("WM_DELETE_WINDOW", self.close)

	def init(self):
		pass

	def close(self):
		self.level = None
		self.destroy()

	def clear(self):
		for widget in self.winfo_children():
			widget.pack_forget()

	# Action effectuée quand on clique sur le bouton "Commencer"
	# Demande une nouvelle partie au controller et se détruit
	def on_confirm(self, event=None):
		self.grab_release()
		self.destroy()

	# Centre la fenêtre de dialogue
	def center(self):
		self.update()
		windowX = self.parent.winfo_x()
		windowY = self.parent.winfo_y()
		windowCenterX = self.parent.winfo_width() / 2
		windowCenterY = self.parent.winfo_height() / 2
		selfCenterX = self.winfo_width() / 2
		selfCenterY = self.winfo_height() / 2
		self.geometry("+%d+%d" % (windowX + windowCenterX - selfCenterX, windowY + windowCenterY - selfCenterY))

	# Affiche la fenêtre de dialogue
	def show(self):
		self.deiconify()
		self.grab_set()
		self.wait_window()
		return None if self.level is None else self.level.get()

	def createButtons(self):
		"""Crée les boutons de la fenêtre de dialogue"""
		Label(self, text="Choisissez la taille de la grille").pack()

		self.level.set("10")
		for (text, value) in self.niveaux.items():
			Radiobutton(self, text=text, variable=self.level, value=value).pack(side=TOP, ipady=5)

		Button(self, text="Commencer", command=self.on_confirm).pack(pady=5)


class NewGameVersusAIDialog(Dialog):

	def __init__(self, parent):
		super().__init__(parent)

	def on_confirm(self, event=None):
		"""
		Action effectuée quand on clique sur le bouton "Commencer"
		Demande une nouvelle partie au controller et se détruit"""
		self.grab_release()
		self.destroy()
		return self.level.get()