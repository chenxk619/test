import ctypes


# Array capacity works by making a new array with double the array capacity when the items in the array(item_count) reaches that amount.
# The items are then put in the new array

class Array(object):

	def _init_(self):
		self.item_count = 0
		self.array_capacity = 1
		self.primary_array = self.create_array(self.array_capacity)

	# Since array_capacity * py_object are types, they need to instantiated using brackets before being returned
	def create_array(self, array_capacity):
		return (array_capacity * ctypes.py_object)()

	def append(self, item):
		if self.item_count >= self.array_capacity:
			self.enlarge_capacity(self.array_capacity * 2)
		self.primary_array[self.item_count] = item
		self.item_count += 1

	def enlarge_capacity(self, new_capacity):
		secondary_array = self.create_array(new_capacity)
		for i in range(self.item_count):
			secondary_array[i] = self.primary_array[i]
		self.array_capacity *= 2
		self.primary_array = secondary_array

	def list(self):
		output = ''
		for i in range(self.item_count):
			output = output + str(self.primary_array[i]) + ','
		return '[' + output[:-1] + ']'


array = Array()
array.append(1)
array.append(4)
array.append(3)
print(array.list())