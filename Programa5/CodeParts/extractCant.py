##.i
##.b=4
def extractCant(string: str):
    """ Método extractCant
        Regresa un entero, que es la cantidad indicada en la marca de un comentario, ya sea .b o .d
    """
    string = string.strip()
    value = int(string)
    return value