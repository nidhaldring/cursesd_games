
from random import randrange,random
from curses import A_DIM

from entity import *
from symbols import *


class Star(Entity,DeplaceMixin):

	frames = [['☆','★','✷'],['✶','✷','✸']] 

	def __init__(self,x,y,stdsrc):

		# choose a random star combination
		frames = self.frames[randrange(len(self.frames))]  
		animation = Animation(frames,[0.2 + random()] * 3)

		super().__init__(x,y,animation,stdsrc)


class World:

	'''
	encapsulates all world design elements
	'''

	def __init__(self,stdsrc):

		self.stdsrc = stdsrc
		self.stars = self._createStars()
		self.screen = Entity(0,0,Animation(symbols,[10,10,10,10]),stdsrc)

		self.screenDim = self.stdsrc.getmaxyx() 

	def _createStars(self,n=40):

		stars = []
		for i in range(n):
			stars.append(Star(*getRandomXY(self.stdsrc),self.stdsrc))

		return stars


	def draw(self):

		for star in self.stars:
			star.draw(A_DIM)

		self.screen.draw(A_DIM)
