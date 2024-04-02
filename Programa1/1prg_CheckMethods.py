def isBlank(string: str):
    string = string.strip()
    if string:
        return False
    return True

def hasCharIn(string: str, position: int, character: str):
    string = string.strip()
    if (string[position] == character):
        return True
    return False

def fileExists(name):
    try:
        open("testCases/"+name,'r',encoding='latin-1')
    except FileNotFoundError:
        return False
    return True