import pygame
import sys
import numpy
import math

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
        self.const = 8
        self.length = 750
        self.space = self.length / self.const
        self.light_green = (235, 245, 208)
        self.dark_green = (23, 153, 58)
        self.light_red = (222, 133, 146)
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
            #board.content[3][i] = black_queen.id
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

def show_moves(temp_pos, selected_pieces, board):
    move_lst = []

    #Knight
    if abs(selected_pieces) == 4:
        print([[temp_pos[0] - 2],[temp_pos[1] - 1]])
        lst =      [[temp_pos[0] + 1,temp_pos[1] + 2], [temp_pos[0] + 1,temp_pos[1] - 2],
                        [temp_pos[0] + 2,temp_pos[1] + 1], [temp_pos[0] + 2,temp_pos[1] - 1],
                        [temp_pos[0] - 1,temp_pos[1] + 2], [temp_pos[0] - 1,temp_pos[1] - 2],
                        [temp_pos[0] - 2,temp_pos[1] + 1], [temp_pos[0] - 2,temp_pos[1] - 1]]

        for i in lst:
            if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
                lst.remove(i)

        move_lst = lst

    return move_lst

def move_block_check(straights, diagonals, maximum_range, temp_pos, mouse_pos, board):

    hdiff = mouse_pos[0] - temp_pos[0]
    vdiff = mouse_pos[1] - temp_pos[1]

    if maximum_range:
        if abs(hdiff) > 1 or abs(vdiff) > 1:
            return False

    if straights:

        #horizontal
        if temp_pos[1] - mouse_pos[1] == 0:
            # move right
            if hdiff > 0:
                for i in range(hdiff):
                    if board.content[temp_pos[0] + i][temp_pos[1]] != 0:
                        return False

            if hdiff < 0:
                for i in range(-hdiff):
                    if board.content[temp_pos[0] - i][temp_pos[1]] != 0:
                        return False

            return True

        # Vertical
        if temp_pos[0] - mouse_pos[0] == 0:
            # move right
            if vdiff > 0:
                for i in range(vdiff):
                    if board.content[temp_pos[0]][temp_pos[1] + i] != 0:
                        return False

            if vdiff < 0:
                for i in range(-vdiff):
                    if board.content[temp_pos[0]][temp_pos[1] - i] != 0:
                        return False

            return True


    if diagonals:
        if abs(vdiff) - abs(hdiff) != 0:
            return False
        if vdiff < 0:
            if hdiff < 0:
                for i in range(-vdiff):
                    if board.content[temp_pos[0] - i][temp_pos[1] - i] != 0:
                        return False

            if hdiff > 0:
                for i in range(-vdiff):
                    if board.content[temp_pos[0] + i][temp_pos[1] - i] != 0:
                        return False

            return True

        if vdiff > 0:
            if hdiff < 0:
                for i in range(vdiff):
                    if board.content[temp_pos[0] - i][temp_pos[1] + i] != 0:
                        return False

            if hdiff > 0:
                for i in range(vdiff):
                    if board.content[temp_pos[0] + i][temp_pos[1] + i] != 0:
                        return False

            return True


def move_set(board, selected_piece, mouse_pos, temp_pos):
    eat = False

    #Can't eat own piece, multiplication of two pieces id must be negative or 0
    if selected_piece * board.content[mouse_pos[0]][mouse_pos[1]] < 0:
        eat = True
    elif selected_piece * board.content[mouse_pos[0]][mouse_pos[1]] == 0:
        eat = False
    else:
        return False

    #Pawns
    if abs(selected_piece) == 1:
        if eat == False:
            if temp_pos[0] - mouse_pos[0] == 0:
                if selected_piece == 1:
                    if temp_pos[1] == 6:
                        if temp_pos[1] - mouse_pos[1] == 1:
                            return True
                        elif temp_pos[1] - mouse_pos[1] == 2 and board.content[temp_pos[0]][temp_pos[1] - 1] == 0:
                            return True
                    else:
                        if temp_pos[1] - mouse_pos[1] == 1:
                            return True


                if selected_piece == -1:
                    if temp_pos[1] == 1:
                        if temp_pos[1] - mouse_pos[1] == -1:
                            return True
                        elif temp_pos[1] - mouse_pos[1] == -2 and board.content[temp_pos[0]][temp_pos[1] + 1] == 0:
                            return True
                    else:
                        if temp_pos[1] - mouse_pos[1] == -1:
                            return True

        if eat == True:
            if selected_piece == 1:
                if abs(temp_pos[0] - mouse_pos[0]) == 1 and temp_pos[1] - mouse_pos[1] == 1:
                    return True
            if selected_piece == -1:
                if abs(temp_pos[0] - mouse_pos[0]) == 1 and temp_pos[1] - mouse_pos[1] == -1:
                    return True

    #Rook
    if abs(selected_piece) == 2:
        return move_block_check(True, False, False, temp_pos, mouse_pos, board)

    #Bishop
    if abs(selected_piece) == 3:
        return move_block_check(False, True, False, temp_pos, mouse_pos, board)

    #Knight
    if abs(selected_piece) == 4:
        if abs(mouse_pos[0] - temp_pos[0]) == 1 and abs(mouse_pos[1] - temp_pos[1]) == 2 or abs(mouse_pos[0] - temp_pos[0]) == 2 and abs(mouse_pos[1] - temp_pos[1]) == 1:
            return True

    #Queen
    if abs(selected_piece) == 5:
        return move_block_check(True, True, False, temp_pos, mouse_pos, board)

    #King
    if abs(selected_piece) == 6:
        return move_block_check(True, True, True, temp_pos, mouse_pos, board)

    return False


def game(board, screen, chess_dic):

    start = True

    #check if mouse is pressed
    pressed = False
    #ensure only one piece is being selected
    selected_piece = None
    temp_pos = None

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

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
                board.content[mouse_pos[0]][mouse_pos[1]] = 0

            else:
                if selected_piece != 0:
                    screen.blit(chess_dic[selected_piece].sprite, (exact_mouse_pos[0] - board.space/2, exact_mouse_pos[1] - board.space/2))

            #To show the available moves
            move_lst = show_moves(temp_pos, selected_piece, board)

            for moves in move_lst:
                pygame.draw.rect(screen, board.light_red, ((board.space * moves[0]), (board.space * moves[1])
                                                     , (board.space), (board.space)))

        #m1 is released
        if not pygame.mouse.get_pressed()[0] and pressed == True:
            pressed = False

            exact_mouse_pos = pygame.mouse.get_pos()
            mouse_pos = [math.floor(exact_mouse_pos[0] / board.space), math.floor(exact_mouse_pos[1] / board.space)]


            if move_set(board, selected_piece, mouse_pos, temp_pos):

                #Check for pawn promotion
                if selected_piece == 1 and mouse_pos[1] == 0:
                    selected_piece = 5
                if selected_piece == -1 and mouse_pos[1] == board.const - 1:
                    selected_piece = -5

                board.content[mouse_pos[0]][mouse_pos[1]] = selected_piece

            else:
                board.content[temp_pos[0]][temp_pos[1]] = selected_piece

            #has to be here to use the piece's id
            selected_piece = None

        pygame.display.update()

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