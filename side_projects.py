# My (bad) recursive implementation of a 2 binary adder (without bin())
a = '0'
b = '0'
a = [int(i) for i in a]
b = [int(i) for i in b]

def binary_add(a, b):
	carry = []
	# to make the list the same length
	if len(a) > len(b):
		b = [0] * (len(a) - len(b)) + b
	elif len(b) > len(a):
		a = [0] * (len(b) - len(a)) + a
	summation = [i + j for i, j in zip(a, b)]
	summation = [0] + summation
	for i in range(len(summation)):
		carry.append(0)

	def recursion(summation, carry):

		#Add carry to summation then clear carry
		summation = [x + y for x, y in zip(summation, carry)]
		carry.clear()

		#Make carry a list of 0 of length len(summation) + 1
		for i in range(len(summation) + 1):
			carry.append(0)

		#For each 2 in summation, set it to 0, then make that carry[position - 1] a 1.
		for j in range(len(summation)):
			if summation[j] == 2:
				summation[j] = 0
				if j == 0:
					j = 1
				carry[j - 1] = 1
		#If 1 is still in carry, then do recursion on the summation and carry
		if 1 in carry:
			return recursion(summation, carry)
		#Else, return summation
		return summation

	return recursion(summation, carry)


output = ''
for i in binary_add(a,b):
	output += str(i)
print(str(int(output)))
