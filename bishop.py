import common
#return limited [up-right, down-left]
#Limited moves
#SHIFT MOVE Bishop Vertical Right
#pos - cell`s number
def shiftmovebvr(pos):
    lim = []
    lm = pos
    for i in range(0, 9):
        a = common.chpmov(lm, 1, 1)
        if (a[0]>0):
            lm = a[3]
            lim+=[a[3]]
        else:
            break
    return lim
#SHIFT MOVE Bishop Vertical Left
#pos - cell`s number
def shiftmovebvl(pos):
    lim = []
    lm = pos
    for i in range(0, 9):
        a = common.chpmov(lm, 1, -1)
        if (a[0]>0):
            lm = a[3]
            lim+=[a[3]]
        else:
            break
    return lim
#SHIFT MOVE Bishop Vertical Right Down
#pos - cell`s number
def shiftmovebvrd(pos):
    lim = []
    lm = pos
    for i in range(0, 9):
        a = common.chpmov(lm, -1, 1)
        if (a[0]>0):
            lm = a[3]
            lim+=[a[3]]
        else:
            break
    return lim
#SHIFT MOVE Bishop Vertical Left Down
#pos - cell`s number
def shiftmovebvld(pos):
    lim = []
    lm = pos
    for i in range(0, 9):
        a = common.chpmov(lm, -1, -1)
        if (a[0]>0):
            lm = a[3]
            lim+=[a[3]]
        else:
            break
    return lim

#return [vr, vl, dr, dl]
def smba(pos):
    lim = []
    lim+= [shiftmovebvr(pos)]
    lim+= [shiftmovebvl(pos)]
    lim+= [shiftmovebvrd(pos)]
    lim+= [shiftmovebvld(pos)]
    return lim
