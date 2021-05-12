import random
import pygame

# import os
# import sys
w_width = 800
w_height = 480
dis = (w_width, w_height)
#dis = (width, height)
	
class Camera(object):
	def __init__(self, camera_func, width, height):
		self.camera_func = camera_func
		self.state = pygame.Rect(0, 0, width, height)
	
	def apply(self, target):
		return target.rect.move(self.state.topleft)
		
	def update(self, target):
		self.state = self.camera_func(self.state, target.rect)

def camera_config(camera, target_rect):
	l, t, _, _ = target_rect
	_, _, w, h = camera
	# for event in pygame.event.get():
		# if event.type == pygame.VIDEORESIZE:
			# width_w, height_w = event.size
	l, t = -l + w_width / 2, -t + w_height / 2
	l = min(0, l)
	l = max(-(camera.width - w_width), l)
	t = min(0, t)
	t = max(-(camera.height - w_height), t)
	return pygame.Rect(l, t, w, h)
		
		



def main():
	pygame.init()
	import player
	import blocks
	

	width = pygame.display.Info().current_w
	height = pygame.display.Info().current_h
	background = '#6586FF'
	entities = pygame.sprite.Group()
	platforms = []
	
	level = [
	'-----------------------------------------',
	'-          *                            -',
	'-                                       -',
	'-      --                ---            -',
	'-    *              -                   -',
	'-----*                       ---        -',
	'-               *       ---             -',
	'- -                                     -',
	'-           --   ---  --    ----        -',
	'- -                                     -',
	'-      --                               -',
	'- -         --                          -',
	'-             --                        -',
	'- -                   ---               -',
	'-                --                     -',
	'- -     -     --                        -',
	'-        *  --                          -',
	'-----------------------------------------']
	
	
	
	running = True
	FPS = pygame.time.Clock()
	#dis = (width, height)
	window = pygame.display.set_mode(dis, pygame.RESIZABLE)
	title = "GAME size x=%s y=%s"%(width, height)
	pygame.display.set_caption(title)
	game_canvas = pygame.Surface((width, height))
	bg = pygame.Surface((width, height))
	bg.fill(background)
	game_canvas.blit(bg, (0, 0))	
	
	# any extra code herre
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
	# PLATFORM_color = '#00861B'
	
	hero = player.Player(4 * PLATFORM_width, 3 * PLATFORM_height)
	left = right = up = False	
	entities.add(hero)
	x = y = 0
	for row in level:
		for col in row:
			if col == "-":
				platform = blocks.Platform(x, y)
				entities.add(platform)
				platforms.append(platform)
				#game_canvas.blit(platform, (x, y))
			if col == "*":
				thorns = blocks.BlockThorns(x, y)
				entities.add(thorns)
				platforms.append(thorns)
			x += PLATFORM_width
			
		y += PLATFORM_height
		x = 0
	total_level_width = len(level[0]) * PLATFORM_width
	total_level_height = len(level) * PLATFORM_height
	camera = Camera(camera_config, total_level_width, total_level_height)
	# # any extra code herre
	window.blit(game_canvas, (0, 0))
	pygame.display.flip()
	pygame.display.update()
	
	
	###########################################################

	#print(pygame.display.Info())
	# <VideoInfo(hw = 0, wm = 1,video_mem = 0
	         # blit_hw = 0, blit_hw_CC = 0, blit_hw_A = 0,
	         # blit_sw = 0, blit_sw_CC = 0, blit_sw_A = 0,
	         # bitsize  = 32, bytesize = 4,
	         # masks =  (16711680, 65280, 255, 0),
	         # shifts = (16, 8, 0, 0),
	         # losses =  (0, 0, 0, 8),
	         # current_w = 1024, current_h = 600
	# >

	while running:
		FPS.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				raise SystemExit
			# if event.type == pygame.VIDEORESIZE:
				# width, height = event.size
				# window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
				# title = "GAME size x=%s y=%s"%(width, height)
				# pygame.display.set_caption(title)
				# game_canvas = pygame.Surface((width, height))
				# bg = pygame.Surface((width, height))
				# bg.fill(background)
				# game_canvas.blit(bg, (0, 0))	
				
				# # any extra code herre
				# screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
				# # print(screen_ratio)
				# # if screen_ratio > 2:
					# # PLATFORM_width = int(20 * screen_ratio)
					# # PLATFORM_height = int(20 * screen_ratio)
				# # elif screen_ratio > 1:
					# # PLATFORM_width = int(40 * screen_ratio)
					# # PLATFORM_height = int(40 * screen_ratio)
				# # else: 
					# # PLATFORM_width = int(20 / screen_ratio)
					# # PLATFORM_height = int(20 / screen_ratio)
				# # PLATFORM_color = '#00861B'
				
				# x = y = 0
				# for row in level:
					# for col in row:
						# if col == "-":
							# platform = blocks.Platform(x, y)
							# entities.add(platform)
							# platforms.append(platform)
							# #game_canvas.blit(platform, (x, y))
						# x += PLATFORM_width
					# y += PLATFORM_height
					# x = 0
			
				
				# # # any extra code herre
				# window.blit(game_canvas, (0, 0))
				# pygame.display.flip()
				# pygame.display.update()				
				
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				left = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				right = True
			if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
				left = False
			if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
				right = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				up = True
			if event.type == pygame.KEYUP and event.key == pygame.K_UP:
				up = False		
						
		window.blit(game_canvas, (0, 0))
		
		hero.update(left, right, up, platforms)
		print(hero.HP)
		camera.update(hero)
		#entities.draw(window)
		for ent in entities:
			window.blit(ent.image, camera.apply(ent))
		pygame.display.update()
	




if __name__ == '__main__':
	main()
