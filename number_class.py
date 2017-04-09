import pygame, sys
from pygame.locals import *
import random
from PIL import Image
from imageEdit import concatenateImages
class Number(pygame.sprite.Sprite):

	def __init__(self, speed, width, height, x_coord, y_coord, collision, shrink_ratio, number):
		''' Initializes every number image into a list. Displays images onto screen. If number is greater than 9 than combine 2 numbers
			Usage: num = Number(speed, width, height, x_coord, y_coord, collision, shrink_ratio, number) '''
		super(Number, self).__init__()
		self.images = [pygame.image.load("0.png").convert_alpha(), pygame.image.load("1.png").convert_alpha(), pygame.image.load("2.png").convert_alpha(),
		pygame.image.load("3.png").convert_alpha(), pygame.image.load("4.png").convert_alpha(), pygame.image.load("5.png").convert_alpha(),pygame.image.load("6.png").convert_alpha(),
		pygame.image.load("7.png").convert_alpha(),pygame.image.load("8.png").convert_alpha(),pygame.image.load("9.png").convert_alpha(),
		pygame.image.load("Multiply.png").convert_alpha(), pygame.image.load("Plus.png").convert_alpha()]
		print (number)
		if number == "X":
			self.surf = self.images[10]
		elif number == "+":
			self.surf = self.images[11]
		elif int(number) > 9:
			numList = list(number)
			concatenateImages(numList[0], numList[1])
			self.surf = pygame.image.load("solution.png").convert_alpha()
		else:
			self.surf = self.images[int(number)]
		self.surf = pygame.transform.scale(self.surf, (shrink_ratio, shrink_ratio))
		self.rect = self.surf.get_rect()
		self.speed = speed
		self.height = height
		self.width = width
		self.collision = collision
		self.rect.x = x_coord
		self.rect.y = y_coord



 
	def gravity(self):
		''' Checks if number has been collided with, unless self.collision == False '''
		if self.collision == False:
			return None
	def update(self, pressed_keys):
		''' updates the number sprite with a new position if neccessary '''
		self.rect.move_ip(-self.speed, 0)

		#self.surf = self.images[random.randint(0, 9)]

		"""if self.collision == True:
			if self.rect.left < 0:
					self.rect.left = 0
			elif self.rect.right > self.width:
				self.rect.right = self.width
			if self.rect.top <= 0:
				self.rect.top = 0
			elif self.rect.bottom >= 305: #If touching ground, stop player
				self.rect.bottom = 305"""