import pygame
import game_window

pygame.init()

width = pygame.display.Info().current_w-200
height = pygame.display.Info().current_h-200
background = '#6586FF'
FPS = pygame.time.Clock()
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

win = game_window.game_window(width, height, background, level)
win.draw(width, height)


while running:
	FPS.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			raise SystemExit
		if event.type == pygame.VIDEORESIZE:
			width, height = event.size
			win.draw(width, height)
	win.update()
	
	

