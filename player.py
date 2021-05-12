import pygame
import blocks
import time
import os

move_speed = 3
jump_power = 10
gravity = 0.35
color = '#FFC457'

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.HP = 100
		self.jump = 0
		self.onGround = False
		self.x_move_speed = 0
		self.startX = x
		self.startY = y
		self.x = x
		self.y = y
		self.screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
		if self.screen_ratio > 2:
			self.width = int(18 * self.screen_ratio)
			self.height = int(35 * self.screen_ratio)
		elif self.screen_ratio > 1:
			self.width = int(36 * self.screen_ratio)
			self.height = int(70 * self.screen_ratio)
		else:
			self.width = int(20 / self.screen_ratio)
			self.height = int(35 / self.screen_ratio)
		self.color = color
		self.image = pygame.Surface((int(self.width), int(self.height)))	
		self.image.fill(color)
		self.body = pygame.Surface((self.width, self.height))
		self.body.fill(color)
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
	def update(self, left, right, up, platforms):
		if up:
			if self.onGround:
				self.jump = -jump_power
		if left:
			self.x_move_speed = -move_speed
		elif right:
			self.x_move_speed = move_speed
		else:
			self.x_move_speed = 0
		if not self.onGround:
			self.jump += gravity
		self.onGround = False		
		self.rect.y += self.jump
		self.collide(0, self.jump, platforms)
		self.rect.x += self.x_move_speed
		self.collide(self.x_move_speed, 0, platforms)
		
		
	def collide(self, x_move_speed, y, platforms):
		#pygame.sprite.spritecollide(self, platforms, True, pygame.sprite.collide_circle)		
		for platform in platforms:
			if pygame.sprite.collide_rect(self, platform):
				if x_move_speed > 0:
					self.rect.right = platform.rect.left
				if x_move_speed < 0:
					self.rect.left = platform.rect.right
				if y > 0:
					self.rect.bottom = platform.rect.top
					self.onGround = True
					self.jump = 0
				if y < 0:
					self.rect.top = platform.rect.bottom
					self.jump = 0				
				if isinstance(platform, blocks.BlockThorns):
					self.damage(1)
						
					
								
	
	def die(self):
		#time.sleep(500)
		self.teleport(self.startX, self.startY)
		self.HP = 100
		
	def teleport(self, goX, goY):
		self.rect.x = goX
		self.rect.y = goY
		
	def damage(self, damage):
		self.HP = self.HP - damage
		if self.HP < 1:
			self.die()
	
	# def draw(self, screen):
		# # self.screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
		# # if self.screen_ratio > 2:
			# # self.width = int(20 * self.screen_ratio)
			# # self.height = int(35 * self.screen_ratio)
		# # elif self.screen_ratio > 1:
			# # self.width = int(40 * self.screen_ratio)
			# # self.height = int(70 * self.screen_ratio)
		# # else:
			# # self.width = int(20 / self.screen_ratio)
			# # self.height = int(35 / self.screen_ratio)
		# self.color = color
		# self.body = pygame.Surface((self.width, self.height))
		# self.body.fill(self.color)
		# screen.blit(self.body, (self.rect.x, self.rect.y))
