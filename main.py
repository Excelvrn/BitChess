import moves, tower

desk=[i for i in range(0,64)]
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
#get list of w/b figures
def getwbfl(color, desk):
    wbfl=[]
    for i in range(0, len(desk)):
        if (desk[i] != 0) and (figure(desk[i])[0] == color):
            wbfl += [[desk[i], i]]
    return wbfl
def shiftmove(pos1, pos2):
    hor = abs(toxy(pos1)[0]  - toxy(pos2)[0])
    ver = abs(toxy(pos1)[1]  - toxy(pos2)[1])
    return [hor, ver]
###
### pawn
def hod1(fig, pos1, pos2):
    move = 0
    if (figure(fig)[0] == 1) and (figure(fig)[1] == 1):
        #move = 1
        startpos = 1
        if (toxy(pos1)[0] == startpos) and (pos2==(pos1+16)):
            move = 1
        elif (toxy(pos1)[0] >= startpos)and (pos2==(pos1+8)):
            move = 1
        elif (toxy(pos1)[0] >= startpos)and (pos2==(pos1+7)) and ((toxy(pos1)[0]+1)==toxy(pos2)[0]):
            move = 1
        elif (toxy(pos1)[0] >= startpos)and (pos2==(pos1+9))and ((toxy(pos1)[0]+1)==toxy(pos2)[0]):
            move = 1
        else:
            move = 0
    elif (figure(fig)[0] == 2) and (figure(fig)[1] == 1):
        startpos = 6
        if (toxy(pos1)[0] == startpos) and (pos1==(pos2+16)):
            move = 1
        elif (toxy(pos1)[0] <= startpos)and (pos1==(pos2+8)):
            move = 1
        elif (toxy(pos1)[0] <= startpos)and (pos1==(pos2+7)) and ((toxy(pos2)[0]+1)==toxy(pos1)[0]):
            move = 1
        elif (toxy(pos1)[0] <= startpos)and (pos1==(pos2+9))and ((toxy(pos2)[0]+1)==toxy(pos1)[0]):
            move = 1
        else:
            move = 0
    else:
        move = 0
    return [move, pos1, pos2]
### knight:
def hod2(pos1, pos2):
    move=0
    if (shiftmove(pos1,pos2)[0] == 2) and (shiftmove(pos1,pos2)[1] == 1):
        print("\tMove:\t:", pos1, pos2)
        move = 1
    elif (shiftmove(pos1,pos2)[0] == 1) and (shiftmove(pos1,pos2)[1] == 2):
        print("\tMove:\t:", pos1, pos2)
        move = 1
    return [move, pos1, pos2]
### bishop:
def hod3(pos1, pos2):
    move=0
    if (shiftmove(pos1, pos2)[0] ==  shiftmove(pos1, pos2)[1]) and (pos1!=pos2) and (shiftmove(pos1, pos2)[0] !=0):
        print("\tMove", pos1, pos2)
        move = 1
    return [move, pos1, pos2]
### Ladja:
def hod4(pos1, pos2):
    move=0
    if (toxy(pos1)==toxy(pos2)):
        print("EQU:\t", pos1, pos2)
    if (toxy(pos1)[0]==toxy(pos2)[0]):
        print("\tHor",pos1,pos2)
        move = 1
    elif (toxy(pos1)[1]==toxy(pos2)[1]):
        print("\tVer",pos1,pos2)
        move = 1
    else:
        print("Error!", pos1, pos2)
    return [move, pos1, pos2]
### Q
def hod5(pos1, pos2):
    move = 0
    if (pos1!=pos2) and ((hod3(pos1,pos2)[0] == 1) or  (hod4(pos1,pos2)[0] == 1)):
        print("\t\t\tQ-Move:\t", pos1, pos2)
        move = 1
    return [move, pos1, pos2]
### K:
def hod6(pos1, pos2):
    move = 0
    #print(toxy(abs(pos1-pos2)),abs(pos1-pos2))
    if (shiftmove(pos1, pos2)[0]<2) and (shiftmove(pos1, pos2)[1]<2) and (pos1!=pos2):
        #print("K-move:\t", pos1, pos2)
        move = 1
#    else:
#        print([pos1, pos2], abs(pos1 - pos2))
    return [move, pos1, pos2]
### The allowed moves of figures: [move1, move2...]
### without check, mate and other figures
def allowedmoves2(fig, pos):
    almoves = []
    mv = figure(fig)[1]
    if (mv == 1):
        pn = hod1
    elif (mv ==2):
        pn = hod2
    elif (mv ==3):
        pn = hod3
    elif (mv ==4) or (mv==8):
        pn = hod4
    elif (mv ==5):
        pn = hod5
    elif (mv ==6) or (mv==7):
        pn = hod6
    for i in range(0,64):
        if (mv==1):
            am = pn(fig,pos, i)
        else:
            am = pn(pos, i)
        if (am[0] == 1):
            almoves+=[am[2]]
    return almoves
def allowedmoves3(fig, pos, desk):
    wbfl= getwbfl(figure(fig)[0],desk)
    almo1 = allowedmoves2(fig, pos)
    wbfl1=[]
    if len(wbfl)>1:
        for i in range(0, len(wbfl)):
                 wbfl1+=[wbfl[i][1]]

    #print("almo1",almo1)
    #print("wbfl1",wbfl1)
    
    for i in range(0, len(wbfl1)):
        #print(wbfl1[i])
        for ii in range(0, len(almo1)):
            #print("\t", almo1[ii])
            if (wbfl1[i] == almo1[ii]):
                almo1.remove(wbfl1[i])
                break
    #print("almo1",almo1)
    return almo1
def main():
    print("\t----")
   # for i in range(0,64):
    #   print("\n") 
       #for ii in range(0,64):
          # if hod1(11, i, ii)[0] == 1:
           #    print("white pawn:\t", i, ii) 
           #if hod1(21, i, ii)[0] == 1:
           #    print("black pawn:\t", i, ii) 
    #   print(i, allowedmoves(11,i))
    setdesk(desk)
    #printdesk(desk)
    #print("\n")
    #print(allowedmoves2(21,10))
    #print(allowedmoves2(12,10))
    #print(figure(79))
    #print(getwbfl(1, desk))
    print(allowedmoves3(11, 10, desk))
    print("thr", tower.shiftmovethr(7))
    print("smta", tower.smta(18))
    #print(getwbfl(2, desk))
    pass

main()
