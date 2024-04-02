from classes.Classes import Classes
##.i
class ClassesContainer:
    def __init__(self):
        self.__baseClasses = []
        self.__newClasses = []
        self.__reusedClasses = []
        self.__totalLDC = 0
    
    def addClass(self, clase: Classes):
        """ Método addClass
            Funciona como un append para agregar los reusltados de la clase que reciba
        """
        classification = clase.getClasification()
        self.calculateTotalLDC(clase.getTotal())

        if (classification == 'base'):
            self.__baseClasses.append(str(clase))
        
        if (classification == 'nueva'):
            self.__newClasses.append(str(clase))
        
        if (classification == 'reusada'):
            self.__reusedClasses.append(str(clase))


    def calculateTotalLDC(self, cantLDC: int):
        """ Método calculateTotalLDC
            Acumula progresivamente la cantidad total de líneas de todas las clases recibidas
        """
        self.__totalLDC += cantLDC

    def reset(self):
        """ Método reset
            Reinicia todo a su estado inicial
        """
        self.__baseClasses = []
        self.__newClasses = []
        self.__reusedClasses = []
        self.__totalLDC = 0

    def __str__(self):
        """ Sobreescritura de método __str__ (método especial que indica qué aparece cuando se convierte la instancia en un string)
            Imprime los resultados en el formato deseado
        """
        result = "CLASES BASE:\n"
        for i in range(0, self.__baseClasses.__len__()):
            result += self.__baseClasses[i] + '\n'
        result += "--------------------------------------------\n"
        result += "CLASES NUEVAS:\n"
        for i in range(0, self.__newClasses.__len__()):
            result += self.__newClasses[i] + '\n'
        result += "--------------------------------------------\n"
        result += "CLASES REUSADAS:\n"
        for i in range(0, self.__reusedClasses.__len__()):
            result += self.__reusedClasses[i] + '\n'
        result += "--------------------------------------------\n"
        result += "Total de LDC:{}".format(self.__totalLDC)

        return result
    
    def __repr__(self):
        """ Sobreescritura de método __str__ (método especial que indica qué aparece cuando se convierte la instancia en un string)
            Imprime los resultados en el formato deseado
        """
        result = "CLASES BASE:\n"
        for i in range(0, self.__baseClasses.__len__()):
            result += self.__baseClasses[i] + '\n'
        result += "--------------------------------------------\n"
        result += "CLASES NUEVAS:\n"
        for i in range(0, self.__newClasses.__len__()):
            result += self.__newClasses[i] + '\n'
        result += "--------------------------------------------\n"
        result += "CLASES REUSADAS:\n"
        for i in range(0, self.__reusedClasses.__len__()):
            result += self.__reusedClasses[i] + '\n'
        result += "--------------------------------------------\n"
        result += "Total de LDC:{}".format(self.__totalLDC)

        return result