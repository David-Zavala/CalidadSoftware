##.i
##.b=5
def GetSumEvens(func, n, W, dof):
    sumEvens = 0
    for i in range(2, n-1, 2):
        sumEvens += 2*func(i * W, dof)
    return sumEvens