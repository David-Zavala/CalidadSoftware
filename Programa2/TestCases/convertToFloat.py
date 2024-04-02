##.i
##.b=10
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