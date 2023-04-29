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
            condition = existPath(Grafo, i, j)
            if condition == False:
                return False
    return True

#Punto 4
#Probable O(V a la cuarta)
def isTree(Grafo):
    if isConnected(Grafo) == False:
        return False
    n = len(Grafo)
    for i in range(0, n):
        currentNode = Grafo[i].head
        while currentNode != None:
            condition = isTreeR(Grafo, currentNode.value, i, i, currentNode.value)
            if condition == False:
                return False
            currentNode = currentNode.nextNode
    return True

def isTreeR(Grafo, firstVertex, searchedVertex, lastVertex, nextVertex):
    if firstVertex != nextVertex:
        if linkedlist.search(Grafo[nextVertex], searchedVertex) != None:
            return False
    currentNode = Grafo[nextVertex].head
    while currentNode != None:
        if (lastVertex != currentNode.value):
            condition = isTreeR(Grafo, firstVertex, searchedVertex, nextVertex, currentNode.value)
            if condition == False:
                return False
        currentNode = currentNode.nextNode
    return True

#Punto 5
#O(V*V), podria mejorarse a O(V) con listas de python
def isComplete(Grafo):
    n = len(Grafo)
    for i in range(0, n):
        if (n-1) != linkedlist.length(Grafo[i]):
            return False
    return True

#Punto 6
"""
def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
"""
def convertTree(Grafo):
    return treeWithBfs(Grafo)

"""
W, G, B son abreviaciones para White, Gray y Black respectivamente. Utiliza el recorrido BFS para encontrar ciclos.
"""
def treeWithBfs(Grafo):
    auxList = linkedlist.LinkedList()
    n = len(Grafo)
    for i in range(0, n):
        node = linkedlist.Node()
        node.value = "W"
        node.nextNode = Grafo[i].head
        Grafo[i].head = node
    stack = linkedlist.LinkedList()
    linkedlist.push(stack, 0)
    currentNode = stack.head
    while currentNode != None:
        linkedlist.pop(stack)
        Grafo[currentNode.value].head.value = "G"
        currentNode2 = Grafo[currentNode.value].head.nextNode
        while currentNode2 != None:
            if Grafo[currentNode2.value].head.value == "W":
                Grafo[currentNode2.value].head.value = "G"
                linkedlist.push(stack, currentNode2.value)
            else:
                if Grafo[currentNode2.value].head.value == "G":
                    linkedlist.add(auxList, (currentNode2.value, currentNode.value))
            currentNode2 = currentNode2.nextNode
        Grafo[currentNode.value].head.value = "B"
        currentNode = stack.head
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return auxList
