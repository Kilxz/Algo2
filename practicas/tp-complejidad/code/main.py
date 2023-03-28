from linkedlist import *
import math

#Queda de complejidad O(n^2) ya que en la 
#ultima parte hay un for que tiene dentro un swap. 
#Por lo que quedaria de n * n, es decir, n cuadrado
def ordenamiento(L):
    if L.head == None:
        return None
    len = length(L)

    if len == 1:
        return L
    
    currentNode = L.head
    #n/2
    medio = round(len/2)
    for i in range(0, medio):
        if i == medio - 1:
            valor = currentNode.value
        currentNode = currentNode.nextNode
    currentNode = L.head
    menorBef = []
    menorAft = []
    mayorBef = []
    mayorAft = []
    contBefore = 0
    contAfter = 0
    #n
    for i in range(0, len):
        if currentNode.value < valor:
            if i < medio - 1:
                menorBef.append(i)
                contBefore = contBefore + 1
            else:
                if i > medio - 1:
                    menorAft.append(i)
                    contAfter = contAfter + 1
        if (currentNode.value >= valor) and (i != medio - 1):
            if i < medio - 1:
                mayorBef.append(i)
            else:
                mayorAft.append(i)
        currentNode = currentNode.nextNode
    difference = abs(contBefore - contAfter)

    #n^2 (Al ser la funcion swap n)
    if difference == 0 or difference == 1:
        return L
    else:
        iteraciones = math.trunc(difference / 2)
        for i in range(0, iteraciones):
            if contBefore > contAfter:
                swap(L, menorBef[0], mayorAft[0])
                menorBef.pop(0)
                mayorAft.pop(0)
            else:
                swap(L, menorAft[0], mayorBef[0])
                menorAft.pop(0)
                mayorBef.pop(0)
    return L

#Es O(n^2) ya que contiene dos bucles que recorren la lista uno dentro de otro.
def ContieneSuma(A, n):
    len = length(A)
    currentNode = A.head
    for i in range(0, len):
        number = n - currentNode.value
        currentNode2 = currentNode.nextNode
        for j in range(i + 1, len):
            if currentNode2.value == number:
                return True
            else:
                if currentNode2 != None:
                 currentNode2 = currentNode2.nextNode
        if currentNode != None:
            currentNode = currentNode.nextNode
    
    return False

print("=========== PRUEBA ORDENAMIENTO ===========")
L = LinkedList()
for i in range(10, 0, -1):
    add(L, i)

C = LinkedList()
for i in range(1, 11):
    add(C, i)

B = LinkedList()
add(B, 1)
add(B, 2)
add(B, 4)
add(B, 5)
add(B, 2)
add(B, 3)

Z = LinkedList()
add(Z, 9)
add(Z, 8)
add(Z, 7)
add(Z, 3)
add(Z, 2)
add(Z, 6)
add(Z, 5)
add(Z, 4)
add(Z, 3)
add(Z, 2)
add(Z, 1)

print("Lista L")
printlist(L)
ordenamiento(L)
printlist(L)

print(" ")

print("Lista C")
printlist(C)
ordenamiento(C)
printlist(C)

print(" ")
print("Lista B")
printlist(B)
ordenamiento(B)
printlist(B)

print(" ")
print("Lista Z")
printlist(Z)
ordenamiento(Z)
printlist(Z)
print(" ")

print("=========== PRUEBA CONTIENESUMA ===========")
print(" ")

print("Lista A")
A = LinkedList()
for i in range(10, 0, -1):
    add(A, i)

printlist(A)
print("ContieneSuma con n = 6?", ContieneSuma(A, 6))
print("ContieneSuma con n = 100?", ContieneSuma(A, 100))

print(" ")
print("Lista F")
F = LinkedList()
add(F, 6)
add(F, 2)
add(F, 7)
add(F, 1)

print("ContieneSuma con n = 8?", ContieneSuma(F, 8))
print("ContieneSuma con n = 1?", ContieneSuma(F, 1))

printlist(F)