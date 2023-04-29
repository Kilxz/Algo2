import linkedlist
from graph import *

V1 = linkedlist.LinkedList()
A = linkedlist.LinkedList()

vertices = [0,1,2,3,4,5,6]
A2 = [(0,1), (1,2), (2,3), (3,4), (4, 5)]

for i in vertices:
    linkedlist.add(V1, i)
for i in A2:
    linkedlist.add(A, i)
print("Prueba createGraph()")
Graph = createGraph(V1, A)

for i in range(0, 7):
    linkedlist.printlist(Graph[i])

print(" ")
print("Prueba existPath()")
print(existPath(Graph, 0, 5))
print(existPath(Graph, 1, 2))
print(existPath(Graph, 1, 0))
print(existPath(Graph, 0, 1))
print(existPath(Graph, 3, 5))
print(existPath(Graph, 5, 3))
print(existPath(Graph, 1, 4))
print(existPath(Graph, 6, 3))
print(existPath(Graph, 0, 6))

#Punto 3
print(" ")
print("Prueba isConnected()")
V1 = linkedlist.LinkedList()
A = linkedlist.LinkedList()
B = linkedlist.LinkedList()
C = linkedlist.LinkedList()
vertices = [0,1,2,3,4,5,6]
for i in vertices:
    linkedlist.add(V1, i)
A2 = [(0,1), (0,2), (2,4), (3,6), (4, 5)]
A3 = [(0,1), (0,2), (2,4), (3,6), (4, 5), (1, 3)]
A4 = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3,5), (3, 6), (4, 5), (4, 6), (5, 6)]
D = linkedlist.LinkedList()
for i in A4:
    linkedlist.add(D, i)
GrafoD = createGraph(V1, D)
for i in A2:
    linkedlist.add(A, i)
for i in A3:
    linkedlist.add(B, i)
A5 = [(0,1), (0,2), (2,4),(4, 5), (1, 3)]
for i in A5:
    linkedlist.add(C, i)
GrafoA = createGraph(V1, A)
GrafoB = createGraph(V1, B)
GrafoC = createGraph(V1, C)
if ((isConnected(GrafoA) == False) and (isConnected(GrafoB) == True) and (isConnected(GrafoC) == False)):
    print("Funciona correctamente")
else:
    print("Error")

#Punto 4
print(" ")
print("Prueba isTree()")
if (isTree(GrafoA) == False) and (isTree(GrafoB) == True) and (isTree(GrafoC) == False) and (isTree(GrafoD) == False):
    print("Funciona correctamente")
else:
    print("Error")

#Punto 5
print(" ")
print("Prueba isComplete()")
if (isComplete(GrafoA) == False) and (isComplete(GrafoB) == False) and (isComplete(GrafoC) == False) and (isComplete(GrafoD) == True):
    print("Funciona correctamente")
else:
    print("Error")

#Punto 6
print(" ")
print("Prueba convertTree()")
print("Grafo B")
print(convertTree(GrafoB).head)

print("Grafo D (completo)")
linkedlist.printlist(convertTree(GrafoD))

V2 = [0, 1, 2, 3]
Aristas = [(0, 1), (1, 2), (0, 2), (2,3)]
aristas2 = [(0, 1), (0, 2), (2,3)]
V2linked = linkedlist.LinkedList()
A2linked = linkedlist.LinkedList()
A3linked = linkedlist.LinkedList()

for i in V2:
    linkedlist.add(V2linked, i)
for i in Aristas:
    linkedlist.add(A2linked, i)
for i in aristas2:
    linkedlist.add(A3linked, i)
GrafoM = createGraph(V2linked, A2linked)
GrafoL = createGraph(V2linked, A3linked)
print("Grafo M")
linkedlist.printlist(convertTree(GrafoM))
print("Grafo L")
print(convertTree(GrafoL).head)
