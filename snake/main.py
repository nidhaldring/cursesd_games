from time import sleep
from curses import *

from food import Food
from snake import Snake
from world import *



def updateGame(stdsrc,world,snake,food,score) -> int:

	'''
	update all game entities
	and return the new screen
	'''

	stdsrc.clear()
	world.draw()
	food.draw()
	snake.draw()

	snake.update()

	stdsrc.addstr(0,0,"SCORE : " + str(score),A_BOLD | A_UNDERLINE)
	stdsrc.refresh()
	sleep(0.1)

	if snake.hasEaten(food):
		food.deplace()
		snake.grow(3)
		score += 3

	return score


def main(stdsrc):

	# don't block the game waiting for keysrokes
	stdsrc.nodelay(True) 

	# disable cursor 
	curs_set(False)	

	# init game elements
	food = Food(stdsrc)
	snake = Snake(stdsrc)
	world = World(stdsrc)
	score = 0

	# game loop
	while True:

		if score >= 100:
			stdsrc.clear()
			stdsrc.addstr(0,0,won,A_BOLD)

		elif snake.isAlive():
			score = updateGame(stdsrc,world,snake,food,score)
		else:
			stdsrc.addstr(0,0,death%score,A_BOLD)
		
		stdsrc.refresh()



try:
	wrapper(main)
except error:
	print("please make sure to maximize your terminal !")
except KeyboardInterrupt:
	print("bye..!")

