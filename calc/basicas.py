class Basicas:
    def __init__(self):
        self.result = 0

    def toSum(self, a, b):
        self.result = a + b
        return self.result
    def toSub(self, a, b):
        self.result = a - b
        return self.result

    def toMult(self, a, b):
        self.result = a * b
        return self.result

    def toDiv(self, a, b):
        self.result = a / b
        return(self.result)

