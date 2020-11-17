import pygame
import sys
from A_star_algo import *

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((0,0,0))
	pygame.display.update()
