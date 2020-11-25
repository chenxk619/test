import time
import random


class Sorts:
	def __init__(self, array):
		self.array = array
		self.lastest = None
		self.time_taken = 0

	def __repr__(self):
		return 'Sorted array using {} : {} in {}'.format(self.lastest, self.array, self.time_taken)

	# For bubble sort, set conditional of swap to be False under a while True loop, and loop throught the list and swap
	# positions 2 by 2. If we are at the end of the list and no swaps occur, return list

	def bubble_sort(self):
		start = time.time()
		self.lastest = 'bubble_sort'
		while True:
			sort_done = True
			for i in range(len(self.array[:-1])):
				if self.array[i] > self.array[i + 1]:
					self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
					sort_done = False
			if i == len(self.array) - 2 and sort_done == True:
				self.time_taken = time.time() - start
				break

	# First iterator i will start from 1 to the end of the list. Second iterator j will start from i-1 and iterate down
	# to the start of the list. The second iteration will be effectively a bubble sort, but only 1 element is out of
	# order(as elements ahead of i will be sorted) so you don't need to loop it.

	def insertion_sort(self):
		start = time.time()
		self.lastest = 'insertion_sort'
		for i in range(1, len(self.array)):
			for j in range(i - 1, -1, -1):
				if self.array[j] > self.array[j + 1]:
					self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
		self.time_taken = time.time() - start

	# The general idea behind quicksort is that 2 pointers, i and j iterate through the array, and are compared to a
	# pivot(chosen to be the last element). Using the j pointer, if a element is larger than the pivot, it is ignored
	# until a element is smaller than pivot is found. Then the 2 elements swapped are the smaller than pivot element
	# and the i-th element(which is definitely larger than pivot). In addition, after each swap, i += 1. After all the
	# swapping, the pivot is swapped with the i + 1 element and the process is repeated with the left and right blocks,
	# similar to a binary search spilting the different blocks.
	# Eg: [8,4,7,2,6] - [4,8,7,2,6] - [4,2,7,8,6] - [4,2,6,7,8]
	# [4,2,6,7,8] - [4,2] [6,7,8] - [2,4] [6,7,8]

	def quick_sort(self):
		start = time.time()
		self.lastest = 'quick_sort'

		def sort(left, right):

			def partition(left, right):
				pivot = self.array[right]
				i = left - 1
				for j in range(left, right):
					if self.array[j] <= pivot:
						i += 1
						self.array[i], self.array[j] = self.array[j], self.array[i]
				self.array[i + 1], self.array[right] = self.array[right], self.array[i + 1]
				return i + 1

			if left < right:
				pi = partition(left, right)
				sort(left, pi - 1)
				sort(pi + 1, right)

		sort(0, len(self.array) - 1)
		self.time_taken = time.time() - start


# Driver code
lst = []
for i in range(100):
	lst.append(random.randint(1, 100))
sorted_obj = Sorts(lst)
sorted_obj.bubble_sort()
print(sorted_obj)