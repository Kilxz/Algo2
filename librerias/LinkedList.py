class LinkedList:
  root = None

class Node:
  value = None
  nextNode = None

def LinkedList():
  L = LinkedList()
  return L

def add(L, element):
  Node = Node()
  Node.value = element
  if L.root == None:
    L.root = Node
    Node.nextNode = None
  else:
    Node.nextNode = L.root
    L.root = Node
  return L

def addend(L, element):
  Node = Node()
  Node.value = element
  if L.root == None:
    L.root = Node
    return L
  else:
    currentNode = L.root
    while currentNode.nextNode != None:
      currentNode = currentNode.nextNode
    currentNode.nextNode = Node

def pop(L):
  element = L.root.value
  L.root = L.root.nextNode
  return element

