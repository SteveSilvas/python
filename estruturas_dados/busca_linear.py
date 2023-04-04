def busca(lista, item):
    for i in lista:
        if(i == item):
            print('possuo o numero: ', i)
            return i
    return
# print(busca([30,5,2,543,6,1,3,4,56,], 4))


def buscaMap(lista, item):
    itemOFList = map(lambda x: item, lista)
    return list(itemOFList)[0]
# print(buscaMap(['casa', 'carro', 'carta', 'cobra'], 'casa'))


def listStringToLower(lista, item):
    nova_lista = map(lambda x: x.lower(), lista)
    return list(nova_lista)
# print(listStringToLower(['Casa', 'carRo', 'cArta', 'COBRA'], 'casa'))


def stringToList(string):
    lista_string = string.split()
    nova_lista = map(lambda x: x.lower(), lista_string)
    return list(nova_lista)
# print(stringToList('def use create drop init'))


def getPair(lista):
    return list(filter(lambda x: x % 2 == 0, lista))
# lista = list(range(0, 21))
# print(getPair(lista))
