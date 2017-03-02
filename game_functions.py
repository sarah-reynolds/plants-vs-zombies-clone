import sys
import pygame
from peashooter import Peashooter
from gatling import Gatling
from bullet import Bullet
from sunflower import Sunflower
import time


def check_events(screen, game_settings, squares, plants, bullets, icons):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if game_settings.game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				# print mouse_x
				# print mouse_y
				for square in squares:
					if square.plant_here == False:
						if square.rect.collidepoint(mouse_x, mouse_y):
							# print "Square: ",square.square_number
							if game_settings.chosen_plant == 1:
								peashooter = Peashooter(screen, square)
								plants.add(peashooter)
								square.plant_here = True
								game_settings.total_sun -= peashooter.sun_cost
							elif game_settings.chosen_plant == 2:
								plants.add(Gatling(screen, square))
								square.plant_here = True
								# game_settings.total_sun -= Gatling.sun_cost
							elif game_settings.chosen_plant == 3:
								plants.add(Sunflower(screen, square))
								square.plant_here = True
								# game_settings.total_sun -= Sunflower.sun_cost
				for icon in icons:
					if icon.rect.collidepoint(mouse_x,mouse_y):
						game_settings.chosen_plant = icon.slot
						
			elif event.type == pygame.MOUSEMOTION:
				for square in squares:
					if square.rect.collidepoint(event.pos):
						game_settings.highlighted_square = square
						# print game_settings.highlighted_square


def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick, icons):
	screen.blit(background.image, background.rect)

	for icon in icons:
		screen.blit(icon.image, icon.rect)

	if game_settings.highlighted_square != 0:
		pygame.draw.rect(screen, (255,215,0), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares["square_width"], game_settings.squares["square_height"]), 5)

	for zombie in zombies.sprites():
		if game_settings.game_active:
			zombie.update_me()
		zombie.draw_me()
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;
		zombie.moving = True
	for plant in plants:
		plant.draw_me()
		# print plant.yard_row
		should_shoot = time.time() - plant.last_shot > plant.shoot_speed
		can_shoot = plant.can_shoot
		in_my_row = game_settings.zombie_in_row[plant.yard_row] > 0
		if should_shoot and can_shoot and in_my_row:
			bullets.add(Bullet(screen,plant))
			plant.last_shot = time.time()
		can_make_sun = plant.can_make_sun;
		should_make_sun = time.time() - plant.last_sun > plant.sun_speed;
		if can_make_sun and should_make_sun:
			plant.make_sun(game_settings);
			plant.last_sun = time.time();

	for bullet in bullets.sprites():
		if game_settings.game_active:
			bullet.update_me()
		bullet.draw_me()

	score_font = pygame.font.SysFont("monospace",36)
	
	score_render = score_font.render("Zombies killed: "+str(game_settings.zombies_killed) +"!!!",1,(255,215,0))
	screen.blit(score_render,(100,100))

	sun_render = score_font.render("Total sun: "+str(game_settings.total_sun),1,(255,215,0));
	screen.blit(sun_render,(100,150));


