from algo1 import *
import linkedlist

"""
def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
"""
def createGraph(ListA, ListB):
    n = linkedlist.length(ListA)
    Graph = Array(n, linkedlist.LinkedList())
    for i in range(0, n):
        Graph[i] = linkedlist.LinkedList()

    currentNode = ListB.head
    while currentNode != None:
        linkedlist.add(Graph[currentNode.value[0]], currentNode.value[1])
        linkedlist.add(Graph[currentNode.value[1]], currentNode.value[0])
        currentNode = currentNode.nextNode
    return Graph

"""
def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
"""
def existPath(Grafo, v1, v2):
    auxList = [v1]
    firstList = Grafo[v1]
    return existPathR(Grafo, firstList, auxList, v2)

def existPathR(Grafo, List, auxList, v2):
    if linkedlist.search(List, v2) != None:
        return True
    currentNode = List.head
    condition = False
    while currentNode != None:
        if currentNode.value not in auxList:
            auxList.append(currentNode.value)
            condition = existPathR(Grafo, Grafo[currentNode.value], auxList, v2)
        if condition == True:
            return condition
        currentNode = currentNode.nextNode
    return False
