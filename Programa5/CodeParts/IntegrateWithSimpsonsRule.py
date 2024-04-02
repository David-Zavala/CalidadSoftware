 ##.i
##.b=13
def IntegrateWithSimpsonsRule(x, dof, n=10):
    E = 0.0000001
    
    probability1 = MathHelper.SimpsonsRuleIntegration(MathHelper.TDistributionPDF, n, x/n, x, dof)
    n *= 2
    probability2 = MathHelper.SimpsonsRuleIntegration(MathHelper.TDistributionPDF, n, x/n, x, dof)

    while True:
        if abs(probability2 - probability1) > E:
            probability1 = probability2
            n *= 2
            probability2 = MathHelper.SimpsonsRuleIntegration(MathHelper.TDistributionPDF, n, x/n, x, dof)
            continue
        
        break

    return probability2