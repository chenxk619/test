import pygame, random, time
pygame.init()

size = width, height = 780 , 490
screen = pygame.display.set_mode(size)

board = pygame.image.load('connect_4.png')

def getPosition(pos):
    if 25 < pos[0] < 115:
        UI = 1
        position(UI, 0)
    if 130 < pos[0] < 220:
        UI = 2
        position(UI, 0)
    if 235 < pos[0] < 325:
        UI = 3
        position(UI, 0)
    if 340 < pos[0] < 430:
        UI = 4
        position(UI, 0)
    if 445 < pos[0] < 535:
        UI = 5
        position(UI, 0)
    if 550 < pos[0] < 640:
        UI = 6
        position(UI, 0)
    if 655 < pos[0] < 745:
        UI = 7
        position(UI, 0)
    if pos[0] < 25 or 115 < pos[0] < 130 or 220 < pos[0] < 235 or 325 < pos[0] < 340 or 430 < pos[0] < 445 or 535 < pos[0] < 550 or 640 < pos[0] < 655 or pos[0] > 745:
        main()


def position(UI, v):
        if UI ==1:
            for a in range(6, 0, -1):
                if screen.get_at((70, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (70, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()
        if UI ==2:
            for a in range(6, 0, -1):
                if screen.get_at((175, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (175, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()
        if UI ==3:
            for a in range(6, 0, -1):
                if screen.get_at((280, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (280, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()
        if UI ==4:
            for a in range(6, 0, -1):
                if screen.get_at((390, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (390, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()
        if UI ==5:
            for a in range(6, 0, -1):
                if screen.get_at((495, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (495, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()
        if UI ==6:
            for a in range(6, 0, -1):
                if screen.get_at((600, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (600, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()
        if UI ==7:
            for a in range(6, 0, -1):
                if screen.get_at((710, a*80 -36)) == (0,0,0,255):
                    pygame.draw.circle(screen, (255, v, 0), (710, a*80 -36), 42)
                    break
                elif a == 1:
                    print('This column is full')
                    if v == 0:
                        main()
                    else:
                        ai_move()

# From 0-41, so range(0,42)
def UI_converter(x):
    j = x // 7
    i = x - 7 * j
    i += 1
    j += 1
    i *= 100
    j *= 70
    return i,j

def ai_move(user_count, ai_count):
    print('It\'s the AI\'s turn')
    time.sleep(0.5)
    choose = 0
    lst = [ 0, 1, 2]
    #Tries to let the AI score in horizontal, vertical and digonal directions
    if choose == 0:
        for x in range(0,42):
            for i in lst:
                if user_count - ai_count == 1:
                    if screen.get_at(UI_converter(x-int(lst[i-1]))) == (255,255,0,255) and screen.get_at(UI_converter(x-int(lst[i-2]))) == (255,255,0,255) and screen.get_at(UI_converter(x-int(lst[i-2]))) == (255,255,0,255):
                        if screen.get_at(UI_converter(x-int(lst[i]))) != (255, 0, 0 ,255):
                            choose += 1
                            position((x-int(lst[i])) - 7*((x-int(lst[i]))//7)+1, 255)
                            for x in range(0, 42):
                                if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                    ai_count += 1
        for x in range(0, 42):
            if user_count - ai_count == 1:
                if screen.get_at(UI_converter(x)) == (255, 255, 0, 255) and screen.get_at(UI_converter(x - 7)) == (255, 255, 0, 255) and screen.get_at(UI_converter(x - 14)) == (255, 255, 0, 255):
                    if screen.get_at(UI_converter(x-21)) != (255, 0, 0 ,255):
                        choose += 1
                        position((x-21) - 7*((x-21)//7)+1, 255)
                        for x in range(0, 42):
                            if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                ai_count += 1
        for x in range(0,42):
            if user_count - ai_count == 1:
                if screen.get_at(UI_converter(x)) == (255,255, 0, 255) and screen.get_at(UI_converter(x-6)) == (255, 255, 0, 255) and screen.get_at(UI_converter(x-12)) == (255, 255, 0, 255):
                    if screen.get_at(UI_converter(x - 18)) != (255, 0, 0, 255):
                        choose += 1
                        position((x-18) - 7*((x-18)//7)+1, 255)
                        for x in range(0, 42):
                            if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                ai_count += 1

        for x in range(20, 42):
            if user_count - ai_count == 1:
                if screen.get_at(UI_converter(x)) == (255, 255, 0, 255) and screen.get_at(UI_converter(x - 8)) == (255, 255, 0, 255) and screen.get_at(UI_converter(x - 16)) == (255, 255, 0, 255):
                    if screen.get_at(UI_converter(x - 24)) != (255, 0, 0, 255):
                        choose += 1
                        position((x-24) - 7*((x-24)//7)+1, 255)
                        for x in range(0, 42):
                            if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                ai_count += 1

    #Tries to prevent the user from scoring in horizontal, vertical and digaonal directions

    if choose == 0:
        for x in range(0,42):
            for i in lst:
                if user_count - ai_count == 1:
                    if screen.get_at(UI_converter(x-int(lst[i-1]))) == (255,0,0,255) and screen.get_at(UI_converter(x-int(lst[i-2]))) == (255,0,0,255):
                        if screen.get_at(UI_converter(x-int(lst[i]))) != (255, 255, 0 ,255):
                            choose += 1
                            position((x-int(lst[i])) - 7*((x-int(lst[i]))//7)+1, 255)
                            for x in range(0, 42):
                                if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                    ai_count += 1

        for x in range(0, 42):
            if user_count - ai_count == 1:
                if screen.get_at(UI_converter(x)) == (255, 0, 0, 255) and screen.get_at(UI_converter(x - 7)) == (255, 0, 0, 255) and screen.get_at(UI_converter(x - 14)) == (255, 0, 0, 255):
                    if screen.get_at(UI_converter(x-21)) != (255, 255, 0 ,255):
                        choose += 1
                        position((x-21) - 7*((x-21)//7)+1, 255)
                        for x in range(0, 42):
                            if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                ai_count += 1

        for x in range(0,42):
            if user_count - ai_count == 1:
                if screen.get_at(UI_converter(x)) == (255,0,0,255) and screen.get_at(UI_converter(x-6)) == (255,0,0,255) and screen.get_at(UI_converter(x-12)) == (255,0,0,255):
                    if screen.get_at(UI_converter(x - 18)) != (255, 255, 0, 255):
                        choose += 1
                        position((x-18) - 7*((x-18)//7)+1, 255)
                        for x in range(0, 42):
                            if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                ai_count += 1

        for x in range(20, 42):
            if user_count - ai_count == 1:
                if screen.get_at(UI_converter(x)) == (255, 0, 0, 255) and screen.get_at(UI_converter(x - 8)) == (255, 0, 0, 255) and screen.get_at(UI_converter(x - 16)) == (255, 0, 0, 255):
                    if screen.get_at(UI_converter(x - 24)) != (255, 255, 0, 255):
                        choose += 1
                        position((x-24) - 7*((x-24)//7)+1, 255)
                        for x in range(0, 42):
                            if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                                ai_count += 1
    if choose == 0:
        if user_count - ai_count == 1:
            print('random')
            Rand = random.randint(1,7)
            position(Rand, 255)


def win_check(v):
    #check horizontal, vertical, diagonals respectively
    for x in range(0,42):
        if screen.get_at(UI_converter(x)) == (255,v,0,255) and screen.get_at(UI_converter(x-1)) == (255,v,0,255) and screen.get_at(UI_converter(x-2)) == (255,v,0,255) and screen.get_at(UI_converter(x-3)) == (255,v,0,255):
            pygame.draw.line(screen, (0,0,0), UI_converter(x), UI_converter(x-3), 10)
            pygame.display.update()
            win(v)

    for x in range(0,42):
        if screen.get_at(UI_converter(x)) == (255,v,0,255) and screen.get_at(UI_converter(x-7)) == (255,v,0,255) and screen.get_at(UI_converter(x-14)) == (255,v,0,255) and screen.get_at(UI_converter(x-21)) == (255,v,0,255):
            pygame.draw.line(screen, (0, 0, 0), UI_converter(x), UI_converter(x - 21), 10)
            pygame.display.update()
            win(v)

    for x in range(0,42):
        if screen.get_at(UI_converter(x)) == (255,v,0,255) and screen.get_at(UI_converter(x-6)) == (255,v,0,255) and screen.get_at(UI_converter(x-12)) == (255,v,0,255) and screen.get_at(UI_converter(x-18)) == (255,v,0,255):
            pygame.draw.line(screen, (0, 0, 0), UI_converter(x), UI_converter(x - 18), 10)
            pygame.display.update()
            win(v)

    for x in range(20,42):
        if screen.get_at(UI_converter(x)) == (255,v,0,255) and screen.get_at(UI_converter(x-8)) == (255,v,0,255) and screen.get_at(UI_converter(x-16)) == (255,v,0,255) and screen.get_at(UI_converter(x-24)) == (255,v,0,255):
            pygame.draw.line(screen, (0, 0, 0), UI_converter(x), UI_converter(x - 24), 10)
            pygame.display.update()
            win(v)

def win(v):
    if v == 0:
        print('You won!')
    else:
        print('The AI won!')
    time.sleep(2)
    screen.fill((0,0,0,))

def main():
    user_count = 0
    ai_count = 0
    ai_choose = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and ai_choose == True:
                ai_choose = False
                pos = pygame.mouse.get_pos()
                getPosition(pos)
                for x in range(0, 42):
                    if screen.get_at(UI_converter(x)) == (255, 0, 0, 255):
                        user_count += 1
                for x in range(0, 42):
                    if screen.get_at(UI_converter(x)) == (255, 255, 0, 255):
                        ai_count += 1
                print(user_count, ai_count)
                screen.blit(board, (0,0))
                pygame.display.update()
                win_check(0)
                ai_move(user_count, ai_count)
                ai_count = 0
                user_count = 0
                ai_choose = True
                screen.blit(board, (0, 0))
                pygame.display.update()
                win_check(255)
        screen.blit(board, (0, 0))
        pygame.display.update()

main()
