##.i
##.b=5
def GetSumOdds(func, n, W, dof):
    sumOdds = 0
    for i in range(1, n, 2):
        sumOdds += 4*func(i * W, dof)
    return sumOdds