def itemExist(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo < maximo:
        meio = (minimo + maximo) // 2

        if valor < lista[meio]:
            minimo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True
        return False