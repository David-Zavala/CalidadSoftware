from math import pi
from Classes.FileHelper import fileExists

##.i
def Gamma(x):
    if (x == 1): return 1
    if (x == 0.5): return pi ** 0.5
    return (x-1) * Gamma(x-1)

##.i
def TDsitributionPDF(x, dof):
    numerator = Gamma((dof + 1) / 2)
    denominator = (Gamma(dof / 2) * ((dof * pi) ** 0.5))
    return (numerator / denominator) * (1 + (x ** 2 / dof)) ** (-(dof + 1) / 2)

##.i
def SimpsonsRuleIntegration(func, n, W, x, dof):
    sumOdds = GetSumOdds(func, n, W, dof)
    sumEvens = GetSumEvens(func, n, W, dof)

    integral = W / 3 * (func(0, dof) + sumOdds + sumEvens + func(x, dof))
    return integral

##.i
def GetSumOdds(func, n, W, dof):
    sumOdds = 0
    for i in range(1, n, 2):
        sumOdds += 4*func(i * W, dof)
    return sumOdds

##.i
def GetSumEvens(func, n, W, dof):
    sumEvens = 0
    for i in range(2, n-1, 2):
        sumEvens += 2*func(i * W, dof)
    return sumEvens

##.i
def IntegrateWithSimpsonsRule(x, dof, n = 10):
    E = 0.0000001
    
    probability1 = SimpsonsRuleIntegration(TDsitributionPDF, n, x/n, x, dof)

    n*=2
    probability2 = SimpsonsRuleIntegration(TDsitributionPDF, n, x/n, x, dof)

    while True:
        if (abs(probability2 - probability1) > E):
            probability1 = probability2
            n*=2
            probability2 = SimpsonsRuleIntegration(TDsitributionPDF, n, x/n, x, dof)
            continue
        
        break

    return probability2

##i
def CalculateIntegrateBySimpsonsRule(x,dof,n=10):
    if fileExists("Cache/"+str(x)+'-'+str(dof)+'.txt'):
        with open("Cache/"+str(x)+'-'+str(dof)+'.txt',"r+") as result:
            print(result.read())
    
    else:
        p = IntegrateWithSimpsonsRule(x,dof,n)

        result = f"  x = {round(x,5):.5f}\ndof = {round(dof,5):.5f}\n  p = {round(p,5):.5f}"
        print (result)
        
        fileName = str(x)+'-'+str(dof)
        SaveResultInCache(result,fileName)

##.i
def SaveResultInCache(content,name):
    path = "Cache/"+name+'.txt'
    with open(path, "w+") as file:
        file.write(content)