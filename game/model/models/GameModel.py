from pprint import pprint

from game.model.Grid import Grid
from game.model.Player.AIFirst import AIFirst
from game.model.Player.Player import Player
import threading
from game.network.Agent import *


class GameModel:
	def __init__(self, controller):
		self.grid = Grid()
		self.player = Player("localPlayer")
		self.player2 = None
		self.AI = AIFirst()
		self.controller = controller
		self.gameOverForced = False

	def _newGame(self, size):
		self.grid.generateGrid(size)
		self.player.reset()
		self.player2 = None

	def GameOver(self):
		if self.gameOverForced is True:
			return True
		return self.grid.GameOver()

	def play(self, i, j):
		"""
		Joue le coup en fonction du mode de jeu
		Return la grille après coup
		"""
		pass

	def nextTurn(self):
		self.player2.turn = not self.player.turn
		self.player.turn = not self.player2.turn

	@property
	def turn(self):
		return self._turn

	@turn.setter
	def turn(self, arg):
		self._turn = arg

	def toArray(self):
		"""
		@see grid.toArray()
		@see Player.toArray()
		Return:
			Modèle de jeu sous forme de tableau :
			{'state': 'game_state'
			'game_mode': jeu.mode
			'grid':
				{
				'size': grille.size,
				'number_of_color': grille.numberOfColors,
				'grid': grille.grid,
				}
			'player1':
				{
					'name': joueur.name,
					'score': joueur.score
					'Turn': joueur.turn
					'colors': joueur.colors
				}

			'player2':
				{
					'name': joueur.name,
					'score': joueur.score
					'Turn': joueur.turn
					'colors': joueur.colors
				}
			}
		"""
		return {
			'state': 'game_state',
			'grid': self.grid.toArray(),
			'player1': self.player.toArray(),
			'player2': self.player2.toArray(),
		}

	def load(self, params):
		if params['state'] == 'game_state':
			self.grid.load(params['grid'])
			self.player = Player.load(params['player1'])
			self.player2 = Player.load(params['player2'])

	@property
	def us(self):
		return self.player

	@property
	def enemy(self):
		return self.player2

	@property
	def getStateString(self):
		return ''
