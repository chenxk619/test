class Node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Binary_tree:

	def __init__(self):
		self.base = None

	def insert(self, key):
		node = Node(key)

		# node is the one added, root is pointer
		def recursion(self, node, root):
			# If the tree was empty prior
			if root is None:
				self.base = node
				root = node
				return
			# If node value is larger/smaller than the root value, check if it exists or not,
			# if it does set it as root.left/right then new root, otherwise recursion on that as new root
			elif node.val > root.val:
				if root.right is None:
					root.right = node
					root = node
				else:
					recursion(self, node, root.right)
			else:
				if root.left is None:
					root.left = node
					root = node
				else:
					recursion(self, node, root.left)

		recursion(self, node, self.base)

	# To check if a node exist
	def find(self, value):
		def recursion(self, value, root):
			if root.val == value:
				return True
			# Check the left/right subtree depending on which value is bigger. If the subtree doesn't exist, return False
			elif value < root.val:
				if root.left is None:
					return False
				return recursion(self, value, root.left)
			else:
				if root.right is None:
					return False
				return recursion(self, value, root.right)

		return recursion(self, value, self.base)

	# To get a node from its value, v. similar to find
	def get(self, value):
		def recursion(self, value, root):
			if root.val == value:
				return root
			elif value < root.val:
				if root.left is None:
					return False
				return recursion(self, value, root.left)
			else:
				if root.right is None:
					return False
				return recursion(self, value, root.right)

		return recursion(self, value, self.base)

	# Return max value from a specified node, as well as the specified node
	def get_max(self, node):
		if node.right is None:
			return node.val, node
		# Note that self.method is used here, as it is a class method, not a method within a class method like the others
		return self.get_max(node.right)

	# Return min value from a specified node and the node itself
	# lst[-1] is the parent node of the successor node
	def _get_min(self, node, lst):
		if node.left is None:
			return node.val, node, lst[-1]
		lst.append(node)
		return self._get_min(node.left, lst)

	# This is basically a modified get_min and get_max, it will return the next highest node after the specified node,
	# return -1 if None. It is supposed to get the smallest value on the right subtree,
	# otherwise get the first element on left subtree. This is known as the successor node(s_node)

	# IMPORTANT TO NOTE IF A (successor) NODE IS REMOVED, IT WILL EITHER HAVE NO CHILD NODES OR ONLY RIGHT CHILD NODES,
	# otherwise it move further left
	def get_successor(self, node):

		# If removed node has no subtrees
		if node.left is None and node.right is None:
			return -1, -1
		# If removed node has right/both subtree(s)
		elif node.right is not None:
			# Pass in a list of node in case it IS the parent of s_node(s_node is nodes child)
			node_val, s_node, parent_node = self._get_min(node.right, [node])
			# check for right child, if None means no child nodes
			if s_node.right is None:
				return node_val, s_node, None
			else:
				return node_val, s_node, parent_node

		else:
			node_val, s_node, parent_node = self._get_min(node, [node])

			if s_node.right is None:
				return node_val, s_node, None
			else:
				return node_val, s_node, parent_node

	"""To delete a node is the most complicated code to handle so far, as the tree after the deleted node
	has to meet the condition of left subtree having smaller nodes and the right subtree having bigger nodes.
	I'm following this website to do so: 
	http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete2.html
	In the case of a node with 2 subtrees, to remove a node, we need to replace that 
	node with a node known as the successor node. This is defined as the 
	node on the RIGHT subtree with the SMALLEST value relative to the deleted node. So we have to find the most left 
	node in the right subtree(if a left subtree doesn't exist for the right subtree, the top node is the successor 
	node). This could have been done all in this method, but spliting it up to get_max, get_min and successor 
	methods above made this easier"""

	def remove(self, value):
		# Get the node from the value
		node = self.get(value)

		def recursion(self, node):
			if self.base is None:
				print('Error: Tree is empty')

			# No subtrees
			elif node.left is None and node.right is None:
				node = None

			# For 1/2 subtrees, dont matter which
			else:
				# Returns the successor node, its value and the parent node(which will be None
				# if the successor node has no child, as parent node is not needed)
				s_node_val, s_node, parent_node = self.get_successor(node)
				# Replace the removed node val
				node.val = s_node_val
				if parent_node is None:
					s_node = None
				else:
					# Since we dont know whether s_node is left or right of parent, we need to check for that
					if s_node is parent_node.right:
						parent_node.right = s_node.right
					else:
						parent_node.left = s_node.right
					s_node = None

		recursion(self, node)

	# This is done in a dfs manner, with the left branch first, then root, then right branch
	def show(self):
		def recursion(self, root):
			if root:
				if root.left is not None:
					recursion(self, root.left)
				print(root.val)
				if root.right is not None:
					recursion(self, root.right)

		recursion(self, self.base)

#Driver Code
b_tree = Binary_tree()
lst = [10, 5, 7, 3, 4]
for i in lst:
	b_tree.insert(i)
b_tree.show()

b_tree.remove(10)
b_tree.show()