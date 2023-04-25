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

Graph = createGraph(V1, A)

for i in range(0, 7):
    linkedlist.printlist(Graph[i])

print(existPath(Graph, 0, 5))
print(existPath(Graph, 1, 2))
print(existPath(Graph, 1, 0))
print(existPath(Graph, 0, 1))
print(existPath(Graph, 3, 5))
print(existPath(Graph, 5, 3))
print(existPath(Graph, 1, 4))
print(existPath(Graph, 6, 3))
print(existPath(Graph, 0, 6))

