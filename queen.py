import bishop, tower, common
#return all moves of queen
def smqa(pos):
    t = tower.smta(pos)
    b = bishop.smba(pos)
    q = t
    q += b
    return q
