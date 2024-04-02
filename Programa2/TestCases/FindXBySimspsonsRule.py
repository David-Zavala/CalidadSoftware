##.i
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