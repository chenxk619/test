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

	#Add an item of item_count at the end of the array
	# ,expand array if necessary
	def append(self, item):
		if self.item_count >= self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 2)
		self.primary_array[self.item_count] = item
		self.item_count += 1

	#Add the item to index 0 of secondary array, then copy
	#the array over, expand the array cap if needed
	def prepend(self, item):
		if self.item_count >= self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 2)
		secondary_array = self.create_array(self.array_capacity)
		secondary_array[0] = item
		for i in range(0, self.item_count):
			secondary_array[i + 1] = self.primary_array[i]
		self.primary_array = secondary_array
		self.item_count += 1

	#Private module here to indicate to others that this should not be explictly called.
	#this creates a new array of double or half the capacity and passes the elements there
	def _enlarge_capacity(self, new_capacity):
		secondary_array = self.create_array(new_capacity)
		for i in range(self.item_count):
			secondary_array[i] = self.primary_array[i]
		self.array_capacity = new_capacity
		self.primary_array = secondary_array

	#Passes the elements prior to the index to a new array, then append the item of specified index to the same array,
	# then pass in the rest of the elements.
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
		#Don't forget about item_count + 1, otherwise it won't show the last element
		self.item_count += 1

	#Similar to insert, but this time don't append the item of specified index.
	def delete(self, index):
		secondary_array = self.create_array(self.array_capacity)
		for i in range(0, index):
			secondary_array[i] = self.primary_array[i]
		for i in range(index + 1, self.item_count):
			secondary_array[i - 1] = self.primary_array[i]
		#Also item_count - 1 for this module
		self.item_count -= 1
		self.primary_array = secondary_array
		if self.item_count == self.array_capacity:
			self._enlarge_capacity(self.array_capacity * 1/2)

	def find(self, item):
		for i in range(self.item_count):
			if self.primary_array[i] == item:
				return i
		return -1

	#prints the array
	def __repr__(self):
		output = ''
		for i in range(self.item_count):
			output = output + str(self.primary_array[i]) + ','
		return '[' + output[:-1] + ']'

#Driver code
array = Array()
array.append(2)
array.append(4)
array.append(5)
array.insert(0,3) #[3,2,4,5]
array.prepend(2)
print(array.find(7))
print(array)