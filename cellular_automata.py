'''
The rules of cellular automata (Conway game of live)

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

'''

import pygame
import sys
import numpy


def backend(grid, cells, board):
	#Note that numpy array is (y,x)
	relive = []
	dying = []
	#For each of alive cells, check their 8 neighbours to see if they survive, and THEN check each of the neighbours
	#to see if it should reanimate
	for cell in cells:
		neighbours = 0
		for i in range(-1,2):
			for j in range(-1,2):
				if not (i == 0 and j == 0):
					if [cell[0] + i, cell[1] + j] in cells:
						neighbours += 1
					dead_neighbour = [cell[0] + i, cell[1] + j]
					live_count = 0
					for x in range(-1,2):
						for y in range(-1,2):
							if not( x == 0 and y == 0):
								if [dead_neighbour[0] + x, dead_neighbour[1] + y] in cells:
									live_count += 1
					if live_count == 3:
						relive.append(dead_neighbour)

		if neighbours < 2 or neighbours > 3:
			dying.append(cell)

	for i in dying:
		cells.remove(i)
	for j in relive:
		if j not in cells:
			cells.append(j)


#Draw the board, copied my previous code
def board_update(screen, grid, multiplier, board, cells):
	screen.fill((255,255,255))
	for i in range(0, grid * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, grid * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (grid * multiplier, i))

	for cell in cells:
		pygame.draw.rect(screen, (0, 0, 0),(cell[0] * multiplier + 1, cell[1] * multiplier + 1, multiplier - 1, multiplier - 1))
	pygame.display.update()


def game(screen, board, grid, cells, Clock, multiplier):
	#If game start is true, starts the game, disallows player to set live cellls and slows down the fps
	stop, game_start = False, False
	while stop == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#Set initial cells when game has not started
		if pygame.mouse.get_pressed()[0] and game_start == False:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // multiplier, mouse_pos[1] // multiplier]
			if mouse_pos not in cells:
				cells.append(mouse_pos)

		#To start the game
		if pygame.key.get_pressed()[pygame.K_SPACE]:
			game_start = True

		if game_start == True:
			#Set the pace of game once it starts
			Clock.tick(3)
			backend(grid, cells, board)

		board_update(screen, grid, multiplier, board, cells)
			

def main():
	pygame.init()
	pygame.display.set_caption('Cellular Automata')
	size = width, height = 750, 750
	grid = 50
	cells = []
	board = numpy.zeros((grid, grid))
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen, board, grid, cells, Clock, 15)

if __name__ == '__main__':
	main()
