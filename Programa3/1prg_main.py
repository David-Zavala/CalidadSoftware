from classes.RegressionCalculator import RegressionCalculator
from methods.Methods import CheckMethods

##.i
##.b=71
##.d=60
"""Declaración de variables"""
archivo = ""
xk = 0

"""Recibir el archivo que se va a procesar y procesarlo"""
while True:
    archivo = input("Ingrese el nombre del archivo: ")
    if not(CheckMethods.fileExists(archivo)): ##.m
        print("Ese archivo no existe :(, asegúrese de escribir bien el nombre. ejem. archivo.txt")
        continue

    with open("testCases/"+archivo,'r',encoding='latin-1') as text:
        lines = text.readlines()
        if lines.__len__() < 3:
            if lines.__len__() > 0:
                print("Ese archivo no es valido, parece ser muy corto, se necesita más de un punto para calcular una regresión")
                continue
            print("Ese archivo no es valido, parece ser que está vacío")
            continue
        
        try:
            xk = int(lines[0])
        except ValueError:
            print("Ese archivo no es valido, la primer linea debe contener un numero entero positivo o 0")
            continue

        if xk < 0:
            print("Ese archivo no es valido, la primer linea debe contener un numero entero positivo o 0")
            continue

        regressionCalculator = RegressionCalculator(xk)
        for line in lines[1:]:
            pair = line.split(',')
            regressionCalculator.addPair(float(pair[0]),float(pair[1]))
    break

"""Imprimir resultados"""
print(regressionCalculator) ##.m