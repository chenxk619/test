import pygame
import sys
import numpy
import math
import ast
import time

save_lst = []

class Board:

    def __init__(self):
        self.check = 0
        self.turn = 1
        self.const = 8
        self.length = 750
        self.space = self.length / self.const
        self.light_green = (235, 245, 208)
        self.dark_green = (23, 153, 58)
        self.pos_color = (237, 247, 49, 200)
        self.prev_color = (235, 35, 0, 200)
        self.content = numpy.zeros((self.const, self.const))
        self.white_lst = []
        self.black_lst = []
        self.default_load = [-2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, -4.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 4.0, -3.0, -1.0, 0.0, 0.0, 0.0, 0.0,
     1.0, 3.0, -5.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 5.0, -6.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 6.0, -3.0, -1.0, 0.0, 0.0,
     0.0, 0.0, 1.0, 3.0, -4.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 4.0, -2.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0]

    #Only call the get list once
    def get_white_lst(self):
        self.white_lst = []
        for i in range(self.const):
            for j in range(self.const):
                if self.content[i][j] > 0:
                    self.white_lst.append([i,j])
        return self.white_lst

    def get_black_lst(self):
        self.black_lst = []
        for i in range(self.const):
            for j in range(self.const):
                if self.content[i][j] < 0:
                    self.black_lst.append([i,j])
        return self.black_lst



#Moved to check for castling and pawn moves
class Pieces:
    def __init__(self, sprite, id, value):
        self.sprite = pygame.transform.scale(pygame.image.load("chess_folder/" + sprite + ".png") , (94,94))
        self.id = id
        self.value = value
        self.moved = False

def load(board):

    black_pawn = Pieces("black_pawn", -1, 1)
    white_pawn = Pieces("white_pawn", 1, 1)
    black_rook = Pieces("black_rook", -2, 1)
    white_rook = Pieces("white_rook", 2, 1)
    black_bishop = Pieces("black_bishop", -3, 1)
    white_bishop = Pieces("white_bishop", 3, 1)
    black_knight = Pieces("black_knight", -4, 1)
    white_knight = Pieces("white_knight", 4, 1)
    black_queen = Pieces("black_queen", -5, 1)
    white_queen = Pieces("white_queen", 5, 1)
    black_king = Pieces("black_king", -6, 1)
    white_king = Pieces("white_king", 6, 1)

    chess_dic = {0: None, -1: black_pawn, 1: white_pawn, -2: black_rook, 2: white_rook, -3: black_bishop, 3: white_bishop,
                 -4: black_knight, 4: white_knight, -5: black_queen, 5: white_queen,
                 -6: black_king, 6: white_king}

    try:
        f = open("chess.txt", 'r')
        if f.mode == 'r':
            saved_lst = f.read()
            board.turn = int(saved_lst[-1]) - 2
            saved_lst = saved_lst[0:-1]
            saved_lst = ast.literal_eval(saved_lst)
            for i in range(len(saved_lst)):
                j = math.floor(i/8)
                board.content[j][i % 8] = saved_lst[int(i)]
    except:
        for i in range(len(board.default_load)):
            j = math.floor(i / 8)
            board.content[j][i % 8] = board.default_load[int(i)]


    return chess_dic

# Pawn chess pieces can only directly forward one square, with two exceptions.
# Pawns can move directly forward two squares on their first move only.
# Pawns can move diagonally forward when capturing an opponent's chess piece.
# Once a pawn chess piece reaches the other side of the chess board, the player may "trade" the pawn in for any other chess
# piece if they choose, except another king.


#Rest is ez

#Castling is when the king moves two spaces to the left or right, assuming it is not under check and neither the king nor the rook in
#question has moved

def check_mate(board):
    if check(board, -board.turn):
        if board.turn > 0:
            for i in board.white_lst:
                moves = show_moves(i, board.content[i[0]][i[1]], board)
                for j in moves:
                    #og pieces
                    new_piece = board.content[j[0]][j[1]]
                    old_piece = board.content[i[0]][i[1]]
                    # New pos piece, king = king , 0
                    board.content[j[0]][j[1]] , board.content[i[0]][i[1]] = board.content[i[0]][i[1]] , 0
                    #update list
                    board.get_white_lst()
                    checked = check(board, -board.turn)
                    board.content[i[0]][i[1]], board.content[j[0]][j[1]] = old_piece , new_piece
                    board.get_white_lst()
                    if not checked:
                        return False

        else:
            for i in board.black_lst:
                moves = show_moves(i, board.content[i[0]][i[1]], board)
                for j in moves:
                    #og pieces
                    new_piece = board.content[j[0]][j[1]]
                    old_piece = board.content[i[0]][i[1]]
                    # New pos piece, king = king , 0
                    board.content[j[0]][j[1]], board.content[i[0]][i[1]] = board.content[i[0]][i[1]], 0
                    # update list
                    board.get_black_lst()
                    checked = check(board, -board.turn)
                    board.content[i[0]][i[1]], board.content[j[0]][j[1]] = old_piece, new_piece
                    board.get_black_lst()
                    if not checked:
                        return False

        return True

    return False

def check(board, turn):
    if turn > 0:
        for i in board.white_lst:
            moves = show_moves(i, board.content[i[0]][i[1]], board)
            for j in moves:
                if board.content[j[0]][j[1]] == -turn * 6:
                    return True

    else:
        for i in board.black_lst:
            moves = show_moves(i, board.content[i[0]][i[1]], board)
            for j in moves:
                if board.content[j[0]][j[1]] == -turn * 6:
                    return True

    return False

def show_moves_check(straights, diagonals, single_move, temp_pos, selected_pieces, board):
    move_lst = []

    if single_move:
        jump = 7
    else:
        jump = 1

    if straights:
        for i in range(1, 8, jump):
            if temp_pos[0] + i <= 7:
                if selected_pieces * board.content[temp_pos[0] + i][temp_pos[1]] <= 0:
                    move_lst.append([temp_pos[0] + i, temp_pos[1]])
                    if selected_pieces * board.content[temp_pos[0] + i][temp_pos[1]] < 0:
                        break
                else:
                    break
            else:
                break

        for i in range(1, 8, jump):
            if temp_pos[1] + i <= 7:
                if selected_pieces * board.content[temp_pos[0]][temp_pos[1] + i] <= 0:
                    move_lst.append([temp_pos[0], temp_pos[1] + i])
                    if selected_pieces * board.content[temp_pos[0]][temp_pos[1] + i] < 0:
                        break
                else:
                    break
            else:
                break

        for i in range(1, 8, jump):
            if temp_pos[0] - i >= 0:
                if selected_pieces * board.content[temp_pos[0] - i][temp_pos[1]] <= 0:
                    move_lst.append([temp_pos[0] - i, temp_pos[1]])
                    if selected_pieces * board.content[temp_pos[0] - i][temp_pos[1]] < 0:
                        break
                else:
                    break
            else:
                break

        for i in range(1, 8, jump):
            if temp_pos[1] - i >= 0:
                if selected_pieces * board.content[temp_pos[0]][temp_pos[1] - i] <= 0:
                    move_lst.append([temp_pos[0], temp_pos[1] - i])
                    if selected_pieces * board.content[temp_pos[0]][temp_pos[1] - i] < 0:
                        break
                else:
                    break
            else:
                break

    if diagonals:
        for i in range(1, 8, jump):
            if temp_pos[0] + i <= 7 and temp_pos[1] + i <= 7:
                if selected_pieces * board.content[temp_pos[0] + i][temp_pos[1] + i] <= 0:
                    move_lst.append([temp_pos[0] + i, temp_pos[1] + i])
                    if selected_pieces * board.content[temp_pos[0] + i][temp_pos[1] + i] < 0:
                        break
                else:
                    break
            else:
                break

        for i in range(1, 8, jump):
            if temp_pos[0] + i <= 7 and temp_pos[1] - i >= 0:
                if selected_pieces * board.content[temp_pos[0] + i][temp_pos[1] - i] <= 0:
                    move_lst.append([temp_pos[0] + i, temp_pos[1] - i])
                    if selected_pieces * board.content[temp_pos[0] + i][temp_pos[1] - i] < 0:
                        break
                else:
                    break
            else:
                break

        for i in range(1, 8, jump):
            if temp_pos[0] - i >= 0 and temp_pos[1] + i <= 7:
                if selected_pieces * board.content[temp_pos[0] - i][temp_pos[1] + i] <= 0:
                    move_lst.append([temp_pos[0] - i, temp_pos[1] + i])
                    if selected_pieces * board.content[temp_pos[0] - i][temp_pos[1] + i] < 0:
                        break
                else:
                    break
            else:
                break

        for i in range(1, 8, jump):
            if temp_pos[0] - i >= 0 and temp_pos[1] - i >= 0:
                if selected_pieces * board.content[temp_pos[0] - i][temp_pos[1] - i] <= 0:
                    move_lst.append([temp_pos[0] - i, temp_pos[1] - i])
                    if selected_pieces * board.content[temp_pos[0] - i][temp_pos[1] - i] < 0:
                        break
                else:
                    break
            else:
                break

    return move_lst

def show_moves(temp_pos, selected_pieces, board):
    move_lst = []
    #Pawn
    if abs(selected_pieces) == 1:
        if selected_pieces == 1:

            if board.content[temp_pos[0]][temp_pos[1] - 1] == 0:
                move_lst.append([temp_pos[0], temp_pos[1] - 1])

            if temp_pos[1] - 2 >= 0:
                if board.content[temp_pos[0]][temp_pos[1] - 2] == 0 and temp_pos[1] == 6:
                    move_lst.append([temp_pos[0], temp_pos[1] - 2])


            if temp_pos[0] - 1 >= 0:
                if selected_pieces * board.content[temp_pos[0] - 1][temp_pos[1] - 1] < 0:
                    move_lst.append([temp_pos[0] - 1, temp_pos[1] - 1])
            if temp_pos[0] + 1 <= 7:
                if selected_pieces * board.content[temp_pos[0] + 1][temp_pos[1] - 1] < 0:
                    move_lst.append([temp_pos[0] + 1, temp_pos[1] - 1])


        if selected_pieces == -1:
            if board.content[temp_pos[0]][temp_pos[1] + 1] == 0:
                move_lst.append([temp_pos[0], temp_pos[1] + 1])

            if temp_pos[1] + 2 <= 7:
                if board.content[temp_pos[0]][temp_pos[1] + 2] == 0 and temp_pos[1] == 1:
                    move_lst.append([temp_pos[0], temp_pos[1] + 2])

            if temp_pos[0] - 1 >= 0:
                if selected_pieces * board.content[temp_pos[0] - 1][temp_pos[1] + 1] < 0:
                    move_lst.append([temp_pos[0] - 1, temp_pos[1] + 1])
            if temp_pos[0] + 1 <= 7:
                if selected_pieces * board.content[temp_pos[0] + 1][temp_pos[1] + 1] < 0:
                    move_lst.append([temp_pos[0] + 1, temp_pos[1] + 1])



        # if temp_pos[0] + 1 <= 7 and temp_pos[1] + 1 <= 7 and selected_pieces * board.content[temp_pos[0] + 1][temp_pos[1] + 1] < 0:
        #     print(board.content[temp_pos[0] + 1][temp_pos[1] + 1])
        #     move_lst.append([temp_pos[0] + 1, temp_pos[1] + 1])

        # if temp_pos[0] - 1 >= 0  and temp_pos[1] - 1 >= 0 and selected_pieces * board.content[temp_pos[0] - 1][temp_pos[1] - 1] < 0:
        #     move_lst.append([temp_pos[0] - 1, temp_pos[1] - 1])

    #Rook
    if abs(selected_pieces) == 2:
        move_lst = show_moves_check(True, False, False, temp_pos, selected_pieces, board)

    #Bishop
    if abs(selected_pieces) == 3:
        move_lst = show_moves_check(False, True, False, temp_pos, selected_pieces, board)

    #Knight
    if abs(selected_pieces) == 4:

        lst =      [[temp_pos[0] + 1,temp_pos[1] + 2], [temp_pos[0] + 1,temp_pos[1] - 2],
                        [temp_pos[0] + 2,temp_pos[1] + 1], [temp_pos[0] + 2,temp_pos[1] - 1],
                        [temp_pos[0] - 1,temp_pos[1] + 2], [temp_pos[0] - 1,temp_pos[1] - 2],
                        [temp_pos[0] - 2,temp_pos[1] + 1], [temp_pos[0] - 2,temp_pos[1] - 1]]

        for i in lst:

            if i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7 and selected_pieces * board.content[i[0]][i[1]] <= 0:
                move_lst.append(i)

    #Queen
    if abs(selected_pieces) == 5:
        move_lst = show_moves_check(True, True, False, temp_pos, selected_pieces, board)

    #King
    if abs(selected_pieces) == 6:
        move_lst = show_moves_check(True, True, True, temp_pos, selected_pieces, board)

    return move_lst


def game(board, screen, chess_dic):

    start = True
    restart = False

    #check if mouse is pressed
    pressed = False
    #ensure only one piece is being selected
    selected_piece = None
    temp_pos = None
    prev_rect = None
    move_lst = []
    board.get_white_lst()
    board.get_black_lst()

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if check_mate(board):
            start = False

        #Draw board : Even is white, odd is black
        #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        for rows in range(board.const):
            for columns in range(board.const):
                if (rows + columns) % 2 == 0:
                    pygame.draw.rect(screen, board.light_green, ((board.space * rows) , (board.space * columns)
                                     , (board.space) , (board.space)))

                if (rows + columns) % 2 == 1:
                    pygame.draw.rect(screen, board.dark_green, ((board.space * rows) , (board.space * columns)
                                     , (board.space) , (board.space)))

        for i in range(board.const):
            for j in range(board.const):

                chess_piece = board.content[i][j]
                if chess_piece != 0:
                    screen.blit(chess_dic[chess_piece].sprite, (board.space * i,board.space * j))


        #m1 is clicked
        if pygame.mouse.get_pressed()[0]:
            pressed = True

            exact_mouse_pos = pygame.mouse.get_pos()
            mouse_pos = [math.floor(exact_mouse_pos[0] / board.space), math.floor(exact_mouse_pos[1] / board.space)]

            #Selecting a piece if not already done
            #Temporarily setting id to 0; reset to original id later on unless valid move is made
            if selected_piece == None:

                temp_pos = mouse_pos
                selected_piece = board.content[mouse_pos[0]][mouse_pos[1]]
                if selected_piece * board.turn > 0:
                    board.content[mouse_pos[0]][mouse_pos[1]] = 0

            elif selected_piece * board.turn > 0:
                #To show the available moves
                move_lst = show_moves(temp_pos, selected_piece, board)


                new_lst = []
                for move in move_lst:
                    temp_piece = board.content[move[0]][move[1]]
                    board.content[move[0]][move[1]] = selected_piece

                    #Check yourself
                    if check(board, -board.turn):
                        board.content[move[0]][move[1]] = 0

                    else:
                        new_lst.append(move)

                    board.content[move[0]][move[1]] = temp_piece

                move_lst = new_lst

                for moves in move_lst:
                    #thank you guy on internet for alpha colours
                    rect = ((board.space * moves[0]), (board.space * moves[1]), (board.space), (board.space))
                    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
                    pygame.draw.rect(shape_surf, board.pos_color, shape_surf.get_rect())
                    screen.blit(shape_surf, rect)

                for i in range(board.const):
                    for j in range(board.const):

                        chess_piece = board.content[i][j]
                        if chess_piece != 0:
                            screen.blit(chess_dic[chess_piece].sprite, (board.space * i, board.space * j))

                if selected_piece != 0:
                    screen.blit(chess_dic[selected_piece].sprite, (exact_mouse_pos[0] - board.space/2, exact_mouse_pos[1] - board.space/2))

            else:
                move_lst = []


        #m1 is released
        if not pygame.mouse.get_pressed()[0] and pressed == True:
            pressed = False

            exact_mouse_pos = pygame.mouse.get_pos()
            mouse_pos = [math.floor(exact_mouse_pos[0] / board.space), math.floor(exact_mouse_pos[1] / board.space)]

            #Move is legal and doesn't cause a self checkmate
            if mouse_pos in move_lst and board.turn * selected_piece > 0:

                #Check for pawn promotion
                if selected_piece == 1 and mouse_pos[1] == 0:
                    selected_piece = 5
                if selected_piece == -1 and mouse_pos[1] == board.const - 1:
                    selected_piece = -5

                board.content[mouse_pos[0]][mouse_pos[1]] = selected_piece

                board.get_black_lst()
                board.get_white_lst()
                # Check for check
                if check(board, board.turn):
                    board.check = -board.turn

                #Show the previous move
                prev_rect = ((board.space * temp_pos[0]), (board.space * temp_pos[1]), (board.space), (board.space))

            else:
                board.content[temp_pos[0]][temp_pos[1]] = selected_piece
                board.turn *= - 1

            #has to be here to use the piece's id
            selected_piece = None
            move_lst = None
            board.turn *= -1

        if prev_rect is not None:
            shape_surf = pygame.Surface(pygame.Rect(prev_rect).size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, board.prev_color, shape_surf.get_rect())
            screen.blit(shape_surf, prev_rect)

        pygame.display.update()

        #Restart board
        if pygame.key.get_pressed()[pygame.K_r] and pygame.key.get_pressed()[pygame.K_LSHIFT]:
            with open('chess.txt', 'w') as f:
                restart = True
                f.write(str(board.default_load))
                f.write("3")
                start = False

        #Save board
        if len(save_lst) == 0:
            if check_mate(board) or pygame.key.get_pressed()[pygame.K_s]:
                print("board saved")
                for i in board.content:
                    for j in i:
                        save_lst.append(j)
                        with open('chess.txt', 'w') as f:
                            f.write(str(save_lst))
                            f.write(str(board.turn + 2))


    #Endgame
    if restart:
        print("board restarted")
    elif board.turn == -1:
        print("Checkmate. White won.")
    elif board.turn == 1:
        print("Checkmate. Black won.")

    print("Space to restart")
    while True:
        event = pygame.event.wait()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            break

def main():
    #Instatiate the board
    board = Board()
    pygame.init()
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode((board.length, board.length))
    chess_dic = load(board)
    game(board, screen, chess_dic)

while __name__ == '__main__':
    main()

#TODO

#2. castling - u cant castle if either rook or king has moved, or if the rook is captured
#3. for restart, take note of turn order