##.i
##.b=13
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