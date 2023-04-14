from dictionary import *
import linkedlist
dict = dictionary(5)

print("-_-_-_-_-_- Prueba insert -_-_-_-_-_-")
insert(dict, 25, 25)
print(dict[0].head.value)
insert(dict, 3, 3)
print(dict[3].head.value)
insert(dict, 4, 4)
print(dict[4].head.value)
insert(dict, 1, 1)
print(dict[1].head.value)
insert(dict, 2, 2)
print(dict[2].head.value)
insert(dict, 6, 6)
insert(dict, 11, 11)
linkedlist.printlist(dict[1])

print(" ")
print("-_-_-_-_-_- Prueba delete -_-_-_-_-_-")
linkedlist.printlist(dict[1])
delete(dict, 11)
print("Borro 11")
linkedlist.printlist(dict[1])
insert(dict, 11, 11)
delete(dict, 1)
print("Borro 1")
linkedlist.printlist(dict[1])
insert(dict, 1, 1)
delete(dict, 11)
print("Borro 11")
linkedlist.printlist(dict[1])
insert(dict, 11, 11)
insert(dict, 16, 16)
insert(dict, 21, 21)
print("Inserto varios con con k = 1")
linkedlist.printlist(dict[1])
print("Borro el ultimo")
delete(dict, 6)
linkedlist.printlist(dict[1])
print("Voy a un k que tenga solo un elemento, k = 2")
linkedlist.printlist(dict[2])
print("Borro key 2")
delete(dict, 2)
print(dict[2])

print(" ")
print("-_-_-_-_-_- Prueba search -_-_-_-_-_-")
print(search(dict, 1))
print(search(dict, 100))
print(search(dict, 87))
print(search(dict, 25))
print(search(dict, 3))
print(search(dict, 7))

print(" ")
print("-_-_-_-_-_- Prueba Ejercicio 4 -_-_-_-_-_-")
print("Permutacion 'sama' de 'hola'?")
print(permutation("hola", "sama"))
print("Permutacion 'olah' de 'hola'?")
print(permutation("olah", "hola"))
print("Permutacion 'cos' de 'osc'?")
print(permutation("cos", "osc"))
print("Permutacion 'sentados' de 'sodatnes'?")
print(permutation("sentados", "sodatnes"))
print("Permutacion 'sentados' de 'sodatene'?")
print(permutation("sentados", "sodatene"))

print(" ")
print("-_-_-_-_-_- Prueba Ejercicio 5 -_-_-_-_-_-")

aux = [1, 2, 3 , 4, 5, 6]
aux2 = [1, 2, 3, 6 , 4, 5, 6]
aux3 = [3, 3, 3, 3, 3, 3, 3 , 4, 5, 6]
aux4 = [0, 1, 2, 3 , 4, 5, 6, 0]

lista = linkedlist.LinkedList()
for i in aux:
    linkedlist.add(lista, i)

print("Lista: ")
linkedlist.printlist(lista)
print("Sus elementos son únicos?")
print(unicos(lista))
lista = None
lista = linkedlist.LinkedList()

for i in aux2:
    linkedlist.add(lista, i)

print("Lista: ")
linkedlist.printlist(lista)
print("Sus elementos son únicos?")
print(unicos(lista))
lista = None
lista = linkedlist.LinkedList()

for i in aux3:
    linkedlist.add(lista, i)

print("Lista: ")
linkedlist.printlist(lista)
print("Sus elementos son únicos?")
print(unicos(lista))
lista = None
lista = linkedlist.LinkedList()

for i in aux4:
    linkedlist.add(lista, i)

print("Lista: ")
linkedlist.printlist(lista)
print("Sus elementos son únicos?")
print(unicos(lista))
lista = None
lista = linkedlist.LinkedList()
linkedlist.add(lista, 4)
print("Lista: ")
linkedlist.printlist(lista)
print("Sus elementos son únicos?")
print(unicos(lista))

print(" ")
print("-_-_-_-_-_- Prueba Ejercicio 7 -_-_-_-_-_-")
print(compression("aaaaaaaabbbbsddddddpppp"))
print(compression("aabbssddpp"))
print(compression("aabbssddp"))

print(" ")
print("-_-_-_-_-_- Prueba Ejercicio 8 -_-_-_-_-_-")
print(insideString("pepe", "parepepe"))
print(insideString("pepe", "parepep"))
print(insideString("pepe", "pepepare"))
print(insideString("pepe", "papepere"))

print(" ")
print("-_-_-_-_-_- Prueba Ejercicio 9 -_-_-_-_-_-")
s = linkedlist.LinkedList()
t = linkedlist.LinkedList()
o = linkedlist.LinkedList()
linkedlist.add(o, 2)
f = linkedlist.LinkedList()
linkedlist.add(f, 11)
for i in range(0, 11):
    if (i > 3) and (i < 8):
        linkedlist.add(s, i)
    linkedlist.add(t, i)
print("Lista S")
linkedlist.printlist(s)
print("Lista T")
linkedlist.printlist(t)
print("Lista O")
linkedlist.printlist(o)
print("Lista F")
linkedlist.printlist(f)
print("S subconjunto de T?")
print(isSubset(s, t))
print("O subconjunto de T?")
print(isSubset(o, t))
print("F subconjunto de T?")
print(isSubset(f, t))
print("T subconjunto de S?")
print(isSubset(t, s))