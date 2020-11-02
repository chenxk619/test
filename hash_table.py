'''Implementation of hash table with separate chaining collision handling
(Guide : “How to Implement a Hash Table in Python” by Steve Grice https://link.medium.com/NkkIZ7aV4ab).
So a hash table ideally hashes its keys equally to an arbitary number of buckets(which are just different positions in the Hash_table buckets attribute)
and does so by mapping large hash values to values corresponding to the buckets.
Of course, there will be collisions in the table, and this is handled by a linked list in each bucket, known as separate chaining.
Of course more efficient methods exist (but separate chaining is the simplest).
Now when we insert an element it will enter the last element in the linked list and the same element will be extracted when called upon.'''


class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None


class Hash_table:
	def __init__(self):
		self.item_count = 0
		self.capacity = 50
		self.buckets = [None] * self.capacity

	# This system of hashing works well enough to keep keys in buckets in the buckets range
	def hashing(self, key):
		hash_value = 0
		key = str(key)
		# Adds index of each element in key to the len(key) and applies power of their character number
		for i, j in enumerate(key):
			hash_value += (i + len(key)) ** ord(j)
		# Modulus on hash value to get a range of 0 to self.capacity - 1
		hash_value %= self.capacity
		return hash_value

	#Allows indexing of the dictionaries
	def __getitem__(self, index):
		return self.buckets[index].val

	#Allows the keys of the dictionaries to be changed by referencing them
	def __setitem__(self, index, value):
		node = self.buckets[index]
		self.item_count += 1
		if node is None:
			#Note that node = Node(index,value) does NOT work as node is a local variable and does not get changed like
			#the class attribute buckets
			self.buckets[index] = Node(index, value)
		else:
			while node.next is not None:
				print('hi')
				node = node.next
			self.buckets[index] = Node(index, value)

	def insert(self, key, value):
		self.item_count += 1
		# Get hash value
		hash_value = self.hashing(key)
		# If that particular bucket is empty, update it to Node(key, value)
		node = self.buckets[hash_value]
		if node is None:
			self.buckets[hash_value] = Node(key, value)
			return
		# If collision happens: link the new node to the linked list present, by going through the linked list.
		prev = node
		while node is not None:
			prev = node
			node = node.next
		prev.next = Node(key, value)

	#prints the hash_table
	def __repr__(self):
		output = ''
		for i in self.buckets:
			if i is not None:
				node = i
				while node.next is not None:
					node = node.next
				output += ' {} : {},'.format(i.key, node.val)
		return '{' + output[:-1] + '}'

	#Get the hash_value, then go through the linked list until the key's node.val is found, otherwise return None
	def find(self, key):
		hash_value = self.hashing(key)
		node = self.buckets[hash_value]
		if node is None:
			return None
		while node.next is not None:
			node = node.next
		if node.key == key:
			return node.val
		return None

#Driver Code
dic = Hash_table()
dic.insert(1, 2)
print(dic.hashing('a'))
dic.insert(290, 'penis')
dic.insert(290, 'balls')
print(dic.find(1))
dic[1] = 4
print(dic)
