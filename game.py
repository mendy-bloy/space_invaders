import  pygame
from settings import *
from player import *
from enemy import *
import random

class Projectile(pygame.sprite.Sprite):
	def __init__(self, shooter, pos_x, pos_y):
		super().__init__()
		if shooter == 'player':
			self.image = projectile_image1
			self.rect = self.image.get_rect(midbottom = (pos_x, pos_y))
			self.direction = -1
		elif shooter == 'enemy':
			self.image = projectile_image2
			self.rect = self.image.get_rect(midtop = (pos_x, pos_y))
			self.direction = 1
		
class ProjectileGroup(pygame.sprite.Group):			
	def fly(self):
		for projectile in self.sprites():
			projectile.rect.y += projectile.direction*4
			if projectile.rect.y<=0 or projectile.rect.y>= hight:
				projectile.kill()
				
				
class Lives_bar(pygame.sprite.Group):
	def __init__(self):
		super().__init__()

		for i in range(lives):
			sprite = pygame.sprite.Sprite()
			sprite.image = ship_bmp_lives
			sprite.rect = sprite.image.get_rect()
			sprite.rect.left = 10 +(i*35)
			sprite.rect.bottom = hight -10
			self.add(sprite)
			
class Game:
	def __init__(self, level, score):
		self.level = level
		self.ship_gs = ship_gs
		self.ship_gs.add(Spaceship(ship_bmp, lives))
		self.aliens = AliensGroup((self.level, columns), speed*self.level)
		self.ship_fire = ProjectileGroup()
		self.alien_projectiles = ProjectileGroup()
		self.lives_bar = Lives_bar()
		self.score = score
		
	def initiate_screen(self):
		screen.fill((225, 225, 225))	
		screen.blit(background_image, (0, 0))

	def collisions(self):
		if pygame.sprite.groupcollide(self.aliens, self.ship_fire, True, True):
			kills[random.randint(1, 2)].play()
			self.score += level*13
		pygame.sprite.groupcollide(self.alien_projectiles, self.ship_fire, True, True)		
		for ship in self.ship_gs:
			if pygame.sprite.groupcollide(self.alien_projectiles, self.ship_gs, True, True) or pygame.sprite.groupcollide(self.aliens, self.ship_gs, True, True):
				if ship.lives >0:
					self.ship_gs.add(ship)
					ship.lives -= 1
					list(self.lives_bar)[-1].kill() 
					memes[random.randint(0,1)].play()

	def end_screen(self):	
			screen.blit(game_over, (0,0))
			sad.play()
			end_score = font.render('final score:' + str(self.score) , True, (225, 225, 225))
			end_score_Rect = end_score .get_rect()
			screen.blit(end_score , (width-250, hight-50))
			start_over = font.render("press 'enter' to start again.", True, (225, 225, 225))
			start_over_Rect = start_over.get_rect()
			screen.blit(start_over , (530, 600))


	def aliens_fire(self):
		if pygame.time.get_ticks() - self.aliens.time >= (900-(self.level*100)) and len(self.aliens) != 0:
			rand_alien = list(self.aliens)[random.randint(0, len(self.aliens)-1)]
			projectile = Projectile('enemy', rand_alien.rect.centerx, rand_alien.rect.bottom)
			self.alien_projectiles.add(projectile)	
			self.aliens.time = pygame.time.get_ticks()

	def update_screen(self):
		self.lives_bar.draw(screen)
		self.aliens.draw(screen)
		self.aliens.move()
		if len(self.ship_fire) != 0:
			self.ship_fire.draw(screen)
			self.ship_fire.fly()
		if len(self.alien_projectiles) != 0:
			self.alien_projectiles.draw(screen)
			self.alien_projectiles.fly()
	
	def control_ship(self):
		for ship in self.ship_gs:
			ship.display_ship()
			ship.move_ship()
			
	def ship_shoot(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and len(self.ship_fire)<10:
				for ship in self.ship_gs:
					self.ship_fire.add(Projectile('player', ship.rect.centerx, ship.rect.y))

	def keep_score(self):
		text = font.render('score:' + str(self.score) , True, (225, 225, 225))
		textRect = text.get_rect()
		screen.blit(text, (width-150, hight-50))
		
	def show_level(self):
		level_txt = font.render('level:' + str(self.level) , True, (225, 225, 225))
		lvltextRect = level_txt.get_rect()
		screen.blit(level_txt, (width-300, hight-50))
