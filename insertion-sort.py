def insertion_sort(lista):
    tam = len(lista)
    for x in range(1,tam):
        num = lista[x]
        i = x - 1
        aux = True
        while i >= 0 and aux:
            if num < lista[i]:
                lista[i+1],lista[i] = lista[i],num
                i -= 1
            else:
                aux = False
    return lista