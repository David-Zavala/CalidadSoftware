class Code:
    def __init__(self, fileName: str):
        self.__blanks = 0
        self.__codes = 0
        self.__comments = 0
        self.__total = 0
        self.__fileName = fileName

    def blanksUp(self):
        """ Método blanksUp
            Aumenta en 1 la cuenta de líneas blancas y la cuenta total de líneas
        """
        self.__blanks += 1
        self.__total += 1
    
    def codesUp(self):
        """ Método codesUp
            Aumenta en 1 la cuenta de líneas de código y la cuenta total de líneas
        """
        self.__codes += 1
        self.__total += 1
    
    def commentsUp(self):
        """ Método cmmentsUp
            Aumenta en 1 la cuenta de líneas de comentarios y la cuenta total de líneas
        """
        self.__comments += 1
        self.__total += 1
    
    def reset(self):
        """ Método reset
            Reinicia todas las cuentas a 0
        """
        self.__blanks = 0
        self.__codes = 0
        self.__comments = 0
        self.__total = 0
    
    def __repr__(self):
        """ Sobreescritura de método __repr__ (método especial que indica qué aparece cuando se imprime una instancia de esta clase)
            Imprime los resultados en el formato deseado
        """
        result = "Nombre del archivo: {}\n".format(self.__fileName)
        result += "--------------------------------------------\n"
        result += "Cantidad de líneas en blanco: {}\n".format(self.__blanks)
        result += "Cantidad de líneas con comentarios: {}\n".format(self.__comments)
        result += "Cantidad de líneas con código: {}\n".format(self.__codes)
        result += "--------------------------------------------\n"
        result += "Cantidad total de líneas: {}\n".format(self.__total)

        return result