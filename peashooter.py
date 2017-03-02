import pygame
from pygame.sprite import Sprite
from plant import Plant


class Peashooter(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 2
		self.health = 5
		self.image_file = './images/peashooter.png'
		self.screen = screen
		self.square = square
		self.can_shoot = True
		self.can_make_sun = False
		self.sun_cost = 100
		super(Peashooter, self).__init__()