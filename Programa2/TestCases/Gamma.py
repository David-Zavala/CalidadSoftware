##.i
##.b=4
def Gamma(x):
    if (x == 1): return 1
    if (x == 0.5): return pi ** 0.5
    return (x-1) * Gamma(x-1)