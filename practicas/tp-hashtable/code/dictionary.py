from algo1 import *
import linkedlist
import math

#Declara un diccionario (Array) de longitud m
def dictionary(m):
    dict = Array(m, linkedlist.LinkedList())
    return dict

#Hash por división k mod m
def hash(k, m):
    return (k % m)

"""
insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
Salida: Devuelve D
"""
def insert(D, key, value):
    k = hash(key, len(D))
    element = (key, value)
    if D[k] == None:
        newList = linkedlist.LinkedList()
        linkedlist.add(newList, element)
        D[k] = newList
    else:
        linkedlist.add(D[k], element)
    return D

"""
search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
"""
def search(D, key):
    k = hash(key, len(D))
    if D[k] == None:
        return None
    
    currentNode = D[k].head
    while currentNode != None:
        if currentNode.value[0] == key:
            return currentNode.value[1]
        currentNode = currentNode.nextNode
    return None

"""
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
"""
def delete(D, key):
    k = hash(key, len(D))
    if D[k] == None:
        return D
    if D[k].head.value[0] == key:
        D[k].head = D[k].head.nextNode
        if D[k].head == None:
            D[k] = None
        return D
    
    currentNode = D[k].head
    while currentNode.nextNode != None:
        if currentNode.nextNode.value[0] == key:
            currentNode.nextNode = currentNode.nextNode.nextNode
            return D
        currentNode = currentNode.nextNode
    return D

#Verifica si dos strings son permutaciones.
#Es O(n) siendo n la longitud de la string más larga o la longitud del alfabeto
#Esto es ya que se recorren las dos string y el diccionario cuyo tamaño es el del alfabeto
def permutation(S, P):
    if len(S) != len(P):
        return False
    
    D = dictionary(ord("z") - ord("a"))
    
    for i in range (0, len(S)):
        key = ord(S[i]) - ord("a")
        insert(D, key, S[i])
    for j in range (0, len(P)):
        key = ord(P[j]) - ord("a")
        delete(D, key)
    for i in range(0, len(D)):
        if D[i] != None:
            return False
    return True

#Verifica que todos los elementos de una lista sean unicos
#Es O(n) ya que lo máximo que se recorre es la longitud de la lista
#Además, el search y el insert son de O(1), por lo que no afectan
def unicos(L):
    D = dictionary(linkedlist.length(L))
    currentNode = L.head
    while currentNode != None:
        if search(D, currentNode.value) == None:
            insert(D, currentNode.value, currentNode.value)
        else:
            return False
        currentNode = currentNode.nextNode
    return True

#Hash por multiplicación
def hashMultiplicar(m, k):
    A = (math.sqrt(5) - 1) / 2
    return m * ((k * A) % 1) 

#Ejercicio 6
def hashPostal(c, m):
    k = 1
    for i in range(1, 10):
        k = k * ord(c[i-1]) * i
    return k % m

#Comprime una cadena básica de cadenas contando los repetidos
#Es O(n) ya que se recorre la longitud de la string como peor caso
def compression(string):
    dict = dictionary(len(string))
    contador = 0
    for i in range(0, len(string)):
        if i == 0:
            insert(dict, contador, string[i])
        else:
            if string[i] == string[i-1]:
                insert(dict, contador, string[i])
            else:
                contador += 1
                insert(dict, contador, string[i])
    contadorFinal = contador
    contador = 0
    newString = ""
    for i in range(0, contadorFinal + 1):
        newString = newString + dict[i].head.value[1]
        newString = newString + str(linkedlist.length(dict[i]))
    if len(newString) >= len(string):
        return string
    else:
        return newString

def compression2(string):
    newString = ""
    newString = newString + string[0]
    contador = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            contador += 1
        else:
            newString = newString + str(contador)
            newString = newString + string[i]
            contador = 1
    newString = newString + str(contador)
    if len(newString) >= len(string):
        return string
    else:
        return newString

#Verifica que la string p este en la string a y devuelve el índice de la primera ocurrencia
#Es O(a - p + 1) o O(n) ya que se recorre la longitud de a - la de p + 1 como peor caso.
def insideString(p, a):
    length = len(p)
    lengthA = len(a)
    lengthDict = (lengthA - length) + 1
    dict = dictionary(lengthDict)
    for i in range(0, lengthDict):
        insert(dict, i, a[i: i + 4])
    for i in range(0, lengthDict):
        if dict[i].head.value[1] == p:
            return i
    return None

#Dados dos conjuntos de enteros verifica que S sea subconjunto de T
#Es O(n) ya que en el peor de los casos se recorre la lista más grande
def isSubset(S, T):
    D = dictionary(linkedlist.length(T))
    if T == None:
        return False
    if S == None:
        return True
    currentNode = T.head
    while currentNode != None:
        insert(D, currentNode.value, currentNode.value)
        currentNode = currentNode.nextNode
    
    currentNode = S.head
    while currentNode != None:
        if search(D, currentNode.value) == None:
            return False
        currentNode = currentNode.nextNode
    return True