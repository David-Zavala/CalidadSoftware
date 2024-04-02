##.i
from classes.Classes import Classes

##.i
##.b=5
def isBlank(string: str):
    """ Método isBlank:
        Regresa True si el string que se paso es una línea en blanco
    """
    string = string.strip()
    if string:
        return False
    return True

##.i
##.b=5
def hasCharIn(string: str, position: int, character: str):
    """ Método hasCharIn:
        Regresa si el string recibido tiene un char específico en un lugar específico
    """
    string = string.strip()
    if (string[position] == character):
        return True
    return False

##.i
##.b=6
def fileExists(name):
    """ Método fileExists:
        Regres True si el nombre del archivo existe
    """
    try:
        open("testCases/"+name,'r',encoding='latin-1')
    except FileNotFoundError:
        return False
    return True


##.i
##.i
def extractCant(string: str):
    """ Método extractCant
        Regresa un entero, que es la cantidad indicada en la marca de un comentario, ya sea .b o .d
    """
    string = string.strip()
    string = string[5:]
    return int(string)

##.i
def convergeClasses(claseA: Classes, claseB: Classes, newClassName: str):
    """ Método convergeClasses:
        Regresa una clase nueva, que será la combinación de dos clases
    """
    newClass = Classes(className=(newClassName+'....'))
    newClass.totalUp(total=(claseA.getTotal() + claseB.getTotal()))
    newClass.itemsUp(items=(claseA.getItems() + claseB.getItems()))
    newClass.baseUp(base=(claseA.getBase() + claseB.getBase()))
    newClass.deletedUp(deleted=(claseA.getDeleted() + claseB.getDeleted()))
    newClass.modifiedUp(modified=(claseA.getModified() + claseB.getModified()))

    return newClass