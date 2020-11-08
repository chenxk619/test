import random, time
import numpy as np
import sys
import math


# User choice
def userC(Board, ava_list, win, lose, tie):
	print('Your turn')
	while True:
		try:
			user = input(
				'====Please enter a integer to choose your choice(1-9), corresponding to a free space on the board====')
			user = int(user)
			if user < 10 and user > 0 and user in ava_list:
				break
		except:
			continue
	gameEnd(Board, win , lose, tie)
	boardUpdate(user, Board, ava_list, win, lose, tie)


def bestChoice(symbol, Board):
	if np.any(np.all(Board == symbol, axis=1)) or np.any(np.all(Board == symbol, axis=0)) or (
			Board[0, 0] == symbol and Board[1, 1] == symbol and Board[2, 2] == symbol) or (
			Board[2, 0] == symbol and Board[1, 1] == symbol and Board[0, 2] == symbol):
		if symbol == 'O':
			return 1
		elif symbol == 'X':
			return -1
	else:
		if np.any(Board == ' '):
			return None
		else:
			return 0


def miniMax(Board, depth, isAITurn):
	# Ai is 'O' and is maxisiming, player is 'X' and is minimising

	# Board uses a (y,x) system
	marker = 'X'
	bestVal = 10

	if isAITurn:
		marker = 'O'
		bestVal = -10

	# check for ending moving
	value = bestChoice(marker, Board)

	if not value is None:
		return value, None

	# loop thru board to find empty spots
	best_move = None

	for i in range(len(Board)):
		for j in range(len(Board)):

			# if position is empty
			if Board[j][i] == ' ':
				# fill with marker
				Board[j][i] = marker

				# no ending move yet
				value, _ = miniMax(Board, depth + 1, not isAITurn)

				# check if a good move is found within this recursive stack
				if isAITurn:
					if value > bestVal:
						bestVal = value
						best_move = (j, i)
				else:
					if value < bestVal:
						bestVal = value
						best_move = (j, i)

				Board[j][i] = ' '

	return bestVal, best_move


def ai_Choice(ava_list, Board, win, lose, tie):

	_, bestMove = miniMax(Board, 0, True)
	print(bestMove)
	# if bestMove[1] == 0:
	# 	ai_choice = 1 + bestMove[2]
	# elif bestMove[1] == 1:
	# 	ai_choice = 4 + bestMove[2]
	# else:
	# 	ai_choice = 7 + bestMove[2]

	ai_choice = bestMove[0]*3+bestMove[1]+1
	ava_list.remove(ai_choice)
	time.sleep(1)
	print('===It\'s the AI\'s turn, they chose', ai_choice, '====')
	converter('ai_turn', ai_choice, Board)
	print(Board)
	gameEnd(Board, win, lose, tie)


def boardUpdate(choice, Board, ava_list, win, lose, tie):
	converter('user_turn', choice, Board)
	print(Board)
	ava_list.remove(choice)
	gameEnd(Board, win ,lose, tie)
	ai_Choice(ava_list, Board, win, lose, tie)


def converter(user, choice, Board):
	if user == 'ai_turn':
		symbol = 'O'
	elif user == 'user_turn':
		symbol = 'X'
	if choice is not None:
		Board[(math.ceil(choice/3) - 1, (choice-1)%3)] = symbol
	

def gameEnd(Board, win, lose, tie):
	if np.any(np.all(Board == 'X', axis=0)) or np.any(np.all(Board == 'X', axis=1)) or (
			Board[0, 0] == 'X' and Board[1, 1] == 'X' and Board[2, 2] == 'X') or (
			Board[2, 0] == 'X' and Board[1, 1] == 'X' and Board[0, 2] == 'X'):
		print('====You won====')
		win += 1
		main()
	if np.any(np.all(Board == 'O', axis=1)) or np.any(np.all(Board == 'O', axis=0)) or (
			Board[0, 0] == 'O' and Board[1, 1] == 'O' and Board[2, 2] == 'O') or (
			Board[2, 0] == 'O' and Board[1, 1] == 'O' and Board[0, 2] == 'O'):
		print('====AI win====')
		lose += 1
		main()
	if ' ' not in Board:
		print('====You tied!====')
		tie += 1
		main()


def scoreboard(win, tie, lose):
	print('====You won', win, 'times, lost', lose, 'times, and tied', tie, 'times====')


def main():
	Board = np.full((3, 3), ' ')

	win = 0
	tie = 0
	lose = 0
	ava_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	while True:

		print('====Welcome to tic-tac-toe!====')
		scoreboard(win, tie, lose)
		while True:
			menu = input('Enter (c) to continue or (q) to quit')
			if menu == 'c':
				break
			elif menu == 'q':
				exit()
			else:
				continue

		print(Board)
		while True:
			userC(Board, ava_list, win, tie, lose)


if __name__ == "__main__":
	main()


