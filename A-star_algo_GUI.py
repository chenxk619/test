import pygame
import sys
import time

class Board:
	x_length = 50
	y_length = 50


class Nodes:

	def __init__(self,start, end, prev_node_pos, pos_from_prev, prev_G_cost):
		#(y,x) coord of the start node
		self.start = start
		#(y,x) coord of the end node
		self.end = end
		#pos of the prev node that explored this node
		self.prev_node_pos = prev_node_pos
		#current node pos is the prev node and difference in pos
		self.node_pos = [x + y for x, y in zip(prev_node_pos, pos_from_prev)]
		#distance from previous node and G_cost of that node
		self.G_cost = (((10 * pos_from_prev[0])** 2 + (10 * pos_from_prev[1])** 2) ** 0.5) + prev_G_cost
		#distance from end node
		self.F_cost = self.get_cost(self.end)
		#CHANGE THIS LATER ON, H_COST SHOULD BE THE LOWEST OF ITS NEIGHBOURING NODES, NOT THE START
		self.H_cost = int(self.G_cost + self.F_cost)

	#distance from start node/end node
	def get_cost(self, pos):
		#This means that this node and start are diagonal
		x_distance = abs(self.node_pos[0] - pos[0])
		y_distance = abs(self.node_pos[1] - pos[1])

		if x_distance == y_distance:
			#return diagonal distance
			return ((10 * x_distance) ** 2 + (10 * y_distance) ** 2) ** 0.5

		elif x_distance == 0:
			return 10 * y_distance

		elif y_distance == 0:
			return 10 * x_distance

		else:
			#split it into diagnoal distance AND horizonatal/vertical distance
			# Eg: (5,2) -- (2,2) + (3,0)
			if x_distance > y_distance:
				return (((10 * y_distance) ** 2 + (10 * y_distance) ** 2) ** 0.5) + (10 * (x_distance - y_distance))

			else:
				return (((10 * x_distance) ** 2 + (10 * x_distance) ** 2) ** 0.5) + (10 * (y_distance - x_distance))


def find(start, end, visited, unvisited, node_path, barricades):
	stop = False
	#first time visiting the board
	if len(visited) == 0:
		visited.add(start)
		for i in range(-1, 2):
			for j in range(-1, 2):

				#To not add the same node it is currently at and to avoid the node from going out of bounds and prevent
				#if from colliding with the barricades
				if i != 0 or j != 0 and start.node_pos[0] + i >= 0  and start.node_pos[0] + i < Board.y_length \
						and start.node_pos[1] + j >= 0 and start.node_pos[1] + j < Board.x_length and \
						[start.node_pos[0] + i,start.node_pos[1] + j] not in barricades:
					#If the end is found (next to the start)

					if start.node_pos[0] + i == end.node_pos[0] and start.node_pos[1] + j == end.node_pos[1]:
						print('Path : {} - {}'.format(start.node_pos, end.node_pos))

					#Instantiate the Nodes surrounding the start node and append them to unvisited list
					unvisited.add(Nodes(start.node_pos, end.node_pos, [start.node_pos[0] , start.node_pos[1]], [i, j], 0))


	else:
		#find the smallest H_cost node in unvisited list, then set it to visited and find the unvisited nodes around it
		cur_node_val, cur_node = 10000, None

		#Get the smallest node in unvisited, then remove it from unvisited and add it to visited
		for i in unvisited:
			if cur_node_val > i.H_cost and i.node_pos not in [k.node_pos for k in visited]:
				cur_node_val, cur_node =  i.H_cost, i

		unvisited.remove(cur_node)
		visited.add(cur_node)

		for i in range(-1, 2):
			if stop == True:
				break
			for j in range(-1, 2):
				if stop == True:
					break

				if (i != 0 or j != 0) and cur_node.node_pos[0] + i >= 0 and cur_node.node_pos[1] + j >= 0 and \
						cur_node.node_pos[0] + i < Board.y_length and cur_node.node_pos[1] + j < Board.y_length and \
						[cur_node.node_pos[0] + i,cur_node.node_pos[1] + j] not in barricades:

					#If current node reaches the end node
					if cur_node.node_pos[0] + i == end.node_pos[0] and cur_node.node_pos[1] + j == end.node_pos[1]:
						#To get the fastest path, from the end node, find the nearest node to the start node
						backtrack_node_pos = [end.node_pos]
						while backtrack_node_pos != [start.node_pos]:
							try:
								#Candidates of nodes whose position is within +-1 range (x,y) of the backtrack node, and has the smallest G_cost value(distance from start)
								candidates = set(node for node in visited if abs(backtrack_node_pos[0][0] - node.node_pos[0]) < 2
											  and abs(backtrack_node_pos[0][1] - node.node_pos[1]) < 2)
								#backtrack node set to the node_pos in candidates
								backtrack_node_pos = [node.node_pos for node in candidates if node.G_cost == min([k.G_cost for k in candidates])]
								#Add correct nodes to node_path
								node_path.append(backtrack_node_pos)
								#Remove the set of previous node pos
								visited -= candidates
							except IndexError:
								stop = True


					#Instantiate the Nodes surrounding the start node and append them to unvisited list
					unvisited.add(Nodes(start.node_pos, end.node_pos, [cur_node.node_pos[0], cur_node.node_pos[1]], [i,j], cur_node.G_cost))


def board_init_state(start_pos, end_pos, barricades, visited, unvisited, node_path, screen, multiplier):
	screen.fill((255, 255, 255))
	for i in range(0, 50 * multiplier + 1, multiplier):
		# Draw horizontal lines
		pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 50 * multiplier))
		# Draw vertical lines
		pygame.draw.line(screen, (0, 0, 0), (0, i), (50 * multiplier, i))

	#Update the start_node, end_node, barricades
	#draw rect argu is (pygame.draw.rect(window, color, (x, y, width, height))
	#Start = Blue (0,0,255), end = purple(204,0,204), visited = red(255,0,0), unvisited = green(0,255,0), barricades = black(0,0,0), node_path = yellow(255,255,0)


	if len(barricades) > 0:
		# Draw barricades
		for nodes in barricades:
			pygame.draw.rect(screen, (0, 0, 0), (nodes[0] * multiplier + 1, nodes[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	if len(unvisited) > 0 :
		#Draw visited nodes
		for nodes in unvisited:
			pygame.draw.rect(screen, (0, 255, 0), (nodes.node_pos[0] * multiplier + 1, nodes.node_pos[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	if len(visited) > 0:
		#Draw visited nodes
		for nodes in visited:
			pygame.draw.rect(screen, (255, 0, 0), (nodes.node_pos[0] * multiplier + 1, nodes.node_pos[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	if len(node_path) >0 :
		#Draw visited nodes
		for nodes in node_path:
			pygame.draw.rect(screen, (255, 255, 0), (nodes[0][0] * multiplier + 1, nodes[0][1] * multiplier + 1, multiplier - 1, multiplier - 1))

	if start_pos is not None:
		#Draw start node
		pygame.draw.rect(screen, (0,0,255), (start_pos[0] * multiplier + 1, start_pos[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	if end_pos is not None:
		#Draw end node
		pygame.draw.rect(screen, (204, 0, 204), (end_pos[0] * multiplier + 1, end_pos[1] * multiplier + 1, multiplier - 1, multiplier - 1))

	pygame.display.update()

def game(start_pos, end_pos, screen, multiplier):

	start_state, stop, skip = False, False, False
	visited, unvisited, node_path, barricades = set(), set(), [], []

	#Main game loop
	while not stop:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#For selecting start, end pos and barricades, they can only be done before game starts
		#Select start node pos
		if pygame.mouse.get_pressed()[0] and pygame.key.get_pressed()[pygame.K_1] and start_state == False:
			mouse_position = pygame.mouse.get_pos()
			if start_pos is None:
				start_pos = [mouse_position[0] // multiplier, mouse_position[1] // multiplier]

		#Select end node pos
		if pygame.mouse.get_pressed()[0] and pygame.key.get_pressed()[pygame.K_2] and start_state == False:
			mouse_position = pygame.mouse.get_pos()
			if end_pos is None:
				end_pos = [mouse_position[0] // multiplier, mouse_position[1] // multiplier]

		#Only able to select barricades if the 'game' hasnt started and both start and end node pos are selected
		if pygame.mouse.get_pressed()[0] and start_pos is not None and end_pos is not None and \
				pygame.key.get_pressed()[pygame.K_3] and start_state == False:
			mouse_position = pygame.mouse.get_pos()
			pos = [mouse_position[0] // multiplier, mouse_position[1] // multiplier]
			if pos not in barricades:
				barricades.append(pos)

		#Press space to start the game (if start_pos and end_pos are not None)
		if pygame.key.get_pressed()[pygame.K_SPACE] and start_pos is not None and end_pos is not None:
			start_state = True

		#Press left shift to skip the game (if start_pos and end_pos are not None)
		if pygame.key.get_pressed()[pygame.K_LSHIFT] and start_pos is not None and end_pos is not None:
			skip, start_state = True, True

		# Driver code
		if start_state:
			# start, end = start_end()
			start, end = Nodes(start_pos, end_pos, start_pos, [0, 0], 0), Nodes(start_pos, end_pos, end_pos, [0, 0], 0)
			find(start, end, visited, unvisited, node_path, barricades)
			#End node found and appended to node_path
			if len(node_path) > 0:
				stop = True
				#If skipping using shift
				if skip == True:
					board_init_state(start_pos, end_pos, barricades, visited, unvisited, node_path, screen, multiplier)

		#If not skipping using shift
		if skip == False:
			board_init_state(start_pos, end_pos, barricades, visited, unvisited, node_path, screen, multiplier)



def main():
	#When starting the game
	multiplier = 15
	pygame.init()
	pygame.display.set_caption('A* pathing algo')
	size = width, height = 50 * multiplier, 50 * multiplier
	screen = pygame.display.set_mode(size)
	game(None, None, screen, multiplier)
	time.sleep(3)

while __name__ == '__main__':
	main()
