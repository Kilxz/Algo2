from algo1 import *
from mylinkedlist import *

def BubbleSort(L):
  if L.head == None:
    return None
  size = length(L)
  currentNode = L.head
  currentNode2 = L.head.nextNode

  for i in range(1, size ):
    currentNode = L.head
    currentNode2 = L.head.nextNode
    if currentNode.value > currentNode2.value:
      L.head = currentNode2
      currentNode.nextNode = currentNode2.nextNode
      currentNode2.nextNode = currentNode
      currentNode2 = currentNode.nextNode
      currentNode = L.head
    for j in range(0, size - i-1):
      if currentNode.nextNode.nextNode != None:
        if currentNode.nextNode.value > currentNode.nextNode.nextNode.value:
          aux = currentNode.nextNode
          currentNode.nextNode = currentNode.nextNode.nextNode
          aux.nextNode = currentNode.nextNode.nextNode
          currentNode.nextNode.nextNode = aux
          
      currentNode = currentNode.nextNode
  return L

def SelectionSort(L):
  if L.head == None:
    return None
  currentNode = L.head
  for i in range(0, length(L)-1):
    currentNode2 = currentNode
    menor = currentNode.value
    cond = False
    for j in range(0, length(L) - i):
      if currentNode2.nextNode != None:
        
        if currentNode2.nextNode.value < menor:
          LastNode = currentNode2
          minorNode = currentNode2.nextNode
          cond = True
          menor = minorNode.value
        currentNode2 = currentNode2.nextNode
        
    if cond == True:
      
      if currentNode == L.head:
        LastNode.nextNode = LastNode.nextNode.nextNode
        minorNode.nextNode = L.head
        L.head = minorNode
        aux = L.head
        currentNode = L.head
      else:
        LastNode.nextNode = LastNode.nextNode.nextNode
        minorNode.nextNode = aux.nextNode
        aux.nextNode = minorNode
        aux = minorNode
        currentNode = minorNode
    else:
      aux = currentNode
    currentNode = currentNode.nextNode
        
  return L

def InsertionSort(L):
  if L.head == None:
    return None
    
  long = length(L)
  currentNode = L.head
  for i in range(1, long):
    vof = False
    if L.head.value > currentNode.nextNode.value:
      aux = currentNode.nextNode
      currentNode.nextNode = currentNode.nextNode.nextNode
      aux.nextNode = L.head
      L.head = aux
      vof = True
    else:
      currentNode2 = L.head
      for j in range(1, i):
        if currentNode.nextNode != None and currentNode2 != None:
          if currentNode.nextNode.value < currentNode2.nextNode.value:
            aux = currentNode.nextNode
            currentNode.nextNode = currentNode.nextNode.nextNode
            aux.nextNode = currentNode2.nextNode
            currentNode2.nextNode = aux
            vof = True
          if currentNode != None:
            currentNode2 = currentNode2.nextNode
    if currentNode != None and vof == False:
      currentNode = currentNode.nextNode
  return L
  


  
def QuickSort(L):
  if L.head == None:
    return None
  definitiveList = LinkedList()
  definitiveList = QuickSortR(L, definitiveList)
  return definitiveList
  
def QuickSortR(L, definitiveList):
  list1 = LinkedList()
  list2 = LinkedList()
  len = length(L)
  if len > 1:
    if L.head.value > L.head.nextNode.value:
      pivote = L.head
    else:
      pivote = L.head.nextNode
    currentNode = L.head
    aux = L.head
    while currentNode != None:
      if currentNode.value >= pivote.value:
        L.head = L.head.nextNode
        addNode(list2, currentNode)
      else:
        L.head = L.head.nextNode
        addNode(list1, currentNode)
      currentNode = L.head

    QuickSortR(list1, definitiveList)
    QuickSortR(list2, definitiveList)
  elif L.head != None:
    addNode(definitiveList, L.head)
  return definitiveList
  
def MergeSort(L):
  if L.head == None:
    return None
  list1 = LinkedList()
  list2 = LinkedList()
  len = length(L)
  i = 0
  currentNode = L.head
  if len > 1:
    while currentNode != None:
      if i % 2 == 0:
        Node = currentNode
        L.head = L.head.nextNode
        addNode(list1, Node)
        i += 1
      else:
        Node = currentNode
        L.head = L.head.nextNode
        addNode(list2, Node)
        i += 1
      currentNode = L.head

    MergeSort(list1)
    MergeSort(list2)

    currentNode1 = list1.head
    aux1 = list1.head
    currentNode2 = list2.head
    aux2 = list2.head
    j = 0

    while currentNode1 != None and currentNode2 != None:
      if currentNode1.value < currentNode2.value:
        aux = currentNode1
        currentNode1 = currentNode1.nextNode
        delete(list1, aux.value)
        insertNode(L, aux, j)
      else:
        aux = currentNode2
        currentNode2 = currentNode2.nextNode
        delete(list2, aux.value)
        insertNode(L, aux, j)
      j += 1

    while currentNode2 != None and currentNode1 == None:
      aux = currentNode2
      currentNode2 = currentNode2.nextNode
      delete(list2, aux.value)
      insertNode(L, aux, j)
      j += 1
    while currentNode1 != None and currentNode2 == None:
      aux = currentNode1
      currentNode1 = currentNode1.nextNode
      delete(list1, aux.value)
      insertNode(L, aux, j)
      j+= 1
  return L
