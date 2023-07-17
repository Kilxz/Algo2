import math
import random
#Ejercicio 5
"""Se asume que los elementos de tareas vienen dado por una tupla (tarea, t0, tf)"""
def adminActividades(tareas, inicio, fin):
    finalList = []
    tareaAux = None
    tiempoFinal = -5
    length = len(tareas) - 1
    for i in tareas:
        if i[1] >= fin:
            if tareaAux != None:
                finalList.append(tareaAux)
            break
        if i[2] > fin:
            continue
        if i[1] < inicio:
            continue
        if tareaAux == None:
            if i[1] < tiempoFinal:
                continue
            tareaAux = i
            if tareas[length] == i:
                finalList.append(tareaAux)
            continue
        if i[1] == tareaAux[1]:
            tiempoTotalAux = tareaAux[2] - tareaAux[1]
            tiempoTotalNew = i[2] - i[1]
            if tiempoTotalNew < tiempoTotalAux:
                tareaAux = i
        else:
            finalList.append(tareaAux)
            tiempoFinal = tareaAux[2]
            tareaAux = None
            if i[1] < tiempoFinal:
                continue
            else:
                tareaAux = i
        if tareas[length] == i:
            if tareaAux != None:
                finalList.append(tareaAux)
    print("Las tareas posibles son:")
    print(finalList)
    return
    
#Ejercicio 6
def buscaPares(vector):
    if vector == []:
        return None
    vector.sort()
    return (vector[0] + vector[1])

#Ejercicio 7
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

#Ejercicio 8
def busquedaBinaria(lista, X):
    if len(lista) == 1:
        if X == lista[0]:
            return True
        return False
    if len(lista) == 2:
        if X == lista[1]:
            return True
        if X == lista[0]:
            return True
        return False
    length = len(lista) - 1
    length = math.trunc(length / 2)
    if lista[length] == X:
        return True
    if lista[length] < X:
        return busquedaBinaria(lista[(length):], X)
    else:
        return busquedaBinaria(lista[0:(length)], X)

#Ejercicio 9
def busquedaKesimo(lista, x):
    if lista == []: return
    if len(lista) == 1:
        print(lista[0])
        return
    length = len(lista) - 1
    i = random.randint(0, length)
    list1Aux = []
    list2Aux = []
    pivote = lista[i]
    for j in range(0, length + 1):
        if j == i: continue
        if lista[j] <= pivote:
            list1Aux.append(lista[j])
        else:
            list2Aux.append(lista[j])
    list1Aux.append(lista[i])
    if len(list1Aux) - 1 == x:
        print(lista[i])
        return
    if len(list1Aux) - 1 < x:
        x = x - len(list1Aux)
        return busquedaKesimo(list2Aux, x)
    else:
        return busquedaKesimo(list1Aux, x)
    