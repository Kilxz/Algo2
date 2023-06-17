
#Ejercicio 5
def buscaPares(vector):
    if vector == []:
        return None
    vector.sort()
    return (vector[0] + vector[1])

#Ejercicio 6
#Latas dado por [(b1, p1), (b2, p2), ...]
def mochila(PesoMax, latas):
    latas.sort()
    pesoAux = 0
    newList = []
    for i in range(latas):
        pesoAux = pesoAux + i[1]
        if pesoAux > PesoMax:
            return newList
        else:
            newList.append(i)
    return newList 
