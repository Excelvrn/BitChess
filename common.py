DeskSize = 64
def setdesk(desk):
    for i in range(0, 64):
        desk[i] = 0
    #white side
    desk[0] = 14
    desk[1] = 12
    desk[2] = 13
    desk[3] = 15
    desk[4] = 16
    desk[5] = 13
    desk[6] = 12
    desk[7] = 14
    desk[8] = 11
    desk[9] = 11
    desk[10] = 11
    desk[11] = 11
    desk[12] = 11
    desk[13] = 11
    desk[14] = 11
    desk[15] = 11
    #black side
    desk[63] = 24
    desk[62] = 22
    desk[61] = 23
    desk[60] = 26
    desk[59] = 25
    desk[58] = 23
    desk[57] = 22
    desk[56] = 24
    desk[55] = 21
    desk[54] = 21
    desk[53] = 21
    desk[52] = 21
    desk[51] = 21
    desk[50] = 21
    desk[49] = 21
    desk[48] = 21
    pass
def printdesk(desk):
    for i in range(0,8):
        print(desk[(8*i):(8*i+8)])
    pass
#   figure(number): [   colour, fig]
#                       0,      1
def figure(number):
    fig = number % 10
    colour = number // 10
    return [colour, fig]
def figure_out(number):
    if (figure(number)[0] == 0) and (figure(number)[1] == 0):
        print("Empty")
    elif (figure(number)[0] == 1) and (figure(number)[1] == 1):
        print("Black pawn")
    elif (figure(number)[0] == 1) and (figure(number)[1] == 2):
        print("Black knight")
    elif (figure(number)[0] == 1) and (figure(number)[1] == 3):
        print("Black bishop")
    elif (figure(number)[0] == 1) and (figure(number)[1] == 4):
        print("Black Ladja")
    elif (figure(number)[0] == 1) and (figure(number)[1] == 5):
        print("Black Q")
    elif (figure(number)[0] == 1) and (figure(number)[1] == 6):
        print("Black K")
    elif (figure(number)[0] == 2) and (figure(number)[1] == 1):
        print("White pawn")
    elif (figure(number)[0] == 2) and (figure(number)[1] == 2):
        print("White knight")
    elif (figure(number)[0] == 2) and (figure(number)[1] == 3):
        print("White bishop")
    elif (figure(number)[0] == 2) and (figure(number)[1] == 4):
        print("White Ladja")
    elif (figure(number)[0] == 2) and (figure(number)[1] == 5):
        print("White Q")
    elif (figure(number)[0] == 2) and (figure(number)[1] == 6):
        print("White K")
    pass
def toxy(pos):
    # [x,y]
    # x - горизонталь
    # y - вертикаль
    return [pos // 8, pos % 8]
