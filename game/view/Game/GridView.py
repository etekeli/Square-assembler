from game.view.TextureFactory import *
from tkinter import *


# Vue de la grille
class GridView:
	def __init__(self, canvas, grid, controller):
		self.grid = grid
		self.canvas = canvas
		self.case_width = int(self.canvas.winfo_width() / self.grid.size)
		self.case_height = int(self.canvas.winfo_height() / self.grid.size)
		self.controller = controller
		self.focus = None
		self.imageGrid = [[None for i in range(grid.size)] for j in range(grid.size)]

	def show(self):
		for i in range(self.grid.size):
			for j in range(self.grid.size):
				if not (self.grid.isEmpty(i, j)):
					image = getTextureFactory().getTexture(self.grid.get(i, j))
					if self.imageGrid[i][j] is None:
						self.createCase(i, j, image)
					else:
						self.canvas.itemconfigure(self.imageGrid[i][j], image=image)
				elif not self.imageGrid[i][j] is None:
					self.deleteCase(i, j)

	def setGrid(self, grid):
		self.grid = grid

	def createCase(self, i, j, image):
		y = int(self.case_width * i)
		x = int(self.case_height * j)
		self.imageGrid[i][j] = self.canvas.create_image(x, y, anchor=NW, image=image)
		self.bindFunctions(self.imageGrid[i][j])

	def deleteCase(self, i, j):
		self.unbindFunctions(self.imageGrid[i][j])
		self.canvas.delete(self.imageGrid[i][j])
		self.imageGrid[i][j] = None

	def unbindFunctions(self, id):
		self.canvas.tag_unbind(id, "<Enter>")
		self.canvas.tag_unbind(id, "<Leave>")
		self.canvas.tag_unbind(id, "<Button-1>")

	def bindFunctions(self, id):
		self.canvas.tag_bind(id, "<Enter>", self.on_case_enter)
		self.canvas.tag_bind(id, "<Leave>", self.on_case_leave)
		self.canvas.tag_bind(id, "<Button-1>", self.on_case_click)

	# Met en évidence la chaîne destructible (si il y en a)
	# quand la souris pointe sur la case, et pointe le focus sur cette case
	def on_case_enter(self, event):
		j = int(event.x / self.case_width)
		i = int(event.y / self.case_height)
		self.focus = (i, j)
		self.highlight(i, j)

	# Affiche la case en [i][j] et ses voisins de même valeur en "highlight"
	def highlight(self, i, j):
		if ((0 <= i and i < self.grid.size) and (0 <= j and j < self.grid.size)):
			if not self.imageGrid[i][j] is None:
				if (self.grid.destroyable(i, j) and not ('highlight' in self.canvas.gettags(self.imageGrid[i][j]))):
					image = getTextureFactory().getTextureHighlight(self.grid.get(i, j))
					self.canvas.itemconfigure(self.imageGrid[i][j], image=image)
					self.canvas.addtag_withtag("highlight", self.imageGrid[i][j])
					self.highlightNeighboors(i, j)

	# Affiche les voisins de même valeur que celle en [i][j] en "highlight"
	def highlightNeighboors(self, i, j):
		value = self.grid.get(i, j)
		if i < (self.grid.size - 1):
			if value == self.grid.get(i + 1, j):
				self.highlight(i + 1, j)
		if i > 0:
			if value == self.grid.get(i - 1, j):
				self.highlight(i - 1, j)
		if j < (self.grid.size - 1):
			if value == self.grid.get(i, j + 1):
				self.highlight(i, j + 1)
		if j > 0:
			if value == self.grid.get(i, j - 1):
				self.highlight(i, j - 1)

	# Annule le mise en évidence de la chaîne desctructible (si il y en a)
	# quand la souris pointe sur la case, et enlève le focus sur cette case
	def on_case_leave(self, event):
		if not self.focus is None:
			i = self.focus[0]
			j = self.focus[1]
			self.stopHighlight(i, j)
			self.focus = None

	# Affiche la case en [i][j] et ses voisins de même valeur en "basic"
	def stopHighlight(self, i, j):
		if (0 <= i < self.grid.size) & (0 <= j < self.grid.size):
			if not self.imageGrid[i][j] is None:
				if 'highlight' in self.canvas.gettags(self.imageGrid[i][j]):
					image = getTextureFactory().getTexture(self.grid.get(i, j))
					self.canvas.itemconfigure(self.imageGrid[i][j], image=image)
					self.canvas.dtag(self.imageGrid[i][j], 'highlight')
					self.stopHighlightNeighboors(i, j)

	# Affiche les voisins de même valeur que celle en [i][j] en "basic"
	def stopHighlightNeighboors(self, i, j):
		value = self.grid.get(i, j)
		if i < (self.grid.size - 1):
			if value == self.grid.get(i + 1, j):
				self.stopHighlight(i + 1, j)
		if i > 0:
			if value == self.grid.get(i - 1, j):
				self.stopHighlight(i - 1, j)
		if j < (self.grid.size - 1):
			if value == self.grid.get(i, j + 1):
				self.stopHighlight(i, j + 1)
		if j > 0:
			if value == self.grid.get(i, j - 1):
				self.stopHighlight(i, j - 1)

	def on_case_click(self, event):
		j = int(event.x / self.case_width)
		i = int(event.y / self.case_height)
		self.controller.play(i, j)
		self.focus = None

	def on_resize(self):
		self.case_width = int(self.canvas.winfo_width() / self.grid.size)
		self.case_height = int(self.canvas.winfo_height() / self.grid.size)

		getTextureFactory().scaleTextures(self.case_width, self.case_height)
		for i in range(self.grid.size):
			for j in range(self.grid.size):
				image = getTextureFactory().getTexture(self.grid.get(i, j))
				if not self.imageGrid[i][j] is None:
					self.deleteCase(i, j)
					self.createCase(i, j, image)
