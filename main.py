import pygame
from settings import Settings
from background import Background
import game_functions as gf
from pygame.sprite import Group, groupcollide
from zombie import Zombie
from square import Square
from plant_icon import Plant_Icon
import time

pygame.init()
game_settings = Settings()
screen = pygame.display.set_mode(game_settings.screen_size)
pygame.display.set_caption("DC PvZ clone")
background  = Background(game_settings)
peashooter_icon = Plant_Icon(game_settings,'peashooter-icon.png',1)
gatling_icon = Plant_Icon(game_settings,'gatling-icon.png',2)
sunflower_icon = Plant_Icon(game_settings,'sunflower-icon.png',3)
icons = [peashooter_icon,gatling_icon,sunflower_icon]

zombies = Group()
plants = Group()
squares = Group()
bullets = Group()

# print game_settings.squares["rows"][1]

for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen, game_settings, i, j))

def run_game():
	tick = 0
	while 1:
		gf.check_events(screen, game_settings, squares, plants, bullets, icons)
		if game_settings.game_active:
			tick += 1
			if tick % 30 == 0:
				zombies.add(Zombie(screen, game_settings))

			zombies_hit = groupcollide(zombies, bullets, False, False)
			
			for zombie in zombies_hit:
				if zombie.yard_row == zombies_hit[zombie][0].yard_row:
					bullets.remove(zombies_hit[zombie][0])
					zombie.hit(1)
					if zombie.health <= 0:
						zombies.remove(zombie)
						game_settings.zombie_in_row[zombie.yard_row] -= 1
						game_settings.zombies_killed += 1
			zombies_eating = groupcollide(zombies, plants, False, False)
			for zombie in zombies_eating:

				damaged_plant = zombies_eating[zombie][0]
				print damaged_plant
				if zombie.yard_row == damaged_plant.yard_row:
					zombie.moving = False
					if time.time() - zombie.started_eating > zombie.damage_time:
						print "Zombie took a bite"
						damaged_plant.take_damage(2)
						zombie.started_eating = time.time()
						if damaged_plant.health <= 0:
							plants.remove(damaged_plant)
							zombie.moving = True
							damaged_plant.square.plant_here = False


		gf.update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick, icons)
		pygame.display.flip()

run_game()