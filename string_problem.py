from copy import copy

def Recursion(word, dictionary, Matches):
	#check if word is in available dictionary
	if word in dictionary and word not in Matches:
		Matches.append(word)

	# Convert the string to a list to use list methods
	word_list = list(word)

	#ending condition for recursion
	if len(word_list) == 1:
		return

	#remove the first item in list
	for pos in range(len(word_list)):
		word_copy = copy(word_list)
		del word_copy[pos]

		#convert word_list to a word
		word = ''.join(word_copy)
		Recursion(word, dictionary, Matches)


def main():
	# Find all the substrings from a word
	word = input('Please enter a word : ')

	# opening the text file containing all the english words, then removing the /n
	words = []
	with open(r'C:\Users\Shao Min\Downloads\words.txt', 'r') as file:
		for line in file:
			words.append(line[:-1])
	# dictionary of all available words, then convert it to a set
	dictionary = set(words)

	# list of the matches
	Matches = []
	# the index of list to remove
	Recursion(word, dictionary, Matches)
	if len(Matches) > 0:
		for i in range(len(Matches)):
			if i % 8 == 0 and i != 0:
				print('\n')
			if i == len(Matches) - 1:
				print("'{}'".format(Matches[i]), end=' ')
			else:
				print("'{}',".format(Matches[i]), end = ' ')

		print('\n')

	else:
		print('Please enter a valid word')

while __name__ == '__main__':
	print('=' * 30)
	main()