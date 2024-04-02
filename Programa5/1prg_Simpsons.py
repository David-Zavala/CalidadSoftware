from math import pi

class MathHelper:
    ##.i
    ##.b=4
    @staticmethod
    def Gamma(x):
        if (x == 1): return 1
        if (x == 0.5): return pi ** 0.5
        return (x-1) * MathHelper.Gamma(x-1)

    ##.i
    ##.b=4
    @staticmethod
    def TDistributionPDF(x, dof):
        numerator = MathHelper.Gamma((dof + 1) / 2)
        denominator = (MathHelper.Gamma(dof / 2) * ((dof * pi) ** 0.5))
        return (numerator / denominator) * (1 + (x ** 2 / dof)) ** (-(dof + 1) / 2)

    ##.i
    ##.b=5
    @staticmethod
    def SimpsonsRuleIntegration(func, n, W, x, dof):
        sumOdds = MathHelper.GetSumOdds(func, n, W, dof)
        sumEvens = MathHelper.GetSumEvens(func, n, W, dof)
        integral = W / 3 * (func(0, dof) + sumOdds + sumEvens + func(x, dof))
        return integral

    ##.i
    ##.b=5
    @staticmethod
    def GetSumOdds(func, n, W, dof):
        sumOdds = 0
        for i in range(1, n, 2):
            sumOdds += 4*func(i * W, dof)
        return sumOdds

    ##.i
    ##.b=5
    @staticmethod
    def GetSumEvens(func, n, W, dof):
        sumEvens = 0
        for i in range(2, n-1, 2):
            sumEvens += 2*func(i * W, dof)
        return sumEvens

    ##.i
    @staticmethod
    def FindXBySimspsonsRule(p:float, dof:int, n:int=10, x:float=1.0, d:float = 0.5, E:float = 0.0000001, lastResult:float = -1, posOfLastP:str = ""):
        pFromCalculation = MathHelper.SimpsonsRuleIntegration(MathHelper.TDistributionPDF, n, x/n, x, dof)

        if abs(lastResult - pFromCalculation) > E:
            if pFromCalculation < p:
                if posOfLastP != "Lower" and posOfLastP != "": d = d/2
                x+=d
                return MathHelper.FindXBySimspsonsRule(p, dof, n, x, d, E, pFromCalculation, "Lower")
            if pFromCalculation > p:
                if posOfLastP != "Higher" and posOfLastP != "": d = d/2
                x-=d
                return MathHelper.FindXBySimspsonsRule(p, dof, n, x, d, E, pFromCalculation, "Higher")
        
        return x
    
    ##.i
    @staticmethod
    def CalculateX(p:float, dof:int, n:int=10, x_initial:float=1.0, E:float = 0.0000001):
        x = MathHelper.FindXBySimspsonsRule(p,dof,n,x_initial,x_initial/2,E)

        result = f"  p = {round(p,5):.5f}\ndof = {round(dof,5):.0f}\n  x = {round(x,5):.5f}"
        print (result)
        return x