import pygame

move_speed = 3
screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
#
width = int((pygame.display.Info().current_h * screen_ratio) / 33)
height = int((pygame.display.Info().current_w / screen_ratio) / 10)
color = '#FFC457'

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.x_move_speed = 0
		self.startX = x
		self.startY = y
		self.x = x
		self.y = y
		self.width = int((pygame.display.Info().current_h * screen_ratio) / 33)
		self.height = int((pygame.display.Info().current_w / screen_ratio) / 10)
		self.color = color
		self.body = pygame.Surface((width, height))
		self.body.fill(color)
		self.rect = pygame.Rect(x, y, width, height)
		
	def update(self, left, right):
		
		if left:
			self.x_move_speed = -move_speed
		elif right:
			self.x_move_speed = move_speed
		else:
			self.x_move_speed = 0
		self.rect.x += self.x_move_speed
	
	def draw(self, screen):
		self.width = int((pygame.display.Info().current_w) / 33)
		self.height = int((pygame.display.Info().current_h) / 10)
		self.color = color
		self.body = pygame.Surface((self.width, self.height))
		self.body.fill(self.color)
		screen.blit(self.body, (self.rect.x, self.rect.y))
