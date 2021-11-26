from tkinter import *

from game.view.TextureFactory import getTextureFactory


class GameOverView:
	def __init__(self, canvas):
		self.canvas = canvas
		self.overimg = None
		self.on_resize()

	def create_image(self):
		getTextureFactory().scaleImageTextures(self.canvas.winfo_width(), self.canvas.winfo_height())
		tmpimg = getTextureFactory().getImageTexture('gameOver')

		x = self.canvas.winfo_width() / 2 - tmpimg.width() / 2
		y = self.canvas.winfo_height() / 2 - tmpimg.height() / 2
		if self.overimg is not None:
			self.canvas.delete(self.overimg)
		self.overimg = self.canvas.create_image(x, y, anchor=NW, image=tmpimg)

	def on_resize(self):
		self.create_image()
