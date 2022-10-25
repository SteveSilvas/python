

class  Converters:
    def __init__(self) -> None:
        pass

    def isInt(self, texto):
        return type(texto) is int


conv = Converters()
txt = 2
a = conv.isInt(txt)
print(str(a))