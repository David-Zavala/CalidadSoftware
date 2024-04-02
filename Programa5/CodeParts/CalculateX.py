##.i
def CalculateX(p:float, dof:int, n:int=10, x_initial:float=1.0, E:float = 0.0000001):
    x = MathHelper.FindXBySimspsonsRule(p,dof,n,x_initial,x_initial/2,E)

    result = f"  p = {round(p,5):.5f}\ndof = {round(dof,5):.0f}\n  x = {round(x,5):.5f}"
    print (result)
    return x