class Heap:
	def __init__(self, array):
		self.array = array
		self.length = len(array) - 1

	def min_heap(self, index):

		left = index * 2 + 1  # index * 2 if start array at 1
		right = index * 2 + 2  # index * 2 +1 if start array at 1
		# parent = (index - 1)//2

		# If the index is at a leaf and left/right dont exist
		if left > self.length or right > self.length:
			return
		# If parent node is bigger than left node and left node becoming parent node will not be greater than right node
		elif self.array[index] > self.array[left] and self.array[left] <= self.array[right]:
			self.array[index], self.array[left] = self.array[left], self.array[index]
			return self.min_heap(left)

		elif self.array[index] > self.array[right] and self.array[right] <= self.array[left]:
			self.array[index], self.array[right] = self.array[right], self.array[index]
			return self.min_heap(right)

	# Applies min_heap to all the nodes in the heap from n/2 rounded down
	def build_min_heap(self):
		for index in range(self.length, -1, -1):
			self.min_heap(index)

	# Insert an element into array then rebuild the heap
	def insert(self, value):
		self.length += 1
		self.array.append(value)
		self.build_min_heap()

	# Remove an element by index
	def remove(self, index):
		self.length -= 1
		self.array.pop(index)
		self.build_min_heap()

	def __repr__(self):
		output = ''
		for index in range((len(self.array) // 2)):
			try:
				output = output + 'PARENT : {}, LEFT CHILD : {}, RIGHT CHILD : {}'.format(self.array[index],
																						  self.array[index * 2 + 1],
																						  self.array[
																							  index * 2 + 2]) + '\n'
			except:
				output = output + 'PARENT : {}, LEFT CHILD : {}, RIGHT CHILD : {}'.format(self.array[index],
																						  self.array[index * 2 + 1],
																						  'None')
		return str(self.array) + '\n' + output


lst = [0, 5, 7, 9, 3, 1, 8, 5]
heap = Heap(lst)
heap.build_min_heap()
heap.insert(-1)
print(heap)
heap.remove(2)
print(heap)