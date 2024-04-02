from Code.Simpsons import MathHelper as MH
from Code.InputHelper import InputHelper as IH

##.i
def main():
    x = IH.askForX()
    dof = IH.askForDof()

    MH.CalculateIntegrateBySimpsonsRule(x, dof)
        
if __name__=="__main__": 
    main()