from algo1 import *
import linkedlist

#Punto 1
"""
def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
"""
#O(A + V)
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

#Punto 2
"""
def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
"""
#O(V al cuadrado) 
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

#Punto 3
#Posible O(V a la cuarta)
def isConnected(Grafo):
    n = len(Grafo)
    for i in range(0, n-1):
        for j in range(i, n):
            condition = existPath(i, j)
            if condition == False:
                return False
    return True

#Punto 5
#O(V*V), podria mejorarse a O(V) con listas de python
def isComplete(Grafo):
    n = len(Grafo)
    for i in range(0, n):
        if (n-1) != linkedlist.length(Grafo[i]):
            return False
    return True