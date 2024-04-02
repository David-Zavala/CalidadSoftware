##.i
##.b=1
from classes.Classes import Classes ##.m
from classes.ClassesContainer import ClassesContainer ##.m
from methods.CheckMethods import *

##.i
##.b=1
"""Declaración de variables"""
archivos = []
classes = ClassesContainer()
multiComment = False
clasesArray = []

"""Recibir el archivo o archivos que se van a procesar"""
##.i
##.d=1
##.b=4
print("***** Si ya no quiere ingresar más archivos, escriba 'no' ******")
while True:
    archivo = input("Ingrese el nombre del archivo: ")
    if archivo == 'no' or archivo == 'No' or archivo == 'NO':
        if archivos.__len__() > 0:
            break
        else:
            print("Debe ingresar por lo menos 1 archivo e ingreso: 0")
    else:
        if fileExists(archivo):
            archivos.append(archivo)
        else:
            print("Ese archivo no existe :(, asegúrese de escribir bien el nombre. ejem. archivo.txt")

"""Ordenar para posteirormente buscar archivos con el mismo nombre"""
archivos.sort()

##.i
##.d=7
##.b=15
"""Iterar sobre los archivos ingresados"""
for indice, archivo in enumerate(archivos):
    """Declaración de variables"""
    clase = Classes(className=archivo)
            
    """Abrir archivo con el nombre dado"""
    with open("testCases/"+archivo,'r',encoding='latin-1') as text:
        """Obtener una lista de las líneas del archivo"""
        lines = text.readlines()

        """Checar si el archvo es solo una línea en blanco"""
        if lines.__len__() < 1:
            """Agregar esa clase vacía"""
            classes.addClass(clase=clase)
        else:
            """Iterar sobre lines"""
            for line in lines:
                """Checar si es la continuación de un comentario multilinea"""
                if multiComment:
                    """Checar si el comentario multilinea termina"""
                    if (hasCharIn(line,-1,'/') and hasCharIn(line,-2,'*')) or (hasCharIn(line,-1,'"') and hasCharIn(line,-2,'"') and hasCharIn(line,-3,'"')):
                        multiComment = False
                else:
                    """Checar si la línea esta en blanco"""
                    if isBlank(line):
                        continue
                    else:
                        """Checar si la línea es un comentario"""
                        if hasCharIn(line,0,'/') or hasCharIn(line,0,'#') or hasCharIn(line,0,'"'):
                            """Checar si el comentario es multilinea"""
                            if hasCharIn(line,1,'*') or (hasCharIn(line,1,'"') and hasCharIn(line,2,'"')):
                                multiComment = True
                                """Checar si el comentario multilinea acaba en la misma línea"""
                                if (hasCharIn(line,-1,'/') and hasCharIn(line,-2,'*')) or (hasCharIn(line,-1,'"') and hasCharIn(line,-2,'"') and hasCharIn(line,-3,'"')):
                                    multiComment = False
                            else:
                                if (line.strip().__len__() >= 4):
                                    """Checar si es un marcardor de líneas base"""
                                    if hasCharIn(line,2,'.') and hasCharIn(line,3,'b'):
                                        clase.baseUp(extractCant(line))
                                    """Checar si es un marcardor de item"""
                                    if hasCharIn(line,-2,'.') and hasCharIn(line,-1,'i'):
                                        clase.itemsUp()
                                    """Checar si es un marcardor de líneas borradas"""
                                    if hasCharIn(line,2,'.') and hasCharIn(line,3,'d'):
                                        clase.deletedUp(extractCant(line))

                        else:
                            if (line.strip().__len__() > 2):
                                clase.totalUp()
                            if (line.strip().__len__() >= 4):
                                if (hasCharIn(line,-4,'/') and hasCharIn(line,-3,'/') and hasCharIn(line,-2,'.') and hasCharIn(line,-1,'m')) or (hasCharIn(line,-4,'#') and hasCharIn(line,-3,'#') and hasCharIn(line,-2,'.') and hasCharIn(line,-1,'m')):
                                    clase.modifiedUp()
                                else:
                                    continue

            clasesArray.append(clase)

##.i
indice = 0
while indice < clasesArray.__len__()-1:
    if clasesArray[indice].getClassName() == clasesArray[indice+1].getClassName():
        convergedClass = convergeClasses(clasesArray[indice], clasesArray[indice+1],clasesArray[indice].getClassName())
        clasesArray[indice] = convergedClass
        clasesArray.remove(clasesArray[indice+1])
    else:
        indice += 1

##.i
for c in clasesArray:
    classes.addClass(c)

##.i
"""Imprimir resultados"""
with open("results/ConteoLDC.txt", 'w', encoding='latin=1') as resultText:
    resultText.write(str(classes))
print(classes) ##.m