'''
The rules of cellular automata

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

'''

import pygame
import sys
import numpy

#Handles the backend of this cellular automata using a numpy array
def backend(grid, cells):
	board = numpy.zeros((grid, grid))
	for cell in cells:
		#Numpy displays its matrix as a (y,x) system
		board[cell[1]][cell[0]] = 1
	#print(board)
	print(cells)



def board_update(screen, grid, multiplier):
	screen.fill((255,255,255))
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (grid * multiplier, i))
	pygame.display.update()


def game(screen, grid, cells, multiplier):
	stop, game_start = False, False
	while stop == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		board_update(screen, grid, multiplier)

		#Set initial cells when game has not started
		if pygame.mouse.get_pressed()[0] and game_start == False:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // multiplier, mouse_pos[1] // multiplier]
			cells.append(mouse_pos)

		#To start the game
		if pygame.key.get_pressed()[pygame.K_SPACE]:
			game_start = True

		if game_start == True:
			backend(grid, cells)
			

def main():
	pygame.init()
	pygame.display.set_caption('Cellular Automata')
	size = width, height = 750, 750
	grid = 50
	cells = []
	screen = pygame.display.set_mode(size)
	game(screen, grid, cells, 15)

main()
	