from Code.Simpsons import MathHelper as MH
from Code.InputHelper import InputHelper as IH

##.i
##.b=6
def main():
    p = IH.askForFloatInput("Ingrese valor de p: ",0,True,0.5,True) ##.m
    dof = IH.askForIntInput("Ingrese valor de dof (grados de libertad): ",0) ##.m

    MH.CalculateX(p,dof) ##.m

if __name__=="__main__": 
    main()