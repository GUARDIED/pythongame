import pygame

class game_window(pygame.Surface):
	def __init__(self, width, height, background, level):
		self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
		self.title = "GAME size x=%s y=%s"%(width, height)
		self.width = width
		self.height = height
		self.background = background
		self.level = level
		pygame.display.set_caption(self.title)		
		
		
	def draw(self, width, height):
		self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
		self.title = "GAME size x=%s y=%s"%(width, height)
		pygame.display.set_caption(self.title)		
		self.game_canvas = pygame.Surface((width, height))
		self.bg = pygame.Surface((width, height))
		self.bg.fill(self.background)
		self.game_canvas.blit(self.bg, (0, 0))	
		
		# any extra code herre
		self.screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
		self.PLATFORM_width = int((pygame.display.Info().current_w) / 33)
		self.PLATFORM_height = int((pygame.display.Info().current_h) / 18)
		self.PLATFORM_color = '#00861B'
		
		self.x = self.y = 0
		for self.row in self.level:
			for self.col in self.row:
				if self.col == "-":
					self.platform = pygame.Surface((self.PLATFORM_width, self.PLATFORM_height))
					self.platform.fill(self.PLATFORM_color)
					self.game_canvas.blit(self.platform, (self.x, self.y))
				self.x += self.PLATFORM_width
			self.y += self.PLATFORM_height
			self.x = 0
	
		
		# any extra code herre
		self.window.blit(self.game_canvas, (0, 0))
		pygame.display.flip()
		pygame.display.update()
	def update(self):
		self.game_canvas = pygame.Surface((self.width, self.height))
		self.bg = pygame.Surface((self.width, self.height))
		self.bg.fill(self.background)
		self.game_canvas.blit(self.bg, (0, 0))	
		
		# any extra code herre
		self.screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
		self.PLATFORM_width = int((pygame.display.Info().current_w) / 33)
		self.PLATFORM_height = int((pygame.display.Info().current_h) / 18)
		self.PLATFORM_color = '#00861B'
		
		self.x = self.y = 0
		for self.row in self.level:
			for self.col in self.row:
				if self.col == "-":
					self.platform = pygame.Surface((self.PLATFORM_width, self.PLATFORM_height))
					self.platform.fill(self.PLATFORM_color)
					self.game_canvas.blit(self.platform, (self.x, self.y))
				self.x += self.PLATFORM_width
			self.y += self.PLATFORM_height
			self.x = 0
	
		
		# any extra code herre
		self.window.blit(self.game_canvas, (0, 0))
		pygame.display.flip()
		pygame.display.update()
