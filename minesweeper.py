import pygame
import sys
import numpy
import time

class Board:
	def __init__(self, grid_size):
		self.grid = grid_size
		self.multiplier = 15
		self.content = numpy.zeros((self.grid, self.grid))

class Grid:
	def __init__(self, pos):
		self.bomb = False
		self.flagged = False
		self.pos = pos


def update(screen, board):
	screen.fill((255,255,255))

	colour = 0
	for i in range(0, board.grid * board.multiplier + 1, board.multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (colour, colour, colour), (i, 0), (i, board.grid * board.multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (colour, colour, colour), (0, i), (board.grid * board.multiplier, i))
	pygame.display.update()

def game(screen):
	#The board size should be changed by the difficultly
	board = Board(50)
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

		update(screen, board)



def main():

	pygame.init()
	pygame.display.set_caption('Minesweeper')
	size = width, height = 750, 750
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen)

while __name__ == '__main__':
	main()