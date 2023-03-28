
class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

""" Busca en una LinkedList un element llamado element.
La diferencia con la función ya implementada de LinkedList es que
devolverá None si no existe o el nodo si ya existe.
def searchInL(L, element):
    if L.head == None:
        return None
    currentNode = L.head
    while currentNode != None:
        if currentNode.value.key == element:
            return currentNode
        currentNode = currentNode.nextnode
    return None
"""
def searchInL(L, element):
    long = len(L)
    for i in range(0, long):
        if L[i].key == element:
            return i
    return None

def insert(T, element):
    element = element.lower()
    if T.root == None:
        L = []
        T.root = L
    else:
        L = T.root
    return insertR(T.root, L, element)

def insertR(LastNode, L, element):
    condition = searchInL(L, element[0])

    if condition == None:
        TNode = TrieNode()
        TNode.key = element[0]
        newList = []
        TNode.parent = LastNode
        TNode.children = newList
        L.append(TNode)
    else:
        TNode = L[condition]

    if len(element) != 1:
        element = element[1:]
        if condition == None:
            insertR(TNode, newList, element)
        else:
            insertR(L[condition], L[condition].children, element)
        return
    else:
        TNode.isEndOfWord = True
        return

def search(T, element):
    return searchR(T.root, element)

def searchR(L, element):
    condition = searchInL(L, element[0])
    if condition == None:
        return False
    
    if len(element) != 1:
        element = element[1:]
        return searchR(L[condition].children, element)
    else:
        if L[condition].isEndOfWord == True:
            return True
        else:
            return False