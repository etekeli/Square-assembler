from game.model.Grid import *


class Player:
    def __init__(self, name):
        self._name = name
        self.reset()

    @staticmethod
    def load(player):
        p = Player(player['name'])
        p.score = player['score']
        p.turn = player['Turn']
        p.colors = player['colors']
        return p
        #p.initColors()

    def cantDestroyAnything(self, grid):
        for i in range(grid.size):
            for j in range(grid.size):
                if self.ownsColor(grid.get(i, j)) and grid.destroyable(i, j):
                    return False

        return True

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, turn):
        self._turn = turn

    def removeColor(self, color):
        if self.colors.count(color) > 0:
            self.colors.remove(color)

    def ownsColor(self, color):
        return self.colors.count(color) > 0

    def initColors(self, level):
        self.colors = Grid.getLevelColorsList(level)

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, colors):
        self._colors = colors

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def addScore(self, toAdd):
        self._score += toAdd

    def reset(self):
        self._score = 0
        self._turn = True
        self._colors = Grid.getAllColorsList()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def toArray(self):
        """
        {
            'name': joueur.name,

            'score': joueur.score

            'Turn': joueur.turn

            'colors': joueur.colors
        }

        Return:
        un joueur sous forme de tableaux

        """
        return {
            'name': self._name,
            'score': self._score,
            'Turn': self._turn,
            'colors': self._colors
        }

