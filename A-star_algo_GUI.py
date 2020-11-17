import pygame
import sys
from A_star_algo import *

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

class Board_gui:
	def __init__(self):
		self.x_lines = Board.x_length + 1
		self.y_lines = Board.y_length + 1



#Main game loop
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if pygame.mouse.get_pressed()[0]:
			mouse_position = pygame.mouse.get_pos()
			print(mouse_position)



	screen.fill((255, 255, 255))
	pygame.display.update()
