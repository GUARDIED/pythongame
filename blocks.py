import pygame

screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
if screen_ratio > 2:
	PLATFORM_width = int(20 * screen_ratio)
	PLATFORM_height = int(20 * screen_ratio)
elif screen_ratio > 1:
	PLATFORM_width = int(40 * screen_ratio)
	PLATFORM_height = int(40 * screen_ratio)
else: 
	PLATFORM_width = int(20 / screen_ratio)
	PLATFORM_height = int(20 / screen_ratio)
PLATFORM_color = '#00861B'

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
		if self.screen_ratio > 2:
			self.PLATFORM_width = int(20 * self.screen_ratio)
			self.PLATFORM_height = int(20 * self.screen_ratio)
		elif self.screen_ratio > 1:
			self.PLATFORM_width = int(40 * self.screen_ratio)
			self.PLATFORM_height = int(40 * self.screen_ratio)
		else: 
			self.PLATFORM_width = int(20 / self.screen_ratio)
			self.PLATFORM_height = int(20 / self.screen_ratio)
		
		self.image = pygame.Surface((int(PLATFORM_width), int(PLATFORM_height)))	
		self.image.fill(PLATFORM_color)
		self.rect = pygame.Rect(x, y, PLATFORM_width, PLATFORM_height)
	
class BlockThorns(Platform):
	def __init__(self, x, y):
		Platform.__init__(self, x, y)
		self.image = pygame.Surface((int(PLATFORM_width), int(PLATFORM_height)))	
		self.image.fill('#F60079')
		self.rect = pygame.Rect(x, y, PLATFORM_width, PLATFORM_height)
