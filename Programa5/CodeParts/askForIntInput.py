##.i
##.b=17
##.d=2
def askForIntInput(message:str=None,min:int=None,minAccepted:int=None,max:int=None,maxAccepted:int=None): ##.m
    while True:
        if message != None:
            inputValue = input(message)
        else:
            inputValue = input("Ingrese un valor entero")

        if SH.isBlank(inputValue):
            print("Debe ingresar un valor")
            continue
        
        if not SH.isNumber(inputValue):
            print("Debe ingresar un valor numérico")
            continue
        
        inputValue = SH.removeCommas(inputValue)

        inputAsNumber = SH.convertToInt(inputValue)
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