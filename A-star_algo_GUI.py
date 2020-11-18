import pygame
import sys
from A_star_algo import *


class Board_gui:
	def __init__(self):
		self.x_lines = Board.x_length + 1
		self.y_lines = Board.y_length + 1

	def draw_barricades(self):
		pass


def board_init_state(start_pos, end_pos, barricades):
	screen.fill((255, 255, 255))
	for i in range(0, 501, 10):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 500))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (500, i))

	#Update the start_node, end_node, barricades
	#draw rect argu is (pygame.draw.rect(window, color, (x, y, width, height))
	#Start = Blue (0,0,255), end = purple(204,0,204), visited = red(255,0,0), unvisited = green(0,255,0), barricades = black(0,0,0), node_path = yellow(255,255,0)
	if start_pos is not None:
		#Draw start node
		pygame.draw.rect(screen, (0,0,255), (start_pos[0] * 10 + 1, start_pos[1] * 10 + 1, 9, 9))

	if end_pos is not None:
		#Draw end node
		pygame.draw.rect(screen, (204, 0, 204), (end_pos[0] * 10 + 1, end_pos[1] * 10 + 1, 9, 9))

	if len(barricades) > 0:
		# Draw barricades
		for barricade in barricades:
			pygame.draw.rect(screen, (0, 0, 0), (barricade[0] * 10 + 1, barricade[1] * 10 + 1, 9, 9))
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

			#Press space to start the game (if start_pos and end_pos are not None)
			if pygame.key.get_pressed()[pygame.K_SPACE] and start_pos is not None and end_pos is not None:
				start_state = True

			# Driver code
			if start_state:
				# start, end = start_end()
				start, end = Nodes(start_pos, end_pos, start_pos, [0, 0], 0), Nodes(start_pos, end_pos, end_pos, [0, 0], 0)
				visited, unvisited, node_path = set(), set(), []
				for i in range(30):
					find(start, end, visited, unvisited, node_path, barricades)
					print('=============')

		board_init_state(start_pos, end_pos, barricades)


#When starting the game
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
game(None, None)




