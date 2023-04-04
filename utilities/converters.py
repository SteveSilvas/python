import pandas as pd

class  Converters:
    def __init__(self) -> None:
        pass

    def isInt(self, texto):
        return type(texto) is int

    def getInteger(self,txt):
        result = []
        for caractere in txt:
            if caractere.isdigit():
                result.append(caractere)
        if(self.arrayToString(result) == '' ): return  
        else: return int(self.arrayToString(result))

    def arrayToString(self, array):
        result = ""
        for char in array:
            result += char
        return result

    def haveInt(self, text):
        if(self.getInteger(text)):
            print('Não possui inteiros')
            return False
        else:
            print('Possui inteiros')
            return True

conv = Converters()
txt = "carao"
isInt = conv.isInt(txt)
b = conv.getInteger(txt)
print('a: ', str(isInt))
print('b: ', str(b))

print('txt HaveInt? ', conv.haveInt(txt))