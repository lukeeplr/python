def bubble_sort(lista):
    tam = len(lista)
    ponteiro = 0
    ordenada = False
    while not ordenada:
        ordenada = True
        for y in range(1, tam - ponteiro):
            if lista[y-1] > lista[y]:
                lista[y-1], lista[y] = lista[y], lista[y-1]
                ordenada = False
        ponteiro += 1
    return lista


def bubble_sortrec(lista, p = 0):
    tam = len(lista)
    ordenada = True
    for x in range(1,tam - p):
        if lista[x-1] > lista[x]:
            lista[x-1], lista[x] = lista[x], lista[x-1]
            ordenada = False
    p += 1
    if not ordenada:
        return bubble_sortrec(lista, p)
    else:
        return lista