import pygame
import sys
import numpy
import math
import time

#General board idea :
#
# my_image = pygame.image.load("image.png")
#
# Create a new surface
#
# surf = pygame.Surface((X, Y))
#
# X and Y are horizontal and vertical dimensions in px respectively.
#
# Place the image on the surface
#
# surf.blit( my_image, (A, B), (C, D, E, F) )

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

    #Load in pieces
    for i in range(board.const):
        board.content[i][1] = black_pawn.id
        board.content[i][6] = white_pawn.id

    for i in range(0, 8, 7):
        if i == 0:
            board.content[0][i] = black_rook.id
            board.content[7][i] = black_rook.id
            board.content[1][i] = black_knight.id
            board.content[6][i] = black_knight.id
            board.content[2][i] = black_bishop.id
            board.content[5][i] = black_bishop.id
            board.content[3][i] = black_queen.id
            board.content[4][i] = black_king.id

        else:
            board.content[0][i] = white_rook.id
            board.content[7][i] = white_rook.id
            board.content[1][i] = white_knight.id
            board.content[6][i] = white_knight.id
            board.content[2][i] = white_bishop.id
            board.content[5][i] = white_bishop.id
            board.content[3][i] = white_queen.id
            board.content[4][i] = white_king.id

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
    for i in range(board.const):
        for j in range(board.const):
            if board.content[i][j] * board.turn > 0:
                lst = show_moves([i,j], board.content[i][j], board)
                for k in lst:
                    temp = board.content[k[0]][k[1]]
                    board.content[k[0]][k[1]] = board.content[i][j]
                    checked = check(board, -board.turn)
                    board.content[k[0]][k[1]] = temp
                    if not checked:
                        return False

    return True

def check(board, turn):
    for i in range(board.const):
        for j in range(board.const):
            if board.content[i][j] * turn > 0:
                lst = show_moves([i,j], board.content[i][j], board)
                for k in lst:
                    if -turn * 6 == board.content[k[0]][k[1]]:
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

    #check if mouse is pressed
    pressed = False
    #ensure only one piece is being selected
    selected_piece = None
    temp_pos = None
    prev_rect = None
    move_lst = []

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if board.check == board.turn:
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

                    #Check opponent
                    elif check(board, board.turn):
                        board.check = -board.turn
                        new_lst.append(move)

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
                #Show the previous move
                prev_rect = ((board.space * temp_pos[0]), (board.space * temp_pos[1]), (board.space), (board.space))
                # shape_surf = pygame.Surface(pygame.Rect(prev_rect).size, pygame.SRCALPHA)
                # pygame.draw.rect(shape_surf, board.pos_color, shape_surf.get_rect())
                # screen.blit(shape_surf, prev_rect)

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

    #Endgame
    if board.turn == -1:
        print("Checkmate. White won. Press space to continue")
    elif board.turn == 1:
        print("Checkmate. Black won. Press space to continue")
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
#3. for each piece, create a list of where all the pieces(eg. all the pawns) are