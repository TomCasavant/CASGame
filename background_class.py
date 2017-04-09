import pygame

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file) #Loads background image as rectangle
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location