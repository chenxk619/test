import pygame
import sys
import time
import numpy

#The demo should include dfs, bfs, A*, dijkastra's and the window should be able to resize, the search should be able to
#run smoothly and should a grdual search for the grid and an instantanial version. Demo should be able to restart easily

class Board:
	def __init__(self, grid_size):
		#The number of grids in the board, and the actual board itself
		self.grid_size = grid_size
		self.content = numpy.zeros((grid_size, grid_size))

def render(grid_size, const, screen, displacement):

	black = (0,0,0)
	white = (255,255,255)

	screen.fill(white)
	#Draw vertical lines
	for i in range(grid_size):
		pygame.draw.line(screen, black, (i * const, displacement), (i * const, const * grid_size + displacement))
	#Draw horizontal lines
	for i in range(grid_size):
		pygame.draw.line(screen, black, (0, i * const + displacement), (const * grid_size, i * const + displacement))

	pygame.display.update()

def update():
	pass

def setup():
	pass

def game(screen, grid_size, const, displacement):
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		render(grid_size, const, screen, displacement)


def main():

	grid_size = 25
	const = 690 // grid_size
	displacement = 100
	pygame.init()
	pygame.display.set_caption('A* pathing algo')
	size = width, height = const * grid_size, const * grid_size + displacement
	screen = pygame.display.set_mode(size)
	game(screen, grid_size, const, displacement)
	time.sleep(5)


main()
