import numpy as np

class Board:
	x_length = 8
	y_length = 8


class Nodes:

	def __init__(self,start, end, node_pos):
		#(x,y) coord of the start node
		self.start = start
		#(x,y) coord of the end node
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


def draw():
	draw_board = np.zeros((Board.x_length, Board.y_length))
	draw_board[5][5] = 1
	print(draw_board)


def find(start, end, visited, unvisited):
	if len(visited) == 0:
		visited.add(start)
		for i in range(-1, 2):
			for j in range(-1, 2):
				#To not add the same node it is currently at
				if i != 0 or j != 0:
					#Instantiate the Nodes surrounding the start node and append them to unvisited list
	 				unvisited.add(Nodes(start.node_pos, end.node_pos, [start.node_pos[0] + i, start.node_pos[1] + j]))
	else:
		#find the smallest H_cost node in unvisited list, then set it to visited and find the unvisited nodes around it
		cur_node_val, cur_node = 0, None
		for i in unvisited:
			if cur_node_val < i.H_cost:
				cur_node_val, cur_node =  i.H_cost, i
		unvisited.remove(cur_node)
		visited.add(cur_node)
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i != 0 or j != 0:
					#Instantiate the Nodes surrounding the start node and append them to unvisited list
					unvisited.add(Nodes(start.node_pos, end.node_pos, [cur_node.node_pos[0] + i, cur_node.node_pos[1] + j]))


def main():
	#start, end = start_end()
	start,end = Nodes([1,1], [9,9], [1,1]), Nodes([1,1], [9,9], [9,9])
	visited, unvisited, barricades = set(), set(), set()
	draw()
	find(start, end, visited, unvisited)
	for i in unvisited:
		print(i.H_cost)
	print('========')
	find(start,end, visited, unvisited)
	for i in unvisited:
		print(i.H_cost)






if __name__ == '__main__':
	board = Board()
	main()
