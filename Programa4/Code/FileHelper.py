from Code.StringHelper import StringHelper as sh

class FileHelper():
    ##.i
    ##.r=6
    @staticmethod
    def fileExists(path):
        """ Método fileExists
            Regres True si el nombre del archivo existe
        """
        try:
            open(path,'r',encoding='latin-1')
        except FileNotFoundError:
            return False
        return True

    ##.i
    @staticmethod
    def SaveResultInCache(content, name):
        if sh.hasCharIn(name,-4,'.') and sh.hasCharIn(name,-3,'t') and sh.hasCharIn(name,-2,'x') and sh.hasCharIn(name,-1,'t'):
            path = "Cache/"+name
        else:    
            path = "Cache/"+name+'.txt'
        with open(path, "w+") as file:
            file.write(content)