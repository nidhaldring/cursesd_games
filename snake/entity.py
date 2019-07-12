from random import randint
from time import time
from curses import *



def getRandomXY(stdsrc):
	maxy,maxx = stdsrc.getmaxyx()
	return  randint(0,maxx - 1),randint(0,maxy - 1)


class DeplaceMixin:

	def deplace(self):

		self.x,self.y = getRandomXY(self.stdsrc)


class Animation:

	def __init__(self,frames:list,secondPerFrame:list):

		self.frames = frames
		self.secondPerFrame = secondPerFrame
		self.currentFrame = 0
		self.time = time()

	def getCurrentFrame(self):

		currentTime = time()
		if currentTime - self.time >= self.secondPerFrame[self.currentFrame]:
				self.time = currentTime
				self.currentFrame += 1
				self.currentFrame %= len(self.frames)

		return self.frames[self.currentFrame]



class Entity:

	def __init__(self,x,y,animation,stdsrc):

		self.x = x
		self.y = y
		self.animation = animation
		self.stdsrc = stdsrc


	def draw(self,attr=A_BOLD):

		frame = self.animation.getCurrentFrame()
		self.stdsrc.addstr(self.y,self.x,frame,attr)


	def contains(self,other) -> bool:

		return self.x == other.x and self.y == other.y
	


