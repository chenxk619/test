import pygame
import sys
import numpy
import random
import time

# Game is like a single board instance with unvisited and visited lists as attributes among other things
# The unvisited lists will be appending with all the grid instances, and each instance will be moved to visited
# when they are checked.

# Ok, so board size is a bit of a headache. Board should be 750 by 750, but i want the grid to be 15,30,50
# depending on difficultly
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



# To render all the digits shown on a node when it is not a bomb (only if there is more than 1 surrounding bomb)
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

	# create a font and render text on it
	font = pygame.font.SysFont('arial', board.multiplier // 2)
	text = font.render('{}'.format(node.surrounding), True, colour_lst[node.surrounding - 1], (visited_colour, visited_colour, visited_colour))
	# Create the text box
	textRect = text.get_rect()
	textRect.center = (node.pos[0] * board.multiplier + board.multiplier // 2, node.pos[1] * board.multiplier + board.multiplier // 2 + displacement)

	return text, textRect



# Used to convey the difficulty choosing at the start, and to show the flags remaining and timer
def render_text(text_shown, pos, bomb_lst, flag_lst):

	if text_shown == '':
		font = pygame.font.SysFont('arial', 20)
		num = len(bomb_lst) - len(flag_lst)
		text = font.render('Bombs remaining : ' + str(num), True, (0, 0, 0), (200, 200, 200))

		textRect = text.get_rect()
		textRect.center = pos

	else:

		font = pygame.font.SysFont('arial', 20)
		text = font.render(text_shown, True, (0,0,0), (200, 200, 200))

		textRect = text.get_rect()
		textRect.center = pos

	return text, textRect



# Basically a board update function, to fill the screen, draw the lines, to draw all the visited and flagged nodes
# and to show the bombs if you die.
def update(screen, board, displacement, bomb_lst, dead, flag_lst, flag_img, bomb_img, intial_text, intial_pos,
		   flag_text, flag_rect, game_start, start_time):

	screen_colour = 200
	screen.fill((screen_colour, screen_colour, screen_colour))

	#At the start to display the text
	if len(board.unvisited) == 0:
		screen.blit(intial_text, intial_pos)

	colour = 0
	for i in range(0, board.grid * board.multiplier + 1, board.multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (colour, colour, colour), (i, displacement), (i, board.grid * board.multiplier + displacement))
		# Draw vertical lines
		pygame.draw.line(screen, (colour, colour, colour), (0, i + displacement), (board.grid * board.multiplier, i + displacement))


	# All the visited nodes will be a slightly darker grey
	visited_colour = 150
	for node in board.visited:
		pygame.draw.rect(screen, (visited_colour, visited_colour, visited_colour), (node.pos[0] * board.multiplier + 1,
		node.pos[1] * board.multiplier + 1 + displacement, board.multiplier - 1, board.multiplier - 1))
		if node.surrounding > 0:
			text, textRect = render_digits(node ,visited_colour, board, displacement)
			screen.blit(text, textRect)

	# Display flags clicked on
	for node in flag_lst:
		screen.blit(flag_img, (node[0] * board.multiplier + 1, node[1] * board.multiplier + 1 + displacement))

	# Show bombs if dead
	if dead:
		for node in bomb_lst:
			screen.blit(bomb_img, (node[0] * board.multiplier + 1, node[1] * board.multiplier + 1 + displacement))

	# Check if you won
	won = False
	if game_start:
		won = True
		for node in board.unvisited:
			if not node.bomb:
				won = False
		if won:
			print('won')
			won = True
			text_shown = 'Congrats! You did not explode'
			pos = (350, 20)
			won_text, won_pos = render_text(text_shown, pos, bomb_lst, flag_lst)
			screen.blit(won_text, won_pos)

	#Update the number of bombs left
	screen.blit(flag_text, flag_rect)

	#Update time
	if game_start:
		time_pos = (50, 20)
		time_text = time.time() - start_time
		time_text, time_pos = render_text('Time: ' + str(int(time_text)), time_pos, bomb_lst, flag_lst)
		screen.blit(time_text, time_pos)

	pygame.display.update()

	# End game condition
	if dead or won:
		time.sleep(3)
		return False
	return True



#Explore function used to check the number of surrounding bombs in a certain node's vercinity (only called when a node
# is clicked)
def explore(board, mouse_pos):
	#Remove the obj that matches the mouse pos in board's unvisited
	target_node = None

	for node in board.unvisited:

		if [node.pos[0], node.pos[1]] == mouse_pos:
			target_node = node
			board.unvisited.remove(target_node)

	# Flag the number of bombs in its neighbours
	flags = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if not (i == 0 and j == 0):
				for k in board.unvisited:
					temp = target_node.pos
					temp = [temp[0] + i, temp[1] + j]
					if [k.pos[0], k.pos[1]] == temp and k.bomb:
						flags += 1


	# Set the targeted node's flags to the correct amount
	target_node.surrounding = flags
	board.visited.append(target_node)



# Setup used to scale the flag_img, bomb_img. Also to append grid instances to board attribute and to set a few grids
# to contain bombs
def setup(board, flag_img, bomb_img, bomb_lst):

	# Scales the flag and bomb images to fit within the grid
	flag_img = pygame.transform.scale(flag_img, (board.multiplier, board.multiplier))
	bomb_img = pygame.transform.scale(bomb_img, (board.multiplier, board.multiplier))

	# loops through the vertical and horizontal length of board, then initializes each coordinate as a grid, then append
	# them to unvisited
	start_pos = None
	for i in range(board.grid):
		for j in range(board.grid):
			grid = Grid((i,j))

			# For grid in this range dont have to worry about bomb
			if i in range(board.grid // 2 - 1, board.grid // 2 ) and j in range(board.grid // 2 - 1, board.grid // 2 ):
				start_pos = grid
				board.visited.append(start_pos)

			if grid not in board.visited:
				board.unvisited.append(grid)

	# Set a few grids to contain bombs
	while len(bomb_lst) != (board.grid * board.grid) * board.bomb_perc//100 :
		x = random.choice([random.randint(0, board.grid // 2 -2), random.randint(board.grid // 2 + 2, board.grid - 1)])
		y = random.choice([random.randint(0, board.grid // 2 -2), random.randint(board.grid // 2 + 2, board.grid - 1)])
		if [x,y] not in bomb_lst:
			bomb_lst.append([x,y])

	for node in board.unvisited:
		if [node.pos[0], node.pos[1]] in bomb_lst:
			node.bomb = True

	return flag_img, bomb_img, bomb_lst



def game(screen, width, displacement, flag_img, bomb_img, Clock):

	# The board size should be changed by the difficultly
	start = True
	dead = False
	game_start = False
	button = set()
	bomb_lst = []
	flag_lst = []
	start_time = 0


	# Intialitial state of board
	board = Board(1, 1, width)
	text_shown = 'Enter 1, 2 or 3 to correspond to easy, normal or hard'
	pos = (350, 200)
	intial_text, intial_pos = render_text(text_shown, pos, bomb_lst, flag_lst)

	flag_text, flag_rect = intial_text, intial_pos

	# Main game loop
	while start:

		button_up = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# The next 2 events are to check if a mouse 2 is pressed and THEN released, which is crucial for the flagging
			# mechanic, otherwise it would flag on and off rapidly
			if pygame.mouse.get_pressed()[2]:
				button.add(1)

			if event.type == pygame.MOUSEBUTTONUP and len(button) == 1:
				button.clear()
				button_up = True

		# Before the game starts, this is used to choose the difficulty settings
		if game_start == False:
			if pygame.key.get_pressed()[pygame.K_1]:
				grid_size, bomb_perc = 15, 10
				board = Board(grid_size, bomb_perc, width)
				flag_img, bomb_img, bomb_lst = setup(board, flag_img, bomb_img, bomb_lst)
				game_start = True

			elif pygame.key.get_pressed()[pygame.K_2]:
				grid_size, bomb_perc = 25, 15
				board = Board(grid_size, bomb_perc, width)
				flag_img, bomb_img, bomb_lst = setup(board, flag_img, bomb_img, bomb_lst)
				game_start = True

			elif pygame.key.get_pressed()[pygame.K_3]:
				grid_size, bomb_perc = 35, 20
				board = Board(grid_size, bomb_perc, width)
				flag_img, bomb_img, bomb_lst = setup(board, flag_img, bomb_img, bomb_lst)
				game_start = True

		if game_start and start_time == 0:
			start_time = time.time()

		# If a grid clicked on is not flagged
		if pygame.mouse.get_pressed()[0] and game_start:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // board.multiplier, (mouse_pos[1] - displacement) // board.multiplier]
			for node in board.unvisited:
				if [node.pos[0], node.pos[1]] == mouse_pos and node.flagged == False:

					# Check if u go KA-BOOOM
					if mouse_pos in bomb_lst:
						dead = True

					for node in board.unvisited:
						# This is needed as mouse_pos is a list, but node.pos is a tuple
						if mouse_pos[0] == node.pos[0] and mouse_pos[1] == node.pos[1]:
							explore(board, mouse_pos)


		# Right mouse button to flag shit, but only if the button_up flag from earlier is True
		if button_up and game_start:
			mouse_pos = pygame.mouse.get_pos()
			mouse_pos = [mouse_pos[0] // board.multiplier, (mouse_pos[1] - displacement) // board.multiplier]

			for node in board.unvisited:
				if [node.pos[0], node.pos[1]] == mouse_pos:
					if node.flagged == False:
						node.flagged = True
						if mouse_pos not in flag_lst:
							flag_lst.append(mouse_pos)
					else:
						node.flagged = False
						if mouse_pos in flag_lst:
							flag_lst.remove(mouse_pos)

		# Instant solve for dev use
		if pygame.mouse.get_pressed()[1] and pygame.key.get_pressed()[pygame.K_z]:
			print('solve')
			for node in board.unvisited:
				if not node.bomb:
					board.unvisited.remove(node)
					board.visited.append(node)


		# Render the number of flags left
		if game_start:
			flag_pos = (600, 20)
			flag_text, flag_rect = render_text('', flag_pos, bomb_lst, flag_lst)

		Clock.tick(20)

		start = update(screen, board, displacement, bomb_lst, dead, flag_lst, flag_img, bomb_img, intial_text,
					   intial_pos, flag_text, flag_rect, game_start, start_time)



def main():

	pygame.init()
	pygame.display.set_caption('Minesweeper')
	flag_img = pygame.image.load('flag.png')
	bomb_img = pygame.image.load('minesweeper_bomb.png')
	displacement = 40
	size = width, height = 750, 750 + displacement
	Clock = pygame.time.Clock()
	screen = pygame.display.set_mode(size)
	game(screen, width, displacement, flag_img, bomb_img, Clock)

while __name__ == '__main__':
	main()