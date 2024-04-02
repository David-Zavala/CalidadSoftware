from math import pi
from Code.fileExists import FileHelper as fh
from Code.hasCharIn import StringHelper as sh

class MathHelper:
    ##.i
    @staticmethod
    def Gamma(x):
        if (x == 1): return 1
        if (x == 0.5): return pi ** 0.5
        return (x-1) * MathHelper.Gamma(x-1)

    ##.i
    @staticmethod
    def TDsitributionPDF(x, dof):
        numerator = MathHelper.Gamma((dof + 1) / 2)
        denominator = (MathHelper.Gamma(dof / 2) * ((dof * pi) ** 0.5))
        return (numerator / denominator) * (1 + (x ** 2 / dof)) ** (-(dof + 1) / 2)

    ##.i
    @staticmethod
    def SimpsonsRuleIntegration(func, n, W, x, dof):
        sumOdds = MathHelper.GetSumOdds(func, n, W, dof)
        sumEvens = MathHelper.GetSumEvens(func, n, W, dof)

        integral = W / 3 * (func(0, dof) + sumOdds + sumEvens + func(x, dof))
        return integral

    ##.i
    @staticmethod
    def GetSumOdds(func, n, W, dof):
        sumOdds = 0
        for i in range(1, n, 2):
            sumOdds += 4*func(i * W, dof)
        return sumOdds

    ##.i
    @staticmethod
    def GetSumEvens(func, n, W, dof):
        sumEvens = 0
        for i in range(2, n-1, 2):
            sumEvens += 2*func(i * W, dof)
        return sumEvens

    ##.i
    @staticmethod
    def IntegrateWithSimpsonsRule(x, dof, n=10):
        E = 0.0000001
        
        probability1 = MathHelper.SimpsonsRuleIntegration(MathHelper.TDsitributionPDF, n, x/n, x, dof)

        n *= 2
        probability2 = MathHelper.SimpsonsRuleIntegration(MathHelper.TDsitributionPDF, n, x/n, x, dof)

        while True:
            if abs(probability2 - probability1) > E:
                probability1 = probability2
                n *= 2
                probability2 = MathHelper.SimpsonsRuleIntegration(MathHelper.TDsitributionPDF, n, x/n, x, dof)
                continue
            
            break

        return probability2

    ##.i
    @staticmethod
    def CalculateIntegrateBySimpsonsRule(x, dof, n=10):
        if fh.fileExists("Cache/"+str(x)+'-'+str(dof)+'.txt'):
            with open("Cache/"+str(x)+'-'+str(dof)+'.txt', "r+") as result:
                print(result.read())
        
        else:
            p = MathHelper.IntegrateWithSimpsonsRule(x, dof, n)

            result = f"  x = {round(x,5):.5f}\ndof = {round(dof,5):.0f}\n  p = {round(p,5):.5f}"
            print (result)
            
            fileName = str(x)+'-'+str(dof)
            fh.SaveResultInCache(result, fileName)