import numpy as np
import time

class Board:
	x_length = 8
	y_length = 8


class Nodes:

	def __init__(self,start, end, node_pos):
		#(y,x) coord of the start node
		self.start = start
		#(y,x) coord of the end node
		self.end = end
		#node pos
		self.node_pos = node_pos
		#distance from starting node
		self.G_cost = self.get_cost(self.start)
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
def draw(start, end, visited, unvisited, node_path):
	draw_board = np.zeros((Board.x_length, Board.y_length))

	for node in unvisited:
		draw_board[node.node_pos[0]][node.node_pos[1]] = 5

	for node in visited:
		draw_board[node.node_pos[0]][node.node_pos[1]] = 3

	for node in node_path:
		print(node)
		draw_board[node[0][0]][node[0][1]] = 7

	draw_board[start.node_pos[0]][start.node_pos[1]] = 1
	draw_board[end.node_pos[0]][end.node_pos[1]] = 10
	print(draw_board)


def find(start, end, visited, unvisited, node_path):
	#first time visiting the board
	if len(visited) == 0:
		visited.add(start)
		for i in range(-1, 2):
			for j in range(-1, 2):

				#To not add the same node it is currently at and to avoid the node from going out of bounds
				if i != 0 or j != 0 and start.node_pos[0] + i >= 0 and start.node_pos[1] + j >= 0:
					#If the end is found (next to the start)

					if start.node_pos[0] + i == end.node_pos[0] and start.node_pos[1] + j == end.node_pos[1]:
						print('Path : {} - {}'.format(start.node_pos, end.node_pos))

					#Instantiate the Nodes surrounding the start node and append them to unvisited list
					unvisited.add(Nodes(start.node_pos, end.node_pos, [start.node_pos[0] + i, start.node_pos[1] + j]))


	else:
		#find the smallest H_cost node in unvisited list, then set it to visited and find the unvisited nodes around it
		cur_node_val, cur_node = 10000, None

		#Get the smallest node in unvisited, then remove it from unvisited and add it to visited
		for i in unvisited:
			if cur_node_val > i.H_cost and i.node_pos not in [k.node_pos for k in visited]:
				cur_node_val, cur_node =  i.H_cost, i

		print(cur_node.node_pos)

		unvisited.remove(cur_node)
		visited.add(cur_node)

		for i in range(-1, 2):
			for j in range(-1, 2):

				if (i != 0 or j != 0) and cur_node.node_pos[0] + i >= 0 and cur_node.node_pos[1] + j >= 0:

					if cur_node.node_pos[0] + i == end.node_pos[0] and cur_node.node_pos[1] + j == end.node_pos[1]:
						#To get the fastest path, from the end node, find the nearest node to the start node
						backtrack_node_pos = [end.node_pos]
						while backtrack_node_pos != [start.node_pos]:
							#Candidates of nodes whose position is within +-1 range (x,y) of the backtrack node, and has the smallest G_cost value(distance from start)
							candidates = set(node for node in visited if abs(backtrack_node_pos[0][0] - node.node_pos[0]) < 2
										  and abs(backtrack_node_pos[0][1] - node.node_pos[1]) < 2)
							#backtrack node set to the node_pos in candidates
							backtrack_node_pos = [node.node_pos for node in candidates if node.G_cost == min([k.G_cost for k in candidates])]
							#Add correct nodes to node_path
							node_path.append(backtrack_node_pos)
							#Remove the set of previous node pos
							visited -= candidates


					#Instantiate the Nodes surrounding the start node and append them to unvisited list
					unvisited.add(Nodes(start.node_pos, end.node_pos, [cur_node.node_pos[0] + i, cur_node.node_pos[1] + j]))


def main():
	#start, end = start_end()
	start,end = Nodes([1,1], [6,7], [1,1]), Nodes([1,1], [6,7], [6,7])
	visited, unvisited, barricades, node_path= set(), set(), set(), []
	for i in range(10):
		find(start,end, visited, unvisited, node_path)
		draw(start, end, visited, unvisited, node_path)
		print('=============')




if __name__ == '__main__':
	board = Board()
	main()
