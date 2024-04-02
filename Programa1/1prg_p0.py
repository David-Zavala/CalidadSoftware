from classes.Code import Code
from methods.CheckMethods import *

while True:
    archivo = input("Ingrese el nombre del archivo: ")
    if fileExists(archivo):
        break
    print("Ese archivo no existe :(, asegúrese de escribir bien el nombre. ejem. archivo.txt")

"""Declaración de variables"""
code = Code(archivo)
multiComment = False

"""Abrir archivo con el nombre dado"""
with open("testCases/"+archivo,'r',encoding='latin-1') as text:
    """Obtener una lista de las líneas del archivo"""
    lines = text.readlines()
    """Checar si el archvo es solo una línea en blanco"""
    if lines.__len__() < 1:
        code.blanksUp()
    else:
        """Iterar sobre lines"""
        for line in lines:
            """Checar si es la continuación de un comentario multilinea"""
            if multiComment:
                code.commentsUp()
                """Checar si el comentario multilinea termina"""
                if hasCharIn(line,-1,'/') and hasCharIn(line,-2,'*'):
                    multiComment = False
            else:
                """Checar si la línea esta en blanco"""
                if isBlank(line):
                    code.blanksUp()
                else:
                    """Checar si la línea es un comentario"""
                    if hasCharIn(line,0,'/'):
                        code.commentsUp()
                        """Checar si el comentario es multilinea"""
                        if hasCharIn(line,1,'*'):
                            multiComment = True
                    else:
                        code.codesUp()
        """Checar si hay una última línea vacía"""
        if lines[-1][-1] == '\n':
            code.blanksUp()

"""Imprimir resultados"""
print(code)