from tkinter import PhotoImage, Image
import math


def getTextureFactory():
	if TextureFactory.INSTANCE is None:
		TextureFactory.INSTANCE = TextureFactory()

	return TextureFactory.INSTANCE


class TextureFactory:
	INSTANCE = None

	def __init__(self):
		# images originales
		self.rawBlue = {"basic": PhotoImage(file='assets/blue.png'), "highlight": PhotoImage(file='assets/blue_highlight.png')}
		self.rawRed = {"basic": PhotoImage(file='assets/red.png'), "highlight": PhotoImage(file='assets/red_highlight.png')}
		self.rawGreen = {"basic": PhotoImage(file='assets/green.png'), "highlight": PhotoImage(file='assets/green_highlight.png')}
		self.rawYellow = {"basic": PhotoImage(file='assets/yellow.png'), "highlight": PhotoImage(file='assets/yellow_highlight.png')}
		self.rawTurquoise = {"basic": PhotoImage(file='assets/turquoise.png'), "highlight": PhotoImage(file='assets/turquoise_highlight.png')}
		self.rawSlategray = {"basic": PhotoImage(file='assets/slategrey.png'), "highlight": PhotoImage(file='assets/slategrey_highlight.png')}
		self.rawPurple = {"basic": PhotoImage(file='assets/purple.png'), "highlight": PhotoImage(file='assets/purple_highlight.png')}
		self.rawOrange = {"basic": PhotoImage(file='assets/orange.png'), "highlight": PhotoImage(file='assets/orange_highlight.png')}

		# images mises à l'échelle
		# elles sont à l'échelle originale par défaut
		self.blue = self.rawBlue.copy()
		self.red = self.rawRed.copy()
		self.green = self.rawGreen.copy()
		self.yellow = self.rawYellow.copy()
		self.turquoise = self.rawTurquoise.copy()
		self.slategray = self.rawSlategray.copy()
		self.purple = self.rawPurple.copy()
		self.orange = self.rawOrange.copy()

		self.rawTextures = list()
		self.rawTextures.append(self.rawBlue)
		self.rawTextures.append(self.rawRed)
		self.rawTextures.append(self.rawGreen)
		self.rawTextures.append(self.rawYellow)
		self.rawTextures.append(self.rawTurquoise)
		self.rawTextures.append(self.rawSlategray)
		self.rawTextures.append(self.rawPurple)
		self.rawTextures.append(self.rawOrange)

		self.textures = list()
		self.textures.append(self.blue)
		self.textures.append(self.red)
		self.textures.append(self.green)
		self.textures.append(self.yellow)
		self.textures.append(self.turquoise)
		self.textures.append(self.slategray)
		self.textures.append(self.purple)
		self.textures.append(self.orange)

		self.GameOver = PhotoImage(file='assets/GameOver.png')
		self.rawImageTextures = {"gameOver": self.GameOver}
		self.imageTextures = {"gameOver": self.GameOver.copy()}

	def getTexture(self, i):
		return self.textures[i]['basic']

	def getImageTexture(self, img):
		return self.imageTextures[img]

	def getTextureHighlight(self, i):
		return self.textures[i]['highlight']

	def scaleTextures(self, wantedWidth, wantedHeight):
		for i in range(0, len(self.textures)):
			if wantedWidth != 0:
				scale_w = math.ceil(self.rawTextures[i]["basic"].width() / wantedWidth)
				scale_h = math.ceil(self.rawTextures[i]["basic"].height() / wantedHeight)
				self.textures[i]["basic"] = self.rawTextures[i]["basic"].subsample(scale_w, scale_h)
				self.textures[i]["highlight"] = self.rawTextures[i]["highlight"].subsample(scale_w, scale_h)

	def scaleImageTextures(self, w, h):
		scale_w = math.ceil(self.rawImageTextures['gameOver'].width() / w)
		scale_h = math.ceil(self.rawImageTextures['gameOver'].height() / h)
		self.imageTextures["gameOver"] = self.rawImageTextures['gameOver'].subsample(scale_w, scale_h)

		#for idx in self.imageTextures.keys():
