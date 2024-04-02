##.i
##.b=7
class CheckMethods:
    def fileExists(name):
        """ Método fileExists
            Regres True si el nombre del archivo existe
        """
        try:
            open("testCases/"+name,'r',encoding='latin-1')
        except FileNotFoundError:
            return False
        return True