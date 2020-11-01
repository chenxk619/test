import ctypes

# Array capacity works by making a new array with double the array capacity when the items in the array(item_count) reaches that amount.
# The items are then put in the new array

class Array(object):

	def __init__(self):
		self.item_count = 0
		self.array_capacity = 1
		self.primary_array = self.create_array(self.array_capacity)

	# Since array_capacity * py_object are types, they need to instantiated using brackets before being returned
	def create_array(self, array_capacity):
		return (array_capacity * ctypes.py_object)()

	def size(self):
		return self.item_count

	def capacity(self):
		return self.array_capacity

	def is_empty(self):
		return self.item_count == 0

	def at(self, index):
		try:
			return self.primary_array[index]
		except:
			print('Index Error : Index out of bounds')

	def append(self, item):
		if self.item_count >= self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 2)
		self.primary_array[self.item_count] = item
		self.item_count += 1

	def prepend(self, item):
		if self.item_count >= self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 2)
		secondary_array = self.create_array(self.array_capacity)
		secondary_array[0] = item
		for i in range(0, self.item_count):
			print(i)
			secondary_array[i + 1] = self.primary_array[i]
		self.primary_array = secondary_array
		self.item_count += 1

	def _enlarge_capacity(self, new_capacity):
		secondary_array = self.create_array(new_capacity)
		for i in range(self.item_count):
			secondary_array[i] = self.primary_array[i]
		self.array_capacity = new_capacity
		self.primary_array = secondary_array

	def insert(self, index, item):
		if self.item_count == self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 2)
		secondary_array = self.create_array(self.array_capacity)
		for i in range(0, index):
			secondary_array[i] = self.primary_array[i]
		secondary_array[index] = item
		for i in range(index + 1 , self.item_count + 1):
			secondary_array[i] = self.primary_array[i - 1]
		self.primary_array = secondary_array
		self.item_count += 1

	def delete(self, index):
		secondary_array = self.create_array(self.array_capacity)
		for i in range(0, index):
			secondary_array[i] = self.primary_array[i]
		for i in range(index + 1, self.item_count):
			print(i)
			secondary_array[i - 1] = self.primary_array[i]
		self.item_count -= 1
		self.primary_array = secondary_array
		if self.item_count == self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 1/2)


	def __repr__(self):
		output = ''
		for i in range(self.item_count):
			output = output + str(self.primary_array[i]) + ','
		return '[' + output[:-1] + ']'




array = Array()
array.append(2)
array.append(4)
array.append(5)
array.insert(0,3) #[3,2,4,5]
array.prepend(2)
print(array)