import  pygame
from settings import *
from player import *
from enemy import *
from game import *

pygame.init()


def game_loop():
	game = Game(1,0)
	running = True
	while running:
		game.initiate_screen()
		for event in pygame.event.get():
			if event.type == pygame.QUIT: running = False
			game.ship_shoot(event)
		game.control_ship()			
		game.update_screen()
		game.aliens_fire()
		game.collisions()	
		game.keep_score()	
		game.show_level()
		if len(game.aliens) ==0 and len(game.ship_gs) !=0:
			game.level+=1
			game = Game(game.level, game.score)
		elif len(game.ship_gs) <=0:
			game.end_screen()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_RETURN]:
				game.lives = 3
				game.level = 1
				game = Game(level, 0)
		pygame.display.flip()
		clock.tick(fps)
		
if __name__ == '__main__':
	game_loop()
