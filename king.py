import queen
#return all moves of king
def smka(pos):
    q = queen.smqa(pos)
    k=[]
    for i in range(0, len(q)):
        if (len(q[i])>0):
            l = q[i][0]
            k+=[q[i][0]]
    return k
