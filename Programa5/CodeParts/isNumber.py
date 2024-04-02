##.i
##.b=6
def isNumber(string: str):
    acceptedChars = ['0','1','2','3','4','5','6','7','8','9',',','.']
    for char in string:
        if char not in acceptedChars:
            return False
    return True