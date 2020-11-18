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


def game(start_pos, end_pos, start_state):
	#Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.K_SPACE:
				start_state = True

			#Select start node pos
			if pygame.mouse.get_pressed()[0] and event.type == pygame.K_1:
				mouse_position = pygame.mouse.get_pos()
				start_pos = [mouse_position[0] // 10, mouse_position[1] // 10]

			#Select end node pos
			if pygame.mouse.get_pressed()[0] and event.type == pygame.K_2:
				mouse_position = pygame.mouse.get_pos()
				end_pos = [mouse_position[0] // 10, mouse_position[1] // 10]

			#Only able to select barricades if the 'game' hasnt started
			if pygame.mouse.get_pressed()[0] and start_state == False and start_pos is not None and end_pos is not None:
				mouse_position = pygame.mouse.get_pos()
				print(mouse_position)

			# Driver code
			def main():
				# start, end = start_end()
				start, end = Nodes([1, 1], [6, 7], [1, 1], [0, 0], 0), Nodes([1, 1], [6, 7], [6, 7], [0, 0], 0)
				visited, unvisited, barricades, node_path = set(), set(), [], []
				for i in range(30):
					find(start, end, visited, unvisited, node_path, barricades)
					print('=============')

		board_init_state()


#When starting the game
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
game(False, False, False)




