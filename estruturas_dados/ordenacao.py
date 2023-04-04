lista = [10, 4, 5, 2, 6, 7]
lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()


lista = [7,4]
if lista[0]> lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux


if lista[0]> lista[1]:
    lista[0], lista[1] = lista[1], lista[0]



    # selection sort
lista = [3,54,2,34,1,6,5,24,67,4,343]

def selection_sort(lista):
    n = len(lista)
    for i in range(0,n):
        index_menor =i
        for j in range(i+1, n):
            if lista[j]< lista[index_menor]:
                index_menor = j
            lista[i], lista[index_menor] = lista[index_menor], lista[i]

    return lista


def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def merge_sort(lista):
    
print(bubble_sort(lista))
