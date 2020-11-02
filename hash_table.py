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

	def insert(self, key, value):
		self.item_count += 1
		# Get hash value
		hash_value = self.hashing(key)
		# If that particular bucket is empty, update it to Node(key, value)
		node = self.buckets[hash_value]
		if node is None:
			self.buckets[hash_value] = Node(key, value)
			return
		# Collision here so link the new Node to the linked list present
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# when node is None
		prev.next = Node(key, value)

	def __repr__(self):
		output = ''
		for i in self.buckets:
			if i is not None:
				node = i
				while node.next is not None:
					node = node.next
				output += ' {} : {},'.format(i.key, node.val)
		return '{' + output[:-1] + '}'

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


dic = Hash_table()
dic.insert(1, 2)
dic.insert(1, 3)
dic.insert(1, 4)
dic.insert(1, 5)
print(dic.hashing('a'))
dic.insert(290, 'penis')
print(dic.find(1))
print(dic)
