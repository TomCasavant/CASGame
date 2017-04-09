import pygame
from background_class import Background
from player_class import Player
from pygame.locals import *
from number_class import Number
import random

class Main():
	def __init__(self, width, height):
		''' Initializes the game and begins game loop.
			Usage: game = Main(self, width, height)'''
		pygame.init()
		self.clock = pygame.time.Clock()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.all_sprites = pygame.sprite.Group()
		self.players = pygame.sprite.Group()
		self.numbers = pygame.sprite.Group()
		self.scores = pygame.sprite.Group()
		self.running = True
		self.BackGround = Background('background.png', [0,0])

	def updateSprites(self, pressed_keys):
		''' Continuously updates the sprite to screen, changing position based on gravity 
			Takes player input pressed_keys'''

		collide = pygame.sprite.spritecollide(self.player, self.numbers, False, collided=None)
		if collide:
			if collide[0] == self.answer: #If collided with correct answer
				self.wins += 1
				win = True
			else: #If collided with wrong answer
				self.losses += 1
				win = False

			self.endGame(win)


		for sprite in self.all_sprites:
			self.screen.blit(sprite.surf, (sprite.rect)) #Blits all sprites onto the screen
			sprite.update(pressed_keys)
			sprite.gravity() #Forces Srite down

	def endGame(self, win):
			self.players.empty()
			self.numbers.empty()
			self.all_sprites.empty()

			self.screen.fill((0,0,0))
			pygame.display.flip()
			if win:
				img = pygame.image.load("Check.png")
			else:
				img = pygame.image.load("X.png")
			self.screen.blit(img, (350, 100))
			pygame.display.flip()
			pygame.time.wait(500)
			self.createSprites()

	def randomEquationGen(self):
		''' Randomly generates an equation and a solution for the game 
			Returns: [equation, solution] '''
		num1 = random.randint(0, 9)
		num2 = random.randint(0, 9)
		sign = random.choice(["+", "X"])
		equation = str(num1) + " " + sign + " " + str(num2)
		if sign == "+":
			solution = num1 + num2
		elif sign == "X":
			solution = num1 * num2

		return [equation, solution]

	def createSprites(self):
		player = Player(2, self.width, self.height) #Create player at speed 2
		self.player = player
		self.loadSprite(player, "player") #load player into sprite group
		

		self.loadSprite(Number(0, self.height, self.width, 0, 100, False, 50, self.wins), "scores")
		self.loadSprite(Number(0, self.height, self.width, 750, 100, False, 50, self.losses), "scores")
		
		numbers = []
		equation = self.randomEquationGen()
		
		xpos = 250
		for val in equation[0].split(" "):
			numbers.append(Number(0, self.height, self.width, xpos , 325, False, 50, val))
			xpos += 100

		

		rand = random.choice([250, 425])
		self.answer = Number(0, self.height, self.width, rand, 100, False, 50, str(equation[1]))
		numbers.append(self.answer)
		if rand == 250:
			numbers.append(Number(0, self.height, self.width, 425, 100, False, 50, str(random.randint(0, 81))))
		else:
			numbers.append(Number(0, self.height, self.width, 250, 100, False, 50, str(random.randint(0, 81))))

		for num in numbers:
			self.loadSprite(num, "number")

	def gameLoop(self):
		''' Game loop, creates the player and regenerates equations once player has gotten answer '''
		self.wins = 0
		self.losses = 0
		self.createSprites()


		while self.running:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.running = False
						pygame.quit()

				elif event.type == QUIT:
					self.running = False
					pygame.quit()

			pressed_keys = pygame.key.get_pressed()
			self.updateSprites(pressed_keys)
			pygame.display.flip()
			self.screen.fill((255, 255, 255))
			self.screen.blit(self.BackGround.image, self.BackGround.rect) #Display background
			self.clock.tick(30) #FPS

	def loadSprite(self, sprite, typ):
		''' Adds sprites into a group
			Usage: self.loadSprite(sprite) '''
		if typ == "player":
		    self.players.add(sprite)
		elif typ == "number":
		    self.numbers.add(sprite)
		elif typ == "scores":
			self.scores.add(sprite)
		self.all_sprites.add(sprite) #Adds sprites into a group

if __name__ == '__main__':
	main = Main(800, 400) #Create screen at (Width, Height)
	main.gameLoop() #Initialize game loop

