##.i
##.b=5
def SimpsonsRuleIntegration(func, n, W, x, dof):
    sumOdds = GetSumOdds(func, n, W, dof)
    sumEvens = GetSumEvens(func, n, W, dof)
    integral = W / 3 * (func(0, dof) + sumOdds + sumEvens + func(x, dof))
    return integral