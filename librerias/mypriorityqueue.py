from algo1 import *
from mylinkedlist import *

class PriorityQueue:
  head=None

class PriorityNode:
  value=None
  nextNode=None
  priority=None

def enqueue_priority(Q, element, priority):
  newNode = PriorityNode()
  newNode.value = element
  newNode.priority = priority
  if Q.head == None:
    Q.head = newNode
    return 0
  else:
    if priority >= Q.head.priority:
      newNode.nextNode = Q.head
      Q.head = newNode
      return 0
    currentNode = Q.head
    pos = 0
    while currentNode.nextNode != None:
      if priority <= currentNode.nextNode.priority:
        currentNode = currentNode.nextNode
        pos += 1
      else:
        newNode.nextNode = currentNode.nextNode
        currentNode = newNode
        return pos
    currentNode.nextNode = newNode
    pos += 1
    return pos
        
def dequeue_priority(Q):
  if Q.head != None:
    currentNode = Q.head.nextNode
    element = Q.head.value
    Q.head.nextNode = None
    Q.head = currentNode
    return element
  else:
    return None