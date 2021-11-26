from game.model.Player.Player import *


class AIFirst(Player):
	def __init__(self):
		self.name = "IA"
		self.reset()

	def getDecision(self, grid):
		for i in range(grid.size):
			for j in range(grid.size):
				color = grid.get(i, j)
				if grid.destroyable(i, j) and self.ownsColor(color):
					return i, j

		return None