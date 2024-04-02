##.i
##.b=5
def isBlank(string: str):
    """ Método isBlank
        Regresa True si el string que se paso es una línea en blanco
    """
    string = string.strip()
    if string:
        return False
    return True