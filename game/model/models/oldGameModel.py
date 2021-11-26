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
		self.gameMode = ""
		self.controller = controller

	def _newGame(self, size):
		self.grid.generateGrid(size)
		self.player.reset()
		self.player2 = None
		self.gameMode = ""

	def newSoloGame(self, size):
		self._newGame(size)
		self.gameMode = "Solo"

	def newGameVersusAI(self, level):
		self._newGame(level)
		self.gameMode = "AI"
		self.AI.reset()
		self.player2 = self.AI
		self.player.turn = True
		self.player.initColors(level)
		self.AI.initColors(level)
		self.__startAI__()

	def newGameMulti(self, level, player2):
		self._newGame(level)
		self.gameMode = "Multi"
		self.player2 = Player(player2)
		self.player.turn = True
		self.player.initColors(level)
		self.player2.initColors(level)

	def GameOver(self):
		return self.grid.GameOver()

	# Joue le coup en fonction du mode de jeu
	def play(self, i, j):
		""" Return la grille après coup """
		if self.gameMode == "Solo":
			self.__playersSoloPlay__(i, j)  # On joue notre coup solo
		elif self.gameMode == "AI" and self.player.turn:
			self.__playersAIPlay__(i, j)  # On joue notre coup en mode multi/AI
		# self.__AIsPlay__()			#Cn laisse l'IA jouer son coup si on est en mode AI
		elif self.gameMode == "MultiHost" and self.player.turn:
			self.__HostMultiPlay__(i, j)  # On joue notre coup en mode multi/AI
		elif self.gameMode == "MultiRemote" and self.player2.turn:
			self.__RemoteMultiPlay__(i, j)  # Cn laisse l'adversaire jouer son coup si on est en mode multi

		return self.grid

	# Joue le coup du joueur en mode solo
	def __playersSoloPlay__(self, i, j):
		if self.grid.destroyable(i, j):
			self.player.addScore(self.grid.destroy(i, j))
			self.grid.gravity()
			self.player.turn = False
			self.controller.showAll()

	def __playersAIPlay__(self, i, j):
		""" Joue le coup du joueur en mode versus AI"""
		# Si la case est détruisable et la couleur de la case fait partie des couleurs du joueur
		color = self.grid.get(i, j)
		if self.grid.destroyable(i, j) and self.player.ownsColor(color):
			self.player.addScore(self.grid.destroy(i, j))
			self.grid.gravity()
			self.player.turn = False
			self.AI.removeColor(color)
			self.controller.showAll()
			self.controller.checkGameOver()

	# Lance l'AI
	def __startAI__(self):
		threading.Timer(3.0, self.__startAI__).start()
		self.__AIsPlay__()

	# Joue le coup de l'AI en mode versus AI
	def __AIsPlay__(self):
		if not self.player.turn or self.player.cantDestroyAnything(self.grid):
			decision = self.AI.getDecision(self.grid)
			if not decision is None:
				color = self.grid.get(decision[0], decision[1])
				self.AI.addScore(self.grid.destroy(decision[0], decision[1]))
				self.grid.gravity()
				self.player.removeColor(color)
				self.controller.showAll()
			self.player.turn = True

	# Joue le coup du joueur en mode multi
	def __HostMultiPlay__(self, i, j):
		if self.grid.destroyable(i, j) and self.player.turn:
			self.player.addScore(self.grid.destroy(i, j))
			self.grid.gravity()
			self.player.turn = not self.player.turn
			self.controller.showAll()
			self.controller.notify({'state': (HOST_MOVE if self.gameMode == 'MultiHost' else REMOTE_MOVE), 'i': i, 'j': j})

	# Joue le coup de l'adversaire en mode multi
	def __RemoteMultiPlay__(self, i, j):
		if self.grid.destroyable(i, j) and self.player2.turn:
			self.player2.addScore(self.grid.destroy(i, j))
			self.grid.gravity()
			self.nextTurn()
			self.controller.showAll()
			self.controller.notify({'state': (HOST_MOVE if self.gameMode == 'MultiHost' else REMOTE_MOVE), 'i': i, 'j': j})

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
			'game_mode': self.gameMode,
			'grid': self.grid.toArray(),
			'player1': self.player.toArray(),
			'player2': self.player2.toArray(),
		}

	def load(self, params):
		if params['state'] == 'game_state':
			self.grid.load(params['grid'])
			self.gameMode = params['game_mode']
			self.player1 = Player.load(params['player1'])
			self.player2 = Player.load(params['player2'])



"""def play(self, i, j):
		if((self.gameMode == "Multi" or self.gameMode == "AI") and self.player.turn) or self.gameMode == "Solo":
			#On joue notre coup
			self.__playersPlay__(i,j)
			self.controller.showAll()

			#Cn laisse l'adversaire jouer son coup si on est en mode multi/AI
			if self.gameMode == "AI":
				self.__AIsPlay__()
			elif self.gameMode == "Multi":
				self.__opponentsPlay__()
			self.controller.showAll()

		return self.grid"""