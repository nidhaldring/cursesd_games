
from curses import *

from entity import Entity,Animation


class Snake:

	animation = Animation(["⚁","⚂","⚃","⚄","⚅"],[0.5,0.2,0.1,0.1,0.1])

	def __init__(self,stdsrc):

		self.stdsrc = stdsrc
		self.head = Entity(1,1,self.animation,self.stdsrc)
		self.parts = []
		self.currentDir = KEY_UP

		self.grow(5)


	def grow(self,n:int):

		x,y = (self.parts[0].x,self.parts[0].y) if self.parts else (0,0)
		self.parts.extend([Entity(x,y,self.animation,self.stdsrc) for i in range(n)])


	def draw(self):

		self.head.draw(A_BOLD)
		for part in self.parts:
			part.draw(A_BOLD)

	def update(self):

		isDir = lambda c : 258 <= c <= 261

		c = self.stdsrc.getch()
		if isDir(c) and not self._areOpposite(c,self.currentDir):
			self._move(c)
			self.currentDir = c
		else:
			self._move(self.currentDir)


	def _move(self,direction:int):

		self._moveParts()
		self._moveHead(direction)
		self._fixBorders()


	def _moveParts(self):


		i = len(self.parts) - 1
		while i > 0:
			self.parts[i].x = self.parts[i-1].x
			self.parts[i].y = self.parts[i-1].y
			i -= 1

		self.parts[0].x = self.head.x
		self.parts[0].y = self.head.y

	def _moveHead(self,direction:int):

		if direction == KEY_UP:
			self.head.y -= 1
		elif direction == KEY_DOWN:
			self.head.y += 1
		elif direction == KEY_RIGHT:
			self.head.x += 1
		elif direction == KEY_LEFT:
			self.head.x -= 1

	def _fixBorders(self):

		maxy,maxx = self.stdsrc.getmaxyx()

		if self.head.x >= maxx:
			self.head.x = 0
		elif self.head.x < 0:
			self.head.x = maxx - 1

		if self.head.y >= maxy:
			self.head.y = 0
		elif self.head.y < 0:
			self.head.y = maxy - 1


	def _areOpposite(self,dir1:int,dir2:int) -> bool:

		return (dir1 == KEY_UP and dir2 == KEY_DOWN) or\
				(dir1 == KEY_DOWN and dir2 == KEY_UP) or\
				(dir1 == KEY_LEFT and dir2 == KEY_RIGHT) or\
				(dir1 == KEY_RIGHT and dir2 == KEY_LEFT)


	def hasEaten(self,food) -> bool:

		return self.head.contains(food)


	def isAlive(self) -> bool:

		'''
		check if the snake eat part of its body
		'''

		for part in self.parts:
			if self.head.contains(part):
				return False

		return True
