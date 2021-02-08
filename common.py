import moves

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
#get ver and hor shift size
def shiftmoveabs(pos1, pos2):
    hor = abs(toxy(pos1)[0]  - toxy(pos2)[0])
    ver = abs(toxy(pos1)[1]  - toxy(pos2)[1])
    return [hor, ver]
#get ver and hor shift size
def shiftmove(pos1, pos2):
    hor = toxy(pos1)[0]  - toxy(pos2)[0]
    ver = toxy(pos1)[1]  - toxy(pos2)[1]
    return [hor, ver]
#check potential move
#-1 - not move
#1 - potential
# return [-1/1, hor, ver, new position]
def chpmov(pos, x, y):
    pot = 0
    xyp = toxy(pos)
    xyp[0] +=x
    xyp[1] +=y
    if (xyp[0]>7) or (xyp[0]<0) or (xyp[1]>7) or (xyp[1]<0):
        pot = -1
    else:
        pot = 1
    npos = xyp[0]*8 + xyp[1]
    return [pot, xyp[0], xyp[1], npos]
#get w/b figures`s position list
def getwbfl(color, desk):
    wbfl=[]
    for i in range(0, len(desk)):
        if (desk[i] != 0) and (figure(desk[i])[0] == color):
            wbfl += [[desk[i], i]]
    return wbfl
    pot = 0
    xyp = toxy(pos)
    xyp[0] +=x
    xyp[1] +=y
    if (xyp[0]>7) or (xyp[0]<0) or (xyp[1]>7) or (xyp[1]<0):
        pot = -1
    else:
        pot = 1
    npos = xyp[0]*8 + xyp[1]
    return [pot, xyp[0], xyp[1], npos]
#get all figures`s position list
# [ [white], [black] ]
def getafl(desk):
    wl=[]
    bl=[]
    for i in range(0, len(desk)):
        if (desk[i] != moves.DEMPTY) and (figure(desk[i])[0] == moves.WHITE):
            wl += [i]
    for i in range(0, len(desk)):
        if (desk[i] != moves.DEMPTY) and (figure(desk[i])[0] == moves.BLACK):
            bl += [i]
    afl=[wl, bl]
    return afl
def GetFigure(desk, pos):
    return desk[pos]
#return equal position of the two lists
# lpot - potential moves` list
# lequ - equal elements` list
def GetFirstEqual(lpot, lequ):
    position = -1
    equalpos = -1
    nl = []
        if (len(lpot)>1):
            for ilpot in range(0, len(lpot)):
                if (k>=0):
                    break
                if (len(lequ)>1):
                    for ilequ in range(0, len(lequ)):
                        if (lpot[ilpot] == lequ[ilequ]):
                            k = ilpot
                            break
                elif (len(lequ)==1):
                    if (lpot[ilpot] == lequ[0]):
                        k = ilpot
                        break
                elif (len(lequ)==0):
                    nl = [lpot]
            if (k>=0):
                nl = lpot[0:k]
        elif (len(lpot)==1):
            if (len(lequ)>1):
                for ilequ in range(0, len(lequ)):
                    if (lpot[0] == lequ[ilequ]):
                        k = 0
                        break
                elif (len(lequ)==1):
                    if (lpot[0] == lequ[0]):
                        k = 0
                        break
                #elif (len(lequ)==0):
                    #nl = [lpot]
                if (k>=0):
                    nl = [lpot[0]]
    return nl
            
                            
                            
            
            
