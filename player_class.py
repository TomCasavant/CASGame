import pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self, speed, width, height):
		''' Creates a player. 
			Usage: player = Player(self, speed, width, height) '''
		super(Player, self).__init__()
		#self.surf = pygame.Surface((75,25))
		#self.surf.fill((255,0,0))
		self.images = [pygame.image.load("f1.png").convert_alpha(), pygame.image.load("f2.png").convert_alpha(), pygame.image.load("f3.png").convert_alpha()]
		self.surf = self.images[0]
		self.rect = self.surf.get_rect()
		self.speed = speed
		self.width = width
		self.height = height
		self.isWalking = 0
		self.x = 2
	def gravity(self):
		''' Moves the player downward until reaching ground '''
		if self.rect.bottom < 305:
			self.rect.move_ip(0, self.x) #If not touching ground, move down at accelerated rate of .25
			self.x += .1
		else:
			self.x = 0
	def update(self,pressedkeys):
		''' Reacts to player input through variable pressedkeys. Moves player appropriately '''
		if pressedkeys[K_UP]:
			self.rect.move_ip(0,-self.speed -2) #If the player presses the UP key
			self.surf = self.images[1]
		
		if pressedkeys[K_DOWN]:
			self.rect.move_ip(0,self.speed) #If the player presses the DOWN key
			self.surf = self.images[0]
		
		if pressedkeys[K_LEFT]:
			self.rect.move_ip(-self.speed, 0)
			if self.isWalking == 0:
				self.surf = self.images[1]
				self.isWalking = 1
			elif self.isWalking == 1:		#If the player presses the LEFT key
				self.surf = self.images[0]
				self.isWalking = 2
			elif self.isWalking == 2:
				self.surf = self.images[2]
				self.isWalking = 0

		elif pressedkeys[K_RIGHT]:
			self.rect.move_ip(self.speed,0)
			if self.isWalking == 0:
				self.surf = self.images[1]
				self.isWalking = 1
			elif self.isWalking == 1:		#If the player presses the RIGHT key
				self.surf = self.images[0]
				self.isWalking = 2
			elif self.isWalking == 2:
				self.surf = self.images[2]
				self.isWalking = 0

		else:
			self.surf = self.images[2]
			self.isWalking = 0
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > self.width:
			self.rect.right = self.width
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= 305: #If touching ground, stop player
			self.rect.bottom = 305

