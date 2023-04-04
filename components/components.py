# import sys
# sys.path.insert(1, 'utilities')
from . import converters
class Components:
   
    def inputNumber(self, message):
        entrada = input(message)
        conv = converters.Converters()
        return conv.Converters.getInteger(entrada)


c = Components()
c.inputNumber("digite")