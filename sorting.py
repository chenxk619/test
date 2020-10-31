# For bubble sort, set conditional of swap to be False under a while True loop, and loop throught the list and swap positions 2 by 2. If we are at the end of the list and no swaps occur, return list
def bubble_sort(lst):
	while True:
		swap = False
		for i in range(1, len(lst)):
			if lst[i - 1] > lst[i]:
				lst[i - 1], lst[i] = lst[i], lst[i - 1]
				swap = True
		if i == len(lst) - 1 and swap == False:
			return lst


# First iterator i will start from 1 to the end of the list. Second iterator j will start from i-1 and iterate down to the start of the list. The second iteration will be effectively a bubble sort, but only 1 element is out of order(as elements ahead of i will be sorted) so you don't need to loop it.
def insertion_sort(lst):
	for i in range(1, len(lst)):
		for j in range(i - 1, -1, -1):
			if lst[j + 1] < lst[j]:
				lst[j + 1], lst[j] = lst[j], lst[j + 1]
	return lst


'''The general idea behind quicksort is that 2 pointers, i and j iterate through the array, and are compared to a pivot(chosen to be the last element). Using the j pointer, if a element is larger than the pivot, it is ignored until a element is smaller than pivot is found. Then the 2 elements swapped are the smaller than pivot element and the i-th element(which is definitely larger than pivot). In addition, after each swap, i += 1. After all the swapping, the pivot is swapped with the i + 1 element and the process is repeated with the left and right blocks, similar to a binary search spilting the different blocks.'''
'''Eg:
	[8,4,7,2,6] - [4,8,7,2,6] - [4,2,7,8,6] - [4,2,6,7,8]
	[4,2,6,7,8] - [4,2] [6,7,8] - [2,4] [6,7,8]'''


def partition(lst, left, right):
	pivot = lst[right]
	i = left - 1
	for j in range(left, right):
		if lst[j] <= pivot:
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
	lst[i + 1], lst[right] = lst[right], lst[i + 1]
	return i + 1


def quicksort(lst, left, right):
	if left < right:
		pi = partition(lst, left, right)
		partition(lst, left, pi - 1)
		partition(lst, pi + 1, right)


lst = [8, 4, 6, 0, 5, 2, 7, 3]
# quicksort(lst, 0, len(lst) -1)
# bubble_sort(lst)
insertion_sort(lst)
print(lst)