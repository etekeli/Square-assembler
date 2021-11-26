import random

from game.model.Observer import *


def switchColor(size):
    switcher = {
        10: 4,
        20: 8
    }
    return switcher.get(size)


VIDE = -1  # Une case vide prend la valeur -1
SCORE_MULTIPLICATOR = 2  # Pour calculer le score en fonction de la chaîne


class Grid(Subject):
    def __init__(self):
        self.numberOfColors = 0

    def generateGrid0(self, size):
        self.size = size
        self.numberOfColors = switchColor(size)
        self.grid = [0 for i in range(size * size)]
        for i in range(size * size):
            self.grid[i] = 0

    def generateGrid(self, size):
        self.grid = [0 for i in range(size * size)]
        self.size = size
        self.numberOfColors = switchColor(size)
        if size > 2:
            maxColor = ((size * size) / self.numberOfColors)
            countColors = [0] * self.numberOfColors

            for i in range(size * size):
                tmp = random.randint(0, self.numberOfColors - 1)
                while countColors[tmp] > maxColor:
                    tmp = random.randint(0, self.numberOfColors - 1)
                self.grid[i] = tmp
                countColors[tmp] += 1

    # Retourne la valeur en [i][j]
    def get(self, i, j):
        return self.grid[self.size * i + j]

    # Assigne la valeur val à [i][j]
    def set(self, i, j, val):
        self.grid[self.size * i + j] = val

    # Retourne la taille de la grille
    def getSize(self):
        return self.size

    # Retourne vrai si la case en [i][j] est destructible,
    # Une case est destructible si il y a au moins
    # une autre case adjacente de même valeur
    def destroyable(self, i, j):
        value = self.get(i, j)
        if value != VIDE:
            if i < (self.size - 1):
                if value == self.get(i + 1, j):
                    return True
            if i != 0:
                if value == self.get(i - 1, j):
                    return True
            if j < (self.size - 1):
                if value == self.get(i, j + 1):
                    return True
            if j != 0:
                if value == self.get(i, j - 1):
                    return True

        return False

    # Détruit récursivement la case [i][j] et les
    # cases adjacentes de même valeur
    # Retourne un score
    def destroy(self, i, j):
        score = 1
        value = self.get(i, j)
        if value != VIDE:
            self.set(i, j, VIDE)
            if i < (self.size - 1):
                if value == self.get(i + 1, j):
                    score += SCORE_MULTIPLICATOR * self.destroy(i + 1, j)
            if i != 0:
                if value == self.get(i - 1, j):
                    score += SCORE_MULTIPLICATOR * self.destroy(i - 1, j)
            if j < (self.size - 1):
                if value == self.get(i, j + 1):
                    score += SCORE_MULTIPLICATOR * self.destroy(i, j + 1)
            if j != 0:
                if value == self.get(i, j - 1):
                    score += SCORE_MULTIPLICATOR * self.destroy(i, j - 1)

        return score

    # Retourne vrai si la case en [i][j] est vide
    def isEmpty(self, i, j):
        return self.get(i, j) == VIDE

    # Fait tomber les cases vers le bas
    # Et décale les cases vers la gauche
    def gravity(self):
        # On fait tomber les cases
        for j in range(self.size):
            for i in reversed(range(self.size)):
                if self.isEmpty(i, j):
                    n = i
                    while self.isEmpty(n, j) and n > 0:
                        n -= 1
                    self.swap(i, j, n, j)

        # On décale les cases à gauche
        for j in range(self.size - 1):
            if self.isEmpty(self.size - 1, j):
                n = j
                while self.isEmpty(self.size - 1, n) and n < self.size - 1:
                    n += 1

                for i in range(self.size):
                    self.swap(i, j, i, n)

    # Swap les cases [i1][j1] et [i2][j2]
    def swap(self, i1, j1, i2, j2):
        temp = self.get(i1, j1)
        self.set(i1, j1, self.get(i2, j2))
        self.set(i2, j2, temp)

    # Retourne vrai si fin de jeu
    # Fin de jeu si plus aucune case destructible
    def GameOver(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.destroyable(i, j):
                    return False

        return True

    # Retourne le tableau avec toutes les couleurs
    def getAllColorsList():
        colors = []
        for i in range(0, 8):
            colors.append(i)
        return colors

    # Retourne le tableau avec toutes les couleurs du niveau
    def getLevelColorsList(level):
        colors = []
        for i in range(0, switchColor(level)):
            colors.append(i)
        return colors

    def toString(self):
        string = ""
        for i in range(self.size):
            string = string + "["
            for j in range(self.size):
                string = string + str(self.get(i, j)) + ","
            string = string + "]\n"
        return string

    def toArray(self):
        """
        Return:
            Grille sous forme de tableau:
            {
            'size': grille.size,
            'number_of_color': grille.numberOfColors,
            'grid': grille.grid,
            }
        """
        return {
                'size': self.size,
                'number_of_color': self.numberOfColors,
                'grid': self.grid,
            }

    def load(self, array):
        self.size = array['size']
        self.numberOfColors = array['number_of_color']
        self.grid = array['grid']