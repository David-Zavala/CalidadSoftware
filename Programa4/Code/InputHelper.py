from Code.StringHelper import StringHelper as SH

class InputHelper:
    ##.i
    @staticmethod
    def askForX():
        while True:
            inputValue = input("Ingrese el valor de x: ")
            
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

            if inputAsNumber < 0:
                print("Debe ser mayor o igual a 0")
                continue

            return inputAsNumber

    ##.i
    @staticmethod
    def askForDof():
        while True:
            inputValue = input("Ingrese el valor de dof (deegres of freedom): ")
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

            if inputAsNumber < 0:
                print("Debe ser mayor o igual a 0")
                continue

            return inputAsNumber