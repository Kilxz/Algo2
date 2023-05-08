import math
from algo1 import *
import linkedlist
"""
L = [1,2,3,4,5,6,7,8]

condition = L.index(8)
print(condition)

for i in "hola":
    print(i)


hola = "Holas"

print(hola[-1])

hola = hola[1:]
print(hola)

hola = "a"
hola[1:]
print(hola == "")
print("asdcadasdas")
print(hola)

def ImprimirLetra(T, letra):
    inicio = searchInL(letra)
    print(inicio.key)
    while inicio != None:
        inicio = inicio.head.value
        print(inicio.key)
        print("isEndOfWord?", inicio.isEndOfWord)
        inicio = inicio.children
    return

hola = "hola"
print(hola)
hola = hola + "ad"
print(hola)

newList = []
print(newList == None)
print(newList == [])


L = ["hola", "chau"]
L.insert(1, L[0])
print(L)


L = [5, 28, 19, 15, 20,  33, 12, 17, 10]

for i in L:
    print(i % 9)

def hashMult(k, m, A):
    return m * ((k * (math.sqrt(5) -1) / 2) % 1)

A = (math.sqrt(5) -1) / 2
L = [61, 62, 63, 64, 65]
m = 1000
lista = []
for i in L:
    lista.append(hashMult(i, m, A))

print(lista)


dict = Array(3, 0)

print(dict[0])

print(7 % 1)

print(ord("a"))
print(ord("A"))
print(ord("z"))
print(ord("Z"))
print(ord("abc"))


k = 61
print(((k * (math.sqrt(5) -1) / 2) % 1))
b = ((math.sqrt(5) -1) / 2) % 1
print(k * b)
print(b % 1)


s = "06:40:03AM"

if "AM" in s:
    print("24")
print(str(int(s[0:2]) + 12) + s[2:8])



a = [23, 23, 1,3, 4, 5]
auxList = a

auxList = [24]
print(a)



Grafo = Array(5, linkedlist.LinkedList())
print(Grafo[0])
def updateBf(T, node):
    currentNode = node
    if currentNode == T.root:
        return T
    if currentNode.bf < -1:
        rotateLeft(T, currentNode)
    else:
        if currentNode.bf > 1:
            rotateRight(T, currentNode)
    return updateBf(T, node.parent)


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
v = [0,1,2,3,4,5]
ar = [(1, 2), (2,3), (3, 4),(0, 4)]
vertices = linkedlist.LinkedList()
aristas = linkedlist.LinkedList()
for i in v:
    linkedlist.add(vertices, i)
for i in ar:
    linkedlist.add(aristas, i)

Grafo = createGraph(vertices, aristas)
def dfs(Grafo):
    n = len(Grafo)
    lista = []
    for i in range(0, n):
        newNode = linkedlist.Node()
        newNode.value = "W"
        newNode.nextNode = Grafo[i].head
        Grafo[i].head = newNode
    for i in range(0, n):
        if Grafo[i].head.value == "W":
            Grafo[i].head.value = "G" 
            lista = dfsR(Grafo, i, lista)
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return lista
def dfsR(Grafo, v, lista):
    currentNode = Grafo[v].head.nextNode
    while currentNode != None:
        if Grafo[currentNode.value].head.value == "W":
            lista.append((v, currentNode.value))
            Grafo[currentNode.value].head.value = "G" 
            lista = dfsR(Grafo, currentNode.value, lista)
        currentNode = currentNode.nextNode
    Grafo[v].head.value = "B"
    return lista

print(dfs(Grafo))


def existPathWithdfs(Grafo, v1, v2):
    n = len(Grafo)
    for i in range(0, n):
        newNode = linkedlist.Node()
        newNode.value = "W"
        newNode.nextNode = Grafo[i].head
        Grafo[i].head = newNode

    i = v1
    if Grafo[i].head.value == "W":
        Grafo[i].head.value = "G" 
        lista = existPathWithdfsR(Grafo, i, v2)
    for i in range(0, n):
        linkedlist.pop(Grafo[i])
    return lista

def existPathWithdfsR(Grafo, v, v2):
    currentNode = Grafo[v].head.nextNode
    condition = False
    while currentNode != None:
        if currentNode.value == v2:
            return True
        if Grafo[currentNode.value].head.value == "W":
            Grafo[currentNode.value].head.value = "G" 
            condition = existPathWithdfsR(Grafo, currentNode.value, v2)
            if condition == True:
                return True
        currentNode = currentNode.nextNode
    Grafo[v].head.value = "B"
    return condition

print(existPathWithdfs(Grafo, 3, 5))
print(existPathWithdfs(Grafo, 3, 4))
print(existPathWithdfs(Grafo, 0, 4))

aux = ""
s = "holacomo"
for i in range(1, len(s) + 1):
    aux = aux + s[-i]
print(aux)

"""

Q = [(1, 1), (0, 2), (3, 4)]
Q.sort()
print(Q)