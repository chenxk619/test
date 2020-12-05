import pygame
import sys
import numpy
import random
import time

# Game is like a single board instance with unvisited and visited lists as attributes among other things
# The unvisited lists will be appending with all the grid instances, and each instance will be moved to visited
# when they are checked.

#  Ok, so board size is a bit of a headache. Board should be 750 by 750, but i want the grid to be 15,30,50
#depending on difficultly
class Board:
	def __init__(self, grid_size, bomb_perc, resoultion):
		self.grid = grid_size
		self.multiplier = resoultion // grid_size
		self.content = numpy.zeros((grid_size, grid_size))
		self.bomb_perc = bomb_perc
		self.unvisited = []
		self.visited = []


class Grid:
	def __init__(self, pos):
		self.bomb = False
		self.flagged = False
		self.surrounding = 0
		self.pos = pos


def render_digits(node, visited_colour, board, displacement):

	# For visited nodes, the colour of their number, in order of increasing flags will be : NIL(0), blue, green, red,
	# dark blue, dark red(5), cyan, black, grey
	blue = (0, 0, 150)
	green = (0, 150, 0)
	red = (150, 0, 0)
	dark_blue = (0, 0, 255)
	dark_red = (255, 0, 0)
	cyan = (0, 255, 255)
	black = (0, 0, 0)
	grey = (150, 150, 150)

	colour_lst = [blue, green, red, dark_blue, dark_red, cyan, black, grey]

	#create a font and render text on it
	font = pygame.font.SysFont('arial', board.multiplier // 2)
	text = font.render('{}'.format(node.surrounding), True, colour_lst[node.surrounding - 1], (visited_colour, visited_colour, visited_colour))
	#Create the text box
	textRect = text.get_rect()
	textRect.center = (node.pos[0] * board.multiplier + board.multiplier // 2, node.pos[1] * board.multiplier + board.multiplier // 2 + displacement)

	return text, textRect


def update(screen, board, displacement, bomb_list, dead):
	screen_colour = 200

	screen.fill((screen_colour, screen_colour, screen_colour))

	colour = 0
	for i in range(0, board.grid * board.multiplier + 1, board.multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (colour, colour, colour), (i, displacement), (i, board.grid * board.multiplier + displacement))
		# Draw vertical lines
		pygame.draw.line(screen, (colour, colour, colour), (0, i + displacement), (board.grid * board.multiplier, i + displacement))


	#All the visited nodes will be a slightly darker grey
	visited_colour = 150
	for node in board.visited:
		pygame.draw.rect(screen, (visited_colour, visited_colour, visited_colour), (node.pos[0] * board.multiplier + 1,
		node.pos[1] * board.multiplier + 1 + displacement, board.multiplier - 1, board.multiplier - 1))
		if node.surrounding > 0:
			text, textRect = render_digits(node ,visited_colour, board, displacement)
			screen.blit(text, textRect)

	if dead == True:
		for node in bomb_list:
			pygame.draw.rect(screen, (255, 0, 0),(node[0] * board.multiplier + 1,
			node[1] * board.multiplier + 1 + displacement, board.multiplier - 1,board.multiplier - 1))

			pygame.draw.circle(screen, (0, 0, 0), (node[0] * board.multiplier + board.multiplier // 2,
			node[1] * board.multiplier + board.multiplier // 2 + displacement), board.multiplier // 3)

	pygame.display.update()


def explore(board, mouse_pos):
	#Remove the obj that matches the mouse pos in board's unvisited
	target_node = None

	for node in board.unvisited:

		if [node.pos[0], node.pos[1]] == mouse_pos:
			target_node = node
			board.unvisited.remove(target_node)

	#Flag the number of bombs in its neighbours
	flags = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if not (i == 0 and j == 0):
				for k in board.unvisited:
					temp = target_node.pos
					temp = [temp[0] + i, temp[1] + j]
					if [k.pos[0], k.pos[1]] == temp and k.bomb:
						flags += 1


	#Set the targeted node's flags to the correct amount
	target_node.surrounding = flags
	board.visited.append(target_node)



def game(screen, width, displacement):
	#The board size should be changed by the difficultly
	board = Board(10, 20, width)
	start = True
	dead = False
	bomb_list = []

	#loops through the vertical and horizontal length of board, then initializes each coordinate as a grid, then append
	#them to unvisited
	for i in range(len(board.content)):
		for j in range(len(board.content[i])):
			grid = Grid((i,j))
			board.unvisited.append(grid)


	#Set a few grids to contain bombs
	while len(bomb_list) != (board.grid * board.grid) * board.bomb_perc//100 :
		x = random.randint(0, board.grid - 1)
		y = random.randint(0, board.grid - 1)
		if [x,y] not in bomb_list:
			bomb_list.append([x,y])

	print(len(bomb_list))
	for node in board.unvisited:
		if [node.pos[0], node.pos[1]] in bomb_list:
			node.bomb = True

	#Main game loop
	while start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if pygame.mouse.get_pressed()[0]:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // board.multiplier, (mouse_pos[1] - displacement) // board.multiplier]

			#Check if u go KA-BOOOM
			if mouse_pos in bomb_list:
				dead = True

			for node in board.unvisited:
				#This is needed as mouse_pos is a list, but node.pos is a tuple
				if mouse_pos[0] == node.pos[0] and mouse_pos[1] == node.pos[1]:
					explore(board, mouse_pos)

		elif pygame.mouse.get_pressed()[2]:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // board.multiplier, (mouse_pos[1] - displacement) // board.multiplier]

		update(screen, board, displacement, bomb_list, dead)



def main():

	pygame.init()
	pygame.display.set_caption('Minesweeper')

	flag_img = pygame.image.load('flag.png')
	bomb_img = pygame.image.load('minesweeper_bomb.png')
	displacement = 40
	size = width, height = 750, 750 + displacement
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	screen.blit(flag_img, (200,200))
	game(screen, width, displacement)

while __name__ == '__main__':
	main()