a = '1111'
b = '1111'
a = [int(i) for i in a]
b = [int(i) for i in b]
print(a, b)


def binary_add(a, b):
	carry = []
	# to make the list the same length
	if len(a) > len(b):
		b = [0] * (len(a) - len(b)) + b
	elif len(b) > len(a):
		a = [0] * (len(b) - len(a)) + a
	summation = [i + j for i, j in zip(a, b)]
	print(summation)
	summation = [0] + summation
	for i in range(len(summation)):
		carry.append(0)

	def recursion(summation, carry):

		summation = [x + y for x, y in zip(summation, carry)]
		# print(summation)
		carry.clear()

		for i in range(len(summation) + 1):
			carry.append(0)

		for j in range(len(summation)):
			if summation[j] == 2:
				summation[j] = 0
				if j == 0:
					j = 1
				carry[j - 1] = 1
		if 1 in carry:
			return recursion(summation, carry)
		return summation

	return recursion(summation, carry)


print(binary_add(a, b))
