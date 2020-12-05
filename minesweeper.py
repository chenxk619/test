import pygame
import sys
import numpy
import time

# Game is like a single board instance with unvisited and visited lists as attributes among other things
# The unvisited lists will be appending with all the grid instances, and each instance will be moved to visited
# when they are checked.

#  Ok, so board size is a bit of a headache. Board should be 750 by 750, but i want the grid to be 15,30,50
#depending on difficultly
class Board:
	def __init__(self, grid_size, resoultion):
		self.grid = grid_size
		self.multiplier = resoultion // grid_size
		self.content = numpy.zeros((grid_size, grid_size))
		self.unvisited = []
		self.visited = []


class Grid:
	def __init__(self, pos):
		self.bomb = False
		self.flagged = False
		self.flags = 0
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


def explore(board, mouse_pos):
	#Remove the obj that matches the mouse pos in board's unvisited
	target_node = None
	for node in board.unvisited:
		if node.pos == mouse_pos:
			target_node = node
			board.unvisited.remove(target_node)

	#Flag the number of bombs in its neighbours
	flags = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if not (i == 0 and j == 0):
				idx = board.unvisited.index((mouse_pos[0] + i, mouse_pos[1] + j))
				if board.unvisited[idx].flagged:
					flags += 1

	#Set the targeted node's flags to the correct amount
	target_node.flags = flags
	board.visited.append(target_node)




def game(screen, width, displacement):
	#The board size should be changed by the difficultly
	board = Board(10, width)
	start = True

	#loops through the vertical and horizontal length of board, then initializes each coordinate as a grid, then append
	#them to unvisited
	for i in range(len(board.content)):
		for j in range(len(board.content[i])):
			grid = Grid((i,j))
			board.unvisited.append(grid)

	for i in board.unvisited:
		print(i.pos)

	while start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if pygame.mouse.get_pressed()[0]:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // board.multiplier, mouse_pos[1] // board.multiplier]
			if mouse_pos in board.unvisited:
				explore(board, mouse_pos)

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