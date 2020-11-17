import pygame
import sys
from A_star_algo import *

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)


while True:
	mouse_position = 'None'
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if pygame.mouse.get_pressed()[0]:
			mouse_position = pygame.mouse.get_pos()
			print(mouse_position)



	screen.fill((0,0,0))
	pygame.display.update()
