import common
#Limited moves
#SHIFT MOVE Tower Vertical Up
#pos - cell`s number
def shiftmovetvu(pos):
    lim = []
    for i in range(pos, common.DeskSize,8):
        if (i!=pos):
            lim+=[i]
    return lim
#SHIFT MOVE Tower Vertical Down
def shiftmovetvd(pos):
    lim = []
    for i in range(pos, 0,-8):
        if (i!=pos):
            lim+=[i]
    return lim
#SHIFT MOVE Tower Horizontal Right
def shiftmovethr(pos):
    lim = []
    side = (common.toxy(pos)[0]+1)*8
    print("Side is \t", side)
    for i in range(pos, side):
        if (i!=pos):
            lim+=[i]
    return lim
#SHIFT MOVE Tower Horizontal Left
def shiftmovethl(pos):
    lim = []
    side = common.toxy(pos)[0]*8-1
    print("Side is \t", side)
    for i in range(pos, side, -1):
        if (pos!=i):
            lim+=[i]
    return lim
#return [vu, vd, hr, hl]
def smta(pos):
    lim = []
    lim+= [shiftmovetvu(pos)]
    lim+= [shiftmovetvd(pos)]
    lim+= [shiftmovethr(pos)]
    lim+= [shiftmovethl(pos)]
    return lim
