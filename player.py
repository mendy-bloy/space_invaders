import  pygame
from settings import *
import random

class Spaceship(pygame.sprite.Sprite):
	def __init__(self, ship_bmp, lives):
		super().__init__()
		self.image = ship_bmp
		self.rect = self.image.get_rect()
		self.rect.top = 5*hight/6
		self.rect.centerx = width/2
		self.lives = lives
		
	def display_ship(self):
		screen.blit(self.image, (self.rect.x, self.rect.y))

	def move_ship(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and self.rect.x>=-30:
			self.rect.move_ip(-10, 0)
		if keys[pygame.K_RIGHT] and self.rect.x<=width-30:
			self.rect.move_ip(10, 0)
		if keys[pygame.K_UP] and self.rect.y>=4*hight/5:
			self.rect.move_ip(0, -5)
		if keys[pygame.K_DOWN] and self.rect.y<=hight-100:
			self.rect.move_ip(0, 5)
		

				
