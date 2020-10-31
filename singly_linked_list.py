# Singly linked list with head and tail pointers, but easy to implement doubly-linked one as well

class Node:
	def __init__(self, val):
		self.val = val
		self.next_node = None


class Linked_list:
	def __init__(self):
		self.head = None
		self.tail = None

	# Adds a node to the back of the list
	def push_back(self, data):
		node = Node(data)
		if self.tail is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next_node = node
			self.tail = node

	# Adds a node to the front of list
	def push_front(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			node.next_node = self.head
			self.head = node

	# Pops the first element of the list
	def pop_front(self):
		if self.head is None:
			print('Cannot pop front(empty)')
		elif self.head.next_node is None:
			self.head = None
		else:
			self.head = self.head.next_node

	# Pops the last element in the list, but have to iterate through the whole linked list to find the 2nd last element
	def pop_back(self):
		if self.head is None:
			print('Cannot pop back(empty)')
		elif self.head.next_node is None:
			self.tail = None
		else:
			cur_node = self.head
			while cur_node.next_node.next_node is not None:
				cur_node = cur_node.next_node
			cur_node.next_node = None
			self.tail = cur_node

	# Besides the edge cases, it will find the (index -1)node and link that node to the node to be inserted.
	# Afterwards link the node to be inserted to the next node of (index -1) using a temp variable
	def insert(self, index, value):
		node = Node(value)
		if index == 0:
			node.next_node = self.head
			self.head = node
		else:
			cur_node = self.head
			for _ in range(index - 1):
				cur_node = cur_node.next_node
				if cur_node is None:
					print('Cannot insert as last index exceeded')
					return
			temp_node = cur_node.next_node
			cur_node.next_node = node
			node.next_node = temp_node
			if temp_node is None:
				self.tail = node

	# Besides the edge cases, just finding the(index -1)node and changing its next to next.next
	def erase(self, index):
		if index == 0:
			self.head = self.head.next_node
		else:
			cur_node = self.head
			for _ in range(index - 1):
				cur_node = cur_node.next_node
				if cur_node is None:
					print('Cannot erase as last index exceeded')
			cur_node.next_node = cur_node.next_node.next_node
			self.tail = cur_node

	# Prints out the list
	def __repr__(self):
		if self.head is None:
			return 'Linked list is empty'
		else:
			ans = ''
			cur_node = self.head
			while cur_node is not None:
				ans = ans + str(cur_node.val) + '-'
				cur_node = cur_node.next_node
			return ans[0:-1]

	# Returns the length of the list
	def size(self):
		length = 0
		if self.head is None:
			return length
		else:
			cur_node = self.head
			while cur_node is not None:
				cur_node = cur_node.next_node
				length += 1
			return length

	# Check if list is empty
	def empty(self):
		return self.head is None

	# Find the value at somewhere by iterating (index) times
	def value_at(self, index):
		cur_node = self.head
		if index < 0:
			length = self.size()
			index = length + index
		for _ in range(index):
			cur_node = cur_node.next_node
			if cur_node is None:
				return None
		return cur_node.val

	# Returns the value of element n spots from the back, using size() and reusing value_at()
	def value_from_end(self, index):
		length = self.size()
		return self.value_at(length - index - 1)

	# Returns front value
	def front(self):
		if self.head is None:
			return None
		return self.head.val

	# Returns back value
	def back(self):
		if self.tail is None:
			return None
		return self.tail.val

	# Good luck understanding this
	# For all cases, set up primary (pri), secondary (sec) pointers, which points to head and head.next
	# For the 0,1,2 nodes, return empty list, return same node and reverse the 2 nodes respectively.
	# Otherwise, set an additional pointer named tertiary(ter), pointing to sec.next.  While ter pointer isn't None, link sec.next to pri, and shift all the pointers down the list by 1 spot using a tuple assignment. Finally, point sec to pri and reset the head pointer.
	def reverse(self):
		pri_node = self.head
		sec_node = pri_node.next_node
		if pri_node is None:
			print('Cannot reverse(empty list)')
		elif sec_node is None:
			return
		elif sec_node.next_node is None:
			sec_node.next_node = pri_node
			pri_node.next_node = None
			self.head, self.tail = sec_node, pri_node
		else:
			self.tail = pri_node
			pri_node.next_node = None
			ter_node = sec_node.next_node
			while ter_node is not None:
				sec_node.next_node = pri_node

				pri_node, sec_node, ter_node = sec_node, ter_node, ter_node.next_node

			sec_node.next_node = pri_node
			self.head = sec_node

#Driver code will be below