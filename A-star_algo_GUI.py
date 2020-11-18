import pygame
import sys
from A_star_algo import *


class Board_gui:
	def __init__(self):
		self.x_lines = Board.x_length + 1
		self.y_lines = Board.y_length + 1

	def draw_barricades(self):
		pass


def board_init_state():
	screen.fill((255, 255, 255))
	for i in range(0, 501, 10):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 500))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (500, i))
	pygame.display.update()


def game(start_pos, end_pos):
	barricades = []
	game_start = False
	start_state = False
	#Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if pygame.key.get_pressed()[pygame.K_SPACE]:
				start_state = True

			#Select start node pos
			if pygame.mouse.get_pressed()[0] and pygame.key.get_pressed()[pygame.K_1]:
				mouse_position = pygame.mouse.get_pos()
				if start_pos is None:
					start_pos = [mouse_position[0] // 10, mouse_position[1] // 10]

			#Select end node pos
			if pygame.mouse.get_pressed()[0] and pygame.key.get_pressed()[pygame.K_2]:
				mouse_position = pygame.mouse.get_pos()
				if end_pos is None:
					end_pos = [mouse_position[0] // 10, mouse_position[1] // 10]

			#Only able to select barricades if the 'game' hasnt started and both start and end node pos are selected
			if pygame.mouse.get_pressed()[0] and start_pos is not None and end_pos is not None and pygame.key.get_pressed()[pygame.K_3]:
				mouse_position = pygame.mouse.get_pos()
				pos = [mouse_position[0] // 10, mouse_position[1] // 10]
				if pos not in barricades:
					barricades.append(pos)
				print(barricades)

			# Driver code
			if start_state:
				# start, end = start_end()
				start, end = Nodes(start_pos, end_pos, start_pos, [0, 0], 0), Nodes(start_pos, end_pos, end_pos, [0, 0], 0)
				visited, unvisited, node_path = set(), set(), []
				for i in range(30):
					find(start, end, visited, unvisited, node_path, barricades)
					print('=============')

		board_init_state()


#When starting the game
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
game(None, None)




