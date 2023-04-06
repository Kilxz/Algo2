import linkedlist

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

#Busca en una LinkedList un nodo con una key == element. Si la encuentre devuelve el TNode, caso contrario devuelve None
def searchInL(L, element):
    if L.head == None:
        return None
    currentNode = L.head
    while currentNode != None:
        if currentNode.value.key == element:
            return currentNode.value
        currentNode = currentNode.nextNode
    return None

#Punto 1
#Inserta un elemento en el Trie
"""
Si la raíz es None, se crea una lista y se inserta como raíz. Luego, se van creando los nodos de cada letra, verificando
que no exista actualmente. En cada llamada se va cortando element (ya que se utiliza el primer caracter) y se detiene
cuando la longitud de element es 1.
"""
def insert(T, element):
    
    if T.root == None:
        L = linkedlist.LinkedList()
        T.root = L
    else:
        L = T.root
    return insertR(T.root, L, element)

def insertR(LastNode, L, element):
    condition = searchInL(L, element[0])

    if condition == None:
        TNode = TrieNode()
        TNode.key = element[0]
        TNode.parent = LastNode
        if len(element) == 1:
            TNode.children = None
        else:
            newList = linkedlist.LinkedList()
            TNode.children = newList
        linkedlist.addatend(L, TNode)
    else:
        TNode = condition

    if len(element) != 1:
        element = element[1:]
        if condition == None:
            insertR(TNode, newList, element)
        else:
            if condition.children == None:
                newList = linkedlist.LinkedList()
                condition.children = newList
            insertR(condition, condition.children, element)
        return
    else:
        TNode.isEndOfWord = True
        return

#Busca un elemento (palabra) en el trie. Si existe devuelve True, caso contrario, devuelve False
"""
Se verifica que la palabra exista en el trie cortando el elemento en cada llamada. Si en algún momento no hay más hijos, se devuelve False.
Si cuando la longitud del elemento es 1 isEndOfWord es falso, devuelve False. Caso contrario devuelve True
"""
def search(T, element):
    return searchR(T.root, element)

def searchR(L, element):
    if L == None:
        return False
    
    condition = searchInL(L, element[0])

    if condition == None:
        return False
    
    if len(element) != 1:
        element = element[1:]
        return searchR(condition.children, element)
    else:
        if condition.isEndOfWord == True:
            return True
        else:
            return False
        

#Función que busca un elemento en el Trie, si existe devuelve el último nodo correspondiente al elemento. Caso contrario, devuelve False
def searchForLastNode(T, element):
    return searchForLastNodeR(T.root, element)

def searchForLastNodeR(L, element):
    condition = searchInL(L, element[0])

    if condition == None:
        return False
    
    if len(element) != 1:
        element = element[1:]
        return searchForLastNodeR(condition.children, element)
    else:
        if condition.isEndOfWord == True:
            return condition
        else:
            return False

#Punto 3
#Elimina un elemento del Trie, si pudo borrarlo devuelve True, caso contrario, devuelve False
"""
Se verifica que la palabra exista en el trie. Luego, mediante searchForLastNode se encuentra el último nodo
presente en el Trie del elemento y a partir de ahí se va borrando cada nodo hacia la raíz, verificando la existencia de otras palabras
en la misma rama
"""
def delete(T, element):
    condition = search(T, element)
    if condition == False:
        return False
    finalNode = searchForLastNode(T, element)
    finalNode.isEndOfWord = False
    
    return deleteR(T, finalNode, element)

def deleteR(T, finalNode, element):

    if finalNode.children != None:
        finalNode.isEndOfWord = False
        return True
    else:
        if finalNode.isEndOfWord == False:
            if finalNode.parent == T.root:
                linkedlist.delete(T.root, finalNode)
                return True
            parentNode = finalNode.parent
            parentList = parentNode.children
            linkedlist.delete(parentList, finalNode)

            if linkedlist.length(parentList) ==  0:
                parentNode.children = None
            return deleteR(T, finalNode.parent, element)
        else:
            return True

#Punto 4
#Imprime todas las palabras de un trie que empiecen con el patrón p y tengan n elementos.
"""
Se busca el último nodo (si existe) del árbol que empiece con el patrón p. Luego, se crea una lista auxiliar donde se almacenarán las palabras.
Se llama a imprimirR donde se recorre cada lista hija de todos los nodos empezando por el nodo encontrado anteriormente. En cada llamada se concatena la letra al
primer nodo de auxiliarList. A su vez, un contador se incrementa en cada llamado. Si cuando llega a n == cont, isEndOfWord == False, entonces el
primer nodo de auxiliarList se elimina. También sucede lo mismo si cuando se está recorriendo el Trie, alguno de los children == None, sin haber llegado a n == cont. 
Caso contrario, se devuelve la lista.
"""

def searchLastNodePattern(T, element):
    return searchLastNodePatternR(T.root, element)

def searchLastNodePatternR(L, element):
    condition = searchInL(L, element[0])
    if condition == None:
        return False
    
    if len(element) != 1:
        element = element[1:]
        return searchLastNodePatternR(condition.children, element)
    else:
        return condition
    

def imprimir(T, p, n):
    node = searchLastNodePattern(T, p)
    if node == False:
        return None
    auxiliarList = linkedlist.LinkedList()
    lenWord = len(p)
    lista = imprimirR(node, p , n - lenWord + 1, 1, auxiliarList)

    if lenWord == n:
        linkedlist.add(auxiliarList, p)
    linkedlist.printlist(lista)
    
def imprimirR(node, p, n, cont, auxiliarList):
    if cont != 1:
        auxiliarList.head.value = auxiliarList.head.value + node.key

    if n == cont:
        if node.isEndOfWord == False:
            linkedlist.pop(auxiliarList)
        return auxiliarList
    
    if node.children == None:
        linkedlist.pop(auxiliarList)
        return auxiliarList
    
    if cont != 1:
        aux = auxiliarList.head.value

    j = 0
    currentNode = node.children.head
    while currentNode != None:
        j = j + 1
        if cont == 1:
            linkedlist.add(auxiliarList, p)
        if (j != 1) and (cont != 1):
            linkedlist.add(auxiliarList, aux)

        imprimirR(currentNode.value, p, n, cont + 1, auxiliarList)
        currentNode = currentNode.nextNode
    return auxiliarList

#Punto 5
#Verifica que dos trie sean iguales.
"""
Se llama a la función getWords en ambos tries para almacenar todas las palabras de ambos en dos listas diferentes.
getWords inicia recorriendo toda la lista de T.root, llamando dentro a getWordsR. Luego, se utiliza un funcionamiento parecido a la función imprimir.
Es decir, se utiliza un contador mientras se recorre el Trie, si está en uno, se inserta en la lista auxiliar el node.key (ya que de ahi empieza la palabra) y se llama
recursivamente a la función para ir concatenando las letras en el primer nodo de la lista auxiliar. Si algun nodo tiene isEndOfWord verdadero, entonces se retorna la lista o
se clona la palabra para seguir recursivamente hacia abajo. Todo dependiendo si tiene node.children == None o no. Retorna la lista con todas las palabras del Trie.

En Equal se comparan ambas listas auxiliares, si son iguales, retorna True, caso contrario, False
"""
def getWords(T):
    if T.root == None:
        return None
    else:
        auxiliarList = linkedlist.LinkedList()
        currentNode = T.root.head
        while currentNode != None:
            auxiliarList = getWordsR(currentNode.value, auxiliarList, 1)
            currentNode = currentNode.nextNode
        return auxiliarList


def getWordsR(node, auxiliarList, cont):
    
    if cont != 1:
        auxiliarList.head.value = auxiliarList.head.value + node.key

    if node.isEndOfWord == True:
        if node.children == None:
            return auxiliarList
        else:
            linkedlist.add(auxiliarList, auxiliarList.head.value)
    
    if node.children == None:
        return auxiliarList
    
    if cont != 1:
        aux = auxiliarList.head.value

    j = 0
    currentNode = node.children.head
    while currentNode != None:
        j = j + 1
        if cont == 1:
            linkedlist.add(auxiliarList, node.key)
        if (j != 1) and (cont != 1):
            linkedlist.add(auxiliarList, aux)
        auxiliarList = getWordsR(currentNode.value, auxiliarList, cont + 1)
        currentNode = currentNode.nextNode
    return auxiliarList
    
def equal(T1, T2):
    list1 = getWords(T1)
    list2 = getWords(T2)

    if (list1.head == None) or (list2.head == None):
        return False
    
    if (linkedlist.length(list1)) != (linkedlist.length(list2)):
        return False
    
    areEqual = False
    currentNode1 = list1.head
    while currentNode1 != None:
        elemento = currentNode1.value
        currentNode2 = list2.head

        while currentNode2 != None:
            if elemento == currentNode2.value:
                areEqual = True
            currentNode2 = currentNode2.nextNode
        if areEqual == False:
            return areEqual
        areEqual = False
        currentNode1 = currentNode1.nextNode
    return True

#Punto 6
#Verifica que un Trie posea dos cadenas invertidas entre sí
"""
Se utiliza la función getWords (definida en el ejercicio anterior) y la función getWordsBackwards. En esencia es la misma función, sin
embargo, cambia en la manera de concatenar la palabra, puesto que en esta nueva función se concatena al revés. Es decir:
node.key + auxiliarList[0], pero, en esencia es el mismo funcionamiento. Al final tendremos una lista con las palabras del Trie
normales y otra con las mismas palabras, pero escritas al revés. Posteriormente se busca si alguna palabra de la lista 1 se encuentra
en la 2. Si esto ocurre, retorna True
"""

def getWordsBackwards(T):
    if T.root == None:
        return None
    else:
        auxiliarList = linkedlist.LinkedList()
        currentNode = T.root.head
        while currentNode != None:
            auxiliarList = getWordsBackwardsR(currentNode.value, auxiliarList, 1)
            currentNode = currentNode.nextNode
        return auxiliarList


def getWordsBackwardsR(node, auxiliarList, cont):
    
    if cont != 1:
        auxiliarList.head.value = node.key + auxiliarList.head.value

    if node.isEndOfWord == True:
        if node.children == None:
            return auxiliarList
        else:
            linkedlist.add(auxiliarList, auxiliarList.head.value)
    
    if node.children == None:
        return auxiliarList
    
    if cont != 1:
        aux = auxiliarList.head.value

    j = 0
    currentNode = node.children.head
    while currentNode != None:
        j = j + 1
        if cont == 1:
            linkedlist.add(auxiliarList, node.key)
        if (j != 1) and (cont != 1):
            linkedlist.add(auxiliarList, aux)
        auxiliarList = getWordsBackwardsR(currentNode.value, auxiliarList, cont + 1)
        currentNode = currentNode.nextNode
    return auxiliarList
    

def invertidas(T):
    if T.root == None:
        return False
    
    list1 = getWords(T)
    list2 = getWordsBackwards(T)
    length = linkedlist.length(list1)
    condition = False
    currentNode = list1.head
    while currentNode != None:
        element = currentNode.value
        currentNode2 = list2.head
        while currentNode2 != None:
            if element == currentNode2.value:
                return True
            currentNode2 = currentNode2.nextNode
        currentNode = currentNode.nextNode
    return False

#Punto 7
#Dada una cadena, devuelve lo que podría seguirle a esa cadena hasta que se encuentre con dos caminos diferentes.
"""
Utilizando la función del punto 4. Busca el último nodo (si existe) de un Trie dada una cadena específica. Se inicializa una string vacía
y se llama a la función autoCompletarR con el nodo y la string. Dentro se concatenan las letras encontradas hasta que o el node.children sea
None o hasta que la lista tenga más de un nodo. Se devuelve la palabra
"""
def autoCompletar(Trie, cadena):
    node = searchLastNodePattern(Trie, cadena)
    word = ""
    return autoCompletarR(node, word)

def autoCompletarR(node, word):
    if node.children == None:
        return word
    if node.children.head.nextNode != None:
        return word
    else:
        word = word + node.children.head.value.key
        return autoCompletarR(node.children.head.value, word)