from linkedlist import *

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

""" Busca en una LinkedList un element llamado element.
La diferencia con la función ya implementada de LinkedList es que
devolverá None si no existe o el nodo si ya existe."""
def searchInL(L, element):
    if L.head == None:
        return None
    currentNode = L.head
    while currentNode != None:
        if currentNode.value.key == element:
            return currentNode
        currentNode = currentNode.nextnode
    return None

def insert(T, element):
    element = element.lower()
    if T.root == None:
        L = LinkedList()
        T.root = L

def insertR(L, element):
    condition = searchInL(L, element[0])
    if condition == None:
        TNode = TrieNode()
        TNode.key = element[0]
        newList = LinkedList()
        TNode.parent = L
        TNode.children = newList

        add(L, TNode)
