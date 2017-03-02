import pygame
from pygame.sprite import Sprite
from plant import Plant


class Gatling(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 4
		self.health = 5
		self.image_file = './images/Gatling_Pea_Fixed.png'
		self.screen = screen
		self.square = square
		self.can_shoot = True
		self.can_make_sun = False
		self.sun_cost = 200
		super(Gatling, self).__init__()