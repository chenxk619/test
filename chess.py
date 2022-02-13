import pygame
import sys
import numpy

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
        self.content = numpy.zeros((self.const, self.const))

class Pieces:
    def __init__(self, sprite, id, value):
        self.sprite = pygame.transform.scale(pygame.image.load("chess_folder/" + sprite + ".png") , (94,94))
        self.id = id
        self.value = value

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

    chess_dic = {-1: black_pawn, 1: white_pawn, -2: black_rook, 2: white_rook, -3: black_bishop, 3: white_bishop,
                 -4: black_knight, 4: white_knight, -5: black_queen, 5: white_queen,
                 -6: black_king, 6: white_king}

    #Load in pieces
    for i in range(board.const):
        board.content[1][i] = black_pawn.id
        board.content[6][i] = white_pawn.id

    for i in range(0, 8, 7):
        if i == 0:
            board.content[i][0] = black_rook.id
            board.content[i][7] = black_rook.id
            board.content[i][1] = black_knight.id
            board.content[i][6] = black_knight.id
            board.content[i][2] = black_bishop.id
            board.content[i][5] = black_bishop.id
            board.content[i][3] = black_queen.id
            board.content[i][4] = black_king.id

        else:
            board.content[i][0] = white_rook.id
            board.content[i][7] = white_rook.id
            board.content[i][1] = white_knight.id
            board.content[i][6] = white_knight.id
            board.content[i][2] = white_bishop.id
            board.content[i][5] = white_bishop.id
            board.content[i][3] = white_queen.id
            board.content[i][4] = white_king.id

    return chess_dic

def game(board, screen, chess_dic):

    start = True

    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Draw board : Even is white, odd is black
        #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        for rows in range(board.const):
            for columns in range(board.const):
                if (rows + columns) % 2 == 0:
                    pygame.draw.rect(screen, (235, 245, 208), ((board.space * rows) , (board.space * columns)
                                     , (board.space) , (board.space)))

                if (rows + columns) % 2 == 1:
                    pygame.draw.rect(screen, (23, 153, 58), ((board.space * rows) , (board.space * columns)
                                     , (board.space) , (board.space)))


        bp = -1
        screen.blit(chess_dic[bp].sprite, (0,0))
        pygame.display.update()

def main():
    #Instatiate the board
    board = Board()
    pygame.init()
    pygame.display.set_caption('Chess')
    screen = pygame.display.set_mode((board.length, board.length))
    chess_dic = load(board)
    print(board.content)
    game(board, screen, chess_dic)

while __name__ == '__main__':
    main()