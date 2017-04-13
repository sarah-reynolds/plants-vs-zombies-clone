# Plants vs Zombies clone
### Made using Python and Pygame
--- 

### Code snippets 
When a zombie is hit by a pea, remove the pea (bullet) from the game, reduce its health (zombie.hit), and check its health. If the zombie's health is less than or equal to zero, then remove the zombie from the game, increase the number of zombies killed by 1.
```
zombies_hit = groupcollide(zombies, bullets, False, False)

for zombie in zombies_hit:
	if zombie.yard_row == zombies_hit[zombie][0].yard_row:
		bullets.remove(zombies_hit[zombie][0])
		zombie.hit(1)
		if zombie.health <= 0:
			zombies.remove(zombie)
			game_settings.zombie_in_row[zombie.yard_row] -= 1
			game_settings.zombies_killed += 1
```