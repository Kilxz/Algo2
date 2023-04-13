from algo1 import *
import linkedlist
    
def dictionary(m):
    dict = Array(m, linkedlist.LinkedList())
    return dict

def hash(k, m):
    return (k % m)

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