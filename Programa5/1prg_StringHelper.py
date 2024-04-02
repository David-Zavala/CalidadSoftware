
class StringHelper():
    ##.i
    ##.b=5
    @staticmethod
    def isBlank(string: str):
        """ Método isBlank
            Regresa True si el string que se paso es una línea en blanco
        """
        string = string.strip()
        if string:
            return False
        return True

    ##.i
    ##.b=6
    @staticmethod
    def isNumber(string: str):
        acceptedChars = ['0','1','2','3','4','5','6','7','8','9',',','.']
        for char in string:
            if char not in acceptedChars:
                return False
        return True

    ##.i
    ##.b=4
    @staticmethod
    def extractCant(string: str):
        """ Método extractCant
            Regresa un entero, que es la cantidad indicada en la marca de un comentario, ya sea .b o .d
        """
        string = string.strip()
        value = int(string)
        return value

    ##.i
    ##.b=6
    @staticmethod
    def removeCommas(string: str):
        newValue = ""
        for char in string:
            if char != ',':
                newValue += char
        return newValue

    ##.i
    ##.b=10
    @staticmethod
    def convertToFloat(string: str):
        try:
            f = float(string)
            return f
        except ValueError:
            print("El valor no pudo ser convertido a float.\nAsegurese de ingresar un valor adecaudo\n")
            return None
        except TypeError:
            print("El tipo de dato no es adecuado para la conversión a float.\nAsegurese de ingresar un valor adecaudo\n")
            return None

    ##.i
    ##.b=13
    @staticmethod
    def convertToInt(string: str):
        try:
            i = StringHelper.extractCant(string)
            return i
        except ValueError:
            print("El valor no pudo ser convertido a int.\nAsegurese de ingresar un valor adecaudo\n")
            return None
        except TypeError:
            print("El tipo de dato no es adecuado para la conversión a int.\nAsegurese de ingresar un valor adecaudo\n")
            return None
        except OverflowError:
            print("El valor es excesivamente grande.\nAsegurese de ingresar un valor adecaudo... Pruebe con un valor mas pequeño\n")
            return None