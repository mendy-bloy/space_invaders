import  pygame
from settings import *
from player import *
import random

class Alien(pygame.sprite.Sprite):
	def __init__(self, kind, row, column):
		super().__init__()
		self.image = aliens_images[kind-1]
		self.rect = self.image.get_rect()
		self.rect.left = row*150
		self.rect.top = (column+0.5)*90
		
class AliensGroup(pygame.sprite.Group):
	def __init__(self, dims, speed):
		super().__init__()
		(rows, columns) = dims
		for column in range(rows):
			self.add(Alien(random.randint(1,2), row, column) for row in range(columns))	
		self.direction = 1
		self.speed = speed
		self.time = time
		
	def move(self):
		if len(self.sprites())!= 0:
			self.rect = self.sprites()[0].rect.unionall([alien.rect for alien in self.sprites()])
			if self.rect.left<0 or self.rect.right>width:
				self.direction *= -1
				self.rect.y += 30
				for alien in self.sprites():
					if alien.rect.bottom>hight:
						alien.kill()
					alien.rect.y += 30
		self.rect.x += self.speed*self.direction
		for alien in self.sprites():
			alien.rect.x += self.speed*self.direction
			

