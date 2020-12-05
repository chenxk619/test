import pygame
import sys
import numpy
import time

#  Ok, so board size is a bit of a headache. Board should be 750 by 750, but i want the grid to be 15,30,50
#depending on difficultly
class Board:
	def __init__(self, grid_size, resoultion):
		self.grid = grid_size
		self.multiplier = resoultion // grid_size
		self.content = numpy.zeros((grid_size, grid_size))

class Grid:
	def __init__(self, pos):
		self.bomb = False
		self.flagged = False
		self.pos = pos


def update(screen, board, displacement):
	screen_colour = 200

	screen.fill((screen_colour, screen_colour, screen_colour))

	colour = 0
	for i in range(0, board.grid * board.multiplier + 1, board.multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (colour, colour, colour), (i, displacement), (i, board.grid * board.multiplier + displacement))
		# Draw vertical lines
		pygame.draw.line(screen, (colour, colour, colour), (0, i + displacement), (board.grid * board.multiplier, i + displacement))
	pygame.display.update()

def game(screen, width, displacement):
	#The board size should be changed by the difficultly
	board = Board(10, width)
	start = True
	unvisited = []
	visited = []

	#loops through the vertical and horizontal length of board, then initializes each coordinate as a grid, then append
	#them to unvisited
	for i in range(len(board.content)):
		for j in range(len(board.content[i])):
			grid = Grid((i,j))
			unvisited.append(grid)

	for i in unvisited:
		print(i.pos)

	while start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if pygame.mouse.get_pressed()[0]:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // board.multiplier, mouse_pos[1] // board.multiplier]

		update(screen, board, displacement)



def main():

	pygame.init()
	pygame.display.set_caption('Minesweeper')
	displacement = 40
	size = width, height = 750, 750 + displacement
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen, width, displacement)

while __name__ == '__main__':
	main()