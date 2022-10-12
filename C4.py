# Single player connect-4 game
# Game is 7Horizontal and 6 Vertical
import random, time

win = 0
lose = 0
theBoard = {}
for j in range(1, 43):
    theBoard.setdefault(j, '  ')


def win_check(board, user):
    # check horizontal wins
    for i in range(1, 40):
        if board[i] == user and board[i + 1] == user and board[i + 2] == user and board[i + 3] == user:
            endgame(user)

    # check vertical wins
    for i in range(1, 22):
        if board[i] == user and board[i + 7] == user and board[i + 14] == user and board[i + 21] == user:
            endgame(user)

    # check ascending diagonal wins
    for i in range(1, 22):
        if board[i] == user and board[i + 6] == user and board[i + 12] == user and board[i + 18] == user:
            endgame(user)

    # check desecnding diagonal wins
    for i in range(1, 19):
        if board[i] == user and board[i + 8] == user and board[i + 16] == user and board[i + 24] == user:
            endgame(user)


def endgame(user):
    if user == ' X':
        print('===You won! Congrats===')
        global win
        win += 1
        main(theBoard)
    else:
        print('===The AI won!===')
        global lose
        lose += 1
        main(theBoard)


def user_input(theBoard):
    while True:
        try:
            UI = input('Where would you like to place your chip (1-7)')
            UI = int(UI)
            if UI < 8 and UI > 0:
                break
        except:
            continue
    placement(theBoard, ' X', UI)


def ai_input(board):
    time.sleep(1)
    user = ' X'
    ai= ' O'
    chosen= 0
    a=0

    # checks if the AI has a opportunity to score horizontally
    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
        for i in range(1, 40):
            try:
                if board[i] == ai and board[i + 1] == ai and board[i + 2] == ai and board[
                    i + 3] == '  ' and chosen == 0:
                    chosen +=1
                    # Tries to stop the user from scoring horizontally
                    place = (i + 3) % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they chose', place)
                elif board[i] == ai and board[i - 1] == ai and board[i - 2] == ai and board[
                    i - 3] == '  ' and chosen == False:
                    place = (i - 3) % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they 1chose', place)
            except:
                break
    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
        # checks if the AI has opportunity to score vertically
        for i in range(1, 29):
            try:
                if board[i] == ai and board[i + 7] == ai and board[i + 14] == ai and board[
                    i - 7] == '  ' and chosen == 0:
                    chosen +=1
                    place = i % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)

                    print('It\'s the AI\'s turn, they chose', place)
            except:
                break

    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
        # checks if the AI has a chance to score ascending diagonally
        for i in range(1, 29):
            try:
                if board[i] == user and board[i + 6] == ai and board[i + 12] == ai and board[
                    i - 6] == '  ' and chosen == 0:
                    chosen +=1
                    place = (i - 6) % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they chose', place)
            except:
                break

    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
        # Checks if the AI has a chance to score descending diagonally
        for i in range(1, 25):
            try:
                if board[i] == ai and board[i + 8] == ai and board[i + 16] == ai and board[
                    i - 8] == '  ' and chosen == 0:
                    chosen +=1
                    place = (i - 8) % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they chose', place)
            except:
                break

    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
        # Tries to stop user from scoring vertically
        for i in range(1, 29):
            try:
                if board[i] == user and board[i + 7] == user and board[i + 14] == user and board[
                    i - 7] == '  ' and chosen == 0:
                    chosen +=1
                    place = i % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)

                    print('It\'s the AI\'s turn, they chose', place)
            except:
                break
    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
    #Tries(being the keyword) to stop the user from scoring horizontally, but doesn't set the user up for a win
        for i in range(1,34):
            if board[i] == user and board[i + 1] == user and board[i + 2] == '  ' and board[i+9]=='  ' and chosen == 0:
                if board[i] == user and board[i +1] == user and board[i - 1] == '  ' and board[i+6]== user and chosen == 0:
                    break
                chosen+=1
                random_choice(board)
            if board[i] == user and board[i + 1] == user and board[i -1] == '  ' and board[i +6] == '  ' and chosen == 0:
                chosen += 1
                random_choice(board)

        for i in range(1, 40):
            try:
                if board[i] == user and board[i+1] == user and board[i-1] == '  ' and chosen== 0:
                    a=2
                    chosen+=1
                    place = (i - 1) % 7
                    if place == 0:
                            break
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they 1chose', place)
                elif board[i] == user and board[i + 1] == user and board[i + 2] == '  ' and chosen== 0 and a==0:
                    chosen +=1
                    place = (i + 2) % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they 1chose', place)

            except:
                break
    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
    # Tries to stop user from scoring ascending diagonally
        for i in range(1, 29):
            try:
                if board[i] == user and board[i + 6] == user and board[i + 12] == user and board[
                    i - 6] == '  ' and board[i+1]== '  ' and chosen == 0:
                    chosen+=1
                    random_choice(board)
                if board[i] == user and board[i + 6] == user and board[i + 12] == user and board[i - 6] == '  ' and chosen== 0:
                    chosen+=1
                    place = (i -6) % 7
                    if place == 0:
                        place += 7
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they chose', place)
            except:
                break

    if int(sum(value == ' X' for value in board.values())) > int(sum(value == ' O' for value in board.values())):
    # Tries to stop the user from scoring descending diagonally
    #If place =0 then it will raise an exception cuz it doesnt need to place 7
        for i in range(1, 25):
            try:
                if board[i] == user and board[i + 8] == user and board[i + 16] == user and board[
                    i - 8] == '  ' and board[i-1] == '  ' and chosen == 0:
                    chosen += 1
                    random_choice(board)
                if board[i] == user and board[i + 8] == user and board[i + 16] == user and board[i - 8] == '  ' and chosen== 0:
                    chosen +=1
                    place = (i - 8) % 7
                    if place == 0:
                        break
                    placement(board, ' O', place)
                    print('It\'s the AI\'s turn, they chose', place)
            except:
                break
    random_choice(board)


def random_choice(board):
    # If none of the other conditions are furfilled
    if int(sum(value==' X' for value in board.values())) > int(sum(value==' O' for value in board.values())):
        Ain = random.randint(1, 7)
        print('It\'s the AI\'s turn, they chose', Ain)
        placement(board, ' O', Ain)


def placement(board, placing, UI):
    if UI % 7 == 0:
        for a in range(6, 0, -1):
            if board[7 * a] == '  ':
                board[7 * a] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)
    if UI % 7 == 6:
        for a in range(6, 0, -1):
            if board[7 * a - 1] == '  ':
                board[7 * a - 1] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)
    if UI % 7 == 5:
        for a in range(6, 0, -1):
            if board[7 * a - 2] == '  ':
                board[7 * a - 2] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)
    if UI % 7 == 4:
        for a in range(6, 0, -1):
            if board[7 * a - 3] == '  ':
                board[7 * a - 3] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)
    if UI % 7 == 3:
        for a in range(6, 0, -1):
            if board[7 * a - 4] == '  ':
                board[7 * a - 4] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)
    if UI % 7 == 2:
        for a in range(6, 0, -1):
            if board[7 * a - 5] == '  ':
                board[7 * a - 5] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)
    if UI % 7 == 1:
        for a in range(6, 0, -1):
            if board[7 * a - 6] == '  ':
                board[7 * a - 6] = placing
                break
            elif a == 1:
                print('This column is full')
                user_input(board)


def scoreBoard():
    print('You won', win, 'times', 'and lost', lose, 'times')


def printBoard(board):
    print('|', board[1], '|', board[2], '|', board[3], '|', board[4], '|', board[5], '|', board[6], '|', board[7], '|')
    print('+----+----+----+----+----+----+----+')
    print('|', board[8], '|', board[9], '|', board[10], '|', board[11], '|', board[12], '|', board[13], '|', board[14],
          '|')
    print('+----+----+----+----+----+----+----+')
    print('|', board[15], '|', board[16], '|', board[17], '|', board[18], '|', board[19], '|', board[20], '|',
          board[21], '|')
    print('+----+----+----+----+----+----+----+')
    print('|', board[22], '|', board[23], '|', board[24], '|', board[25], '|', board[26], '|', board[27], '|',
          board[28], '|')
    print('+----+----+----+----+----+----+----+')
    print('|', board[29], '|', board[30], '|', board[31], '|', board[32], '|', board[33], '|', board[34], '|',
          board[35], '|')
    print('+----+----+----+----+----+----+----+')
    print('|', board[36], '|', board[37], '|', board[38], '|', board[39], '|', board[40], '|', board[41], '|',
          board[42], '|')
    print('------------------------------------')


def main(theBoard):
    print('==Welcum to connect 4:D===')
    scoreBoard()
    theBoard = {}
    for j in range(1, 43):
        theBoard.setdefault(j, '  ')
    while True:
        printBoard(theBoard)
        user_input(theBoard)
        win_check(theBoard, ' X')
        printBoard(theBoard)
        ai_input(theBoard)
        win_check(theBoard, ' O')


main(theBoard)