import time
import random


class Sorts:
	def __init__(self, array):
		self.array = array
		self.latest = None
		self.time_taken = 0

	def show(self, *show):
		if len(show) > 0:
			print('Sorted array using {} : {} in {} seconds'.format(self.latest, self.array, self.time_taken))
		else:
			print('Sorted array using {} in {} seconds'.format(self.latest, self.time_taken))

	# For bubble sort, set conditional of swap to be False under a while True loop, and loop throught the list and swap
	# positions 2 by 2. If we are at the end of the list and no swaps occur, return list

	def bubble_sort(self):

		start = time.time()
		self.latest = 'bubble_sort'

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
		self.latest = 'insertion_sort'

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
		self.latest = 'quick_sort'

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

	#The idea behind merge sort is to divide the input array into two halves, calls itself for the two halves,
	# and then merges the two sorted halves recursively. The merging process is done by 2 iterators, one on each array.
	# When a element is appending to the output array, its iterator is incremented. At the last element, the other list
	# is automatically added to output array.

	def merge_sort(self):

		start = time.time()
		self.latest = 'merge_sort'

		def sort(lst):
			i, j = 0, 0
			output = []

			if len(lst) > 1:
				mid = len(lst) // 2
				arr1 = sort(lst[:mid])
				arr2 = sort(lst[mid:])
				# Merge the two lists together to a output list
				while i < len(arr1) and j < len(arr2):
					if arr1[i] < arr2[j]:
						output.append(arr1[i])
						i += 1
					else:
						output.append(arr2[j])
						j += 1

				# When one of the list is not empty, combine the remaining elements with the output list
				if i == len(arr1):
					output += arr2[j:]
				elif j == len(arr2):
					output += arr1[i:]

				return output

			else:
				return lst
		self.array = sort(self.array)
		self.time_taken = time.time() - start


	def heap_sort(self):
		start = time.time()
		self.latest = 'heap_sort'

		def heapify(index):
			left = index * 2
			right = index * 2 + 1

			if left > len(self.array) - 1 or right > len(self.array) - 1:
				return

			elif self.array[left] < self.array[index] and self.array[left] < self.array[right]:
				self.array[left] , self.array[index] = self.array[index], self.array[left]
				return heapify(left)

			elif self.array[right] < self.array[index] and self.array[right] < self.array[left]:
				self.array[index], self.array[right] = self.array[right], self.array[index]
				return heapify(right)


		def sort():
			output = []
			while len(self.array) > 0:
				for i in range(len(self.array) // 2, -1, -1):
					heapify(i)
				output.append(self.array[0])
				self.array = self.array[1:]
			return output

		self.array = sort()
		self.time_taken = time.time() - start


# Driver code
lst = []
for i in range(2000):
	lst.append(random.randint(1, 100))
sorted_obj = Sorts(lst)
sorted_obj.quick_sort()
#optional input to show the actual array
sorted_obj.show()