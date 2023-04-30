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

print(" ")
print("Prueba countConnections()")
print("Grafo A")
print(countConnections(GrafoA))
print("Grafo B")
print(countConnections(GrafoB))
print("Grafo C")
print(countConnections(GrafoC))
print("Grafo D")
print(countConnections(GrafoD))
print("Grafo M")
print(countConnections(GrafoM))
print("Grafo L")
print(countConnections(GrafoL))

aristasB = linkedlist.LinkedList()
verticesA = linkedlist.LinkedList()
for i in range(0, 7):
    linkedlist.add(verticesA, i)
GrafoZ = createGraph(verticesA, aristasB)
print("Grafo Z")
print(countConnections(GrafoZ))

print(" ")
print("Prueba convertToBFSTree()")
newGraphM2 = convertToBFSTree(GrafoM, 2)
newGraphM3 = convertToBFSTree(GrafoM, 3)
newGraphM0 = convertToBFSTree(GrafoM, 0)
newGraphL0 = convertToBFSTree(GrafoL, 0)
newGraphL1 = convertToBFSTree(GrafoL, 1)
print("Grafo M - Vértice 2")
for i in range(0, 4):
    linkedlist.printlist(newGraphM2[i])
print("Grafo M - Vértice 3")
for i in range(0, 4):
    linkedlist.printlist(newGraphM3[i])
print("Grafo M - Vértice 0")
for i in range(0, 4):
    linkedlist.printlist(newGraphM0[i])
print("Grafo L - Vértice 0")
for i in range(0, 4):
    linkedlist.printlist(newGraphL0[i])
print("Grafo L - Vértice 1")
for i in range(0, 4):
    linkedlist.printlist(newGraphL0[i])
newGraphM2 = None
newGraphM3 = None
newGraphM0 = None
newGraphL0 = None
newGraphL1 = None

print(" ")
print("Prueba convertToDFSTree()")
ar = [(0, 1), (0, 2), (0, 3), (3, 2), (2, 1)]
ar2 = linkedlist.LinkedList()
for i in ar:
    linkedlist.add(ar2, i)
GrafoX = createGraph(V2linked, ar2)
GrafoXD = convertToDFSTree(GrafoX, 0)
GrafoXD2 = convertToDFSTree(GrafoX, 1)
GrafoBD = convertToDFSTree(GrafoB, 0)
GrafoBD2 = convertToDFSTree(GrafoB, 3)
GrafoMD = convertToDFSTree(GrafoM, 0)
GrafoMD2 = convertToDFSTree(GrafoM, 3)
GrafoLD = convertToDFSTree(GrafoL, 0)
GrafoLD2 = convertToDFSTree(GrafoL, 3)
print("Grafo B - Vértice 0")

for i in range(0, len(GrafoBD)):
    linkedlist.printlist(GrafoBD[i])
print("Grafo B - Vértice 3")
for i in range(0, len(GrafoBD2)):
    linkedlist.printlist(GrafoBD2[i])
print("Grafo M - Vértice 0")
for i in range(0, len(GrafoMD)):
    linkedlist.printlist(GrafoMD[i])
print("Grafo M - Vértice 3")
for i in range(0, len(GrafoMD2)):
    linkedlist.printlist(GrafoMD2[i])
print("Grafo L - Vértice 0")
for i in range(0, len(GrafoLD)):
    linkedlist.printlist(GrafoLD[i])
print("Grafo L - Vértice 3")
for i in range(0, len(GrafoLD2)):
    linkedlist.printlist(GrafoLD2[i])
print("Grafo X - Vértice 0")
for i in range(0, len(GrafoXD)):
    linkedlist.printlist(GrafoXD[i])
print("Grafo X - Vértice 1")
for i in range(0, len(GrafoXD2)):
    linkedlist.printlist(GrafoXD2[i])

print(" ")
print("Prueba bestRoad()")
print("Grafo A - 0, 6")
print(bestRoad(GrafoA, 0, 6))

print("Grafo B - 0, 6")
print(bestRoad(GrafoB, 0, 6))

print("Grafo B - 6, 5")
print(bestRoad(GrafoB, 6, 5))

