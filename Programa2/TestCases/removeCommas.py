##.i
##.b=6
def removeCommas(string: str):
    newValue = ""
    for char in string:
        if char != ',':
            newValue += char
    return newValue