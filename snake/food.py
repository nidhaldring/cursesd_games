
from entity import *


class Food(Entity,DeplaceMixin):

	animation = Animation(["▧","▨","▩","▦"],[0.2,0.3,0.4,0.2])

	def __init__(self,stdsrc):

		super().__init__(*getRandomXY(stdsrc),self.animation,stdsrc)
	
