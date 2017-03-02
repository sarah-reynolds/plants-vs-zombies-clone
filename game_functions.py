import sys
import pygame
from peashooter import Peashooter
from bullet import Bullet


def check_events(screen, game_settings, squares, plants, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			print mouse_x
			print mouse_y
			for square in squares:
				if square.rect.collidepoint(mouse_x, mouse_y):
					print "Square: ",square.square_number
					plants.add(Peashooter(screen, square))
		elif event.type == pygame.MOUSEMOTION:
			for square in squares:
				if square.rect.collidepoint(event.pos):
					game_settings.highlighted_square = square
					print game_settings.highlighted_square


def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick):
	screen.blit(background.image, background.rect)

	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen, (255,215,0), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares["square_width"], game_settings.squares["square_height"]), 5)

	for zombie in zombies.sprites():
		zombie.update_me()
		zombie.draw_me()
		if zombie.rect.left <= screen.rect.left:
			game_settings.game_active = False

	for plant in plants:
		plant.draw_me()
		print plant.yard_row
		if tick % 30 == 0:
			if game_settings.zombie_in_row[plant.yard_row] >= 0:
				bullets.add(Bullet(screen,plant))

	for bullet in bullets.sprites():
		bullet.update_me()
		bullet.draw_me()

