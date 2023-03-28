
class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None


def printlist(L):
  if L.head != None:
    currentNode = L.head
    print("[", end="")
    while currentNode != None:
      if currentNode.nextNode != None:
        print(currentNode.value, end=", ")
      else:
        print(currentNode.value, end="")
        print("]")
      currentNode = currentNode.nextNode
  else:
    return None
    
#O(1)
def add(L, element):
  newNode = Node()
  newNode.value = element
  if L.head != None:
    newNode.nextNode = L.head
  L.head = newNode
  return

#O(n)
def search(L, element):
  current = L.head
  position = 0
  if current != None:
    while (current != None):
      if current.value == element:
        return position
      else:
        current = current.nextNode
        position = position + 1
  else:
    position = None
  position = None
  return position
  
#O(n)
def insert(L, element, position):
    
  if position == 0:
    add(L, element)
    return position

  if position > 0:
    currentNode = L.head
    newNode = Node()
    newNode.value = element
    pos = 0
    while (currentNode != None):
      if pos + 1 != position:
        currentNode = currentNode.nextNode
        pos = pos + 1
      else:
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode
        pos = pos + 1
        return position
    return None


#O(n)
def delete(L, element):
  currentNode = L.head
  position = search(L, element)
  if position != None:
    cont = 0
    while cont <= position:
  
      if position==0:
        L.head = currentNode.nextNode
        currentNode.nextNode = None
        return position
        
      if cont == position-1:
        
        if currentNode.nextNode == None:
          currentNode = None
          return position
          
        else:
          aux = currentNode.nextNode
          currentNode.nextNode = aux.nextNode
          aux.nextNode = None
          
        
          return position
      
      else:
        currentNode = currentNode.nextNode
        cont += 1
  else: 
    return None

#O(n)
def length(L):
  currentNode = L.head
  position = 0
  while currentNode != None:
    position += 1
    currentNode = currentNode.nextNode
  return position
  
#O(n)
def access(L, position):
  currentNode = L.head
  if position >= 0:
    for i in range(0, position):
      if currentNode == None:
        return None
      currentNode = currentNode.nextNode
    return currentNode.value

#O(n)
def update(L, element, position):
  currentNode = L.head
  if position >= 0:
    for i in range(0, position):
      currentNode = currentNode.nextNode
      if (currentNode == None) and (i != position):
        return None
    currentNode.value = element
  return position


#Devuelve el nodo posicionado en la posición ingresada
def accessNode(L, position):
  currentNode = L.head
  if position >= 0:
    for i in range(0, position):
      if currentNode == None:
        return None
      currentNode = currentNode.nextNode
    return currentNode

#Inserta el nodo ingresado en la posición ingresada
def insertNode (L, Node, position):
  Node.nextNode = None
  if position == 0:
    Node.nextNode = L.head
    L.head = Node
    return position

  if position > 0:
    currentNode = L.head
    pos = 0
    while (currentNode != None):
      if pos + 1 != position:
        currentNode = currentNode.nextNode
        pos = pos + 1
      else:
        Node.nextNode = currentNode.nextNode
        currentNode.nextNode = Node
        pos = pos + 1
        return position
    return None

#La función dequeue, pero en vez del elemento, devuelve el nodo del final
def dequeueNode(L):
  if L.head == None:
    return None
  currentNode = L.head
  while currentNode.nextNode != None:
    aux = currentNode
    currentNode = currentNode.nextNode
  aux.nextNode = None
  return currentNode

#Añade el nodo ingresado al final de la lista
def addNode(L, Node):
  if L.head != None:
    if Node != None:
      Node.nextNode = None
      currentNode = L.head
      while currentNode.nextNode != None:
        currentNode = currentNode.nextNode
      currentNode.nextNode = Node
  else:
    L.head = Node
    Node.nextNode = None
  return L

#Añade el nodo ingresado al principio de la lista
def addNodeAtBegining(L, Node):
  if L.head == None:
    L.head = Node
    Node.nextNode = None
  else:
    Node.nextNode = L.head
    L.head = Node
  return L

#Añade el elemento ingresado al final de la lista
def addatend(L, element):
  if L.head == None:
    newNode = Node()
    L.head = newNode
    L.head.value = element
  else:
    currentNode = L.head
    while currentNode != None:
      if currentNode.nextNode == None:
        newNode = Node()
        currentNode.nextNode = newNode
        newNode.value = element
        return element
      currentNode = currentNode.nextNode


def swap(L, pos1, pos2):
  if pos1 == pos2:
    return None
  len = length(L)

  if pos1 > len or pos1 < 0:
    return None
  
  if pos2 > len or pos2 < 0:
    return None
  currentNode1 = L.head
  for i in range(0, pos1):
    lastNode1 = currentNode1
    currentNode1 = currentNode1.nextNode

  currentNode2 = L.head
  for i in range(0, pos2):
    lastNode2 = currentNode2
    currentNode2 = currentNode2.nextNode
  
  if pos1 == 0:
    L.head = currentNode2
    aux = currentNode2.nextNode
    currentNode2.nextNode = currentNode1.nextNode
    lastNode2.nextNode = currentNode1
    currentNode1.nextNode = aux
  else:
    if pos2 == 0:
      L.head = currentNode1
      aux = currentNode1.nextNode
      currentNode1.nextNode = currentNode2.nextNode
      lastNode1.nextNode = currentNode2
      currentNode2.nextNode = aux
    else:
      lastNode1.nextNode = currentNode2
      aux = currentNode2.nextNode
      currentNode2.nextNode = currentNode1.nextNode
      lastNode2.nextNode = currentNode1
      currentNode1.nextNode = aux

  return L 
  
"""

def inversa(L):
  if L.head == None:
    return None
  currentNode = L.head
  while currentNode.nextNode != None:
    currentNode = currentNode.nextNode
  currentNode2 = L.head
  for i in range(0, length(L)-1):
    L.head = currentNode2.nextNode
    aux = currentNode2.nextNode
    if currentNode.nextNode != None:
      currentNode2.nextNode = currentNode.nextNode
    else:
      currentNode2.nextNode = None
    currentNode.nextNode = currentNode2
    currentNode2 = aux
  return L

  
def move(LinkedList, position_orig, position_dest):
  currentNode = LinkedList.head
  if position_orig == 0:
    aux = LinkedList.head
    LinkedList.head = LinkedList.head.nextNode
  else:
    for i in range(0, position_orig - 1):
      currentNode = currentNode.nextNode
  
    aux = currentNode.nextNode
    if currentNode.nextNode.nextNode != None:
      currentNode.nextNode = currentNode.nextNode.nextNode
    else:
      currentNode.nextNode = None
    
  if position_dest == 0:
    aux.nextNode = LinkedList.head
    LinkedList.head = aux
    return position_dest
  elif position_dest == 1:
    aux.nextNode = LinkedList.head.nextNode
    LinkedList.head.nextNode = aux
    return position_dest
  else:
    currentNode = LinkedList.head
    for i in range(0, position_dest - 1):
     currentNode = currentNode.nextNode

  aux.nextNode = currentNode.nextNode
  currentNode.nextNode = aux
  return position_dest
"""