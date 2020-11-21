import numpy as np


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


def start_end():
	print('Please enter a start and end position in tuples(they cannot be the same)')
	while True:
		###make this work
		try:
			start = tuple(input('Start: '))
			end = tuple(input('End: '))
			if start != end and len(start) == len(end) == 3:
				#Had to use list comprehension with join to change a string of list to a list lol
				return [int(i) for i in ''.join(start) if i != ','], [int(j) for j in ''.join(end) if j != ',']
		except:
			continue

#Legend(what the board shows) : unknown = 0, start = 1, end = 10, visited = 3, surrounding = 5
def draw(start, end, visited, unvisited, node_path, barricades):
	draw_board = np.zeros((Board.x_length, Board.y_length))

	for node in unvisited:
		draw_board[node.node_pos[0]][node.node_pos[1]] = 5

	for node in barricades:
		draw_board[node[0]][node[1]] = 9

	for node in visited:
		draw_board[node.node_pos[0]][node.node_pos[1]] = 3

	for node in node_path:
		print(node)
		draw_board[node[0][0]][node[0][1]] = 7

	draw_board[start.node_pos[0]][start.node_pos[1]] = 1
	draw_board[end.node_pos[0]][end.node_pos[1]] = 10
	print(draw_board)


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


def main():
	#start, end = start_end()
	start,end = Nodes([1,1], [6,7], [1,1], [0,0], 0), Nodes([1,1], [6,7], [6,7], [0,0], 0)
	visited, unvisited, barricades, node_path= set(), set(), [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5]], []
	while [end.node_pos] != [start.node_pos]:
		find(start,end, visited, unvisited, node_path, barricades)
		#draw(start, end, visited, unvisited, node_path, barricades)
		#print('=============')




if __name__ == '__main__':
	board = Board()
	main()
