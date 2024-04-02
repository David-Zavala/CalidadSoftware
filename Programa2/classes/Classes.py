##.i
class Classes:
    def __init__(self, className: str):
        self.__total_T = 0
        self.__items_I = 0
        self.__base_B = 0
        self.__deleted_D = 0
        self.__modified_M = 0
        self.__added_A = 0
        self.__className = className[:-3] if className.endswith('.py') else className[:-4]

    def totalUp(self, total: int = 1):
        """ Método totalUp
            Aumenta en 1 o en la cantidad que se pase como argumento la cuenta de LDC totales
        """
        self.__total_T += total
    
    def itemsUp(self, items: int = 1):
        """ Método itemsUp
            Aumenta en 1 o en la cantidad que se pase como argumento la cuenta de items en el código
        """
        self.__items_I += items
    
    def baseUp(self, base: int = 1):
        """ Método baseUp
            Aumenta en 1 o en la cantidad que se pase como argumento la cuenta de líneas base en el código
        """
        self.__base_B += base
    
    def deletedUp(self, deleted: int = 1):
        """ Método baseUp
            Aumenta en 1 o en la cantidad que se pase como argumento la cuenta de líneas base en el código
        """
        self.__deleted_D += deleted

    def modifiedUp(self, modified: int = 1):
        """ Método baseUp
            Aumenta en 1 o en la cantidad que se pase como argumento la cuenta de líneas base en el código
        """
        self.__modified_M += modified
        
    def calculateAdded(self):
        """ Método calculateAdded
            Calcula la cantidad de líneas agregadas que tiene el código
        """
        self.__added_A = self.__total_T - self.__base_B + self.__deleted_D
    
    def getClasification(self):
        """ Método getClasification
            Retorna la clasificación de la clase, dependiendo las características
        """
        self.calculateAdded()
        if (self.__base_B > 0 and (self.__modified_M > 0 or self.__deleted_D > 0 or self.__added_A > 0)):
            return 'base'
        
        if (self.__base_B == 0 and self.__modified_M == 0 and self.__deleted_D == 0 and self.__added_A > 0):
            return 'nueva'
        
        if (self.__base_B > 0 and self.__modified_M == 0 and self.__deleted_D == 0 and self.__added_A == 0):
            return 'reusada'

    def getTotal(self):
        """ Método getTotal
            Retorna la cuenta de líneas totales de esta clase
        """
        return self.__total_T

    def getItems(self):
        """ Método getItems
            Retorna la cuenta de items de esta clase
        """
        return self.__items_I

    def getBase(self):
        """ Método getBase
            Retorna la cuenta de líneas base de esta clase
        """
        return self.__base_B
    
    def getDeleted(self):
        """ Método getBase
            Retorna la cuenta de líneas borradas de esta clase
        """
        return self.__deleted_D
    
    def getModified(self):
        """ Método getBase
            Retorna la cuenta de líneas modificadas de esta clase
        """
        return self.__modified_M
    
    def getClassName(self):
        """ Método getTotal
            Retorna la cuenta de líneas totales de esta clase
        """
        return self.__className
    
    def reset(self):
        """ Método reset
            Reinicia todas las cuentas a 0
        """
        self.__total_T = 0
        self.__items_I = 0
        self.__base_B = 0
        self.__deleted_D = 0
        self.__modified_M = 0
        self.__added_A = 0
    
    def __str__(self):
        """ Sobreescritura de método __str__ (método especial que indica qué aparece cuando se convierte la instancia en un string)
            Imprime los resultados en el formato deseado
        """
        result = "{}: ".format(self.__className)
        if (self.__total_T > 0):
            result += "T={}, ".format(self.__total_T)
        if (self.__items_I > 0):
            result += "I={}, ".format(self.__items_I)
        if (self.__base_B > 0):
            result += "B={}, ".format(self.__base_B)
        if (self.__deleted_D > 0):
            result += "D={}, ".format(self.__deleted_D)
        if (self.__modified_M> 0):
            result += "M={}, ".format(self.__modified_M)
        if (self.__added_A > 0) and not (self.__added_A == self.__total_T):
            result += "A={}, ".format(self.__added_A)

        result = result[:-2]
        return result