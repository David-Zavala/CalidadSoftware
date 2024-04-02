##.i
##.b=4
def TDistributionPDF(x, dof):
    numerator = Gamma((dof + 1) / 2)
    denominator = (Gamma(dof / 2) * ((dof * pi) ** 0.5))
    return (numerator / denominator) * (1 + (x ** 2 / dof)) ** (-(dof + 1) / 2)