'''
The rules of cellular automata

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

'''

import pygame
import sys


def board_update(screen, multiplier):
	screen.fill((255,255,255))
	for i in range(0, 50 * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 50 * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (50 * multiplier, i))
	pygame.display.update()
		

def game(screen, multiplier):
	stop = False
	while stop == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		board_update(screen, multiplier)
		
			

def main():
	pygame.init()
	size = width, height = 750, 750
	screen = pygame.display.set_mode(size)
	game(screen, 15)

main()
	