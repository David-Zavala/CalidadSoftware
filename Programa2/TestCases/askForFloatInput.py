##.i
##.b=16
##.d=2
##.a=22
def askForFloatInput(message:str=None,min:float=None,minAccepted:bool=False,max:float=None,maxAccepted:bool=False): ##.m
    while True:
        if message != None:
            inputValue = input(message)
        else:
            inputValue = input("Ingrese un valor decimal")
        
        if SH.isBlank(inputValue):
            print("Debe ingresar un valor")
            continue

        if not SH.isNumber(inputValue):
            print("Debe ingresar un valor numérico")
            continue
        
        inputValue = SH.removeCommas(inputValue)
        
        inputAsNumber = SH.convertToFloat(inputValue)
        if not inputAsNumber:
            continue
        
        if min != None:
            if minAccepted:
                if inputAsNumber <= min:
                    print("Debe ser mayor o igual a ", min)
                    continue
            else:
                if inputAsNumber < min:
                    print("Debe ser mayor a ", min)
                    continue

        if max != None:
            if maxAccepted:
                if inputAsNumber >= max:
                    print("Debe ser menor o igual a ", max)
                    continue
            else:
                if inputAsNumber > max:
                    print("Debe ser menor a ", max)
                    continue

        return inputAsNumber