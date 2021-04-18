import random
import pygame

# import os
# import sys

def main():
	pygame.init()
	
	width = pygame.display.Info().current_w-200
	height = pygame.display.Info().current_h-200
	background = '#6586FF'
	level = [
	'---------------------------------',
	'-                               -',
	'-                               -',
	'-      --                       -',
	'-                   -           -',
	'-                               -',
	'-                               -',
	'-                               -',
	'-                    ----       -',
	'-                               -',
	'-      --                       -',
	'-                               -',
	'-                               -',
	'-                  ----         -',
	'-                               -',
	'-       -                       -',
	'-           --                  -',
	'---------------------------------']

	running = True
	FPS = pygame.time.Clock()
	# import game_window
	# window = game_window.game_window(width, height, background, level)
	
	window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
	title = "GAME size x=%s y=%s"%(width, height)
	pygame.display.set_caption(title)
	game_canvas = pygame.Surface((width, height))
	bg = pygame.Surface((width, height))
	bg.fill(background)
	game_canvas.blit(bg, (0, 0))	
	
	# any extra code herre
	screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
	print(screen_ratio)
	PLATFORM_width = int((pygame.display.Info().current_w) / 33)
	PLATFORM_height = int((pygame.display.Info().current_h) / 18)
	PLATFORM_color = '#00861B'
	
	x = y = 0
	for row in level:
		for col in row:
			if col == "-":
				platform = pygame.Surface((PLATFORM_width, PLATFORM_height))
				platform.fill(PLATFORM_color)
				game_canvas.blit(platform, (x, y))
			x += PLATFORM_width
		y += PLATFORM_height
		x = 0

	
	# # any extra code herre
	window.blit(game_canvas, (0, 0))
	pygame.display.flip()
	pygame.display.update()
	
	
	###########################################################
	import player
	hero = player.Player(100, 90)
	left = right = False
	
	
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
			if event.type == pygame.VIDEORESIZE:
				width, height = event.size
				window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
				title = "GAME size x=%s y=%s"%(width, height)
				pygame.display.set_caption(title)
				game_canvas = pygame.Surface((width, height))
				bg = pygame.Surface((width, height))
				bg.fill(background)
				game_canvas.blit(bg, (0, 0))	
				
				# any extra code herre
				screen_ratio = pygame.display.Info().current_w / pygame.display.Info().current_h
				print(screen_ratio)
				PLATFORM_width = int((pygame.display.Info().current_w) / 33)
				PLATFORM_height = int((pygame.display.Info().current_h) / 18)
				PLATFORM_color = '#00861B'
				
				x = y = 0
				for row in level:
					for col in row:
						if col == "-":
							platform = pygame.Surface((PLATFORM_width, PLATFORM_height))
							platform.fill(PLATFORM_color)
							game_canvas.blit(platform, (x, y))
						x += PLATFORM_width
					y += PLATFORM_height
					x = 0
			
				
				# # any extra code herre
				window.blit(game_canvas, (0, 0))
				pygame.display.flip()
				pygame.display.update()				
				
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
				left = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
				right = True
			if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
				left = False
			if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
				right = False
					
		window.blit(game_canvas, (0, 0))
		
		hero.update(left, right)
		hero.draw(window)
		pygame.display.flip()
		pygame.display.update()
	




if __name__ == '__main__':
	main()
