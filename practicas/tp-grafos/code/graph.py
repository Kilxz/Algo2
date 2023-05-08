from algo1 import *
import linkedlist
import math

class vertex:
    key = None
    value = None

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
def existPath(Grafo, v1, v2):
    n = len(Grafo)
    for i in range(0, n):
        node = linkedlist.Node()
        node.value = "W"
        node.nextNode = Grafo[i].head
        Grafo[i].head = node
    stack = linkedlist.LinkedList()
    linkedlist.push(stack, v1)
    currentNode = stack.head
    condition = False
    while currentNode != None:
        linkedlist.pop(stack)
        Grafo[currentNode.value].head.value = "G"
        currentNode2 = Grafo[currentNode.value].head.nextNode
        while currentNode2 != None:
            if Grafo[currentNode2.value].head.value == "W":
                Grafo[currentNode2.value].head.value = "G"
                linkedlist.push(stack, currentNode2.value)
            if currentNode2.value == v2:
                condition = True
                stack.head = None
                break
            currentNode2 = currentNode2.nextNode
        Grafo[currentNode.value].head.value = "B"
        currentNode = stack.head
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return condition

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
"""

#Punto 3
"""
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
"""

def isConnected(Grafo):
    return isConnectedWithBfs(Grafo)
def isConnectedWithBfs(Grafo):
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
            currentNode2 = currentNode2.nextNode
        Grafo[currentNode.value].head.value = "B"
        currentNode = stack.head
    condition = True
    for i in range(0, n):
        if Grafo[i].head.value == "W":
            condition = False
        linkedlist.pop(Grafo[i])
    return condition

"""
def isConnected(Grafo):
    n = len(Grafo)
    for i in range(0, n-1):
        for j in range(i, n):
            condition = existPath(Grafo, i, j)
            if condition == False:
                return False
    return True
"""

#Punto 4
"""
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
"""

def isTree(Grafo):
    if isConnected(Grafo) == False:
        return False
    return isTreeWithBfs(Grafo)

def isTreeWithBfs(Grafo):
    n = len(Grafo)
    for i in range(0, n):
        node = linkedlist.Node()
        node.value = "W"
        node.nextNode = Grafo[i].head
        Grafo[i].head = node
    stack = linkedlist.LinkedList()
    linkedlist.push(stack, 0)
    currentNode = stack.head
    condition = True
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
                    condition = False
            currentNode2 = currentNode2.nextNode

        if condition == True:
            Grafo[currentNode.value].head.value = "B"
            currentNode = stack.head
        else:
            break
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return condition
"""
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
"""



#Punto 5
"""
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.
"""
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

#Punto 7
"""
def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
"""
def countConnections(Grafo):
    return countConnectionsWithBfs(Grafo)
def countConnectionsWithBfs(Grafo):
    n = len(Grafo)
    for i in range(0, n):
        node = linkedlist.Node()
        node.value = "W"
        node.nextNode = Grafo[i].head
        Grafo[i].head = node
    stack = linkedlist.LinkedList()
    linkedlist.push(stack, 0)
    currentNode = stack.head
    contador = 1
    while currentNode != None:
        linkedlist.pop(stack)
        Grafo[currentNode.value].head.value = "G"
        currentNode2 = Grafo[currentNode.value].head.nextNode
        while currentNode2 != None:
            if Grafo[currentNode2.value].head.value == "W":
                Grafo[currentNode2.value].head.value = "G"
                linkedlist.push(stack, currentNode2.value)
            currentNode2 = currentNode2.nextNode
        Grafo[currentNode.value].head.value = "B"
        currentNode = stack.head
        if currentNode == None:
            for i in range(0, n):
                if Grafo[i].head.value == "W":
                    contador += 1
                    linkedlist.push(stack, i)
                    currentNode = stack.head
                    break
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return contador

#Punto 8
"""
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
"""

def convertToBFSTree(Grafo, v):
    n = len(Grafo)
    newGraph = Array(n, linkedlist.LinkedList())
    for i in range(0, n):
        newGraph[i] = linkedlist.LinkedList()
        node = linkedlist.Node()
        node.value = "W"
        node.nextNode = Grafo[i].head
        Grafo[i].head = node
    stack = linkedlist.LinkedList()
    linkedlist.push(stack, v)
    currentNode = stack.head
    while currentNode != None:
        linkedlist.pop(stack)
        Grafo[currentNode.value].head.value = "G"
        currentNode2 = Grafo[currentNode.value].head.nextNode
        while currentNode2 != None:
            if Grafo[currentNode2.value].head.value == "W":
                Grafo[currentNode2.value].head.value = "G"
                linkedlist.push(stack, currentNode2.value)
                linkedlist.add(newGraph[currentNode.value], currentNode2.value)
                linkedlist.add(newGraph[currentNode2.value], currentNode.value)
            currentNode2 = currentNode2.nextNode
        Grafo[currentNode.value].head.value = "B"
        currentNode = stack.head
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return newGraph

#Punto 9
"""
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
"""
def convertToDFSTree(Grafo, v):
    n = len(Grafo)
    newGraph = Array(n, linkedlist.LinkedList())
    for i in range(0, n):
        newGraph[i] = linkedlist.LinkedList()
        node = linkedlist.Node()
        node.value = "W"
        node.nextNode = Grafo[i].head
        Grafo[i].head = node
    Grafo[v].head.value = "G"
    newGraph = convertToDFSTreeR(Grafo, newGraph, v, v)
    for i in range(0, n):
        if Grafo[i].head.value == "W":
            Grafo[i].head.value = "G"
            newGraph = convertToDFSTreeR(Grafo, newGraph, i, i)
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return newGraph

def convertToDFSTreeR(Grafo, newGraph, lastVertex, v):
    currentNode = Grafo[v].head.nextNode
    while currentNode != None:
        if currentNode.value != lastVertex:
            if Grafo[currentNode.value].head.value == "W":
                Grafo[currentNode.value].head.value = "G"
                linkedlist.add(newGraph[v], currentNode.value)
                linkedlist.add(newGraph[currentNode.value], v)
                convertToDFSTreeR(Grafo, newGraph, v, currentNode.value)
        currentNode = currentNode.nextNode
    Grafo[v].head.value = "B"
    return newGraph

#Punto 10
"""
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
"""

def bestRoad(Grafo, v1, v2):
    if (len(Grafo) < v1) or len(Grafo) < v2:
        return []
    newGraph = convertToBFSTree(Grafo, v1)
    condition = bestRoadR(newGraph, v2, [v1], v1, v1)
    if condition != False:
        return condition
    else:
        return []
    
def bestRoadR(Grafo, v2, auxList, lastVertex, Vertex):
    if linkedlist.search(Grafo[Vertex], v2) != None:
        auxList.append(v2)
        return auxList
    condition = False 
    currentNode = Grafo[Vertex].head
    while currentNode != None:
        if currentNode.value != lastVertex:
            auxList.append(currentNode.value)
            condition = bestRoadR(Grafo, v2, auxList, Vertex, currentNode.value)
            if condition == False:
                auxList.pop()
            else:
                return condition
        currentNode = currentNode.nextNode
    return False

"""
Crea un grafo ponderado mediante MATRIZ de adyacencia. En cada posición de la matriz se encuentra el respectivo 1 o 0 en una tupla, 
junto a el valor de la arista.
Forma: (0, valor)
"""
def createWeightedGraph(ListA, ListB):
    n = linkedlist.length(ListA)
    Graph = Array(n, Array(n, (0, 0)))
    for i in range(0, n):
        for j in range(0, n):
            Graph[i][j] = (0,0)

    currentNode = ListB.head
    while currentNode != None:
        Graph[currentNode.value[0]][currentNode.value[1]] = (1, currentNode.value[2])
        Graph[currentNode.value[1]][currentNode.value[0]] = (1, currentNode.value[2])
        currentNode = currentNode.nextNode
    return Graph


#Punto 14
"""
def PRIM(Grafo): 
Descripción: Implementa el algoritmo de PRIM 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo

Va añadiendo las aristas de los nodos a los que va visitando, en ese orden.
En cada iteración inserta la arista de menor costo de esa lista, siempre y cuando
el vértice no este en "visited".
"""
def PRIM(Graph):
    Q = []
    n = len(Graph)
    newGraph = []
    visited = [0]
    Q = neighbourEdges(Graph, 0, Q, visited)
    edge = 0
    while (Q != []) and (len(newGraph) != (n-1)):
        edge = getMinor(Q, visited)

        if edge != None:
            newGraph.append(edge)
        else:
            return newGraph
        visited.append(edge[1])
        Q = neighbourEdges(Graph, edge[1], Q, visited)
    return newGraph

def getMinor(Q, visited):
    aux = None
    store = []
    print(Q)
    for i in range(len(Q)):
        if (Q[i][1] in visited):
            store.append(i)
    for i in store:
        Q.pop(i)
    for i in range(len(Q)):
        if aux == None:
                aux = i
        else:
            if Q[aux][2] > Q[i][2]:
                aux = i
    if aux == None:
        return None
    aux2 = Q[aux]
    Q.pop(aux)
    return aux2

def neighbourEdges(Graph, v, Q, visited):
    for i in range(0, len(Graph)):
        if i not in visited:
            if Graph[v][i][0] != 0:
                Q.append((v, i, Graph[v][i][1]))
    return Q

#Punto 15
"""
def KRUSKAL(Grafo): 
Descripción: Implementa el algoritmo de KRUSKAL 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo

Agrega todas las aristas, las ordena con sort() y luego en orden las va agregando al AACM
si se verifica que no se forma un ciclo (Mediante la función union explicada más abajo)
"""
def KRUSKAL(Graph):
    edges = getEdges(Graph)
    edges.sort()
    newGraph = []
    parent, contador = makeSet(len(Graph))
    for i in edges:
        if union(i[1], i[2], parent, contador) == True:
            newGraph.append((i[1], i[2], i[0]))
    return newGraph


def getEdges(Graph):
    edges = []
    for i in range(0, len(Graph)):
        for j in range(i, len(Graph)):
            if Graph[i][j][0] != 0:
                edges.append((Graph[i][j][1], i, j))
    return edges


#Extras
"""
Se usa para verificar los ciclos en KRUSKAL, crea varios conjuntos (al principio con cantidad de elementos igual a vértices) y
los va uniendo en KRUSKAL.
Si en un momento esos conjuntos están unidos, retorna false. Caso contrario, los une y retorna True
contador es aproximadamente la altura de cada subárbol y se usa para más o menos intentar balancear el árbol que va quedando.
"""
def makeSet(n):
    parent = []
    contador = []
    for i in range(n):
        parent.append(i)
        contador.append(0)
    return parent, contador

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, contador):
    raizX = find(x, parent)
    raizY = find(y, parent)
    if raizX == raizY:
        return False

    if contador[raizX] < contador[raizY]:
        parent[raizX] = raizY
    elif contador[raizX] > contador[raizY]:
        parent[raizY] = raizX
    else:
        parent[raizY] = raizX
        contador[raizX] = contador[raizX] + 1
    return True


"""
Proceso de PRIM FALLIDO
def PRIM(Graph):
    Q = []
    newGraph = []
    for i in range(len(Graph)):
        node = vertex()
        node.value = i
        node.key = math.inf
        Q.append(node)
    edge = minEdge(Graph, 0, Q)
    Q[0].key = edge[1]
    while Q != []:
        u = Q[0].value
        edge = minEdge(Graph, Q[0].value, Q)
        Q.pop(0)
        if edge != None:
            newGraph.append(edge)
        for i in range(len(Graph)):
            if Graph[u][i][0] != 0:
                v = (i, Graph[u][i][1])
                if edge != None:
                    if i == edge[1]:
                        v = (i, math.inf)
                aux = None
                for j in range(len(Q)):
                    if (Q[j].value == v[0]) and Q[j].key > v[1]:
                        aux = j
                        Q[j].key = v[1]
                        break
                if aux != None:
                    aux2 = Q[aux]
                    Q.pop(aux)
                    condition = False
                    for k in range(len(Q)):
                        if Q[k].key > aux2.key:
                            condition = True
                            Q.insert(k, aux2)
                            break
                    if condition == False:
                        Q.append(aux2)
    return newGraph

def minEdge(Graph, vertex, Q):
    aux = None
    for i in range(0, len(Graph)):
        if Graph[vertex][i][0] != 0:
            for j in range(len(Q)):
                if i == Q[j].value:
                    if aux == None:
                        aux = (vertex, i, Graph[vertex][i][1])
                    else:
                        if aux[2] > Graph[vertex][i][1]:
                            aux = (vertex, i, Graph[vertex][i][1])
                    break
    if aux == None:
        return None
    else:
        return aux
    
"""