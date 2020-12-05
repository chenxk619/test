import pygame
import sys
import time

class Board:
	def __init__(self):
		self.s_grid = 30
		self.m_grid = 50
		self.b_grid = 70
		self.multiplier = 15



def game(screen):

	start = True
	while start == True:
		for event in pygame.event.get():
			if event == pygame.QUIT:
				sys.exit()



def main():

	pygame.init()
	pygame.display.set_caption('Minesweeper')
	size = width, height = 750, 750
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen)

while __name__ == '__main__':
	main()